export type Brand<T, Name extends string> = T & { readonly __brand: Name };

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
