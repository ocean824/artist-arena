import type { CorrelationId } from './ids.js';

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
