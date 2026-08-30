import type { Amount, PolicyDecisionId, UtcInstant, WalletId } from '@artist-arena/contracts';

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
