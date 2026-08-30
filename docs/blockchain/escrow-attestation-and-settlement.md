# Escrow, Result Attestation, Blockchain Finality, and Settlement

**Document Status:** Governing Specification
**Domain:** Economic and Blockchain Control Corpus
**Version:** 1.0
**Target:** Artist Arena V1

---

## 1. Introduction

Artist Arena V1 operates as the full competitive infrastructure layer for the global creator economy. A core component of this infrastructure is the economic and blockchain control corpus, which governs how value moves through the system. This document specifies the implementation-grade architecture for escrow, result attestation, blockchain finality, and settlement.

This specification dictates the mandatory construction of the V1 native blockchain path, credit purchase, one-to-one credit wagers, paid entry, participant/sponsor/mixed prize pools, creator payments, and the 1% conversion fee. While activation of these features is governed by strict policy gates (jurisdiction, identity, provider approval, etc.), their implementation, testing, and operational readiness are mandatory for V1. The founder's directive explicitly overrides any previous documentation that labeled these features as future or optional.

## 2. Boundaries and Actors

The economic and blockchain systems operate across distinct trust zones, coordinating actions among multiple actors while maintaining strict invariants. The architecture is designed to prevent any single point of failure from compromising the integrity of the ledger or the blockchain state.

### 2.1 Actors

| Actor | Role in Economic System |
|---|---|
| **Competitor** | Purchases credits, stakes wagers, enters paid battles, and receives settled payouts. Competitors must pass identity and jurisdiction checks before interacting with regulated financial features. |
| **Sponsor / Organizer** | Funds prize pools, defines escrow terms, and approves rulesets. Sponsors can dictate the distribution of funds and the criteria for winning. |
| **Judge** | Submits attested scores that influence provisional results. Judges are bound by conflict-of-interest declarations and their scores are cryptographically signed. |
| **Moderator / Trust Analyst** | Reviews disputes, initiates holds, and adjudicates appeals affecting finality. They have the authority to freeze escrow and reverse transactions under specific conditions. |
| **Finance Operator** | Manages reconciliation, reviews chargebacks, and executes manual adjustments under dual control. Finance operators monitor the health of the economic system and resolve exceptions. |
| **Policy Engine** | Automated system enforcing jurisdiction, identity, and age gates before financial transactions. The policy engine evaluates rules dynamically based on user attributes and context. |

### 2.2 System Boundaries

1. **Canonical Postgres Ledger:** The ultimate source of truth for all off-chain financial state, operating as a double-entry, append-only journal. It ensures that every transaction is recorded immutably and can be audited.
2. **Blockchain / Sovereign App-Chain:** The native chain for provenance, attestation, and on-chain escrow, serving as the immutable audit trail for competition evidence and economic settlement. The blockchain provides a decentralized verification mechanism.
3. **Provider Adapters:** Isolated interfaces for standard commerce, regulated contest wallets, and internal sandboxes. These adapters abstract the underlying payment providers, allowing the system to switch providers without altering core business logic.

## 3. Economic Entities and Accounts

The system models value using strictly separated economic instruments. There is no single mutable "balance" field. This separation ensures that promotional credits cannot be withdrawn as cash and that escrowed funds are untouchable until settled.

### 3.1 Account Types

| Account Type | Description | Transferability | Withdrawable |
|---|---|---|---|
| **Arena Points** | Promotional or earned units for testing and onboarding. Used to incentivize user behavior without creating financial liability. | No | No |
| **Purchased Credits** | Value acquired via fiat conversion. Subject to compliance gates. These credits represent real monetary value and are tightly regulated. | Restricted | No |
| **Creator Earnings** | Proceeds from sales, subscriptions, and eligible prizes. This is the balance that creators can eventually convert to fiat. | No | Yes (subject to holds) |
| **Contest Escrow** | Reserved funds for entries, stakes, and prize pools. Funds in escrow are locked and cannot be accessed by any party until the contest concludes. | No | No (until settled) |
| **Bonus Credits** | Promotional value with expiration rules. Often used for marketing campaigns and user retention. | No | No |
| **Withdrawable Balance** | Provider-backed eligible amount after verification. This is the final state before funds are transferred to a user's bank account. | No | Yes |
| **Reserve / Hold** | Temporary risk reserve for chargebacks or disputes. Protects the platform from financial loss due to fraudulent activity. | No | No |
| **Platform Revenue** | Accounts for the 1% conversion fee and other platform fees. This is the primary revenue stream for Artist Arena. | N/A | N/A |

## 4. State Machines and Invariants

### 4.1 Battle and Escrow State Machine

The lifecycle of a wagered battle or funded contest dictates the movement of funds into and out of escrow. The state machine is strictly enforced by the backend, and clients cannot transition states directly.

1. **DRAFT** -> **PUBLISHED**: Battle created with stake amount. The ruleset and prize distribution are defined.
2. **MATCHING** -> **ACCEPTED**: Opponent accepts the challenge. Both parties commit to the terms.
3. **FUNDING_PENDING**: Policy engine checks jurisdiction, age, and limits. This step ensures compliance before any funds are moved.
4. **FUNDED**: Stakes from both parties are reserved and moved to Contest Escrow. The battle is now financially secured.
5. **SUBMISSION_OPEN** -> **SUBMISSIONS_LOCKED**: Submissions are finalized. No further changes to entries are allowed.
6. **REVIEW_PENDING** -> **SCORING**: Judging and voting occur. The community and appointed judges evaluate the submissions.
7. **PROVISIONAL_RESULT**: Result calculated based on attested scores. The outcome is announced but remains open to challenge.
8. **DISPUTE_WINDOW**: Open period for moderation or appeals. Users can raise concerns regarding copyright, fraud, or rule violations.
9. **FINAL**: Result is immutable. The dispute window has closed, and the outcome is locked.
10. **SETTLEMENT_PENDING**: Outbox event triggers settlement process. The system prepares to distribute the escrowed funds.
11. **SETTLED**: Escrow is released to the winner, fees are deducted, and the ledger is updated. The financial transaction is complete.

### 4.2 Conversion State Machine

Conversion between fiat and credits (and vice versa) follows a strict flow to ensure regulatory compliance and accurate accounting:

1. **QUOTED**: Exchange rate and 1% fee calculated. The user is presented with the exact terms of the conversion.
2. **USER_CONFIRMED**: User accepts the quote. The user acknowledges the fees and terms.
3. **POLICY_APPROVED**: Identity and jurisdiction gates passed. The system verifies that the user is allowed to perform the transaction.
4. **PROVIDER_PENDING**: Awaiting payment provider confirmation. The external gateway processes the payment.
5. **SETTLED**: Ledger updated with purchased credits or fiat withdrawal. The transaction is finalized in the internal ledger.

Exceptional states include `REJECTED`, `EXPIRED`, `FAILED`, `REVERSED`, `CHARGEBACK`, and `UNDER_REVIEW`. These states handle errors, timeouts, and fraud investigations.

### 4.3 Invariants

- **Double-Entry:** For every valid journal entry, debits must equal credits. This is the fundamental rule of accounting and prevents value creation out of thin air.
- **Conservation of Value:** No money is created or destroyed except through defined external/source accounts. The total value in the system must always reconcile with external provider balances.
- **Append-Only:** Reversals net the original transaction; deletion is prohibited. This ensures a complete and immutable audit trail.
- **Idempotency:** Repeat processing of events or API calls must not duplicate value or votes. This protects against network retries and duplicate requests.
- **Escrow Integrity:** The system cannot release more funds than are held in escrow. This prevents the platform from operating at a loss.
- **Settlement Finality:** Escrow cannot settle twice, and a dispute prevents settlement. This ensures that funds are distributed correctly and only once.
- **Outbox Rule:** The system must *never* publish a "battle settled" event before the underlying ledger transaction commits. This prevents inconsistencies between the event stream and the database.

## 5. Result Attestation and Blockchain Finality

Artist Arena V1 mandates a native blockchain or sovereign app-chain implementation for provenance and economic auditability. This provides a decentralized layer of trust and transparency.

### 5.1 On-Chain Commitments

The blockchain state model records versioned identities, contest commitments, and escrow holds. When a battle is funded, a chain commitment is generated, anchoring the off-chain Postgres state to the immutable ledger. This commitment includes a cryptographic hash of the battle rules, the participants' identities, and the total escrowed amount.

### 5.2 Authoritative Results

Upon reaching the `PROVISIONAL_RESULT` state, the system aggregates judge scores and eligible audience votes. This result is attested via cryptographic signatures from the scoring entities. These signatures prove that the scores were genuinely submitted by authorized users and have not been tampered with.

### 5.3 Dispute Freezes

During the `DISPUTE_WINDOW`, the result is provisional. If a dispute is raised (e.g., copyright claim, collusion, AI disclosure fraud), the state transitions to `DISPUTED`. This immediately freezes the associated Contest Escrow. Settlement is blocked until a Trust Analyst or Moderator resolves the case, resulting in either a finalized result, a rescore, a voided battle, or a refund. The dispute process is logged on-chain to maintain transparency.

### 5.4 Finality

Once the dispute window expires or a dispute is resolved, the state transitions to `FINAL`. The final result, including the ruleset hash, submission commitments, and settlement directives, is anchored to the blockchain, providing immutable evidence of the competition outcome. This on-chain record serves as the ultimate source of truth for the battle's resolution.

## 6. Settlement and Exact Posting Plans

### 6.1 Idempotent Settlement

Settlement is triggered by the `battle.result_finalized.v1` event via the outbox pattern. The settlement worker processes the event idempotently. If the worker crashes or the event is delivered multiple times, the system ensures that the settlement is only executed once.

### 6.2 Exact Posting Plan (One-to-One Wager)

Assume a 100 Credit wager between Challenger (A) and Opponent (B). The system executes the following journal entries:

**1. Funding Phase:**
- Debit: User A Purchased Credits (100)
- Debit: User B Purchased Credits (100)
- Credit: Contest Escrow (200)

**2. Settlement Phase (User A Wins):**
- Debit: Contest Escrow (200)
- Credit: User A Creator Earnings (200)

**3. Cash-Out Conversion (User A withdraws 200 Credits):**
- Debit: User A Creator Earnings (200)
- Credit: Platform Revenue (2) [1% Conversion Fee]
- Credit: User A Withdrawable Balance (198)

*Note: The 1% conversion fee is calculated separately from provider network fees and is recorded in distinct ledger entries. This ensures transparent reporting of platform revenue versus operational costs.*

### 6.3 Retries, Reversals, and Chargebacks

- **Retries:** Network failures during settlement trigger exponential backoff retries via Cloudflare Queues. Idempotency keys prevent double-posting. The system is designed to eventually succeed or alert an operator if the failure is persistent.
- **Reversals:** If a settlement must be undone (e.g., post-finality legal mandate), a reversal journal is posted, negating the original settlement without deleting the history. This maintains the append-only nature of the ledger.
- **Chargebacks:** External disputes (e.g., credit card chargebacks) transition the affected funds to a `Reserve / Chargeback Hold` account. If the user's balance is insufficient, a negative balance is recorded, and the account is restricted pending review. The chargeback process is integrated with the payment provider adapters to handle notifications and evidence submission automatically.

## 7. Indexer Reconciliation, Incidents, and Recovery

### 7.1 Reconciliation

A daily scheduled job reconciles the canonical Postgres ledger against the payment provider records and the blockchain indexer. This ensures that the internal state perfectly matches the external reality.

- **Ledger-to-Provider Diff:** Identifies discrepancies between internal state and external gateways. Any mismatch triggers an alert for immediate investigation.
- **Unresolved Exception Queue:** Flags anomalies for Finance Operator review. Operators can investigate the root cause of the discrepancy and take corrective action.
- **Manual Adjustments:** Require dual control (two authorized operators) and a documented reason code. This prevents unilateral manipulation of the ledger by any single employee.

### 7.2 Incidents and Recovery

- **Fail-Closed:** In the event of a ledger or blockchain node failure, financial operations fail closed. No funds are moved if the transaction cannot be durably committed. This prevents partial state updates and financial inconsistencies.
- **Recovery Drills:** Regular testing of point-in-time recovery for the Postgres database and state sync for the blockchain nodes. These drills ensure that the system can recover from catastrophic failures without data loss.

## 8. Responsible Participation and Policy Enforcement

All financial flows are gated by the Policy Engine. The V1 implementation includes schemas and checks for responsible participation, ensuring that the platform complies with global regulations and protects vulnerable users.

- **Jurisdiction Blocks:** Prevents users in restricted regions from accessing real-money features.
- **User Value Limits:** Enforces daily, weekly, and monthly limits on deposits, wagers, and withdrawals.
- **Cooling-off and Self-Exclusion Periods:** Allows users to voluntarily restrict their access to paid features.
- **Fraud and Collusion Monitoring:** Analyzes betting patterns and voting behavior to detect coordinated manipulation.

These features default to `DISABLED_BY_POLICY` but are fully integrated into the architecture. They can be enabled dynamically based on the user's location and verified identity.

## 9. V1 Definition of Done and Work Packages

### 9.1 Definition of Done

The economic and blockchain corpus is build-complete when the following criteria are met:
- The double-entry ledger is implemented and passes exhaustive property-based tests.
- Escrow hold and release mechanisms function correctly in sandbox environments, with all edge cases (e.g., ties, cancellations) handled.
- The 1% conversion fee is accurately calculated and posted to the correct revenue accounts.
- The outbox pattern reliably triggers settlement without race conditions, even under high concurrency.
- Blockchain commitments and attestation logic are fully integrated, with a working indexer and block explorer.
- Real-money features remain behind disabled feature flags, while sandbox flows execute flawlessly and provide a realistic simulation of the production environment.

### 9.2 Work Packages

The implementation is broken down into the following work packages, which must be executed in dependency order:

1. **Implement Double-Entry Schema:** Define Postgres tables for accounts, journals, and postings. Create the foundational data model for the ledger.
2. **Implement Journal Service:** Create APIs for ledger transactions with strict idempotency and validation rules.
3. **Implement Escrow Logic:** Build state transitions for funding, holds, and releases. Ensure that the state machine invariants are enforced at the database level.
4. **Develop Conversion Engine:** Implement quoting, 1% fee calculation, and state management. Integrate with the provider adapters for fiat conversion.
5. **Build Settlement Worker:** Create queue consumers for idempotent settlement processing. Implement exponential backoff and dead-letter queues for error handling.
6. **Integrate Blockchain Attestation:** Develop node interfaces and state sync for result finality. Implement the cryptographic signing and verification logic.
7. **Establish Reconciliation Jobs:** Implement daily diffs and exception queues. Build the administrative dashboard for finance operators to review and resolve discrepancies.

## 10. Open Decisions

The following decisions remain open but do not block the V1 implementation. The system is designed with provider-agnostic adapters to accommodate these choices once finalized:

- **Regulated Payment Provider:** Selection of the provider for cash-convertible credits (e.g., Stripe, PayPal, or a specialized gaming provider).
- **Blockchain Consensus Model:** Final selection of the consensus mechanism for the sovereign app-chain (e.g., Proof of Stake, Proof of Authority).
- **Credit Exchange Rate:** The exact fiat-to-credit denomination (e.g., 100 Credits = $1.00 USD).
- **Tax Provider Integration:** Selection of the automated tax reporting service to handle 1099 generation and withholding.

*(These decisions do not block implementation; the system is built with provider-agnostic adapters.)*

## 11. Detailed Workflows and Edge Cases

### 11.1 Participant Prize Pool Funding

When a tournament features a participant-funded prize pool, the escrow mechanism scales to handle multiple contributors.

1. **Entry Fee Collection:** As each participant registers, their entry fee is deducted from their Purchased Credits and moved to the Tournament Escrow account.
2. **Dynamic Prize Pool:** The total prize pool is dynamically calculated based on the number of entrants, minus any predefined organizer fees.
3. **Cancellation and Refunds:** If the tournament is cancelled before it begins, the escrow is dissolved, and the entry fees are refunded to the participants' original accounts.
4. **Tiered Payouts:** Upon tournament completion, the settlement worker processes tiered payouts (e.g., 1st place gets 50%, 2nd place gets 30%, 3rd place gets 20%) by executing multiple ledger journals atomically.

### 11.2 Sponsor-Funded Prize Pools

Sponsor-funded pools involve external capital entering the ecosystem.

1. **Sponsor Deposit:** The sponsor deposits fiat, which is converted to Credits and placed in a dedicated Sponsor Escrow account.
2. **Milestone Releases:** For long-running challenges, the escrow may be released in milestones (e.g., 20% upon finalist selection, 80% upon final winner declaration).
3. **Unawarded Funds:** If no submission meets the sponsor's criteria (and the ruleset allows), the funds may be returned to the sponsor or rolled over to a future challenge.

### 11.3 Negative Balances and Reserves

In rare cases, such as a delayed chargeback after a user has already withdrawn their earnings, the system must handle negative balances.

1. **Chargeback Notification:** The payment provider adapter receives a chargeback webhook.
2. **Account Freeze:** The user's account is immediately restricted, preventing further withdrawals or contest entries.
3. **Negative Balance Recording:** A journal entry debits the user's Creator Earnings and credits the Chargeback Reserve. If the Creator Earnings balance drops below zero, the system records the negative state.
4. **Debt Recovery:** Future earnings or deposits are automatically routed to clear the negative balance before the user can access funds.

## 12. Security and Privacy Considerations

The economic and blockchain corpus is designed with security and privacy as paramount concerns.

### 12.1 Financial Security

- **Webhook Replay Defense:** All incoming webhooks from payment providers are verified using cryptographic signatures and checked against a nonce cache to prevent replay attacks.
- **Velocity Limits:** The system monitors the frequency and volume of transactions to detect anomalous behavior indicative of account takeover or money laundering.
- **Dual Control:** As previously mentioned, manual adjustments to the ledger require approval from two distinct, authorized operators.

### 12.2 Privacy and Data Minimization

- **Separation of KYC Data:** Sensitive identity verification data (e.g., government IDs) is stored in a segregated, highly secure database or managed entirely by a third-party KYC provider. The core Postgres ledger only stores abstract user IDs.
- **On-Chain Privacy:** The blockchain records cryptographic hashes and pseudonymous identifiers. It does not store plain-text personal information or large media files, ensuring compliance with data privacy regulations like GDPR.

## 13. Observability and Auditing

To maintain trust and operational excellence, the system provides comprehensive observability.

### 13.1 Audit Logging

Every state transition in the battle lifecycle and every financial transaction generates an immutable audit log entry. These logs include the actor, timestamp, previous state, next state, reason code, and associated policy evaluations.

### 13.2 Finance Dashboard

Finance operators have access to a dedicated dashboard that provides real-time visibility into:
- Total funds in escrow
- Daily conversion volume and platform revenue
- Pending chargebacks and disputes
- Reconciliation exception queues

This dashboard is critical for monitoring the health of the economic ecosystem and responding quickly to issues.

## 14. Conclusion

The Artist Arena V1 economic and blockchain control corpus is a robust, scalable, and secure foundation for the creator economy. By strictly separating economic instruments, enforcing rigorous state machines, and leveraging blockchain technology for immutable attestation, the platform ensures fairness, transparency, and compliance. The mandatory construction of these features in V1 guarantees that Artist Arena is ready to operate as a premier competitive platform as soon as the necessary policy gates are lifted.
