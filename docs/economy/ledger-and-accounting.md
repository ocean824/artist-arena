# Artist Arena V1: Economic and Blockchain Architecture Specification

**Status:** Implementation-Ready
**Domain:** Economy, Ledger, and Blockchain
**Version:** 1.0
**Target:** V1 Build-Complete

## 1. Executive Summary

This document specifies the implementation-grade architecture for the Artist Arena V1 economic and blockchain infrastructure. In accordance with the governing directive, V1 requires the complete construction of a native blockchain, a double-entry ledger, a credit economy, one-to-one wagers, paid entry, prize pools, escrow, settlement, creator payments, and cash conversion capabilities.

While activation in production may be gated by jurisdiction, compliance, identity verification, payment provider approval, or founder authorization, the architecture, schemas, state machines, integrations, and tests must be fully built and verified in V1.

## 2. System Boundaries and Actors

The system relies on specific actors to function within defined boundaries. The primary actor is the User, representing an authenticated individual participating in the economy, whether as a creator, sponsor, judge, or audience member. The Platform Operator acts as the administrative entity responsible for managing the platform, enforcing policies, and configuring fees. External systems include the Payment Provider, which handles fiat deposits, withdrawals, and chargebacks, and the Identity/Compliance Provider, which verifies user identity, age, and jurisdiction. Finally, the Blockchain Node represents the infrastructure participating in the native application chain for provenance and settlement attestations.

The system architecture is divided into distinct boundaries. The Internal Ledger serves as the authoritative double-entry accounting system, tracking all internal value movements, including credits, holds, liabilities, and revenue. The Native Blockchain acts as the sovereign application chain, providing immutable records of creator provenance, contest evidence, programmable rights, and settlement attestations. The Policy Engine functions as the rule evaluation system, enforcing jurisdiction, age, value limits, and feature flags before allowing any economic actions to proceed.

## 3. Double-Entry Ledger and Accounting Architecture

### 3.1 Instruments and Chart of Accounts

The ledger operates strictly on double-entry principles, ensuring that every transaction balances perfectly. The core instruments utilized within this system are USD (or Local Fiat), representing fiat currency held in platform bank accounts or payment provider balances, and CREDIT, the internal platform currency used for entry, wagers, and payments.

The Chart of Accounts is structured to categorize financial data accurately.

| Category | Account | Description |
| :--- | :--- | :--- |
| **Assets (A)** | `A:Cash:Bank` | Fiat currency held in the platform's bank account. |
| | `A:Cash:Provider:Stripe` | Fiat currency held by the payment provider. |
| | `A:Receivables:Chargebacks` | Funds owed by users due to chargebacks. |
| **Liabilities (L)** | `L:UserBalances:Credits:{UserID}` | Available credits for a specific user. |
| | `L:Escrow:Contest:{ContestID}` | Credits locked in escrow for a specific contest or wager. |
| | `L:Payables:Creator:{UserID}` | Fiat currency owed to a creator for cash-out. |
| | `L:Reserves:Platform` | Funds held in reserve to cover operational risks or disputes. |
| **Equity (E)** | `E:PlatformCapital` | The platform's capital equity. |
| **Revenue (R)** | `R:Fees:Conversion` | Revenue generated from the 1% conversion fee. |
| | `R:Fees:Marketplace` | Revenue generated from creator marketplace commissions. |
| **Expenses (X)** | `X:Fees:PaymentProcessor` | Costs incurred from utilizing payment providers. |
| | `X:Losses:Fraud` | Financial losses written off due to fraudulent activity. |

### 3.2 Transaction Invariants and Idempotency

The ledger enforces strict invariants to maintain financial integrity. The primary invariant dictates that the sum of all debits must equal the sum of all credits for every transaction. Furthermore, user credit balances must never fall below zero unless explicitly authorized, such as in specific chargeback scenarios handled via receivables.

To ensure reliability, every economic command must include a unique, client-generated idempotency key. The ledger is designed to reject duplicate keys within a 30-day window, returning the result of the original transaction instead of processing it again. Additionally, ledger updates must utilize optimistic concurrency control through version numbers on accounts, or pessimistic row-level locks, to prevent race conditions during simultaneous transactions, such as a user attempting to enter multiple battles concurrently.

### 3.3 Core Economic Flows

The following sections detail the core economic flows managed by the ledger.

**Credit Purchase (Cash-to-Credit):** When a user purchases 10,000 Credits for $100.00 USD, the platform charges a configurable 1% conversion fee, equivalent to $1.00 USD or 100 Credits. Assuming the payment processor charges a $3.00 fee, the system records a `CreditPurchaseCompleted` event. The ledger debits the provider account by $97.00 and the processor fee account by $3.00. Simultaneously, it credits the user's balance with 9,900 Credits ($99.00 equivalent) and the conversion fee revenue account with 100 Credits ($1.00 equivalent). This ensures the conversion fee is applied separately from processor fees.

**Battle Entry and Escrow (Wagers / Paid Entry):** When two users enter a one-to-one wager for 500 Credits each, the system records two `ContestEntryCommitted` events. For each user, the ledger debits their available credit balance by 500 Credits and credits the specific contest escrow account by the same amount, locking the funds until the contest concludes.

**Settlement and Payout:** Upon the conclusion of a contest, if one user wins, the system records a `ContestSettled` event. The ledger then debits the contest escrow account for the total amount of 1,000 Credits and credits the winning user's balance with the full 1,000 Credits.

**Cash-Out (Credit-to-Cash):** When a user initiates a withdrawal of 1,000 Credits ($10.00 USD), the system records a `CashOutInitiated` event. The platform charges the 1% conversion fee ($0.10 USD). The ledger debits the user's credit balance by the full $10.00 equivalent, credits the creator payables account with $9.90, and credits the conversion fee revenue account with $0.10. Once the provider confirms the payout, a `CashOutCompleted` event is recorded, prompting the ledger to debit the creator payables account and credit the platform bank account by $9.90.

### 3.4 Chargebacks and Disputes

In the event a user initiates a chargeback on a credit purchase, the system immediately places a hold on the disputed amount, freezing it in the user's account if available, or moving it to a receivable account. An investigation is then conducted through the external provider's process. If the resolution results in a loss for the platform, the ledger debits the user's credit balance to reverse the purchase, debits the fraud losses account for any processor chargeback fees, and credits the provider account to reflect the funds pulled by the provider.

### 3.5 Revenue Recognition Boundaries

Revenue is recognized precisely when the platform's performance obligation is satisfied. Conversion fees are recognized immediately upon the execution of a cash-to-credit or credit-to-cash conversion. Marketplace commissions are recognized only when the digital good or service is successfully delivered to the buyer. Finally, the platform's cut of entry fees is recognized only when the contest officially concludes and the results are finalized.

## 4. Native Blockchain Architecture

The native blockchain serves as the immutable source of truth for provenance, commitments, and settlement attestations. It ensures transparency without exposing sensitive data or large media payloads to the public ledger.

### 4.1 Blockchain Domain and Consensus

The network operates as a sovereign application chain, potentially based on frameworks like the Cosmos SDK or a similar deterministic state machine. The consensus mechanism will utilize Proof-of-Stake or Proof-of-Authority, depending on the decentralization phase, with a strong emphasis on achieving fast finality and maintaining low transaction costs. The state model manages accounts, versioned assets representing creator works, escrow contracts, and policy references.

### 4.2 On-Chain Modules

The blockchain functionality is divided into specific modules.

| Module | Responsibility |
| :--- | :--- |
| **Identity** | Manages pseudonymous user mapping, public keys, and hashed KYC status using zero-knowledge or blinded techniques. |
| **Provenance** | Records content hashes, timestamps, creator signatures, tool/AI disclosures, and license metadata. |
| **Contest** | Handles battle and tournament definitions, ruleset hashes, entry commitments, and state transitions. |
| **Escrow** | Manages the cryptographic locking of digital assets or credits pending the resolution of a contest. |
| **Settlement** | Records attestations of contest results, triggering the release of escrowed funds according to predefined splits. |

### 4.3 Off-Chain / On-Chain Reconciliation

The internal double-entry ledger handles high-throughput, real-time balances, while the blockchain acts as the settlement layer and audit trail. When a user enters a wager, the internal ledger processes the transaction immediately, and simultaneously, a transaction is submitted to the blockchain committing the user to the contest. Upon contest completion, a platform oracle submits the result to the blockchain. An independent reconciliation service continuously compares the internal ledger's escrow balances and settlement events against the blockchain's state, immediately alerting administrators and halting related payouts if discrepancies are detected.

## 5. Security, Privacy, and Compliance

### 5.1 Policy Engine and Gates

The architecture implements a centralized Policy Engine that intercepts all economic commands. This engine enforces jurisdiction rules, blocking cash-out or wagering in prohibited regions based on IP and verified identity. It also enforces identity and age requirements, demanding KYC/AML verification before users can exceed value limits or participate in real-money wagers. Furthermore, it strictly enforces daily and monthly limits on deposits, wagers, and withdrawals.

### 5.2 Data Privacy

Personally Identifiable Information, such as names, addresses, and tax IDs, is stored securely off-chain, encrypted at rest, and never published to the blockchain. The blockchain itself only stores cryptographic hashes, pseudonymous IDs, and public metadata, ensuring user privacy is maintained while providing necessary transparency.

## 6. Implementation and Testing

### 6.1 Work Packages

The implementation is structured into specific work packages. The Foundation package establishes the Chart of Accounts, the basic double-entry ledger, and idempotency and concurrency controls. The Credit Economy package implements cash-to-credit and credit-to-cash flows, including the configurable 1% fee. The Contest Escrow package handles wager commitments, holds, and automated settlement splits. The Blockchain Integration package covers node setup, the provenance module, and contest attestation contracts. The Reconciliation package develops automated reconciliation jobs between the ledger, payment providers, and the blockchain. Finally, the Policy Engine package implements jurisdiction, age, and value gates.

### 6.2 Property Tests and Acceptance Criteria

The system must pass rigorous property tests. The sum of all account balances must always equal zero. Concurrent wager entries must never result in a negative user balance. Processing the same idempotency key twice must only apply the transaction once. Blockchain settlement attestations must exactly match the internal ledger distribution. The Policy Engine must successfully reject real-money wagers for users tagged as underage or residing in a restricted jurisdiction.

### 6.3 V1 Definition of Done

The economic and blockchain architecture is considered complete when the double-entry ledger handles all core flows flawlessly in a sandbox environment, the native blockchain accurately records provenance and contest state transitions, the reconciliation service successfully detects and reports simulated discrepancies, the Policy Engine correctly gates actions based on mock compliance data, and all property tests and end-to-end flows pass in the continuous integration pipeline.

## 7. Open Decisions

Several architectural decisions remain open for finalization. The specific blockchain framework, such as Cosmos SDK, Substrate, or a custom rollup, must be selected for the application chain. The final selection of the primary fiat payment processor for V1 integration is pending. Additionally, the precise design of the trusted oracle system responsible for submitting contest results to the blockchain requires further definition.

## 8. Detailed State Machines

### 8.1 Contest State Machine

The contest lifecycle is governed by a strict state machine to ensure economic integrity and prevent race conditions. The states progress linearly, with specific actions allowed only in designated states.

**State: DRAFT**
The contest is being configured by a creator or sponsor. Entry rules, prize pools, and judging criteria are defined. No economic commitments are allowed in this state. The contest can be freely edited or deleted.

**State: OPEN_FOR_ENTRY**
The contest is published and accepting participants. Users submit entry commands, which trigger the `ContestEntryCommitted` event. The ledger places a hold on the user's credit balance and transfers the required entry fee to the contest's specific escrow account. If a user cancels their entry before the contest begins, the funds are released back to their available balance. The contest cannot progress to the next state until the minimum required participants are met, or the entry deadline passes.

**State: ACTIVE**
The contest has officially begun. No further entries are accepted. The escrowed funds are locked and cannot be withdrawn by participants. Creators submit their work, and judges or the audience evaluate the submissions based on the defined ruleset. The blockchain records the start of the contest and the hash of the finalized ruleset to ensure no changes occur during the competition.

**State: VOTING_CLOSED**
Submissions and evaluations have concluded. The system calculates the final scores and determines the winners. This state is transitional, allowing for automated checks, fraud detection algorithms, and manual reviews if flagged by the moderation system. No economic movements occur in this state.

**State: SETTLEMENT_PENDING**
The preliminary results are calculated, and the system prepares the payout distributions based on the prize pool splits. A designated dispute window opens, allowing participants to challenge the results if they suspect foul play or technical errors. If a dispute is filed, the contest transitions to the `DISPUTED` state. If the window closes without disputes, the contest transitions to `SETTLED`.

**State: DISPUTED**
The settlement is paused due to a filed dispute. Platform administrators or a decentralized arbitration panel review the evidence. The escrowed funds remain locked. Once a decision is reached, the administrators execute a resolution command, which either confirms the original results or adjusts the payout distribution. The contest then transitions to `SETTLED`.

**State: SETTLED**
The results are final and immutable. The system records the `ContestSettled` event. The ledger executes the payout distributions, moving funds from the contest escrow account to the winning users' available credit balances. The platform's cut of the entry fees is recognized as revenue. The blockchain oracle submits the final attestation, recording the winners and the payout hashes on-chain. This state is terminal.

### 8.2 Escrow State Machine

The escrow accounts follow a lifecycle tightly coupled with the contest state machine, ensuring funds are properly managed and protected.

**State: FUNDING**
The escrow account is created when the contest enters the `OPEN_FOR_ENTRY` state. As users commit to the contest, funds are transferred from their available balances to the escrow account. The account balance increases with each successful entry.

**State: LOCKED**
When the contest transitions to the `ACTIVE` state, the escrow account is locked. No further funds can be added, and no funds can be withdrawn. The balance remains static throughout the competition, evaluation, and dispute periods. This guarantees that the prize pool is fully funded and available for payout upon resolution.

**State: RELEASING**
Upon the contest reaching the `SETTLED` state, the escrow account transitions to `RELEASING`. The ledger executes the predefined payout splits, transferring funds to the winners and recognizing platform revenue. This state is transient and exists only during the execution of the settlement transactions.

**State: CLOSED**
Once all funds have been distributed and the escrow account balance reaches zero, the account is closed. No further transactions can be posted to this account. The lifecycle is complete, and the account remains in the ledger history for auditing and reconciliation purposes.

## 9. Advanced Economic Scenarios

### 9.1 Mixed Funding Prize Pools

Artist Arena supports complex prize pools funded by multiple sources, requiring careful accounting and settlement logic. A contest may feature a base prize pool provided by a corporate sponsor, augmented by entry fees collected from participants, and further increased by audience contributions or tips during a livestream event.

The ledger must track each funding source independently within the contest's escrow account. Sponsor funds are credited to the escrow account upon the sponsor's commitment, subject to the same idempotency and concurrency controls as user entries. Participant entry fees are added as they join. Audience contributions are processed in real-time, debiting the contributor's balance and crediting the escrow account.

Upon settlement, the payout distribution logic must account for the different funding sources. The platform may charge different fee percentages based on the source of the funds (e.g., a higher fee for audience tips compared to sponsor contributions). The ledger executes multiple postings to distribute the combined prize pool accurately, ensuring all revenue recognition boundaries are respected and the final escrow balance reaches exactly zero.

### 9.2 Creator Subscriptions and Commissions

Beyond contests, the economy supports direct creator monetization through subscriptions and commissions. These transactions utilize the same internal credit system but follow different revenue recognition and escrow rules.

For subscriptions, a user authorizes a recurring monthly payment in credits to access a creator's premium content. The system automatically debits the user's balance and credits the creator's balance at the start of each billing cycle. The platform recognizes its marketplace commission revenue immediately upon each successful transfer. If a user lacks sufficient credits, the subscription is paused until they replenish their balance via a cash-to-credit conversion.

For commissions, a user requests a custom piece of work from a creator, agreeing on a price in credits. The system places the agreed amount in a specific commission escrow account. The funds remain locked while the creator completes the work. Upon delivery and acceptance by the user, the funds are released from escrow, the creator receives their payment minus the platform commission, and the platform recognizes its revenue. If a dispute arises regarding the quality or delivery of the work, the funds remain in escrow until resolved by platform administrators.

## 10. Auditability and Observability

### 10.1 Ledger Audit Trails

The double-entry ledger is designed for complete auditability. Every transaction posting includes metadata detailing the user initiating the action, the timestamp, the specific event triggering the transaction, and a reference to the related contest, subscription, or commission. This metadata ensures that every movement of value can be traced back to its origin and authorized intent.

The ledger maintains an immutable history of all postings. Modifications to historical records are strictly prohibited. Any corrections or adjustments must be made through explicit reversing entries, ensuring the original error and the subsequent correction are both permanently recorded. This append-only design is crucial for financial compliance and internal auditing.

### 10.2 Telemetry and Monitoring

The economic and blockchain infrastructure requires comprehensive telemetry and monitoring to ensure stability, detect anomalies, and prevent fraud. The system emits structured logs for every state transition, ledger posting, and blockchain interaction.

Key metrics are monitored in real-time, including the total volume of credits in circulation, the velocity of transactions, the ratio of cash-to-credit versus credit-to-cash conversions, and the frequency of failed transactions or idempotency key collisions. Alerts are configured to trigger when these metrics deviate from expected baselines, indicating potential issues such as a sudden spike in chargebacks, a failure in the payment provider integration, or a potential exploit attempting to manipulate the ledger.

The reconciliation service provides its own set of metrics, tracking the frequency and magnitude of discrepancies detected between the internal ledger, payment providers, and the blockchain. Any discrepancy, no matter how small, triggers an immediate high-severity alert, requiring manual investigation by the engineering and finance teams to identify the root cause and implement corrective measures.
