# Artist Arena V1 Economic and Blockchain Control Corpus

## 1. Introduction and Scope

This document provides the complete, implementation-grade specification for the Artist Arena V1 economic and blockchain control corpus. In accordance with Owner Directive 0001, Artist Arena V1 is designed and built as the full competitive infrastructure layer for the global creator economy. Every capability described herein—including native blockchain, credits, cash-in/cash-out, paid battle entry, one-to-one credit wagers, prize pools, escrow, settlement, creator payments, and conversion fees—is mandatory V1 engineering scope.

This specification covers:
- Credits, conversions, and the 1% platform fee.
- Wallet architecture (managed and self-custodial).
- Deposits, purchased credits, and earned balances.
- Arena Points separation.
- Quote/order lifecycle and cash-in/cash-out processes.
- Trusted confirmation, payout holds, recovery, and limits.
- Provider adapters, taxes, and failure handling.
- Blockchain and off-chain reconciliation.
- Boundaries, actors, entities, accounts, and state machines.
- Commands, queries, events, and exact invariants.
- Security, privacy, responsible participation, and dispute resolution.
- V1 Definition of Done, work packages, and open decisions.

*Note: All features are built for V1. Activation of real-money features may be restricted by jurisdiction, identity, or provider approval, but implementation, testing, and sandbox execution are never deferred.*

## 2. Boundaries, Actors, and Entities

### 2.1 System Boundaries

The economic and blockchain control system operates at the intersection of user activity, platform policy, external payment providers, and the native blockchain (or application-chain). The boundaries are:
- **Off-Chain Ledger:** High-throughput, synchronous relational database tracking user balances, holds, and transaction history.
- **On-Chain Ledger:** Sovereign blockchain state recording provenance, escrow commitments, final settlements, and creator splits.
- **Provider Gateway:** Adapters for external payment processors, identity verification services, and tax reporting systems.
- **Policy Engine:** Evaluates jurisdiction, age, identity, and risk rules to approve or block transactions.

### 2.2 Actors

| Actor | Description |
|---|---|
| **User** | A creator, fan, or sponsor interacting with the platform. |
| **Creator** | A user who participates in battles, receives tips, or earns revenue. |
| **Sponsor** | A user or entity funding prize pools. |
| **Administrator** | Platform operator managing configurations, disputes, and holds. |
| **Payment Provider** | External service processing fiat deposits, withdrawals, and chargebacks. |
| **Validator** | Node operator securing the native blockchain network. |

### 2.3 Entities

| Entity | Description |
|---|---|
| **Account** | A user's financial profile, containing balances for different asset types. |
| **Wallet** | The cryptographic key pair (managed or self-custodial) associated with an Account. |
| **Credit** | The primary unit of account for real-value transactions (purchased or earned). |
| **Arena Point** | A non-convertible, promotional or engagement-based unit of account. |
| **Transaction** | A discrete movement of value between accounts or states (e.g., deposit, wager, payout). |
| **Escrow** | A locked state for funds committed to a battle or prize pool. |
| **Quote** | A time-bound offer for conversion between fiat and Credits, including all fees. |

## 3. Account and Balance Architecture

### 3.1 Balance Types

To comply with regulatory requirements and platform policy, user accounts must maintain strict separation of balance types:

1.  **Purchased Credits:** Credits bought directly with fiat currency. Eligible for wagers and entry fees. May have restricted cash-out eligibility depending on jurisdiction.
2.  **Earned Credits:** Credits received from winning wagers, prize pools, or creator payments. Fully eligible for cash-out, subject to identity and policy checks.
3.  **Arena Points:** Promotional balances used for engagement, non-monetary voting, or platform rewards. Strictly non-convertible to fiat. Never commingled with Credits.

### 3.2 Exact Invariants

- **Conservation of Value:** The sum of all user balances, escrowed funds, and platform revenue must exactly equal the total issued Credits minus total retired/cashed-out Credits.
- **No Negative Balances:** A user's available balance for any asset type cannot fall below zero. (Chargebacks may result in a negative *account state* requiring resolution, but not a negative *spendable balance*).
- **Escrow Integrity:** Funds committed to an active battle or prize pool cannot be withdrawn or used for other purposes until the battle is resolved or cancelled.
- **Strict Separation:** Arena Points cannot be used to fund real-value wagers or converted to Credits.

## 4. Wallet and Custody

The V1 architecture supports both managed and self-custodial wallet paths, allowing seamless onboarding while preserving sovereign ownership options.

### 4.1 Managed Wallet Path

- **Key Management:** Platform securely generates and stores keys using an HSM or secure enclave.
- **User Experience:** Users authenticate via standard Web2 methods (email, OAuth). Transactions are signed automatically by the platform on behalf of the user, subject to policy and session validation.
- **Recovery:** Account recovery follows standard Web2 password reset and identity verification flows.

### 4.2 Self-Custodial Wallet Path

- **Key Management:** Users hold their own private keys (e.g., via browser extension or hardware wallet).
- **User Experience:** Users must explicitly sign transactions for on-chain actions (wagers, escrow funding).
- **Recovery:** Platform cannot recover lost keys. Users are solely responsible for seed phrase management.

### 4.3 Trusted Confirmation

High-value actions (e.g., large cash-outs, key rotation, significant wagers) require out-of-band trusted confirmation, such as MFA (SMS, Authenticator app) or email verification, regardless of the wallet path.

## 5. Economic Flows and State Machines

### 5.1 Credit Purchase (Cash-In)

1.  **Quote Generation:** User requests to buy Credits. System queries Provider Gateway for current exchange rates and calculates the 1% platform fee and any provider fees. A time-bound `Quote` is presented.
2.  **User Confirmation:** User accepts the Quote.
3.  **Authorization:** System requests payment authorization from the Provider.
4.  **Ledger Posting:** Upon successful authorization, Purchased Credits are credited to the user's account.
5.  **Receipt:** User receives a detailed receipt itemizing the principal, the 1% platform fee, and provider costs.

### 5.2 Wagers and Escrow

1.  **Match Terms:** Users agree to one-to-one wager terms or enter a paid battle.
2.  **Reservation:** System verifies sufficient available balances and places a hold on the required Credits.
3.  **Commitment (Escrow):** Funds are moved to an Escrow state (off-chain hold + on-chain commitment).
4.  **Resolution:** Battle concludes and results are finalized.
5.  **Settlement:** Escrowed funds are distributed to the winner(s) as Earned Credits. Platform fees (if applicable to the battle type) are deducted.

### 5.3 Cash-Out (Payouts)

1.  **Eligibility Check:** System verifies user identity (KYC), jurisdiction, and minimum Earned Credit balance.
2.  **Hold Review:** System checks for active disputes, chargebacks, or mandatory cooling-off periods.
3.  **Quote Generation:** System calculates the fiat value, deducting the 1% platform conversion fee and any provider payout fees.
4.  **Provider Payout:** System instructs the Provider Gateway to initiate the fiat transfer.
5.  **Reconciliation:** Upon provider confirmation, Earned Credits are burned/deducted from the ledger.

### 5.4 State Machines

**Transaction State Machine:**
`PENDING` -> `AUTHORIZED` -> `SETTLED` (Success)
`PENDING` -> `FAILED` / `DECLINED` (Failure)
`SETTLED` -> `DISPUTED` -> `REVERSED` / `RESOLVED` (Chargeback flow)

**Escrow State Machine:**
`PROPOSED` -> `FUNDED` -> `LOCKED` -> `RELEASED` (Settlement)
`PROPOSED` -> `CANCELLED` (Pre-funding cancellation)
`LOCKED` -> `REFUNDED` (Battle cancelled or invalid)

## 6. The 1% Conversion Fee

The Artist Arena conversion fee is a locked product requirement.

- **Rate:** Defaults to 1.00%.
- **Configuration:** Must be configuration-driven (e.g., via environment variables or database config), never hardcoded.
- **Application:** Applied bidirectionally on cash-to-credit (deposits) and credit-to-cash (withdrawals) conversions.
- **Separation:** This fee is distinct from, and accounted for separately from, third-party processor fees, network gas fees, FX spreads, and taxes.
- **Disclosure:** Must be explicitly line-itemized in all user quotes and receipts.

## 7. Blockchain Implementation

The V1 native blockchain (or sovereign app-chain) serves as the immutable record for high-stakes platform activity.

### 7.1 Required V1 Capabilities

- **Node and Network:** Runnable node software, peer networking, state synchronization.
- **Consensus:** Byzantine Fault Tolerant (BFT) consensus mechanism.
- **State Model:** Tracking of creator works, escrow commitments, and settlement attestations.
- **Execution:** Deterministic runtime for executing settlement logic and creator splits.

### 7.2 Off-Chain / On-Chain Reconciliation

To ensure performance and privacy, not all actions occur directly on-chain.
- **Off-Chain:** High-frequency trading, balance updates, and matching occur in the relational database.
- **On-Chain:** Final settlements, escrow commitments, and significant provenance events are anchored to the blockchain.
- **Reconciliation:** A background worker continuously verifies that the off-chain ledger state matches the on-chain settlement attestations. Any divergence triggers an immediate administrative alert and halts affected withdrawals.

## 8. Provider Adapters, Taxes, and Compliance

### 8.1 Provider Interfaces

The system must use abstract interfaces for all external services, ensuring no vendor lock-in and allowing mock implementations for testing.
- `IPaymentGateway`: `authorize()`, `capture()`, `refund()`, `payout()`.
- `IIdentityVerification`: `verifyUser()`, `checkSanctions()`.
- `ITaxService`: `calculateTax()`, `generateForm()`.

### 8.2 Tax Records

- The system must record all taxable events (e.g., creator earnings, prize winnings).
- Must support generating necessary tax forms (e.g., 1099-K, 1099-MISC) based on jurisdiction thresholds.
- Tax liabilities are the responsibility of the user, but the platform must provide accurate reporting data.

### 8.3 Fraud, Chargebacks, and Disputes

- **Monitoring:** System must monitor for velocity anomalies, unusual wager patterns, and known fraud indicators.
- **Chargebacks:** If a fiat deposit is charged back, the corresponding Credits are immediately invalidated. If the Credits have been spent, the user account enters a restricted, negative state until resolved.
- **Reserves:** The platform maintains an internal reserve ledger to account for potential chargeback liabilities.

## 9. Commands, Queries, and Events (CQRS)

The architecture follows a CQRS pattern to separate read and write concerns.

### 9.1 Commands
- `InitiateDeposit(UserId, Amount, Currency)`
- `ConfirmQuote(QuoteId)`
- `ProposeWager(ChallengerId, OpponentId, Amount)`
- `AcceptWager(WagerId)`
- `ResolveBattle(BattleId, WinnerId)`
- `RequestPayout(UserId, Amount)`

### 9.2 Queries
- `GetUserBalances(UserId)` -> Returns `PurchasedCredits`, `EarnedCredits`, `ArenaPoints`.
- `GetTransactionHistory(UserId, DateRange)`
- `GetActiveEscrows(UserId)`

### 9.3 Events
- `DepositCompletedEvent`
- `WagerEscrowedEvent`
- `BattleSettledEvent`
- `PayoutInitiatedEvent`
- `ChargebackReceivedEvent`

## 10. Observability, Tests, and Acceptance

### 10.1 Observability
- All financial state transitions must emit structured logs.
- Metrics must track deposit success rates, average conversion times, and reconciliation discrepancies.
- Distributed tracing must link API requests to database transactions and blockchain RPC calls.

### 10.2 Testing Strategy
- **Unit Tests:** Validate invariant logic (no negative balances, fee calculations).
- **Integration Tests:** Verify provider adapters using mock endpoints.
- **End-to-End Tests:** Simulate full user journeys from deposit, to wager, to settlement, to payout.
- **Adversarial Testing:** Attempt race conditions, double-spends, and policy bypasses in the sandbox environment.

### 10.3 V1 Definition of Done (Economic Scope)
The economic corpus is "Done" for V1 when:
1. The relational ledger and blockchain state machines are fully implemented and reconciled.
2. Users can complete simulated deposits, wagers, and payouts in a sandbox environment.
3. The 1% fee is correctly applied and separated from provider costs.
4. Policy gates (jurisdiction, age, identity) successfully block unauthorized transactions without requiring code changes.
5. All exact invariants are verified by automated tests.

## 11. Work Packages

1. **Core Ledger:** Implement the relational database schema for accounts, balances, and transactions.
2. **Policy Engine:** Build the ruleset evaluator for jurisdiction and identity gates.
3. **Provider Adapters:** Implement interfaces and mock providers for payments and KYC.
4. **Blockchain Integration:** Deploy the native node, define state models, and build the reconciliation worker.
5. **Economic Flows:** Implement the CQRS commands/handlers for deposits, wagers, escrow, and payouts.
6. **Admin Tooling:** Create dashboards for monitoring holds, disputes, and system invariants.

## 12. Open Decisions

- **Blockchain Framework:** Selection of the specific underlying framework (e.g., Cosmos SDK, Substrate) for the native chain.
- **Primary Payment Provider:** Selection of the initial real-world payment processor (Stripe, PayPal, etc.) pending legal clearance.
- **Identity Vendor:** Selection of the KYC/AML provider.

*These open decisions do not block the V1 implementation, as abstract adapters and mock providers must be used during construction.*
