# Artist Arena V1: Compliance and Activation Policy Engine Specification

## 1. Executive Summary

This specification defines the implementation-grade architecture for the Artist Arena V1 Compliance and Activation Policy Engine, Economic Ledger, and Blockchain Control Corpus. The Artist Arena platform is positioned as the competitive infrastructure layer for the global creator economy, requiring a robust, scalable, and highly secure foundation for managing real-world value. In strict adherence to Owner Directive 0001, the system mandates the complete construction of all economic capabilities within the V1 repository. These capabilities include native blockchain integration, credit purchasing, one-to-one wagers, paid entry for competitions, participant and sponsor prize pools, escrow mechanisms, deterministic settlement, creator payments, and cash-out functionality.

The architectural philosophy enforces a rigorous separation between the engineering construction of a capability and its activation in a production environment. Every feature must be fully implemented, tested, and verifiable in sandbox and testnet environments. However, exposure to real-world users, live payment rails, and production environments is strictly gated by a deterministic policy engine. This engine evaluates jurisdiction, identity verification status, operator profiles, and explicit founder approval before permitting any sensitive action.

This document outlines the system boundaries, actors, state machines, strict invariants, and reconciliation processes necessary to satisfy the V1 Definition of Done. It ensures the platform is structurally prepared for regulated operation and financial compliance without presuming immediate legal clearance or payment provider approval at the time of development.

## 2. Build Versus Activation Model

The core philosophy of the Artist Arena V1 architecture is that capability construction is a mandatory engineering obligation, while capability exposure is a tightly controlled operational decision.

### 2.1 The Separation Principle

The system must never use a missing external dependency, such as pending payment provider approval or unresolved legal clearance in a specific state, as a justification to defer the implementation of a core economic feature. The codebase must contain the complete schemas, application programming interfaces, state machines, and provider adapters necessary for full functionality. Developers are required to build against these interfaces using simulated providers in local and sandbox environments, ensuring the system is entirely complete and ready for production activation once external approvals are secured.

### 2.2 Activation Dimensions and States

Capabilities are evaluated across multiple dimensions before they are presented to a user or allowed to execute. The policy engine determines the current state based on a matrix of these dimensions.

| Dimension | Description | Valid States |
| :--- | :--- | :--- |
| **Build Obligation** | The fundamental requirement to implement the feature in the V1 codebase. | `V1-BUILD-REQUIRED` |
| **Environment** | The deployment context in which the system is currently running. | `LOCAL`, `TEST`, `SANDBOX`, `TESTNET`, `STAGING`, `PRODUCTION` |
| **Activation State** | The operational status of the feature as determined by the policy engine for a specific user context. | `ENABLED`, `DISABLED_BY_POLICY`, `REGION_LIMITED`, `INVITE_ONLY`, `VALUE_CAPPED`, `PROVIDER_PENDING` |
| **Assurance Level** | The degree of verification and auditing the capability has undergone. | `PROTOTYPE`, `INTEGRATED`, `VERIFIED`, `AUDITED`, `PRODUCTION_QUALIFIED` |
| **Economic Effect** | The nature of the value being transacted in the current environment. | `NO_VALUE`, `SIMULATED_VALUE`, `TEST_VALUE`, `REAL_VALUE` |

### 2.3 Policy Evaluation Mechanics

Every sensitive action, such as initiating a wager, purchasing credits, or requesting a payout, routes through the central Policy Engine. The engine evaluates the user's attributes, including age, verified location, and KYC status, against the active ruleset for the requested action. It returns an explicit authorization decision along with associated reasoning, ensuring that all actions are explicitly permitted rather than implicitly allowed.

## 3. Actors, Entities, and Boundaries

### 3.1 Primary Actors

The platform serves a diverse set of actors, each with specific roles and permitted actions within the economic ecosystem.

Competitor Creators represent the core supply side of the platform. They enter battles, wager credits on their performance, earn prizes from pools, and eventually withdraw funds. Their actions require the highest level of identity verification when interacting with real value.

Audience Members and Fans participate by purchasing credits, tipping creators, funding sponsor pools, and engaging in permitted economic activities that do not involve competitive wagering.

Sponsors and Brands inject external capital into the ecosystem. They fund prize pools and create sponsored challenges, requiring robust business verification and invoicing capabilities.

Compliance Operators and Finance Operators are internal administrative roles. Compliance Operators review flagged transactions, manage KYC exceptions, and handle sanctions alerts. Finance Operators oversee daily reconciliation, manage reserve accounts, and process manual payouts or chargebacks when automated systems require intervention.

Administrators configure the policy engine, manage feature flags, and hold the highest level of system access. Crucially, any sensitive administrative action requires dual control, ensuring no single administrator can unilaterally alter the financial state or compliance policies.

### 3.2 Core Entities

The system architecture is built around several core entities that manage the flow of value and the enforcement of rules.

The Account entity serves as the root identity, linking to KYC data, connected wallets, and specific policy profiles. It is the primary subject of policy evaluation.

The Ledger Account is a double-entry accounting record representing a user's balance. It is strictly categorized by asset type, distinguishing between purchased credits, earned credits, and cash reserves.

A Wager or Commitment represents a cryptographically verifiable intent to risk value on a specific outcome. It locks funds within the ledger until the outcome is determined.

The Escrow Contract is a state machine holding funds until a determinable event, such as battle finality or tournament completion, occurs. It ensures that funds cannot be withdrawn or repurposed while a competition is active.

A Transaction represents an atomic movement of value between ledger accounts, adhering to strict double-entry principles.

A Policy Rule is a versioned, computable condition that dictates feature availability, forming the basis of the Policy Engine's decision-making process.

## 4. Compliance and Activation Policy Engine

The Policy Engine acts as the central authority for determining what actions are permissible in any given context, ensuring strict adherence to legal and operational constraints.

### 4.1 Operator Profiles and Jurisdiction Rules

The platform may operate through different legal entities depending on the geographic region, each with its own set of capabilities and constraints.

Operator Profiles define the legal entity responsible for a specific region, including its associated tax obligations and provider relationships. This allows the platform to segregate operations where legally required.

The Jurisdiction Matrix provides a comprehensive mapping of geographic regions to permitted activities. For example, paid entry wagers might be fully enabled in one jurisdiction but strictly disabled by policy in another. The policy engine queries this matrix during every transaction attempt.

Geolocation Enforcement is critical. The engine requires verifiable geolocation data, such as IP analysis and GPS where permitted, at the time of transaction. Any attempt to spoof location data must trigger an immediate denial of service and flag the account for compliance review.

### 4.2 Identity, KYC, KYB, AML, and Sanctions

Real-value interactions require stringent identity verification to prevent fraud and comply with anti-money laundering regulations.

The system implements robust adapters for industry-standard KYC, KYB, and AML providers. In sandbox environments, these adapters return simulated results to facilitate end-to-end testing without incurring external costs or exposing real data.

The Result Handling State Machine governs the user's verification status. The default state is unverified, limiting the user to actions with no economic value. Upon document submission, the state moves to pending review. Successful verification unlocks configured capabilities, while rejection allows for policy-based appeals. Crucially, if a user matches against global sanctions lists, the account is immediately frozen, and a manual compliance review is mandated.

Strict age gating mechanisms are enforced. Users under the jurisdiction's legal age for competitive wagering are permanently blocked from real-value features, regardless of other verification statuses.

### 4.3 Responsible Participation and Self-Exclusion

The platform incorporates safeguards to promote responsible engagement and protect vulnerable users.

Velocity limits enforce configurable caps on deposit amounts, wager sizes, and total losses over daily, weekly, and monthly periods. These limits can be adjusted globally by administrators or personalized based on user profiles.

Self-exclusion mechanisms allow users to voluntarily suspend their access to real-value features. Once initiated, this action is irreversible for the selected duration, ensuring users can effectively manage their participation.

Automated cooling-off periods are enforced following significant losses or erratic betting patterns, providing a mandatory break from competitive financial activities.

Explicit, cryptographically signed consent is required for terms of service, assumption of financial risk, and data processing agreements. This consent is versioned and must be renewed when policies change.

### 4.4 Tax, App Store, and Provider Constraints

The policy engine must account for external constraints imposed by tax authorities, platform providers, and payment processors.

Tax withholding logic calculates and reserves necessary withholdings based on the user's jurisdiction and accumulated earnings. These reserved funds are moved to a dedicated ledger account for eventual remittance to tax authorities.

When accessed via native clients, the policy engine can dynamically disable specific payment methods or features to comply with platform guidelines, such as Apple or Google in-app purchase rules, preventing application rejection.

Transaction size limits dictated by payment processors are enforced proactively by the policy engine, preventing failed transactions at the provider level.

### 4.5 Administrative Controls and Dual Control

Secure administration is paramount for maintaining platform integrity and preventing internal fraud.

Any modification to the Policy Engine ruleset, manual ledger adjustments, or overrides of sanctions flags requires cryptographically signed approval from at least two distinct, authorized administrators. This dual control mechanism ensures oversight for all sensitive operations.

Every policy evaluation, configuration change, and administrative action generates an immutable audit log entry. These logs are essential for compliance reporting and internal investigations.

Rulesets are strictly versioned. A transaction is evaluated against the ruleset active at the exact time of execution, ensuring consistency and predictability even as policies evolve.

### 4.6 Deny and Degraded Behavior

When the Policy Engine returns a denial, the system must handle the situation gracefully without compromising user experience or system stability.

The user interface must provide clear, non-punitive messaging explaining the restriction, such as informing the user that paid entry is not currently available in their location.

The system must ensure that denied actions do not leave orphaned records or partially executed state transitions. The transaction must be rolled back completely, and the denial must be explicitly logged for auditing purposes.

### 4.7 Launch Dossiers

A Launch Dossier is a compiled artifact required to transition a feature from disabled to enabled in a production environment. It serves as the formal record of approval.

The dossier includes legal clearance documentation references, evidence of payment provider approval, a comprehensive risk assessment, and signed sign-off from the Founder and Chief Compliance Officer. Only when a complete dossier is approved can the policy engine configuration be updated to enable the feature.

## 5. Economic Ledger and State Machines

The economic engine is built upon a rigorous, double-entry ledger system designed to track every unit of value with absolute precision.

### 5.1 The 1% Conversion Fee

The Artist Arena platform charges a default fee on cash-to-credit and credit-to-cash conversions, which is central to the platform's revenue model.

This 1% rate is the default but is defined entirely in the system configuration, never hardcoded. This allows for adjustments based on future business requirements or specific promotional periods.

Crucially, this fee is recorded as platform revenue and is explicitly separated from third-party costs. Processor fees, network gas costs, foreign exchange spreads, tax withholdings, and chargeback fees are accounted for in distinct ledger categories. This separation ensures transparent financial reporting and accurate margin analysis.

Users are presented with a clear, itemized breakdown of the conversion fee and any applicable third-party costs before confirming a transaction, ensuring complete transparency.

### 5.2 Accounts and Balances

The ledger maintains various account types to accurately reflect the state of funds within the ecosystem.

User Accounts hold balances of credits, distinctly categorized as either purchased or earned. This distinction is vital for regulatory compliance, as purchased credits may be subject to different refund and withdrawal rules than earned credits.

Escrow Accounts hold funds committed to active battles, tournaments, or sponsored challenges. These funds are locked and cannot be accessed by the platform or the users until the associated event reaches finality.

Platform Accounts track revenue generated from fees, operational funds, and designated reserve pools.

Liability Accounts track funds owed to users, such as pending cash-outs, or funds owed to external providers.

### 5.3 Transaction State Machine

The lifecycle of a transaction is governed by a strict state machine to ensure atomicity and consistency.

| State | Description |
| :--- | :--- |
| `INITIATED` | The user's intent is recorded, but no funds have moved. |
| `AUTHORIZED` | The policy engine has approved the action, and funds are reserved or locked in the ledger. |
| `PROCESSING` | The system is awaiting confirmation from an external payment provider or blockchain finality. |
| `SETTLED` | The transaction is complete, and the ledger is permanently updated. |
| `FAILED` | The transaction was rejected by a provider or failed an invariant check; locks are released. |
| `REVERSED` | The transaction was undone due to a dispute, chargeback, or administrative override. |

### 5.4 Wagers, Escrow, and Prize Pools

The system supports complex financial interactions centered around competitive events.

In one-to-one wagers, both participants commit an equal amount of credits. The ledger moves these credits from the individual user accounts to a specific battle escrow account.

Prize pools can be funded by participants through entry fees, by external sponsors, or subsidized by the platform itself. All funds are aggregated in a tournament escrow account.

Upon the finality of the contest, determined by judging completion and the expiration of any appeal windows, the escrowed funds are distributed deterministically to the winner or winners, minus any applicable platform fees defined in the event ruleset.

### 5.5 Cash-Out and Payouts

The process of converting earned credits back to fiat currency is heavily regulated and strictly controlled.

Users must meet comprehensive eligibility requirements, including full KYC verification, minimum balance thresholds, and jurisdiction checks, to initiate a cash-out request.

Payouts may be subject to automated security holds. For example, large withdrawal amounts or requests following suspicious betting activity may trigger a 72-hour hold pending manual review by a Finance Operator.

Approved cash-outs are routed to the configured payment provider adapter for execution, with the ledger state updating only upon confirmed receipt by the provider.

### 5.6 Chargebacks, Disputes, and Reserves

The platform must be resilient to fraud and payment disputes.

When a payment provider reports a chargeback, the system immediately locks the associated user account and deducts the disputed amount from their balance. This may result in a negative balance, which must be resolved before the user can participate further.

The platform maintains a separate reserve ledger account specifically to absorb the impact of chargebacks and fraud. This ensures that the solvency of escrowed prize pools is never compromised by individual payment disputes.

Administrators have access to tools for dispute resolution, allowing them to review evidence such as login logs and contest participation records, and submit counter-evidence to the payment provider when appropriate.

## 6. Blockchain Control Corpus

Artist Arena V1 includes a native blockchain or sovereign application-chain architecture to ensure provenance, transparency, and programmable settlement, even if the user experience abstracts these mechanics.

### 6.1 Blockchain Domain Requirements

The repository includes comprehensive configurations for running local, testnet, and simulated production nodes, ensuring the blockchain infrastructure is fully integrated into the development lifecycle.

The architecture defines the consensus mechanism and validator requirements, providing a clear path to decentralization or permissioned operation depending on the final launch strategy.

The chain state model includes versioned identities, cryptographic hashes of creator works, contest commitments, escrow balances, and settlement attestations. This provides an immutable record of all critical platform activities.

Smart contracts or native execution modules govern the logic for wagers, revenue splits, and payouts. These modules are strictly deterministic and subject to rigorous metering to prevent resource exhaustion attacks.

### 6.2 Wallet Integration

The platform supports multiple wallet integration models to accommodate different user segments.

For mainstream users, the platform provides managed wallets, securely handling key custody via hardware security modules or multi-party computation. This abstracts the complexity of blockchain interaction while maintaining security.

Advanced users have the option to link external, self-custodial wallets, providing them with direct control over their assets.

Crucially, all on-chain transactions initiated via the platform user interface are subject to the off-chain Policy Engine before being broadcast to the network, ensuring compliance rules are enforced regardless of the custody model.

### 6.3 Provenance and Evidence

The blockchain serves as the ultimate source of truth for creator provenance and competition integrity.

Media uploads generate cryptographic hashes that are anchored to the blockchain, establishing an immutable timestamp and proof of existence for creator works.

Battle rules, submission hashes, judge scores, and final outcomes are recorded on-chain. This creates a transparent, verifiable record of the competition, mitigating disputes and building trust in the platform's adjudication process.

### 6.4 On-Chain and Off-Chain Reconciliation

Maintaining consistency between the high-performance off-chain ledger and the on-chain state is critical.

The off-chain double-entry ledger periodically anchors its state root to the blockchain, providing a verifiable checkpoint of the platform's financial status.

Automated background jobs continuously reconcile the off-chain ledger balances with the on-chain state and external payment provider reports. This process identifies any discrepancies immediately.

The system strictly enforces mathematical invariants. For example, the total user balances plus total escrow must always equal the total fiat in custody plus total on-chain assets. Any violation of these invariants immediately halts real-value operations and triggers critical alerts to administrators.

## 7. Architecture and Implementation Details

### 7.1 Commands, Queries, and Events (CQRS)

The system employs a Command Query Responsibility Segregation architecture to separate read and write concerns, optimizing performance and scalability.

Commands represent state-altering requests, such as placing a wager or initiating a cash-out. All commands must pass through the Policy Engine and are executed within strict transaction boundaries.

Queries are read-only requests, such as retrieving a user's balance or checking the status of a battle. These are optimized for speed and do not affect the system state.

Domain events are emitted upon the successful execution of a command. These events, such as a wager placed event or a battle settled event, are handled by downstream systems to trigger notifications, update analytics, or initiate external processes.

### 7.2 Outbox Pattern

To ensure reliable delivery of events and synchronization between the primary database and message brokers or the blockchain, the system implements the Transactional Outbox pattern. This guarantees that events are only published if the corresponding database transaction commits successfully, preventing data inconsistencies.

### 7.3 Provider Interfaces

All external integrations, including payment processors, KYC vendors, and blockchain RPC nodes, are abstracted behind strict, strongly typed interfaces. This design ensures that the core domain logic remains completely isolated from third-party software development kits. It allows for the seamless swapping of providers or the injection of mock implementations during testing, satisfying the requirement that external dependencies do not block development.

## 8. Testing and Observability

### 8.1 Testing Strategy

A comprehensive testing strategy is mandatory to ensure the reliability of the economic engine.

Unit tests must provide high coverage of all domain logic, state machines, and fee calculation algorithms.

Integration tests verify database interactions, outbox processing, and provider adapters using sophisticated mock implementations.

End-to-end tests automate the complete flow from credit purchase to wager, settlement, and cash-out. These tests must run continuously against the sandbox environment to ensure the integrated system functions flawlessly.

Adversarial testing simulates attacks on the policy engine, attempts double-spends, and submits concurrent wager requests to verify that all invariants hold under extreme conditions.

### 8.2 Observability

Robust observability is required to monitor the health and security of the platform.

Metrics track transaction volume, fee revenue, policy engine denial rates, and reconciliation discrepancies in real-time.

Distributed tracing across all services identifies performance bottlenecks and allows operators to trace the complete lifecycle of any transaction.

Automated alerting notifies administrators immediately of invariant violations, high chargeback rates, or provider API failures, enabling rapid response to critical issues.

## 9. Work Packages and Open Decisions

### 9.1 Work Packages

The implementation of the Compliance and Activation Policy Engine is divided into several distinct work packages.

1.  **Core Ledger Implementation:** Develop the double-entry accounting system and the basic transaction state machine.
2.  **Policy Engine V1:** Implement the jurisdiction matrix, age gating logic, and basic identity state handling.
3.  **Provider Adapters:** Create mock implementations of payment and KYC interfaces for sandbox testing.
4.  **Escrow and Settlement:** Build the logic for wager commitments, tournament pools, and deterministic payouts.
5.  **Blockchain Integration:** Configure nodes, define the state model, and develop basic smart contracts.
6.  **Reconciliation Engine:** Implement automated invariant checking and discrepancy reporting.
7.  **Admin Tooling:** Develop secure interfaces for policy management, dual control execution, and audit log review.

### 9.2 Open Decisions

Several decisions remain open and will be finalized closer to production launch, but must not block current development.

*   **Blockchain Selection:** The final selection of the specific Layer 1 or Layer 2 network for the native blockchain implementation.
*   **Primary Payment Provider:** The selection of the initial fiat payment processor, pending legal and commercial negotiations.
*   **KYC Vendor:** The selection of the global identity verification partner.

## 10. V1 Definition of Done

The Compliance and Activation Policy Engine, Economic Ledger, and Blockchain Control Corpus are considered complete for V1 when the following criteria are met:

1.  All capabilities described in this specification, including credits, wagers, escrow, payouts, and native blockchain integration, are fully implemented in code and merged into the master branch.
2.  The Policy Engine successfully and deterministically gates these features based on simulated jurisdiction, identity, and operator configurations.
3.  The double-entry ledger accurately tracks all transactions, enforces the configurable 1% conversion fee separately from other costs, and maintains strict mathematical invariants.
4.  Automated end-to-end tests successfully execute the full economic loop in a sandbox environment without relying on manual intervention.
5.  Secure administrative tooling is available to manage policies, review audit logs, and execute dual-control actions.
6.  The architecture explicitly supports future production activation without requiring a structural rebuild or significant refactoring.

---
*Author: Manus AI*
