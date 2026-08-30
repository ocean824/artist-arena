import type { CorrelationId, PolicyDecisionId, UserId, UtcInstant } from '@artist-arena/contracts';

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
