# Artist Arena V1 Data Model Specification

## 1. Overview and Architectural Directives

This document outlines the complete relational and on-chain data model for Artist Arena V1. It is derived from the master specification and explicitly adheres to Owner Directive 0001, which mandates that all features—including the native blockchain, credits, wagers, cash-out, and multi-discipline support—must be architected and implemented in V1, regardless of real-world activation gates. The architecture follows a modular monolith approach with event-driven boundaries, leveraging a Cloudflare/Neon/R2 stack with strict TypeScript, provider adapters, and immutable financial records.

The primary goal of this data model is to provide a robust, scalable, and secure foundation for the competitive infrastructure layer of the global creator economy. It bridges the gap between high-performance relational data necessary for user experience and the immutable, trustless nature of blockchain technology required for provenance, escrow, and financial settlement. By strictly adhering to the owner directive, this specification ensures that no feature is deferred to a future version simply due to regulatory or business activation gates; the engineering capability must exist in V1.

The system is designed to support a wide array of creative disciplines—including music, beat production, rap, dance, visual art, film, writing, gaming, and AI creation—while maintaining stable, discipline-agnostic core primitives. The separation of Pure Human, Hybrid, and AI Open divisions is enforced at the data layer to guarantee transparency and fair competition.

## 2. Relational Data Model (Neon PostgreSQL)

The relational database handles high-throughput operations, user management, content metadata, and off-chain states. It is designed to support the immediate performance needs of a global platform while maintaining strict referential integrity. The use of Neon PostgreSQL provides scalable, serverless database capabilities suited for variable workloads.

### 2.1 Users, Identity, and Access Control

The user domain is the foundation of the platform, managing identity, roles, and compliance states. It strictly separates authentication credentials from public profiles and sensitive compliance data.

| Entity | Primary Key | Attributes | Description |
|---|---|---|---|
| `User` | `id` (UUID) | `handle` (String, Unique), `email` (String, Unique), `role` (Enum: user, creator, verified_creator, judge, organizer, admin), `status` (Enum: active, suspended, banned), `created_at` (Timestamp), `updated_at` (Timestamp) | Core identity record. Authentication is handled via external providers, mapped to this internal UUID. |
| `Profile` | `id` (UUID) | `user_id` (UUID, FK), `bio` (Text), `avatar_url` (String), `banner_url` (String), `discipline_preferences` (JSONB), `social_links` (JSONB) | Public persona and display information. Separated from the User table to optimize query performance for public views. |
| `Verification` | `id` (UUID) | `user_id` (UUID, FK), `status` (Enum: pending, approved, rejected, expired), `provider` (String), `verified_at` (Timestamp), `document_hash` (String), `jurisdiction` (String) | KYC/AML status and compliance tracking. Crucial for enabling real-money features as mandated by V1 requirements. |
| `Wallet` | `id` (UUID) | `user_id` (UUID, FK), `balance_credits` (Numeric, Precision 18, Scale 4), `status` (Enum: active, locked, restricted), `currency` (String) | Off-chain ledger cache for rapid balance checks and user experience optimization. |
| `Team` | `id` (UUID) | `slug` (String, Unique), `name` (String), `description` (Text), `created_at` (Timestamp), `owner_id` (UUID, FK) | Collective identities for group participation, essential for bands, studios, or esports organizations. |
| `TeamMember` | `team_id`, `user_id` | `role` (Enum: admin, member, contributor), `joined_at` (Timestamp), `revenue_share` (Numeric) | Mapping entity for team rosters, permissions, and default split allocations. |

### 2.2 Content, Media, and R2 Integration

This domain manages the metadata and references to raw media files stored in Cloudflare R2, ensuring that large blobs are kept out of the relational database while maintaining strict access controls. It supports the diverse media types required by the multi-discipline mandate.

| Entity | Primary Key | Attributes | Description |
|---|---|---|---|
| `Media` | `id` (UUID) | `owner_id` (UUID, FK), `r2_key` (String), `content_type` (String), `size` (BigInt), `hash` (String, SHA-256), `duration_seconds` (Integer, Nullable) | Raw media references and technical metadata. The hash is used for both deduplication and on-chain provenance. |
| `Work` | `id` (UUID) | `owner_id` (UUID, FK), `title` (String), `description` (Text), `discipline` (Enum: music, art, video, etc.), `division` (Enum: Pure Human, Hybrid, AI Open), `created_at` (Timestamp) | Creative works submitted to the platform. The division attribute is mandatory for all works. |
| `WorkMedia` | `work_id`, `media_id` | `role` (Enum: primary, thumbnail, source_file, stem), `order` (Integer) | Mapping entity linking works to their component media, allowing complex multi-file submissions (e.g., project files + renders). |
| `License` | `id` (UUID) | `work_id` (UUID, FK), `type` (Enum: exclusive, non_exclusive, public_domain), `terms` (Text), `price_credits` (Numeric, Nullable) | Usage rights and restrictions associated with a work, facilitating the creator marketplace. |

### 2.3 Competitions, Battles, and Tournaments

The competition domain is the core engine of Artist Arena, supporting various formats from 1v1 battles to massive tournaments across multiple disciplines. It is designed to be highly flexible while maintaining strict state machines.

| Entity | Primary Key | Attributes | Description |
|---|---|---|---|
| `Competition` | `id` (UUID) | `type` (Enum: battle, tournament, challenge, ladder), `status` (Enum: draft, open, locked, voting, resolved, settled, disputed), `discipline` (Enum), `division` (Enum), `ruleset_hash` (String), `start_time` (Timestamp), `end_time` (Timestamp), `organizer_id` (UUID, FK) | Base competition record defining the parameters of the event. |
| `Entry` | `id` (UUID) | `competition_id` (UUID, FK), `user_id` (UUID, FK), `work_id` (UUID, FK), `status` (Enum: pending, accepted, rejected, disqualified), `submitted_at` (Timestamp) | Participant entry linking a user and a specific work to a competition. |
| `Wager` | `id` (UUID) | `entry_id` (UUID, FK), `amount` (Numeric), `status` (Enum: pending, reserved, committed, released, refunded), `escrow_id` (String) | Associated stakes for paid entries or 1v1 battles, linking to on-chain escrow. |
| `Vote` | `id` (UUID) | `competition_id` (UUID, FK), `voter_id` (UUID, FK), `entry_id` (UUID, FK), `weight` (Numeric), `criteria_scores` (JSONB), `submitted_at` (Timestamp) | Audience or judge evaluations. `criteria_scores` allows for complex, multi-dimensional judging rubrics. |
| `Result` | `id` (UUID) | `competition_id` (UUID, FK), `winner_id` (UUID, FK), `finalized_at` (Timestamp), `attestation_hash` (String), `prize_distribution` (JSONB) | Final outcome and reference to on-chain proof of settlement. |

### 2.4 Commerce, Marketplace, and Creator Economy

This domain handles the financial interactions beyond competition wagers, enabling creators to monetize their work directly through sales, subscriptions, and commissions.

| Entity | Primary Key | Attributes | Description |
|---|---|---|---|
| `Listing` | `id` (UUID) | `work_id` (UUID, FK), `seller_id` (UUID, FK), `price` (Numeric), `type` (Enum: sale, license, commission), `status` (Enum: active, inactive, sold_out) | Marketplace item definition, exposing works for purchase. |
| `Transaction` | `id` (UUID) | `buyer_id` (UUID, FK), `seller_id` (UUID, FK), `listing_id` (UUID, FK), `amount` (Numeric), `status` (Enum: pending, completed, refunded, disputed), `created_at` (Timestamp) | Purchase record for marketplace activities. |
| `Subscription` | `id` (UUID) | `subscriber_id` (UUID, FK), `creator_id` (UUID, FK), `tier` (String), `status` (Enum: active, past_due, canceled), `next_billing_date` (Timestamp), `amount` (Numeric) | Recurring support mechanisms for ongoing creator patronage. |
| `LedgerEntry` | `id` (UUID) | `wallet_id` (UUID, FK), `amount` (Numeric), `type` (Enum: deposit, withdrawal, fee, wager, prize, purchase, sale), `reference_id` (String), `created_at` (Timestamp) | Immutable off-chain accounting log. This is critical for auditability and reconciliation with payment providers. |

## 3. On-Chain Data Model (Native Blockchain)

The native blockchain is a mandatory V1 requirement, serving as the ultimate source of truth for provenance, rights, competition evidence, escrow, and settlement. It is designed to minimize on-chain storage of personal data and media files, relying instead on cryptographic hashes and attestations. This approach ensures scalability and privacy while maintaining the benefits of decentralization.

### 3.1 Provenance and Rights Management

This module anchors the existence and ownership of creative works at specific points in time, providing undeniable proof for copyright claims and dispute resolution.

| State Object | Attributes | Purpose |
|---|---|---|
| `WorkCommitment` | `creator_address` (Address), `work_hash` (Hash, SHA-256), `timestamp` (Timestamp), `license_flags` (Bitmask), `division_flag` (Byte) | Immutable proof of creation and ownership at a specific time. The division flag ensures AI disclosure is permanently recorded. |
| `SplitAgreement` | `work_hash` (Hash), `beneficiaries` (Array of {Address, Percentage, Role}) | Smart contract defining revenue routing for collaborative works, ensuring automatic, trustless distribution of earnings. |
| `ConsentRecord` | `subject_address` (Address), `work_hash` (Hash), `scope` (Enum: likeness, voice, ip_derivation), `revoked_at` (Timestamp, Nullable) | On-chain record of consent for use of likeness or IP, crucial for AI-generated or derivative works. |

### 3.2 Competition Evidence and Finality

This module ensures that the rules, participants, and outcomes of competitions cannot be altered retroactively, providing a transparent and verifiable history of all events.

| State Object | Attributes | Purpose |
|---|---|---|
| `ContestState` | `contest_id` (String, UUID mapping), `ruleset_hash` (Hash), `status` (Enum), `participants` (Array of Addresses), `start_block` (Integer), `end_block` (Integer) | Immutable record of contest parameters and participants. |
| `SubmissionCommitment` | `contest_id` (String), `participant_address` (Address), `work_hash` (Hash), `timestamp` (Timestamp) | Proof that a specific work was submitted to a specific contest before the deadline. |
| `ResultAttestation` | `contest_id` (String), `winner_address` (Address), `judge_signatures` (Array of Signatures), `score_hash` (Hash) | Cryptographically verifiable proof of the final outcome, signed by authorized judges or the platform oracle. |

### 3.3 Escrow, Settlement, and Economics

This module handles the locking and distribution of value, ensuring that wagers and prize pools are secure and that payouts are executed exactly according to the rules and the mandatory 1% fee structure.

| State Object | Attributes | Purpose |
|---|---|---|
| `EscrowAccount` | `contest_id` (String), `locked_balance` (Numeric), `conditions_hash` (Hash), `sponsor_address` (Address, Nullable) | Trustless holding of prize pools or wagers until resolution. Funds cannot be moved without the corresponding `ResultAttestation`. |
| `SettlementEvent` | `contest_id` (String), `recipients` (Array of Addresses), `amounts` (Array of Numeric), `fee_deducted` (Numeric), `timestamp` (Timestamp) | Immutable record of payout distribution. The smart contract logic explicitly enforces the 1% platform fee deduction before distribution. |
| `TokenContract` | `balances` (Map<Address, Numeric>), `allowances` (Map<Address, Map<Address, Numeric>>), `total_supply` (Numeric) | Native implementation of the platform credit system, facilitating all on-chain value transfers. |

## 4. State Transitions and Lifecycles

The system relies on strict state machines to ensure consistency between the high-speed relational database and the slower, immutable blockchain.

### 4.1 Competition Lifecycle

1. **DRAFT**: Organizer is configuring the rules, prize pool, and entry requirements in the relational database. No on-chain activity occurs yet.
2. **OPEN**: The competition is accepting entries and associated wagers/fees. A `ContestState` is initialized on-chain.
3. **LOCKED**: Entry period is closed. The relational database rejects new entries. All required funds are verified as committed to the on-chain `EscrowAccount`.
4. **VOTING**: Judges or audience members are evaluating the submissions off-chain.
5. **RESOLVED**: A winner has been determined by the off-chain system, pending finality and dispute windows.
6. **SETTLED**: The dispute window has closed. The off-chain system submits a `ResultAttestation` to the blockchain, triggering the `EscrowAccount` to release funds and generate a `SettlementEvent`.
7. **DISPUTED**: An outcome has been challenged by a participant or flagged by fraud controls, halting settlement until manual or tribunal review resolves the issue.

### 4.2 Wager and Escrow Lifecycle

1. **PENDING**: User intent to wager is recorded in the relational database.
2. **RESERVED**: Credits are locked in the off-chain `Wallet` ledger cache to prevent double-spending while the on-chain transaction is prepared.
3. **COMMITTED**: Funds are officially moved to the on-chain `EscrowAccount` via the `TokenContract`. The off-chain `Wager` status is updated upon blockchain confirmation.
4. **RELEASED**: Funds are distributed to the winner(s) upon contest settlement via the `SettlementEvent`.
5. **REFUNDED**: Funds are returned to the original wallets if the contest is cancelled, drawn, or fails to meet minimum participant thresholds.

## 5. Privacy, Security, and Compliance Classes

Data is classified to ensure appropriate storage and access controls, balancing transparency with privacy and regulatory requirements. This is critical for operating a platform that handles real money and personal identity.

| Class | Examples | Storage Location | Access Control |
|---|---|---|---|
| **Public** | Profiles, Public Works, Leaderboards, Competition Rules, Aggregated Analytics | Neon (Indexed for search) | Unrestricted access via public APIs. |
| **Protected** | Wager amounts, Private entries, Direct messages, Draft works | Neon (Row-Level Security) | Restricted to participants, authorized team members, and specific admin roles. |
| **Immutable** | Hashes, Attestations, Settlement records, Public Addresses | Native Blockchain | Publicly verifiable, but pseudonymous. No PII is stored here. |
| **Sensitive** | PII, KYC documents, Fiat banking details, Tax identification numbers | External Vault / Encrypted Storage (e.g., Stripe Identity, specialized compliance providers) | Restricted to compliance operators and automated verification systems only. Never exposed to general platform APIs. |

## 6. Failure and Degraded Behavior

The architecture is designed to degrade gracefully in the event of subsystem failures, ensuring that the platform remains usable even if specific components are temporarily unavailable.

- **Blockchain RPC Failure**: If the native chain is unreachable, off-chain operations (browsing, profile updates, media playback) continue normally. Wager commitments, escrow funding, and settlements are queued in the relational database and retried automatically via background workers once connectivity is restored.
- **R2 Storage Outage**: New media uploads fail gracefully with user-facing errors. Existing media cached via the Cloudflare CDN remains available for playback and viewing.
- **Payment Provider Downtime**: Fiat deposits and withdrawals are temporarily disabled with clear user messaging. Internal credit transfers, wagers using existing balances, and free competitions continue uninterrupted.
- **Database Degradation**: In the event of Neon read-replica lag, the system prioritizes consistency for financial transactions by routing them to the primary instance, while allowing eventual consistency for non-critical reads like follower counts.

## 7. Migration Strategy

The deployment of this complex data model requires a phased approach to ensure stability and data integrity.

1. **Initial Schema Deployment**: Deploy core relational tables via Prisma or Drizzle migrations, establishing the modular monolith foundation. This includes all user, media, and basic competition structures.
2. **Blockchain Genesis**: Launch the native chain with an initial validator set and deploy core smart contracts (Escrow, Token, Provenance). This must occur in V1 as per the directive.
3. **State Synchronization Engine**: Implement robust event listeners (e.g., using Kafka or Redis Streams) to synchronize off-chain Neon state with on-chain commitments, ensuring eventual consistency between the two systems.
4. **Data Portability and Export**: Ensure all user data, including media, metadata, and financial history, can be exported in standardized formats (JSON, CSV) to comply with data rights regulations (e.g., GDPR, CCPA).
5. **Provider Adapter Implementation**: Deploy the initial set of payment and identity provider adapters, ensuring they conform to the standardized interfaces defined in the architecture, allowing for easy swapping or addition of providers in the future.

## 8. Open Architectural Decision Records (ADRs)

The following decisions remain open for final technical review but must be resolved within the V1 development cycle:

- **ADR-001: Blockchain Consensus Mechanism**: Selection of the underlying consensus mechanism for the native blockchain (e.g., Tendermint vs. Substrate) balancing speed, finality, and validator hardware requirements.
- **ADR-002: Identity Mapping Strategy**: Specific mapping strategy between off-chain UUIDs and on-chain cryptographic addresses to maintain privacy while allowing verifiable claims and seamless user experience.
- **ADR-003: 1% Fee Implementation**: Exact implementation mechanism for the mandatory 1% conversion fee deduction (whether calculated off-chain and enforced via contract parameters, or natively programmed into the token transfer logic at the protocol level).
- **ADR-004: Media Hashing Algorithm**: Definition of the exact cryptographic hashing algorithm used for media provenance (e.g., SHA-256 vs. BLAKE3) to ensure long-term collision resistance and performance during large file uploads.
- **ADR-005: Event Bus Technology**: Selection of the event bus technology (e.g., Apache Kafka, AWS EventBridge, or Redis Streams) for managing the event-driven boundaries within the modular monolith and synchronizing with the blockchain indexer.
