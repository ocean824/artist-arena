from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + '\n', encoding='utf-8')


def write_json(relative: str, value: object) -> None:
    write(relative, json.dumps(value, indent=2))

write('packages/contracts/src/ids.ts', '''export type Brand<T, Name extends string> = T & { readonly __brand: Name };

export type UserId = Brand<string, 'UserId'>;
export type ProfileId = Brand<string, 'ProfileId'>;
export type BattleId = Brand<string, 'BattleId'>;
export type TournamentId = Brand<string, 'TournamentId'>;
export type SubmissionId = Brand<string, 'SubmissionId'>;
export type LedgerTransactionId = Brand<string, 'LedgerTransactionId'>;
export type ChainTransactionId = Brand<string, 'ChainTransactionId'>;
export type WalletId = Brand<string, 'WalletId'>;
export type PolicyDecisionId = Brand<string, 'PolicyDecisionId'>;
export type CorrelationId = Brand<string, 'CorrelationId'>;

export function asBrand<T extends string>(value: string, field: string): T {
  if (value.trim().length === 0) throw new Error(`${field} must not be empty`);
  return value as T;
}
''')

write('packages/contracts/src/time.ts', '''export type UtcInstant = string & { readonly __brand: 'UtcInstant' };

export function asUtcInstant(value: string): UtcInstant {
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime()) || !value.endsWith('Z')) {
    throw new Error('UtcInstant must be a valid ISO-8601 UTC timestamp ending in Z');
  }
  return parsed.toISOString() as UtcInstant;
}
''')

write('packages/contracts/src/money.ts', '''export type EconomicInstrument =
  | 'ARENA_POINTS'
  | 'PURCHASED_CREDIT'
  | 'EARNED_CREDIT'
  | 'FIAT'
  | 'CHAIN_ASSET';

export interface Amount {
  readonly instrument: EconomicInstrument;
  readonly currencyOrDenom: string;
  readonly minorOrAtomicUnits: bigint;
}

function assertCompatible(left: Amount, right: Amount): void {
  if (left.instrument !== right.instrument || left.currencyOrDenom !== right.currencyOrDenom) {
    throw new Error('Amounts with different instruments or currencies/denominations cannot be combined');
  }
}

export function addAmount(left: Amount, right: Amount): Amount {
  assertCompatible(left, right);
  return { ...left, minorOrAtomicUnits: left.minorOrAtomicUnits + right.minorOrAtomicUnits };
}

export function subtractAmount(left: Amount, right: Amount): Amount {
  assertCompatible(left, right);
  return { ...left, minorOrAtomicUnits: left.minorOrAtomicUnits - right.minorOrAtomicUnits };
}

export function calculateBasisPointFee(amount: Amount, basisPoints: bigint): Amount {
  if (amount.minorOrAtomicUnits < 0n) throw new Error('Fee input must not be negative');
  if (basisPoints < 0n || basisPoints > 10_000n) throw new Error('Basis points must be between 0 and 10000');
  return { ...amount, minorOrAtomicUnits: (amount.minorOrAtomicUnits * basisPoints) / 10_000n };
}

export const FOUNDER_DEFAULT_CONVERSION_FEE_BPS = 100n;
''')

write('packages/contracts/src/http.ts', '''import type { CorrelationId } from './ids.js';

export interface ApiMeta {
  readonly requestId: string;
  readonly correlationId: CorrelationId;
  readonly apiVersion: 'v1';
}

export interface ApiSuccess<T> {
  readonly ok: true;
  readonly data: T;
  readonly meta: ApiMeta;
}

export interface ApiErrorDetail {
  readonly code: string;
  readonly message: string;
  readonly field?: string;
}

export interface ApiFailure {
  readonly ok: false;
  readonly error: {
    readonly code: string;
    readonly message: string;
    readonly details: readonly ApiErrorDetail[];
    readonly retryable: boolean;
  };
  readonly meta: ApiMeta;
}

export interface CursorPage<T> {
  readonly items: readonly T[];
  readonly nextCursor: string | null;
}
''')

write('packages/contracts/src/index.ts', '''export * from './ids.js';
export * from './time.js';
export * from './money.js';
export * from './http.js';
''')

write('packages/events/src/index.ts', '''import type { CorrelationId, UserId } from '@artist-arena/contracts';
import type { UtcInstant } from '@artist-arena/contracts';

export interface DomainEvent<TPayload extends object = Record<string, never>> {
  readonly eventId: string;
  readonly eventType: `${string}.${string}.v${number}`;
  readonly eventVersion: number;
  readonly aggregateType: string;
  readonly aggregateId: string;
  readonly aggregateVersion: number;
  readonly actorId: UserId | 'SYSTEM';
  readonly occurredAt: UtcInstant;
  readonly recordedAt: UtcInstant;
  readonly requestId: string;
  readonly traceId: string;
  readonly correlationId: CorrelationId;
  readonly causationId: string | null;
  readonly policyVersion: string;
  readonly privacyClass: 'PUBLIC' | 'INTERNAL' | 'CONFIDENTIAL' | 'RESTRICTED';
  readonly retentionClass: string;
  readonly payload: TPayload;
}
''')

write('packages/ledger/src/index.ts', '''import type { EconomicInstrument } from '@artist-arena/contracts';

export type PostingSide = 'DEBIT' | 'CREDIT';

export interface Posting {
  readonly accountId: string;
  readonly side: PostingSide;
  readonly instrument: EconomicInstrument;
  readonly currencyOrDenom: string;
  readonly units: bigint;
}

export interface JournalTransaction {
  readonly transactionId: string;
  readonly idempotencyKey: string;
  readonly effectiveAt: string;
  readonly reasonCode: string;
  readonly referenceType: string;
  readonly referenceId: string;
  readonly postings: readonly Posting[];
  readonly reversesTransactionId: string | null;
}

export function assertBalanced(transaction: JournalTransaction): void {
  if (transaction.postings.length < 2) throw new Error('A journal transaction requires at least two postings');
  const totals = new Map<string, { debit: bigint; credit: bigint }>();
  for (const posting of transaction.postings) {
    if (posting.units <= 0n) throw new Error('Posting units must be positive');
    const key = `${posting.instrument}:${posting.currencyOrDenom}`;
    const current = totals.get(key) ?? { debit: 0n, credit: 0n };
    current[posting.side === 'DEBIT' ? 'debit' : 'credit'] += posting.units;
    totals.set(key, current);
  }
  for (const [key, total] of totals) {
    if (total.debit !== total.credit) throw new Error(`Unbalanced journal for ${key}`);
  }
}

export interface BalanceHold {
  readonly holdId: string;
  readonly accountId: string;
  readonly instrument: EconomicInstrument;
  readonly currencyOrDenom: string;
  readonly originalUnits: bigint;
  readonly releasedUnits: bigint;
  readonly state: 'PENDING' | 'ACTIVE' | 'PARTIALLY_RELEASED' | 'RELEASED' | 'CANCELLED' | 'INCIDENT_HOLD';
  readonly referenceType: 'CONTEST_ENTRY' | 'PRIZE_POOL' | 'MARKETPLACE_ORDER' | 'PAYOUT' | 'OTHER';
  readonly referenceId: string;
}

export function availableHoldUnits(hold: BalanceHold): bigint {
  const available = hold.originalUnits - hold.releasedUnits;
  if (available < 0n) throw new Error('Hold released units exceed original units');
  return available;
}
''')

write('packages/contests/src/index.ts', '''export type ContestState =
  | 'DRAFT'
  | 'PUBLISHED'
  | 'ENTRY_OPEN'
  | 'FUNDING_PENDING'
  | 'FUNDED'
  | 'SUBMISSION_OPEN'
  | 'SUBMISSIONS_LOCKED'
  | 'JUDGING_OPEN'
  | 'VOTING_OPEN'
  | 'CALCULATION_PENDING'
  | 'PROVISIONAL_RESULT'
  | 'DISPUTED'
  | 'FINAL_RESULT'
  | 'SETTLEMENT_PENDING'
  | 'SETTLED'
  | 'CANCELLED'
  | 'VOID';

const transitions: Readonly<Record<ContestState, readonly ContestState[]>> = {
  DRAFT: ['PUBLISHED', 'CANCELLED'],
  PUBLISHED: ['ENTRY_OPEN', 'FUNDING_PENDING', 'SUBMISSION_OPEN', 'CANCELLED'],
  ENTRY_OPEN: ['FUNDING_PENDING', 'FUNDED', 'SUBMISSION_OPEN', 'CANCELLED'],
  FUNDING_PENDING: ['FUNDED', 'CANCELLED'],
  FUNDED: ['SUBMISSION_OPEN', 'CANCELLED'],
  SUBMISSION_OPEN: ['SUBMISSIONS_LOCKED', 'CANCELLED'],
  SUBMISSIONS_LOCKED: ['JUDGING_OPEN', 'VOTING_OPEN', 'CALCULATION_PENDING', 'VOID'],
  JUDGING_OPEN: ['CALCULATION_PENDING', 'VOID'],
  VOTING_OPEN: ['CALCULATION_PENDING', 'VOID'],
  CALCULATION_PENDING: ['PROVISIONAL_RESULT', 'VOID'],
  PROVISIONAL_RESULT: ['DISPUTED', 'FINAL_RESULT', 'VOID'],
  DISPUTED: ['FINAL_RESULT', 'VOID'],
  FINAL_RESULT: ['SETTLEMENT_PENDING', 'SETTLED'],
  SETTLEMENT_PENDING: ['SETTLED'],
  SETTLED: [],
  CANCELLED: [],
  VOID: [],
};

export function canTransitionContest(from: ContestState, to: ContestState): boolean {
  return transitions[from].includes(to);
}
''')

write('packages/policy/src/index.ts', '''export type ActivationState =
  | 'LOCAL'
  | 'SANDBOX'
  | 'TESTNET'
  | 'PILOT'
  | 'REGION_LIMITED'
  | 'VALUE_CAPPED'
  | 'PRODUCTION_ENABLED'
  | 'DISABLED_BY_POLICY';

export interface PaidContestPolicyContext {
  readonly operatorProfile: string;
  readonly jurisdiction: string | null;
  readonly locationConfidence: 'NONE' | 'LOW' | 'MEDIUM' | 'HIGH';
  readonly ageEligible: boolean;
  readonly identityLevel: string;
  readonly sanctionsResult: 'UNKNOWN' | 'CLEAR' | 'REVIEW' | 'DENY';
  readonly selfExcluded: boolean;
  readonly withinLimits: boolean;
  readonly accountAllowed: boolean;
  readonly walletAllowed: boolean;
  readonly providerAvailable: boolean;
  readonly activationState: ActivationState;
  readonly policyVersion: string;
}

export interface PolicyDecision {
  readonly allowed: boolean;
  readonly reasonCodes: readonly string[];
  readonly policyVersion: string;
}

export function evaluatePaidContestPolicy(context: PaidContestPolicyContext): PolicyDecision {
  const reasons: string[] = [];
  if (context.activationState === 'DISABLED_BY_POLICY') reasons.push('ACTIVATION_DISABLED');
  if (!context.jurisdiction || context.locationConfidence !== 'HIGH') reasons.push('LOCATION_NOT_VERIFIED');
  if (!context.ageEligible) reasons.push('AGE_NOT_ELIGIBLE');
  if (context.sanctionsResult !== 'CLEAR') reasons.push('SANCTIONS_OR_RISK_NOT_CLEAR');
  if (context.selfExcluded) reasons.push('SELF_EXCLUDED');
  if (!context.withinLimits) reasons.push('LIMIT_EXCEEDED');
  if (!context.accountAllowed || !context.walletAllowed) reasons.push('ACCOUNT_OR_WALLET_RESTRICTED');
  if (!context.providerAvailable) reasons.push('PROVIDER_UNAVAILABLE');
  return { allowed: reasons.length === 0, reasonCodes: reasons, policyVersion: context.policyVersion };
}
''')

write('packages/chain/src/index.ts', '''import type { CorrelationId, PolicyDecisionId, UserId, UtcInstant } from '@artist-arena/contracts';

export interface ChainTransactionEnvelope<TPayload extends object> {
  readonly networkId: string;
  readonly chainId: string;
  readonly transactionId: string;
  readonly commandType: string;
  readonly commandVersion: number;
  readonly actorId: UserId | 'SYSTEM';
  readonly signingAuthorityId: string;
  readonly nonce: string;
  readonly expiresAt: UtcInstant;
  readonly resourceLimit: bigint;
  readonly policyDecisionId: PolicyDecisionId;
  readonly correlationId: CorrelationId;
  readonly payload: TPayload;
  readonly signatureSet: readonly string[];
}

export type ChainFinalityState = 'NOT_SUBMITTED' | 'PENDING' | 'FINALIZED' | 'FAILED' | 'REPLACED' | 'INCIDENT_HOLD';

export interface ChainFinalityRecord {
  readonly transactionId: string;
  readonly state: ChainFinalityState;
  readonly blockHeight: bigint | null;
  readonly stateRoot: string | null;
  readonly failureCode: string | null;
  readonly updatedAt: UtcInstant;
}
''')

write('packages/wallet/src/index.ts', '''import type { Amount, PolicyDecisionId, UtcInstant, WalletId } from '@artist-arena/contracts';

export type CustodyMode = 'MANAGED' | 'SELF_CUSTODIAL' | 'ORGANIZATION';

export interface TrustedSigningIntent {
  readonly intentId: string;
  readonly walletId: WalletId;
  readonly custodyMode: CustodyMode;
  readonly action: string;
  readonly amount: Amount | null;
  readonly counterparty: string | null;
  readonly feeBreakdown: readonly Amount[];
  readonly permissions: readonly string[];
  readonly irreversibleConsequences: readonly string[];
  readonly policyDecisionId: PolicyDecisionId;
  readonly expiresAt: UtcInstant;
  readonly humanReadableSummary: string;
}
''')

# Add local package dependencies needed by the baseline types.
for package, deps in {
    'events': {'@artist-arena/contracts': 'workspace:*'},
    'ledger': {'@artist-arena/contracts': 'workspace:*'},
    'chain': {'@artist-arena/contracts': 'workspace:*'},
    'wallet': {'@artist-arena/contracts': 'workspace:*'},
}.items():
    path = ROOT / 'packages' / package / 'package.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    data['dependencies'] = deps
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')

write('packages/contracts/openapi.yaml', '''openapi: 3.1.0
info:
  title: Artist Arena API
  version: 0.1.0
  description: Contract-first V1 skeleton; no provider or production activation is implied.
servers:
  - url: /api/v1
paths:
  /health:
    get:
      operationId: getHealth
      responses:
        '200':
          description: Service health
  /battles:
    get:
      operationId: listBattles
      responses:
        '200': { description: Cursor page of visible battles }
    post:
      operationId: createBattle
      responses:
        '201': { description: Battle created in DRAFT }
  /economy/conversions/quote:
    post:
      operationId: createConversionQuote
      description: Quotes cash-to-credit or credit-to-cash with the configured founder fee and separate costs.
      responses:
        '201': { description: Expiring conversion quote created }
        '403': { description: Policy denied }
  /contests/{contestId}/entry-commitments:
    post:
      operationId: commitContestEntry
      parameters:
        - in: path
          name: contestId
          required: true
          schema: { type: string }
        - in: header
          name: Idempotency-Key
          required: true
          schema: { type: string }
      responses:
        '201': { description: Eligibility approved and funds reserved }
        '403': { description: Eligibility or activation denied }
        '409': { description: State, funding, or idempotency conflict }
  /chain/transactions/{transactionId}:
    get:
      operationId: getChainTransactionFinality
      parameters:
        - in: path
          name: transactionId
          required: true
          schema: { type: string }
      responses:
        '200': { description: Current transaction and finality projection }
components:
  schemas:
    ApiFailure:
      type: object
      required: [ok, error, meta]
      properties:
        ok: { const: false }
        error:
          type: object
          required: [code, message, details, retryable]
          properties:
            code: { type: string }
            message: { type: string }
            details: { type: array, items: { type: object } }
            retryable: { type: boolean }
        meta:
          type: object
          required: [requestId, correlationId, apiVersion]
          properties:
            requestId: { type: string }
            correlationId: { type: string }
            apiVersion: { const: v1 }
''')

write_json('docs/schemas/domain-event.schema.json', {
  '$schema': 'https://json-schema.org/draft/2020-12/schema',
  '$id': 'https://artist-arena.invalid/schemas/domain-event.schema.json',
  'title': 'Artist Arena Domain Event',
  'type': 'object',
  'additionalProperties': False,
  'required': ['eventId','eventType','eventVersion','aggregateType','aggregateId','aggregateVersion','actorId','occurredAt','recordedAt','requestId','traceId','correlationId','policyVersion','privacyClass','retentionClass','payload'],
  'properties': {
    'eventId': {'type':'string','minLength':1},
    'eventType': {'type':'string','pattern':'^[a-z][a-z0-9_]*\\.[a-z][a-z0-9_]*\\.v[1-9][0-9]*$'},
    'eventVersion': {'type':'integer','minimum':1},
    'aggregateType': {'type':'string','minLength':1},
    'aggregateId': {'type':'string','minLength':1},
    'aggregateVersion': {'type':'integer','minimum':1},
    'actorId': {'type':'string','minLength':1},
    'occurredAt': {'type':'string','format':'date-time'},
    'recordedAt': {'type':'string','format':'date-time'},
    'requestId': {'type':'string','minLength':1},
    'traceId': {'type':'string','minLength':1},
    'correlationId': {'type':'string','minLength':1},
    'causationId': {'type':['string','null']},
    'policyVersion': {'type':'string','minLength':1},
    'privacyClass': {'enum':['PUBLIC','INTERNAL','CONFIDENTIAL','RESTRICTED']},
    'retentionClass': {'type':'string','minLength':1},
    'payload': {'type':'object'},
  },
})

write_json('docs/schemas/work-package.schema.json', {
  '$schema': 'https://json-schema.org/draft/2020-12/schema',
  '$id': 'https://artist-arena.invalid/schemas/work-package.schema.json',
  'title': 'Artist Arena Work Package',
  'type': 'object',
  'additionalProperties': False,
  'required': ['ticketId','requirementIds','objective','scope','dependencies','affectedPaths','acceptanceCriteria','requiredTests','evidence','rollback','activationEffect'],
  'properties': {
    'ticketId': {'type':'string','pattern':'^AA-[0-9]{4}$'},
    'requirementIds': {'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'string','pattern':'^AA-[A-Z]+-[0-9]{3}$'}},
    'objective': {'type':'string','minLength':20},
    'scope': {'type':'string','minLength':20},
    'dependencies': {'type':'array','uniqueItems':True,'items':{'type':'string','pattern':'^AA-[0-9]{4}$'}},
    'affectedPaths': {'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'string','minLength':1}},
    'acceptanceCriteria': {'type':'array','minItems':1,'items':{'type':'string','minLength':10}},
    'requiredTests': {'type':'array','minItems':1,'items':{'type':'string','minLength':3}},
    'evidence': {'type':'array','minItems':1,'items':{'type':'string','minLength':3}},
    'rollback': {'type':'string','minLength':10},
    'activationEffect': {'type':'string','minLength':3},
  },
})

write('tests/contract/README.md', '''# Contract Test Plan

Contract tests validate branded identifiers, UTC instants, integer amount arithmetic, API envelopes, pagination, idempotency, optimistic concurrency, OpenAPI, JSON Schemas, event compatibility, outbox/inbox behavior, provider webhooks, chain transaction envelopes, wallet signing intents, and generated clients. Fixtures must be deterministic and must not contain production credentials or personal data.
''')
write('tests/ledger/README.md', '''# Ledger Property Test Plan

Properties include debits equal credits for every instrument/currency; units are integral and positive per posting; balances derive from journals; one idempotency key produces one transaction; holds never release above funding or twice; reversals use compensating entries; founder conversion fee is independently posted; concurrent settlement is exactly once; and statements reconcile to provider and chain records.
''')
write('tests/chain/README.md', '''# Native Chain Test Plan

Tests cover deterministic transitions, invalid transactions, replay/expiry, signatures, resource limits, state roots, migrations, consensus faults, partitions, node restart/state sync, snapshot restore, module pause, governance authority, wallet recovery, indexer rebuild, bridge idempotency, escrow/settlement, privacy review, load/soak, and disaster recovery.
''')
write('tests/policy/README.md', '''# Policy Test Plan

Decision tables cover operator, jurisdiction, location confidence, age, identity level, sanctions/risk, self-exclusion, limits, account/wallet restrictions, contest class, instrument, provider availability, value cap, assurance level, and activation state. Unknown or failed consequential inputs deny safely and return attributable reason codes.
''')
write('tests/reconciliation/README.md', '''# Reconciliation Test Plan

Reconciliation compares provider events, payment records, journals/postings, holds, credit projections, chain transactions/finality, indexer state, escrow, settlement, creator payables, payouts, refunds, chargebacks, and user statements. Every variance has classification, owner, evidence, resolution, and incident linkage.
''')

print('Generated Artist Arena typed contract, OpenAPI, schema, and test baseline')
