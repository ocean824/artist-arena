import type { EconomicInstrument } from '@artist-arena/contracts';

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
