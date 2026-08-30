import type { CorrelationId, UserId } from '@artist-arena/contracts';
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
