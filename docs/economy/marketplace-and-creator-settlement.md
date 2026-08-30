# Artist Arena V1 Economic and Blockchain Control Corpus

## 1. Executive Summary

Artist Arena V1 is designed as the competitive infrastructure layer for the global creator economy. This document provides the complete implementation-grade specification for the V1 economic and blockchain control corpus, overriding any previous assumptions that these features were deferred. Every capability described here—including native blockchain integration, credits, wagers, escrow, payouts, reconciliation, and activation policies—is mandatory for V1 construction.

The architecture separates the *construction* of these capabilities from their *activation*. While the codebase must fully support real-money transactions, native blockchain ledgers, and complex economic interactions, the actual exposure of these features is governed by strict compliance, jurisdiction, identity, provider, and founder-approval gates. This approach ensures that the platform is technologically ready for global scale and regulatory compliance from day one, even if initial rollouts are geographically restricted or operate in a simulated value mode.

## 2. Economic Primitives and Ledger Architecture

### 2.1 The Dual-Ledger System

Artist Arena operates a robust dual-ledger system to ensure absolute financial integrity, high-throughput performance, and immutable traceability:

1.  **Off-Chain Transactional Ledger (System of Record):** A high-performance, horizontally scalable relational database (e.g., PostgreSQL with strict isolation levels) tracking all user balances, pending transactions, holds, platform fees, and operational state in real-time. This ledger uses strict double-entry accounting principles where every credit movement requires balanced debit and credit entries across defined chart of accounts.
2.  **Native Blockchain Ledger (System of Provenance):** A sovereign application-chain (or dedicated Layer 2 rollup) providing immutable provenance for creator works, competition results, complex rights management, and settlement attestations. It acts as the ultimate source of truth for long-term economic state, programmable rights, and decentralized auditability.

### 2.2 Credits, Currency, and Value Representation

The primary unit of account within the Artist Arena ecosystem is the **Credit**. The credit abstracts underlying fiat complexities while maintaining a stable peg for user comprehension.

*   **Cash-to-Credit Conversion:** Users purchase credits using fiat currency via approved payment providers (e.g., Stripe, PayPal). The system must handle multiple fiat currencies, applying real-time FX rates to determine the credit yield, minus applicable fees.
*   **Credit-to-Cash Conversion (Cash-out):** Eligible users can convert earned credits back to fiat currency. This process is heavily gated, subject to comprehensive KYC/AML checks, minimum withdrawal thresholds, mandatory holding periods to mitigate chargeback risk, and compliance with local tax reporting requirements.
*   **The 1% Founder Fee:** A configuration-driven 1% fee is applied to both cash-to-credit and credit-to-cash conversions. This fee is strictly separated in the ledger from third-party processor costs, network gas fees, FX spreads, tax withholdings, identity verification costs, and chargeback reserves. It must be fully transparent in the user interface.
*   **Value Representation:** Credits maintain a stable peg to a designated base fiat currency (e.g., 1 Credit = $0.01 USD) to simplify user understanding. However, the internal ledger must support fractional credits (up to 6 decimal places) to handle micro-transactions, complex royalty splits, and precise fee calculations.

### 2.3 Account Types, Entities, and State Machines

Every participant, organization, and system pool has an associated financial account governed by a strict state machine to prevent unauthorized state transitions.

*   **Account States:**
    *   `UNVERIFIED`: Can hold simulated value or test credits, but restricted from real-money deposits, withdrawals, or competitive wagers.
    *   `VERIFIED`: Has passed basic identity checks; allowed to participate in standard commerce and limited wagering.
    *   `ENHANCED_VERIFIED`: Has passed full KYC/AML; eligible for cash-out, large prize pools, and high-value wagers.
    *   `RESTRICTED`: Temporarily blocked from specific actions (e.g., withdrawals) due to suspicious activity or pending disputes.
    *   `SUSPENDED`: All financial activity halted; pending manual review or permanent ban.
    *   `CLOSED`: Account deactivated; final settlement completed.

*   **Balance Buckets (Per Account):**
    *   `AVAILABLE`: Credits ready for immediate use, transfer, or withdrawal.
    *   `PENDING`: Credits incoming but not yet cleared (e.g., pending ACH transfer or unconfirmed blockchain transaction).
    *   `RESERVED`: Credits cryptographically locked for an active wager, tournament entry, or pending purchase escrow.
    *   `HELD`: Credits frozen by system administrators or automated risk engines due to a dispute, chargeback investigation, or compliance flag.

## 3. Marketplace and Creator Economy Settlement

### 3.1 Listings, Orders, and Subscriptions

Creators can monetize their work and audience through various integrated channels, all settling through the unified credit economy.

*   **Listings (Standard Commerce):** One-off sales of digital assets (beats, stems, artwork, templates, digital merchandise). The system must support instant delivery and immediate fund settlement.
*   **Subscriptions:** Recurring payments for gated access to premium content, exclusive community channels, early releases, or ongoing mentorship. The system must handle subscription lifecycles (creation, renewal, cancellation, grace periods, dunning).
*   **Services and Commissions:** Custom work requests with defined milestones, deliverables, and revision cycles. This requires a multi-stage escrow process where funds are locked upon agreement and released progressively as milestones are approved by the buyer.

**Standard Settlement Flow:**
1.  Buyer initiates purchase and confirms the transaction.
2.  System verifies sufficient `AVAILABLE` balance and deducts the required funds.
3.  Funds are moved to an intermediary `ESCROW` system account.
4.  Upon delivery/fulfillment (or immediately for instant digital downloads), funds are released from `ESCROW`.
5.  Platform fees, processing costs, and collaborator splits are calculated and deducted.
6.  Net earnings are credited to the Creator's `AVAILABLE` (or `PENDING`, subject to clearance rules) balance.
7.  The transaction is committed to the off-chain ledger, and a settlement attestation is optionally anchored to the blockchain for high-value items.

### 3.2 Collaborator/Team Splits and Royalties

The system natively supports complex, automated revenue sharing to empower collaborative creation.

*   **Splits:** Creators can define percentage-based splits for any asset, listing, or prize pool (e.g., Producer gets 40%, Vocalist gets 40%, Mixer gets 20%). When a settlement occurs, the system automatically calculates the fractional amounts and distributes funds to all configured parties simultaneously.
*   **Royalties:** For secondary sales, ongoing usage licenses, or derivative works, the blockchain ledger enforces programmable royalty payouts. Smart contracts automatically route a percentage of future revenue back to the original creators, ensuring long-term value capture.

### 3.3 Tips, Entitlements, and Gated Access

*   **Tips:** Where jurisdictionally allowed and policy-enabled, users can send direct, non-refundable tips to creators during livestreams, on profiles, or attached to specific works.
*   **Entitlements:** Purchases grant cryptographically verifiable entitlements. For example, buying a beat grants a specific license (e.g., non-exclusive lease, exclusive rights). This entitlement is recorded on the blockchain as a non-fungible or semi-fungible token, providing immutable proof of ownership and usage rights.
*   **Gated Access:** The platform evaluates these on-chain entitlements or off-chain subscription states to gate access to premium content, private discord channels, or exclusive tournament entry.

## 4. Competition Economy: Wagers, Escrow, and Prize Pools

### 4.1 One-to-One Credit Wagers

Users can challenge each other to direct battles with real value at stake, requiring precise state management and dispute resolution.

**Wager Lifecycle and State Machine:**
1.  **Proposal:** User A proposes a wager (e.g., 500 Credits) with specific rules and deadlines.
2.  **Acceptance:** User B accepts the wager.
3.  **Reservation:** The system deducts 500 Credits from both users' `AVAILABLE` balances and locks them in a `RESERVED` state tied to the specific Battle ID. The system must guarantee that neither user can withdraw or spend these funds.
4.  **Execution:** The battle commences, media is submitted, and the judging mechanism (community vote, verified panel, or hybrid) is activated.
5.  **Finality:** The judging concludes, and a cryptographic attestation of the result is generated.
6.  **Settlement:** The system moves the total pool (1000 Credits) from `RESERVED` to the winner's `AVAILABLE` balance, minus any applicable platform fees or judge compensation.
7.  **Dispute Window:** A configurable window (e.g., 24 hours) allows for appeals before funds are fully cleared for withdrawal.

### 4.2 Prize Pools and Tournaments

Tournaments and open challenges can feature dynamic, multi-source prize pools.

*   **Participant-Funded:** Entry fees from competitors aggregate into the prize pool. The system must handle dynamic pool sizing based on the number of entrants.
*   **Sponsor-Funded:** Brands or organizers inject capital into the pool. This requires specific invoicing, fiat collection, and credit minting workflows separate from standard user purchases.
*   **Mixed Funding:** A combination of entry fees, sponsor contributions, and platform subsidies.

**Escrow and Settlement:** All prize pool funds are held in secure escrow (either off-chain reserved accounts or on-chain smart contracts) until the competition result is finalized. The system must support complex payout structures (e.g., Winner takes all, Top 3 split, tiered payouts based on ranking).

## 5. Risk, Compliance, and Operations

### 5.1 Refunds, Disputes, and Chargebacks

The platform must gracefully handle economic exceptions, adversarial behavior, and external financial disputes.

*   **Refunds:** Automated or manual return of funds for canceled events, undelivered services, or mutual agreement. Refunds must correctly reverse all fee calculations and split distributions.
*   **Disputes:** A structured workflow for users to contest a transaction, wager outcome, or service delivery. Initiating a dispute triggers an immediate freeze on the associated funds (moving them to the `HELD` state) until resolved by a Trust Analyst or automated arbitration system.
*   **Chargebacks:** When a user disputes a fiat charge with their bank or credit card provider, the system receives a webhook from the payment processor. The system must immediately reflect this liability, potentially resulting in a negative credit balance for the offending user, or the clawback of funds from the creator, pending investigation. A dedicated `CHARGEBACK_RESERVE` account must be maintained to absorb temporary shocks.

### 5.2 Standard-Commerce vs. Regulated-Rail Separation

The architecture maintains a strict boundary between standard commerce (buying a digital good, subscribing) and regulated activities (wagering, cash-out, high-value prize pools).

*   **Standard Commerce:** Lower friction, basic identity checks, broader jurisdictional availability.
*   **Regulated Rails:** Require higher levels of KYC/AML assurance, strict jurisdiction checks (blocking users from regions where wagering is illegal), velocity limits (capping daily/weekly spend), and enhanced fraud monitoring.
*   **Policy Engine:** A centralized policy engine evaluates every transaction attempt against these requirements, user state, and current regulatory configurations before allowing the state transition.

### 5.3 Tax Records and Reconciliation

*   **Tax Reporting:** The system automatically tracks gross earnings for all creators and generates required tax documentation (e.g., 1099-K in the US, DAC7 in the EU) based on jurisdictional thresholds. It must support tax withholding where mandated by law.
*   **Reconciliation:** Automated daily reconciliation processes are mandatory. These jobs compare the off-chain database balances, the blockchain ledger state, and external payment provider settlement reports. Any discrepancy (e.g., a missing stripe charge, an unbalanced ledger entry) must immediately trigger a high-priority alert to the finance operations team.

## 6. Blockchain Integration Details

### 6.1 Provenance, Evidence, and AI Disclosure

The native blockchain is used to anchor critical platform data, ensuring censorship resistance and long-term verifiability.

*   **Content Hashes:** Cryptographic hashes (e.g., SHA-256) of uploaded media files are committed to the chain to establish prior art, timestamp creation, and support copyright claims.
*   **Competition Evidence:** Immutable records of battle rulesets, participant submission hashes, judge scores, audience voting aggregates, and final outcomes. This ensures that historical competition results cannot be altered by platform administrators.
*   **AI Disclosures:** Transparent, on-chain declarations of AI tool usage in the creation process, aligning with the platform's Pure Human, Hybrid, and AI Open divisions.

### 6.2 Smart Contracts and Invariants

Key economic logic is deployed as smart contracts to ensure trustless execution and public auditability.

*   **Escrow Contract:** Holds wagered funds and prize pools.
    *   *Invariant:* Funds can only be released upon a cryptographically signed attestation of the competition result from an authorized platform oracle or a decentralized consensus mechanism.
*   **Split and Royalty Contract:** Manages revenue distribution.
    *   *Invariant:* The sum of distributed shares must exactly equal the total input amount. The contract must handle rounding errors gracefully (e.g., allocating the remainder to the first recipient or a designated charity pool).

## 7. Activation Policy and Gates

As mandated by Owner Directive 0001, the full economic engine is built into V1, but its exposure is controlled by granular gates. This allows the engineering team to build the complete vision without waiting for legal or provider approvals.

*   `DISABLED_BY_POLICY`: The feature exists, is fully tested, but is turned off for a specific region, user cohort, or globally.
*   `REGION_LIMITED`: Available only in approved jurisdictions (e.g., wagering allowed in UK, but blocked in US-CA).
*   `VALUE_CAPPED`: Transactions are allowed but limited to a maximum amount (e.g., max wager of $10) to reduce risk during initial rollout.
*   `PROVIDER_PENDING`: The code is ready, but awaiting final API keys or approval from a payment processor.
*   `SIMULATED_VALUE`: The system operates using test credits that have no fiat backing, allowing for beta testing of the full economic loop without financial risk.

These gates are configuration-driven (e.g., via LaunchDarkly or a custom feature flag service) and can be toggled by administrators without requiring code changes or redeployments.

## 8. V1 Definition of Done (Economic & Blockchain)

The economic and blockchain control corpus is considered complete for V1 when the following criteria are met:

1.  **Ledger Integrity:** All state machines, off-chain ledgers, and on-chain smart contracts are fully implemented, tested, and demonstrate zero balance drift under high-concurrency load testing.
2.  **End-to-End Flows:** Complete user flows for fiat deposit, credit purchase, wagering, escrow locking, split calculation, and fiat cash-out operate successfully in a staging/sandbox environment.
3.  **Fee Separation:** The 1% conversion fee is accurately calculated, explicitly logged in the ledger, and separated from all other operational costs (processor fees, network gas).
4.  **Reconciliation:** Automated reconciliation scripts run daily and successfully identify intentionally injected simulated ledger discrepancies.
5.  **Policy Engine:** All activation gates (jurisdiction, KYC, value caps) are functional, evaluate correctly in real-time, and are configurable via a secure admin interface.
6.  **Security and Assurance:** Comprehensive unit, integration, and adversarial tests (fuzzing smart contracts, race condition testing on the off-chain ledger) are passing. The system architecture has been reviewed for common financial vulnerabilities (e.g., double-spend, reentrancy).
7.  **Documentation:** API contracts, database schemas, and operational runbooks for finance teams are documented and up-to-date.
