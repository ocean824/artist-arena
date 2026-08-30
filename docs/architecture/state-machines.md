# Artist Arena: Canonical State Machines Specification

**Version:** 1.0
**Author:** Manus AI
**Status:** Governing Architecture Specification
**Primary Destination:** `docs/architecture/state-machines.md`

## 1. Executive Summary

This document defines the canonical state machines for Artist Arena V1, serving as the foundational architecture for the competitive infrastructure layer of the global creator economy. In accordance with Owner Directive 0001, this specification covers all capabilities described in the product canon—including those previously marked as future, later, or sandbox-only—as mandatory V1 engineering scope. The architecture enforces a modular monolith with event-driven boundaries, utilizing Cloudflare, Neon, R2, strict TypeScript, and a native blockchain path for immutable financial and provenance records.

The state machines defined herein govern battles, challenges, tournaments, submissions, media, results, disputes/appeals, marketplace orders, service contracts, credits/conversions, escrow, payouts, chargebacks, blockchain transactions/finality, and moderation cases. Each machine is designed to be deterministic, auditable, and resilient to failure, ensuring that real-world activation controls (such as jurisdiction policy and provider approval) are implemented as configuration gates rather than architectural omissions.

## 2. Architecture and Boundaries

### 2.1 Modular Monolith and Event-Driven Boundaries

Artist Arena is architected as a modular monolith. Domains are strictly separated but deployed together to simplify operations and ensure transactional integrity where necessary. Communication across domain boundaries occurs via asynchronous events, ensuring loose coupling and allowing individual domains to scale or be extracted if required in the future.

### 2.2 Core Infrastructure

- **Database:** Neon (Serverless Postgres) for relational data, configured with strict schemas and migrations.
- **Compute:** Cloudflare Workers/Pages for edge execution and API routing.
- **Storage:** Cloudflare R2 for media assets, submission artifacts, and large JSON payloads.
- **Language:** Strict TypeScript across the entire stack, sharing types between frontend, backend, and state machines.
- **Blockchain:** A native blockchain or sovereign application-chain path for immutable provenance, rights, competition evidence, and economic settlement.

### 2.3 Blockchain Integration and Provenance

The native Artist Arena blockchain path is a mandatory V1 component. It anchors provenance, rights, competition evidence, escrow, and settlement while minimizing on-chain personal and media data.

- **Provenance and Rights:** Content hashes, timestamps, creator declarations, tool/AI disclosures, and licenses are recorded on-chain.
- **Competition Evidence:** Battle/tournament identity, ruleset hashes, submission commitments, judge/audience evidence, and result attestations are anchored to ensure an immutable record of competition.
- **Escrow and Settlement:** Credits/tokens, holds, entry commitments, prize pools, creator splits, fees, refunds, and reversals are managed via deterministic native modules or smart contracts.

## 3. Canonical State Machines

### 3.1 Battles and Challenges

Battles and challenges represent the core competitive units of Artist Arena. A battle is typically a one-to-one or multi-participant event, while a challenge is an open call for submissions.

| State | Description | Allowed Transitions |
|---|---|---|
| `DRAFT` | The battle/challenge is being configured by the organizer. | `PUBLISHED`, `CANCELLED` |
| `PUBLISHED` | The event is visible, but the submission period has not started. | `OPEN`, `CANCELLED` |
| `OPEN` | Submissions are actively being accepted. | `JUDGING`, `CANCELLED` |
| `JUDGING` | The submission period is closed, and judges/audience are evaluating. | `RESOLVED`, `DISPUTED`, `CANCELLED` |
| `RESOLVED` | A final outcome has been determined, and settlement is initiated. | `SETTLED`, `APPEALED` |
| `DISPUTED` | An issue has been raised regarding the outcome or process. | `RESOLVED`, `CANCELLED` |
| `APPEALED` | A formal appeal has been submitted against the resolution. | `RESOLVED`, `CANCELLED` |
| `SETTLED` | All financial and reputational updates are finalized. | None (Terminal State) |
| `CANCELLED` | The event is terminated without a resolution. Refunds are issued. | None (Terminal State) |

**Commands:** `CreateBattle`, `PublishBattle`, `OpenSubmissions`, `CloseSubmissions`, `SubmitResolution`, `RaiseDispute`, `FileAppeal`, `SettleBattle`, `CancelBattle`.
**Events:** `BattleCreated`, `BattlePublished`, `SubmissionsOpened`, `SubmissionsClosed`, `ResolutionSubmitted`, `DisputeRaised`, `AppealFiled`, `BattleSettled`, `BattleCancelled`.

### 3.2 Tournaments

Tournaments are structured sequences of battles or challenges, often organized into brackets or stages.

| State | Description | Allowed Transitions |
|---|---|---|
| `PLANNING` | Tournament structure, rules, and prize pools are being defined. | `ANNOUNCED`, `CANCELLED` |
| `ANNOUNCED` | Tournament is public, accepting registrations. | `IN_PROGRESS`, `CANCELLED` |
| `IN_PROGRESS` | Active competition across various stages/brackets. | `COMPLETED`, `PAUSED`, `CANCELLED` |
| `PAUSED` | Tournament is temporarily halted (e.g., for moderation or dispute). | `IN_PROGRESS`, `CANCELLED` |
| `COMPLETED` | All stages are finished, and final winners are declared. | `SETTLED`, `DISPUTED` |
| `DISPUTED` | A dispute affects the final tournament outcome. | `COMPLETED`, `CANCELLED` |
| `SETTLED` | Final prizes distributed and records finalized. | None (Terminal State) |
| `CANCELLED` | Tournament aborted. Escrowed funds returned. | None (Terminal State) |

**Commands:** `CreateTournament`, `AnnounceTournament`, `StartTournament`, `PauseTournament`, `ResumeTournament`, `CompleteTournament`, `RaiseTournamentDispute`, `SettleTournament`, `CancelTournament`.
**Events:** `TournamentCreated`, `TournamentAnnounced`, `TournamentStarted`, `TournamentPaused`, `TournamentResumed`, `TournamentCompleted`, `TournamentDisputeRaised`, `TournamentSettled`, `TournamentCancelled`.

### 3.3 Submissions and Media

Submissions are the creative works entered into competitions. Media represents the underlying files (audio, video, images, text) associated with submissions, profiles, or marketplace listings.

| State | Description | Allowed Transitions |
|---|---|---|
| `UPLOADING` | Media files are being transferred to R2. | `PROCESSING`, `FAILED` |
| `PROCESSING` | Media is being transcoded, analyzed, or verified. | `READY`, `REJECTED`, `FAILED` |
| `READY` | Media is available for viewing/playback. Submission is valid. | `FLAGGED`, `REMOVED` |
| `FLAGGED` | Submission/media is under review by moderation. | `READY`, `REMOVED` |
| `REJECTED` | Media failed processing or violates initial automated checks. | None (Terminal State) |
| `REMOVED` | Submission/media taken down due to moderation or user action. | None (Terminal State) |
| `FAILED` | Technical failure during upload or processing. | `UPLOADING` (Retry) |

**Commands:** `InitiateUpload`, `CompleteUpload`, `ProcessMedia`, `ApproveMedia`, `RejectMedia`, `FlagSubmission`, `RemoveSubmission`.
**Events:** `UploadInitiated`, `UploadCompleted`, `MediaProcessingStarted`, `MediaReady`, `MediaRejected`, `SubmissionFlagged`, `SubmissionRemoved`, `MediaProcessingFailed`.

### 3.4 Results, Disputes, and Appeals

Results represent the outcome of judging or audience voting. Disputes and appeals handle challenges to these outcomes.

| State | Description | Allowed Transitions |
|---|---|---|
| `PENDING_REVIEW` | Result submitted, awaiting automated or manual validation. | `CONFIRMED`, `DISPUTED` |
| `CONFIRMED` | Result is accepted and ready for settlement. | `APPEALED`, `SETTLED` |
| `DISPUTED` | A participant or system has flagged the result for review. | `CONFIRMED`, `OVERTURNED` |
| `APPEALED` | A formal escalation of a confirmed or disputed result. | `CONFIRMED`, `OVERTURNED` |
| `OVERTURNED` | The original result is invalidated and replaced. | `SETTLED` |
| `SETTLED` | The result is final and financial/reputational actions are complete. | None (Terminal State) |

**Commands:** `SubmitResult`, `ConfirmResult`, `RaiseDispute`, `FileAppeal`, `ResolveDispute`, `OverturnResult`, `FinalizeSettlement`.
**Events:** `ResultSubmitted`, `ResultConfirmed`, `DisputeRaised`, `AppealFiled`, `DisputeResolved`, `ResultOverturned`, `SettlementFinalized`.

### 3.5 Marketplace Orders and Service Contracts

Marketplace orders handle the purchase of digital goods, licenses, or physical items. Service contracts govern commissions and freelance work.

| State | Description | Allowed Transitions |
|---|---|---|
| `INITIATED` | Buyer has started the checkout or contract creation process. | `PENDING_PAYMENT`, `CANCELLED` |
| `PENDING_PAYMENT` | Awaiting confirmation of funds transfer or credit deduction. | `PAID`, `FAILED`, `CANCELLED` |
| `PAID` | Funds secured. For digital goods, delivery is imminent. For services, work begins. | `DELIVERED`, `IN_PROGRESS`, `REFUNDED` |
| `IN_PROGRESS` | (Service Contracts) Creator is working on the commission. | `DELIVERED`, `DISPUTED`, `CANCELLED` |
| `DELIVERED` | Digital good provided or service completed. | `COMPLETED`, `DISPUTED` |
| `DISPUTED` | Buyer or seller raises an issue with delivery or quality. | `COMPLETED`, `REFUNDED` |
| `COMPLETED` | Transaction final. Funds released to seller. | None (Terminal State) |
| `REFUNDED` | Transaction reversed. Funds returned to buyer. | None (Terminal State) |
| `FAILED` | Payment or delivery failed technically. | None (Terminal State) |
| `CANCELLED` | Order/contract aborted before payment or work commenced. | None (Terminal State) |

**Commands:** `InitiateOrder`, `ProcessPayment`, `ConfirmPayment`, `StartWork`, `DeliverOrder`, `CompleteOrder`, `RaiseOrderDispute`, `RefundOrder`, `CancelOrder`, `FailOrder`.
**Events:** `OrderInitiated`, `PaymentPending`, `PaymentConfirmed`, `WorkStarted`, `OrderDelivered`, `OrderCompleted`, `OrderDisputed`, `OrderRefunded`, `OrderCancelled`, `OrderFailed`.

### 3.6 Credits, Conversions, and Escrow

Credits are the internal currency of Artist Arena. Conversions handle moving value between fiat and credits. Escrow holds funds during active competitions or contracts.

| State | Description | Allowed Transitions |
|---|---|---|
| `PENDING` | Conversion requested, awaiting external provider confirmation. | `COMPLETED`, `FAILED`, `CANCELLED` |
| `ESCROWED` | Credits locked for a battle entry, wager, or service contract. | `RELEASED`, `REFUNDED`, `FORFEITED` |
| `RELEASED` | Escrowed funds transferred to the intended recipient (winner/seller). | None (Terminal State) |
| `REFUNDED` | Escrowed funds returned to the original sender. | None (Terminal State) |
| `FORFEITED` | Funds seized due to penalty or rule violation. | None (Terminal State) |
| `COMPLETED` | Conversion successful. Credits minted or fiat disbursed. | None (Terminal State) |
| `FAILED` | Conversion failed due to provider error or insufficient funds. | None (Terminal State) |
| `CANCELLED` | Conversion aborted by user or system before completion. | None (Terminal State) |

**Commands:** `RequestConversion`, `CompleteConversion`, `FailConversion`, `CancelConversion`, `LockEscrow`, `ReleaseEscrow`, `RefundEscrow`, `ForfeitEscrow`.
**Events:** `ConversionRequested`, `ConversionCompleted`, `ConversionFailed`, `ConversionCancelled`, `EscrowLocked`, `EscrowReleased`, `EscrowRefunded`, `EscrowForfeited`.

### 3.7 Payouts and Chargebacks

Payouts handle the withdrawal of funds. Chargebacks represent external disputes initiated via payment providers.

| State | Description | Allowed Transitions |
|---|---|---|
| `REQUESTED` | User requested a payout. | `PROCESSING`, `HELD`, `REJECTED` |
| `PROCESSING` | Payout is being handled by the external provider. | `COMPLETED`, `FAILED` |
| `HELD` | Payout paused for compliance, fraud review, or audit. | `PROCESSING`, `REJECTED` |
| `COMPLETED` | Funds successfully transferred to the user's external account. | None (Terminal State) |
| `REJECTED` | Payout denied due to policy violation or failed verification. | None (Terminal State) |
| `FAILED` | Technical failure during the payout process. | `REQUESTED` (Retry) |
| `CHARGEBACK_INITIATED` | External payment provider notified of a chargeback. | `CHARGEBACK_DISPUTED`, `CHARGEBACK_ACCEPTED` |
| `CHARGEBACK_DISPUTED` | Artist Arena is contesting the chargeback with evidence. | `CHARGEBACK_WON`, `CHARGEBACK_LOST` |
| `CHARGEBACK_ACCEPTED` | Artist Arena accepts the chargeback without dispute. | None (Terminal State) |
| `CHARGEBACK_WON` | Dispute successful; funds retained. | None (Terminal State) |
| `CHARGEBACK_LOST` | Dispute unsuccessful; funds returned to external source; internal balance adjusted. | None (Terminal State) |

**Commands:** `RequestPayout`, `ProcessPayout`, `HoldPayout`, `CompletePayout`, `RejectPayout`, `FailPayout`, `InitiateChargeback`, `DisputeChargeback`, `AcceptChargeback`, `WinChargeback`, `LoseChargeback`.
**Events:** `PayoutRequested`, `PayoutProcessing`, `PayoutHeld`, `PayoutCompleted`, `PayoutRejected`, `PayoutFailed`, `ChargebackInitiated`, `ChargebackDisputed`, `ChargebackAccepted`, `ChargebackWon`, `ChargebackLost`.

### 3.8 Blockchain Transactions and Finality

This state machine governs the lifecycle of transactions submitted to the native Artist Arena blockchain.

| State | Description | Allowed Transitions |
|---|---|---|
| `CONSTRUCTED` | Transaction payload built and signed. | `BROADCASTED`, `FAILED` |
| `BROADCASTED` | Transaction sent to the network mempool. | `INCLUDED`, `DROPPED` |
| `INCLUDED` | Transaction included in a block (optimistic). | `FINALIZED`, `REVERTED` |
| `FINALIZED` | Transaction has reached cryptographic finality. | None (Terminal State) |
| `REVERTED` | Transaction failed execution on-chain or block was reorganized out. | `CONSTRUCTED` (Retry) |
| `DROPPED` | Transaction removed from mempool (e.g., due to low fees or timeout). | `CONSTRUCTED` (Retry) |
| `FAILED` | Error during construction or signing. | None (Terminal State) |

**Commands:** `ConstructTransaction`, `BroadcastTransaction`, `ConfirmInclusion`, `ConfirmFinality`, `HandleRevert`, `HandleDrop`, `FailTransaction`.
**Events:** `TransactionConstructed`, `TransactionBroadcasted`, `TransactionIncluded`, `TransactionFinalized`, `TransactionReverted`, `TransactionDropped`, `TransactionFailed`.

### 3.9 Moderation Cases

Moderation cases handle reports of policy violations, copyright infringement, or abusive behavior.

| State | Description | Allowed Transitions |
|---|---|---|
| `OPEN` | Report received and case created. | `UNDER_REVIEW`, `AUTO_RESOLVED` |
| `UNDER_REVIEW` | A trust analyst or automated system is actively investigating. | `ACTION_TAKEN`, `DISMISSED` |
| `ACTION_TAKEN` | Moderation action (e.g., ban, content removal) applied. | `APPEALED`, `CLOSED` |
| `DISMISSED` | Report found to be invalid or unactionable. | `CLOSED` |
| `APPEALED` | User appeals the moderation action. | `UNDER_REVIEW` |
| `CLOSED` | Case finalized and archived. | None (Terminal State) |
| `AUTO_RESOLVED` | Case handled entirely by automated policy engines. | `CLOSED` |

**Commands:** `OpenCase`, `StartReview`, `TakeAction`, `DismissCase`, `AppealCase`, `CloseCase`, `AutoResolveCase`.
**Events:** `CaseOpened`, `ReviewStarted`, `ActionTaken`, `CaseDismissed`, `CaseAppealed`, `CaseClosed`, `CaseAutoResolved`.

## 4. Failure and Degraded Behavior

The system must handle failures gracefully, ensuring that data corruption and financial discrepancies are prevented.

- **Idempotency:** All commands altering financial or critical state must be idempotent.
- **Dead Letter Queues (DLQ):** Events that fail processing after retries must be routed to a DLQ for manual inspection and replay.
- **Circuit Breakers:** External integrations (e.g., payment providers, blockchain RPCs) must be protected by circuit breakers to prevent cascading failures.
- **Degraded Mode:** If the blockchain network is unavailable, non-critical reads can be served from the Neon database cache. Critical financial transactions must be queued or rejected with a clear user message until connectivity is restored.

## 5. Security, Privacy, Rights, and Compliance

- **Data Ownership:** Creators retain ownership of their intellectual property. The blockchain anchors licenses and consent metadata.
- **Privacy:** Personal Identifiable Information (PII) and raw media files are never stored directly on the public blockchain. Only cryptographic hashes and decentralized identifiers (DIDs) are anchored.
- **Compliance Gates:** While all capabilities (including real-money wagering and cash-outs) are fully implemented in V1, their execution is gated by the policy engine. A user's jurisdiction, age, and identity verification status dictate whether they can transition states in the financial state machines.
- **Auditability:** Every state transition emits an immutable event. Financial state transitions are additionally anchored to the blockchain to provide a verifiable audit trail.

## 6. Observability and Performance

- **Tracing:** Distributed tracing must correlate API requests, state machine commands, and emitted events.
- **Metrics:** Key metrics include state transition latency, event processing throughput, DLQ depth, and blockchain finality times.
- **SLAs:** The system targets a P95 latency of <200ms for standard state transitions (excluding blockchain finality, which depends on network consensus).

## 7. Tests and Acceptance

- **Unit Tests:** Every state machine must have exhaustive unit tests covering all valid transitions and rejecting all invalid transitions.
- **Integration Tests:** End-to-end tests must simulate full user journeys (e.g., from battle creation to final payout), verifying interactions between the Neon database, R2 storage, and the blockchain module.
- **Adversarial Testing:** Financial state machines must undergo adversarial testing to ensure resilience against double-spend attempts, race conditions, and unauthorized state manipulations.
- **Acceptance Criteria:** A feature is only considered "Done" when its state machine is fully implemented, tested, and capable of operating in a real-world scenario (even if currently gated by policy in production).

## 8. Dependency-Ordered Work Packages

1.  **Core Infrastructure:** Setup Neon schemas, Cloudflare Workers routing, and R2 buckets.
2.  **Identity and Policy Engine:** Implement RBAC/ABAC and the configuration-driven policy gates.
3.  **Media and Submissions:** Implement the media upload, processing, and submission state machines.
4.  **Battles and Challenges:** Implement the core competition state machines.
5.  **Blockchain Foundation:** Deploy the native blockchain node, consensus mechanism, and state sync.
6.  **Financial Ledger:** Implement credits, escrow, and conversion state machines, integrated with the blockchain.
7.  **Moderation and Disputes:** Implement the moderation case and dispute resolution state machines.
8.  **Marketplace and Commerce:** Implement the order and service contract state machines.
9.  **Integration and E2E Testing:** Connect all domains and perform comprehensive adversarial and journey testing.

## 9. Open ADRs (Architecture Decision Records)

- **ADR-001:** Selection of specific consensus mechanism for the native blockchain (e.g., Tendermint vs. Substrate).
- **ADR-002:** Detailed schema for on-chain provenance metadata to balance privacy and verifiability.
- **ADR-003:** Specific payment provider integration strategies for handling chargebacks and localized payout methods.

## 10. References

[1] ARTIST-ARENA-V1-Master-Specification.md
[2] 0001-v1-build-complete.md
