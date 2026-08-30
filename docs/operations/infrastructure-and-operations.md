# Artist Arena V1 Infrastructure and Operations Architecture Specification

## 1. Executive Summary

This document specifies the implementation-grade infrastructure and operations architecture for Artist Arena V1. It is designed as a modular monolith deployed primarily on Cloudflare infrastructure, utilizing Neon for relational data and Cloudflare R2 for media storage. The architecture supports a discipline-agnostic creator economy platform, incorporating mandatory V1 capabilities including a native blockchain path, real-value economic transactions, comprehensive security, and strict operational controls.

The design adheres to the Owner Directive 0001, ensuring that all capabilities previously marked as future, later, non-goal, post-V1, gated, sandbox-only, or disabled are included in the V1 construction scope. While the deployment and activation of certain features may be gated by policy, jurisdiction, or founder approval, their architectural foundation, implementation, and testability are mandatory.

## 2. Guiding Principles

1.  **Build-Complete V1:** All capabilities described in the product canon are mandatory V1 engineering scope.
2.  **Modular Monolith:** A cohesive codebase with event-driven boundaries, avoiding premature microservice fragmentation while enabling independent scaling and future extraction.
3.  **Cloudflare Native:** Maximize the use of Cloudflare Workers, Durable Objects, Queues, and R2 for global distribution, low latency, and operational simplicity.
4.  **Immutable Financial Records:** All economic transactions, including credit purchases, wagers, prize pools, and creator payments, must be recorded in an immutable ledger.
5.  **Blockchain as Infrastructure:** A native blockchain path is mandatory for provenance, rights, competition evidence, escrow, and settlement, abstracting mechanics from the user experience while ensuring auditability.
6.  **Strict TypeScript:** End-to-end type safety using strict TypeScript configurations.
7.  **Provider Adapters:** Abstract external dependencies (payments, identity, blockchain nodes) behind provider-neutral adapters to facilitate testing, mock environments, and future provider swaps.

## 3. High-Level Architecture

The Artist Arena V1 architecture is composed of the following core layers:

### 3.1 Edge Compute and Routing (Cloudflare Workers)

*   **API Gateway:** Handles routing, authentication, rate limiting, and initial request validation.
*   **Application Workers:** Implement the core business logic (user management, battle coordination, marketplace, etc.).
*   **Media Workers:** Specialized workers for media upload, processing (transcoding, resizing), and secure delivery via R2.

### 3.2 State Management and Real-time (Cloudflare Durable Objects)

*   **Battle State DO:** Manages the lifecycle of active battles, ensuring transactional integrity for entries, wagers, and state transitions.
*   **Ledger DO:** Handles high-throughput, transactional financial operations, ensuring double-entry accounting principles.
*   **Real-time DO:** Manages WebSocket connections for live updates, chat, and audience participation.

### 3.3 Asynchronous Processing (Cloudflare Queues)

*   **Event Bus:** Decouples services by routing domain events (e.g., `BattleCompleted`, `MediaUploaded`, `PaymentProcessed`).
*   **Background Jobs:** Handles tasks such as email delivery, push notifications, search indexing, and blockchain transaction submission.

### 3.4 Data Storage

*   **Relational Database (Neon Postgres):** The primary source of truth for user profiles, relationships, historical battle data, configuration, and the immutable financial ledger. Accessed via Drizzle ORM.
*   **Object Storage (Cloudflare R2):** Stores all user-uploaded media (audio, video, images) and static assets.
*   **Search (Typesense / Elasticsearch via adapter):** Provides fast, faceted search for creators, battles, and marketplace items.

### 3.5 Blockchain Infrastructure

*   **Native Chain / App-Chain:** A sovereign blockchain implementation for provenance, rights management, and settlement.
*   **Node Infrastructure:** Managed nodes or provider adapters for interacting with the blockchain network.

## 4. Component Boundaries and Typed Contracts

The system is organized into distinct domain modules, communicating via well-defined, typed contracts.

### 4.1 Core Domains

| Domain | Responsibilities | Key Entities |
| :--- | :--- | :--- |
| **Identity & Access** | Authentication, authorization, RBAC/ABAC, user profiles, verification status. | `User`, `Role`, `Session`, `Verification` |
| **Competition** | Battles, tournaments, challenges, rule sets, judging, scoring. | `Battle`, `Tournament`, `Submission`, `Score` |
| **Economy & Ledger** | Credits, wagers, prize pools, creator payments, cash-out, immutable ledger. | `Account`, `Transaction`, `Hold`, `Wager` |
| **Media & Provenance** | Uploads, transcoding, storage, content hashing, AI disclosures, rights management. | `MediaAsset`, `License`, `ProvenanceRecord` |
| **Social & Community** | Follows, comments, teams, notifications, live events. | `Follow`, `Comment`, `Team`, `Notification` |
| **Moderation & Trust** | Reporting, dispute resolution, fraud detection, compliance checks. | `Report`, `Dispute`, `AuditLog` |

### 4.2 Event-Driven Contracts (Example)

Events are defined using strict TypeScript interfaces and validated before being published to Cloudflare Queues.

```typescript
// Example: Battle Completed Event
interface BattleCompletedEvent {
  eventId: string;
  timestamp: string;
  battleId: string;
  winnerId: string;
  loserId: string;
  prizePoolAmount: number;
  currency: 'CREDITS' | 'USD';
  settlementStatus: 'PENDING' | 'COMPLETED';
}
```

## 5. Data and State Management

### 5.1 Relational Schema (Neon Postgres & Drizzle)

The database schema must support the full breadth of V1 requirements.

*   **Users:** `id`, `handle`, `email`, `password_hash`, `status`, `verification_level`, `created_at`, `updated_at`.
*   **Ledger:** `id`, `account_id`, `amount`, `currency`, `type` (CREDIT, DEBIT), `reference_type` (BATTLE, DEPOSIT, WITHDRAWAL), `reference_id`, `created_at`.
*   **Battles:** `id`, `organizer_id`, `status` (DRAFT, OPEN, ACTIVE, JUDGING, COMPLETED, CANCELLED), `discipline`, `entry_fee`, `prize_pool`, `created_at`, `updated_at`.

### 5.2 State Transitions (Durable Objects)

Complex state machines, such as the lifecycle of a battle, are managed within Durable Objects to ensure consistency and prevent race conditions.

*   **Battle State Machine:** `Draft` -> `Open` -> (Participants Join, Funds Reserved) -> `Active` -> (Submissions) -> `Judging` -> (Scores Finalized) -> `Completed` -> (Settlement).

### 5.3 Immutable Financial Records

All financial transactions must adhere to double-entry accounting principles. A transaction must credit one account and debit another equally. The ledger is append-only; corrections are made via compensating transactions, never by updating existing records.

## 6. Mandatory V1 Blockchain Integration

The native blockchain path is a core architectural requirement, providing a verifiable layer for provenance and economic settlement while minimizing on-chain PII and large media files.

### 6.1 Blockchain Architecture

*   **Network:** A permissioned or sovereign app-chain optimized for high throughput and low transaction costs.
*   **Consensus:** A fast finality consensus mechanism (e.g., Tendermint/CometBFT or similar).
*   **State Model:** Stores cryptographic hashes of media, license references, creator splits, and settlement attestations.

### 6.2 Key Capabilities

| Capability | On-Chain Implementation | Off-Chain (Database/R2) |
| :--- | :--- | :--- |
| **Provenance** | Content hash, timestamp, creator address, license ID. | Actual media file, detailed AI disclosure text. |
| **Competition Evidence** | Ruleset hash, submission commitments, result attestation. | Full submission media, detailed judge feedback. |
| **Escrow & Settlement** | Smart contract managing prize pools, enforcing splits and payouts based on attested results. | User balances (synced), fiat payment gateway interactions. |

### 6.3 Data Privacy

Personal Identifiable Information (PII) and large media assets are strictly stored off-chain. The blockchain only stores cryptographic commitments, public keys, and pseudonymous identifiers.

## 7. Security, Privacy, and Compliance

### 7.1 Security Controls

*   **Authentication:** Multi-factor authentication (MFA) support, secure session management, and strict password policies.
*   **Authorization:** Granular RBAC and ABAC applied at the API Gateway and within Application Workers.
*   **Data Protection:** Encryption at rest (Neon, R2) and in transit (TLS 1.3). Sensitive data (e.g., payment details) must be tokenized and handled by compliant providers.
*   **Secrets Management:** Secrets must be injected via Cloudflare environment variables, never hardcoded or committed to the repository.

### 7.2 Privacy and Rights

*   **Consent Management:** Clear tracking of user consent for data usage, cookies, and marketing.
*   **Data Minimization:** Collect only necessary data. Implement automated data retention and deletion policies.
*   **Rights Controls:** Mechanisms for creators to specify licenses, manage splits, and issue DMCA takedown requests.

### 7.3 Compliance Gates

While all features are built, activation is controlled by a policy engine.

*   **Jurisdiction Blocking:** IP-based and KYC-based blocking of real-money features in restricted regions.
*   **Age Verification:** Mandatory age checks for participation in real-money contests or accessing mature content.
*   **KYC/AML:** Integration with identity verification providers (e.g., Stripe Identity, Persona) before enabling cash-out or high-value transactions.

## 8. Operations, Observability, and Deployment

### 8.1 Infrastructure as Code (IaC)

All infrastructure (Cloudflare, Neon, R2) must be provisioned and managed using IaC tools (e.g., Terraform, Pulumi, or Cloudflare Wrangler configurations). Manual configuration via UI is prohibited for production environments.

### 8.2 Environments

*   **Local:** Developer machines using Miniflare/Wrangler for Cloudflare emulation and local Postgres.
*   **Sandbox/Test:** Automated testing environment with mock providers.
*   **Staging:** Pre-production environment mirroring production configuration.
*   **Production:** Live environment with real user data and active policy gates.

### 8.3 Observability and SLOs

*   **Logging:** Structured JSON logging across all workers, aggregated into a centralized logging platform (e.g., Datadog, Axiom).
*   **Metrics:** Tracking API latency, error rates, queue depths, and business metrics (e.g., active battles, transaction volume).
*   **Tracing:** Distributed tracing (OpenTelemetry) to track requests across the API Gateway, Workers, and Database.
*   **SLOs:**
    *   API Availability: 99.9%
    *   P95 Latency (Read): < 100ms
    *   P95 Latency (Write): < 250ms

### 8.4 Incident Response and Disaster Recovery

*   **Alerting:** Automated alerts based on SLO breaches, high error rates, or security anomalies.
*   **Runbooks:** Documented procedures for handling common incidents (e.g., database failover, payment provider outage).
*   **Backup/Restore:** Automated, encrypted backups of the Neon database (point-in-time recovery) and R2 buckets. Regular restoration drills must be conducted.

## 9. Dependency-Ordered Work Packages

The V1 implementation is structured into sequential work packages to ensure foundational components are established before complex features are added.

1.  **Phase 1: Foundation & Infrastructure:** Monorepo setup, IaC, database schema initialization, authentication, basic user profiles.
2.  **Phase 2: Core Competition Engine:** Battle state machine (Durable Objects), media upload (R2), basic scoring, event bus setup.
3.  **Phase 3: Immutable Economy:** Ledger implementation, virtual credits, simulated wagering, provider adapters (mocked).
4.  **Phase 4: Blockchain Integration:** Node setup, provenance smart contracts, state synchronization.
5.  **Phase 5: Social & Discovery:** Search indexing, feeds, follows, notifications.
6.  **Phase 6: Moderation & Compliance:** Policy engine, reporting, KYC/AML adapters, jurisdiction gating.
7.  **Phase 7: Real-Value Activation (Gated):** Live payment provider integration, cash-out flows, rigorous security auditing.

## 10. Open Architecture Decision Records (ADRs)

*   **ADR-001: Selection of Search Provider:** Evaluate Typesense vs. Elasticsearch for cost, latency, and operational overhead within the Cloudflare ecosystem.
*   **ADR-002: Blockchain Consensus Mechanism:** Finalize the selection of the consensus algorithm for the native app-chain, balancing speed, decentralization, and operational cost.
*   **ADR-003: Real-time Infrastructure:** Decide between Cloudflare Durable Objects WebSockets vs. a dedicated real-time provider (e.g., Pusher, Ably) for live chat and voting at scale.


## 11. Detailed Component Specifications

### 11.1 API Gateway and Routing Logic

The API Gateway, implemented as a Cloudflare Worker, serves as the single entry point for all client requests. It is responsible for:

*   **Request Routing:** Directing incoming HTTP requests to the appropriate backend service or Durable Object based on the URL path and HTTP method.
*   **Authentication & Authorization:** Verifying JWTs (JSON Web Tokens) or session cookies to authenticate users. It then checks the user's roles and permissions against the requested resource (RBAC/ABAC).
*   **Rate Limiting:** Protecting the backend from abuse and denial-of-service attacks by enforcing rate limits based on IP address or user ID.
*   **Input Validation:** Performing initial validation of request payloads (e.g., checking for required fields, validating data types) before passing the request to the application logic.
*   **CORS Management:** Handling Cross-Origin Resource Sharing (CORS) preflight requests and setting appropriate headers.

### 11.2 Media Processing Pipeline

The Media Processing Pipeline is crucial for handling the diverse range of creator uploads (audio, video, images).

*   **Upload Flow:** Clients request a pre-signed URL from the API Gateway. They then upload the media directly to a Cloudflare R2 bucket using this URL, bypassing the application workers to reduce load.
*   **Processing Triggers:** Upon successful upload, an event is published to a Cloudflare Queue. A dedicated Media Worker consumes this event and begins processing.
*   **Transcoding & Optimization:** For video and audio, the Media Worker may use external services (e.g., AWS Elemental MediaConvert, Mux) or internal FFmpeg-based processes (if feasible within Worker limits) to transcode the media into web-optimized formats (e.g., HLS for streaming, WebP for images).
*   **Content Hashing:** The Media Worker calculates a cryptographic hash (e.g., SHA-256) of the original file. This hash is stored in the database and eventually anchored on the blockchain for provenance.
*   **Storage & Delivery:** The processed files are stored back in R2 and served to clients via the Cloudflare CDN, ensuring low latency and high availability.

### 11.3 Ledger and Financial Operations

The Ledger is the heart of the Artist Arena economy, handling all transactions with strict consistency and auditability.

*   **Double-Entry Accounting:** Every financial movement involves at least two ledger entries (a debit and a credit) that sum to zero. This ensures that money is never created or destroyed arbitrarily.
*   **Transaction Types:** The ledger supports various transaction types, including:
    *   `DEPOSIT`: User adds funds via a payment provider.
    *   `WITHDRAWAL`: User cashes out funds.
    *   `WAGER_RESERVE`: Funds are held in escrow when a user enters a battle.
    *   `WAGER_RELEASE`: Funds are returned if a battle is cancelled.
    *   `PRIZE_PAYOUT`: Funds are distributed to winners and the platform (fees).
    *   `CREATOR_PAYMENT`: User pays a creator (e.g., subscription, tip).
*   **Idempotency:** All ledger operations must be idempotent to prevent double-charging in case of network retries. Clients must provide a unique idempotency key with each financial request.
*   **Reconciliation:** Automated background jobs periodically reconcile the internal ledger balances with the records of external payment providers (e.g., Stripe, PayPal) to detect and resolve discrepancies.

### 11.4 Blockchain Smart Contracts (Native Path)

The native blockchain path utilizes smart contracts to enforce rules and ensure transparency without relying solely on the centralized database.

*   **Provenance Contract:** Stores the cryptographic hash of creator uploads, along with the creator's public address, timestamp, and any associated license identifiers. This provides an immutable record of creation.
*   **Competition Contract:** Manages the lifecycle of a battle on-chain. It stores the ruleset hash, participant commitments (e.g., wager amounts), and the final attested results from the judges.
*   **Escrow & Settlement Contract:** Holds prize pools in escrow during a competition. Once the results are finalized and attested by authorized oracles (the platform's backend), the contract automatically distributes the funds according to the predefined splits (winners, platform fees, sponsors).

### 11.5 Moderation and Trust Systems

Maintaining a safe and fair environment is critical for Artist Arena.

*   **Automated Scanning:** Uploaded media and text are scanned by automated systems (e.g., Cloudflare Web Application Firewall, external AI moderation APIs) for CSAM, malware, hate speech, and other prohibited content.
*   **User Reporting:** Users can flag content, profiles, or battle results for review. Reports are categorized and prioritized based on severity and the reporter's trust score.
*   **Moderation Dashboard:** A dedicated interface for Trust & Safety analysts to review reports, view context (e.g., chat logs, previous offenses), and take action (e.g., remove content, suspend accounts, issue warnings).
*   **Dispute Resolution:** A formalized process for handling disputes related to wagers, creator payments, or copyright claims (DMCA). The system tracks the status of disputes, evidence submitted, and the final resolution.

## 12. Testing and Quality Assurance

A rigorous testing strategy is mandatory to ensure the reliability and security of the platform, especially concerning financial transactions and competitive integrity.

*   **Unit Tests:** Comprehensive unit tests for all business logic, particularly the state machines (Durable Objects) and ledger operations. Must achieve high code coverage.
*   **Integration Tests:** Tests verifying the interaction between different components, such as the API Gateway, Workers, Database, and external provider adapters.
*   **End-to-End (E2E) Tests:** Automated tests simulating user journeys (e.g., creating an account, depositing funds, entering a battle, winning, and cashing out) to ensure the entire system works cohesively.
*   **Security Audits:** Regular penetration testing and code reviews by external security firms, focusing on the financial ledger, authentication mechanisms, and smart contracts.
*   **Adversarial Testing:** Simulating malicious behavior (e.g., concurrent wager attempts, race conditions in state transitions, fraudulent uploads) to identify and mitigate vulnerabilities.

## 13. Future Considerations (Post-V1)

While V1 encompasses the full foundational scope, certain expansions are planned for subsequent phases.

*   **Native Mobile Applications:** Developing dedicated iOS and Android apps using frameworks like React Native or Flutter, connecting to the established V1 APIs.
*   **Native Livestreaming:** Integrating a fully native, low-latency livestreaming solution (e.g., Cloudflare Stream) directly into the platform, replacing or augmenting external embeds.
*   **Advanced AI Integrations:** Expanding AI capabilities for content discovery, personalized recommendations, and sophisticated moderation analysis, while maintaining the clear distinction between Human, Hybrid, and AI Open divisions.
*   **Decentralized Identity (DID):** Exploring the integration of DID standards to give creators more control over their identity and reputation across different platforms.
