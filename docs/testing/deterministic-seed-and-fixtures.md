# Artist Arena V1: Deterministic Seed, Fixtures, Mocks, and Demonstration Plan

## 1. Overview

This document defines the deterministic seed, fixtures, mocks, and demonstration plan for Artist Arena V1, acting as a mandatory implementation-control artifact for CodeSpring execution. It translates the locked product canon from the Master Specification [1] and the comprehensive V1 build mandate from Owner Directive 0001 [2] into a testable, reproducible state.

All capabilities, including native blockchain, wallets, purchased credits, 1% conversions, paid entry, one-to-one wagers, escrow, settlement, and multi-discipline support, must be mocked, seeded, and verifiable in local/testnet environments regardless of real-world activation gates [2].

## 2. Deterministic Seed Configuration

To ensure reproducibility across all environments (local, continuous integration, testnet, staging), the system must utilize a deterministic seeding mechanism. The global random seed is set to `0xAA20260830V1CORE`, which must be used for all pseudo-random number generation in data creation. The time clock anchor is established as `2026-08-30T00:00:00Z`, ensuring all relative dates in fixtures derive from this fixed point. The testnet chain identifier is defined as `artist-arena-testnet-1`. For financial simulations, the base currency mock is `USD_MOCK`, and the platform token is designated as `ARENA_CREDIT`, where one credit is equivalent to one mock US dollar. The configuration-driven conversion fee default is set at 1.00% [1].

The system must support a hard reset to the deterministic seed state via an administrative command, such as `make reset-seed`. This process must sequentially wipe all relational databases, key-value stores, and local ledger state. Following the wipe, it must initialize the genesis block for the native blockchain testnet. The system then loads configuration flags and policy engine defaults before injecting the defined fixtures and personas in dependency order.

## 3. Fixtures and Personas

The seed data must populate the system with a diverse, non-infringing set of fictional personas and organizations that exercise every role, discipline, and division.

### 3.1 Fictional Personas

| ID | Handle | Role | Discipline | Division | Status | Balances | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `USR-001` | `@lyric_forge` | Competitor | Rap/Freestyle | Pure Human | Verified | 500 Credits | High win rate, frequent wagerer. |
| `USR-002` | `@synth_weaver` | Competitor | Beat Prod. | Hybrid | Active | 150 Credits | Discloses AI sample generation. |
| `USR-003` | `@pixel_ghost` | Competitor | Visual Art | AI Open | Active | 1000 Credits | Sells generated assets in marketplace. |
| `USR-004` | `@judge_dread` | Judge/Curator | Music | N/A | Verified | 0 Credits | High reputation, strict scoring. |
| `USR-005` | `@fan_prime` | Audience | N/A | N/A | Active | 50 Credits | Subscribes to multiple creators. |
| `USR-006` | `@scout_x` | Scout/A&R | N/A | N/A | Verified | 0 Credits | Represents `ORG-002`. |
| `USR-007` | `@mod_alpha` | Moderator | N/A | N/A | Active | 0 Credits | Handles disputes and rights claims. |

### 3.2 Organizations and Teams

| ID | Name | Type | Balances | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-001` | `Beat Collective` | Team/Split | 2000 Credits | Shares revenue among 3 creators. |
| `ORG-002` | `Neon Records` | Sponsor | 50000 Credits | Funds sponsored prize pools. |

## 4. Mocks and Provider Integrations

All external dependencies must be abstracted behind provider interfaces with deterministic mocks for local and continuous integration environments.

The payment and fiat gateway mock, designated as `MockPay`, simulates credit card authorization, capture, and failure. Specific test card numbers trigger deterministic outcomes. For instance, a card starting with `4242` results in success, `4000` simulates insufficient funds, and `4111` triggers a chargeback. Furthermore, `MockPay` mocks the 1% platform conversion fee calculation during cash-out simulations [1].

The identity and compliance mock, named `MockKYC`, simulates identity verification delays and results. Specific test inputs trigger approvals, rejections, or manual review holds. It also simulates jurisdiction checks, such as allowing wagers for a user located in 'US-NV' while blocking paid entry for a user in 'US-WA'.

The native blockchain testnet must be implemented as a local single-node or lightweight consensus network. Its capabilities include minting `ARENA_CREDIT` to test wallets, executing escrow smart contracts for battles, recording provenance hashes for uploaded media, and simulating network congestion or failure states via an administrative API.

## 5. Demonstration Plan and E2E Scenarios

The demonstration plan must prove the complete V1 architecture through end-to-end automated tests and manual runbooks.

### 5.1 Scenario 1: The One-to-One Paid Wager (Music)

The scenario begins with `@lyric_forge` and a new competitor `@bars_smith` agreeing to a one-to-one Rap battle. Both users commit by wagering 50 Credits each. The system deducts 50 Credits from each wallet and locks 100 Credits in a native chain escrow contract. During execution, both participants upload audio, which is provenance hashed to the chain. The adjudication phase involves `@judge_dread` scoring the battle and favoring `@lyric_forge`. Finally, the escrow contract releases 100 Credits to `@lyric_forge`. The verification step asserts the updated balances, showing `@lyric_forge` with an additional 50 Credits and `@bars_smith` with a deduction of 50 Credits, alongside verifying the chain state.

### 5.2 Scenario 2: Sponsored Tournament with Team Splits (Visual Art)

`Neon Records` (`ORG-002`) creates a sponsored visual art challenge in the AI Open division, funding a 10,000 Credit prize pool. `Beat Collective` (`ORG-001`) enters the competition by submitting collaborative artwork. Audience voting adjudicates the challenge, determining `Beat Collective` as the winner. During settlement, 10,000 Credits are transferred from `Neon Records` to `Beat Collective`. The system automatically distributes the 10,000 Credits according to the team's pre-configured split contract on the ledger, such as a 40/40/20 division.

### 5.3 Scenario 3: Marketplace Commerce and Cash-Out

The marketplace scenario starts with `@synth_weaver` listing a sample pack for 20 Credits. `@fan_prime` purchases the pack, resulting in a 20 Credit transfer from `@fan_prime` to `@synth_weaver`. Subsequently, `@synth_weaver` requests to convert 100 Credits to fiat currency via the `MockPay` provider. The system applies the mandatory 1% conversion fee, equivalent to 1 Credit [1]. The remaining 99 Credits are burned, and `MockPay` simulates a $99.00 USD payout. The final reconciliation step asserts ledger consistency and verifies the fee collection account balance.

### 5.4 Scenario 4: Dispute and Chargeback Handling

`@fan_prime` initiates a chargeback via `MockPay` for a previous 50 Credit purchase. The system receives the webhook, deducts 50 Credits from `@fan_prime`'s balance, potentially resulting in a negative balance, and flags the account. `@mod_alpha` reviews the case in the admin tool and uploads necessary evidence. The system simulates a lost dispute scenario, where the negative balance remains, and the account is suspended pending repayment.

### 5.5 Scenario 5: Provider Failure and Recovery

A tournament settlement is triggered while the `MockPay` provider or the native chain node is intentionally taken offline. The system attempts the settlement but must gracefully catch the resulting error. It places the settlement in a `PENDING_RETRY` state and alerts operators. Once the node is brought back online, a background worker or a manual administrative trigger successfully completes the settlement.

## 6. ADR Register (Architecture Decision Records)

Unresolved choices must be documented as Architecture Decision Records to ensure clear communication and tracking of technical choices.

| ADR ID | Title | Status | Description |
| :--- | :--- | :--- | :--- |
| `ADR-001` | Native Chain Selection | Proposed | Evaluate sovereign app-chain versus L2 rollup for V1 native blockchain implementation. |
| `ADR-002` | Media Storage and CDN | Proposed | Define the storage architecture for large audio/video files ensuring provenance hashes match chain records. |
| `ADR-003` | Real-time Voting Protocol | Proposed | Select WebSocket versus Server-Sent Events for live audience voting during battles. |

## 7. Full V1 Backlog

The following represents the full, dependency-ordered backlog for V1 construction. All items are mandatory for the V1 build phase, regardless of their eventual activation status in production.

The first phase focuses on Core Infrastructure and Identity. It includes the system scaffolding and seed framework epic, which requires implementing the deterministic seed generator using `0xAA20260830V1CORE`, creating the hard reset administrative command, and configuring the monorepo structure with shared contracts and design tokens. The identity and RBAC epic involves implementing user registration, authentication, the policy engine for access control, and creating the `MockKYC` provider for simulated identity verification. The native blockchain testnet integration epic requires deploying a local single-node consensus network, implementing `ARENA_CREDIT` minting and wallet generation, and developing smart contracts for provenance hashing and basic escrow.

The second phase implements the Battle Loop, prioritizing music first. The media pipeline epic involves implementing secure audio uploads with format validation, generating cryptographic hashes of uploaded media to commit to the native chain, and implementing media playback controls. The battle primitives epic requires implementing the battle creation state machine, challenge issuance workflows, and enforcing division rules across Pure Human, Hybrid, and AI Open categories. The adjudication system epic involves implementing judge panel assignments, conflict-of-interest declarations, structured scoring rubrics, and audience voting mechanics.

The third phase establishes the Credit Economy. The wallet and purchasing epic involves implementing the user wallet interface to display the `ARENA_CREDIT` balance, integrating `MockPay` for simulated purchases, and implementing transaction history and ledger auditing. The wagering and escrow epic requires implementing the one-to-one wager commitment flow, developing smart contract interactions for locking funds during battles, and implementing automated settlement and fund release. The cash-out and fees epic involves implementing the cash-out request workflow, the configuration-driven 1% conversion fee deduction, and integrating `MockPay` for simulated fiat payouts.

The fourth phase expands into Discovery, Commerce, and Support. The creator profiles and discovery epic involves implementing detailed profiles with verified records, search filtering by discipline and rating, and global rankings. The marketplace and subscriptions epic requires implementing digital product listings, direct creator commissions, subscriptions, and revenue split functionality for teams. The moderation and support epic involves implementing reporting tools for fraud and abuse, developing an admin dashboard for reviewing disputes, and implementing account suspension mechanics.

## 8. CodeSpring Contract and Execution Guidelines

This section defines the explicit contract for CodeSpring execution. CodeSpring must treat this document and the associated repository structure as the immutable source of truth for V1 construction.

CodeSpring must adhere strictly to mandatory compliance rules. There can be no deferrals of any capability described in this document or the Master Specification to a later phase. Complex features, such as native blockchain integration, must be built using the specified mocks or local testnets. All automated tests must utilize the deterministic seed `0xAA20260830V1CORE`, and tests failing due to non-deterministic behavior will be rejected. Furthermore, mocking a provider does not permit mocking the internal platform logic. The internal ledger, state machines, fee calculations, and error handling must be fully implemented and tested as if the provider were real.

Deliverable expectations require that every epic in the V1 Backlog be accompanied by comprehensive unit, integration, and end-to-end tests demonstrating functionality against the deterministic seed. All API endpoints, database schemas, and smart contracts must be thoroughly documented within the repository. CodeSpring must also provide operational runbooks for common administrative tasks, including seed reset, dispute resolution, and manual settlement triggers.

When CodeSpring encounters an architectural ambiguity not covered by the specifications, they must document it as a new Architecture Decision Record. They should propose a solution based on industry best practices and implement it using feature flags or modular interfaces to allow for easy replacement if the Founder overrides the decision.

## 9. Security, Privacy, and Rights Architecture

Security and privacy are foundational to the Artist Arena architecture, given the financial and competitive nature of the platform.

Data protection requires that Personally Identifiable Information be stored in a segregated, encrypted database schema, completely separate from public profile data and competitive records. The platform must also adhere to data minimization principles, collecting only the data strictly necessary for operation and compliance with simulated jurisdictional requirements.

Cryptographic provenance must be established by hashing all uploaded media upon ingestion. These hashes, along with creator signatures and timestamp data, must be committed to the native blockchain testnet to create an immutable record of provenance.

Financial security relies on an append-only internal financial ledger. Any corrections must be made via explicit reversing entries, never by modifying past records. Funds locked in escrow must be cryptographically secured by the native chain smart contracts, preventing unauthorized release or tampering.

## 10. Acceptance Criteria and Evidence

The successful completion of the V1 build will be measured against specific functional and architectural acceptance criteria. Functionally, all scenarios outlined in the demonstration plan must execute successfully in the local or testnet environment without manual intervention. The reset command must successfully restore the system to the defined deterministic state, and all tests in the comprehensive suite must pass. Architecturally, the monorepo structure must adhere to the defined boundaries, the native blockchain testnet must be fully integrated, and the policy engine must correctly enforce access control and simulated jurisdictional rules.

Upon completion, CodeSpring must provide evidence including a link to the fully populated private GitHub repository, a recorded demonstration of the end-to-end scenarios executing against the deterministic seed, a comprehensive test coverage report, and a finalized ADR register documenting all architectural decisions.

## References

[1] Founder / Product Owner Ø. "ARTIST-ARENA-V1-Master-Specification".
[2] Founder / Product Owner Ø. "Owner Directive 0001: Artist Arena V1 Is Build-Complete".
