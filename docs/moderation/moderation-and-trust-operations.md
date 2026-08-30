# Moderation and Trust Operations

## 1. Overview
This document specifies the Moderation and Trust Operations domain for Artist Arena V1. It defines the systems, workflows, policies, and integrations required to ensure content safety, manage rights claims, handle disputes, protect minors, prevent fraud, and maintain platform integrity. In accordance with Owner Directive 0001, all capabilities described herein—including moderation of real-value transactions, complex appeals, and blockchain-anchored evidence—are mandatory V1 implementation scope, regardless of production activation gates.

## 2. Product Rules and Policies

### 2.1 Content Safety and Acceptable Use
*   **Prohibited Content:** Illegal content, non-consensual intimate imagery (NCII), child sexual abuse material (CSAM), terrorism/extremism, incitement to violence, targeted harassment, and doxxing.
*   **Regulated Content:** Hate speech, severe profanity, mature themes, and adult content must be labeled, age-gated, and subject to jurisdiction-specific visibility rules.
*   **AI and Synthetic Media:** Must comply with the Pure Human, Hybrid, and AI Open division rules. Undisclosed AI generation in Pure Human or Hybrid divisions is a violation of trust policies, not strictly a safety issue, but is handled via the dispute system. Deepfakes used for impersonation or non-consensual depiction are strictly prohibited.

### 2.2 Rights, Consent, and Intellectual Property
*   **Copyright Infringement:** Handled via a formal DMCA-style notice and takedown process, adapted for global jurisdictions.
*   **Counter-Notices:** Users have the right to submit counter-notices to restore content removed due to rights claims, subject to legal timelines.
*   **Consent and Likeness:** Unauthorized use of a person's likeness, voice, or identity (especially via AI) requires explicit consent. Violations are subject to immediate removal and account penalties.

### 2.3 Fraud, Trust, and Economic Integrity
*   **Collusion and Match-Fixing:** Coordinated efforts to manipulate battle outcomes, rankings, or prize distributions are prohibited.
*   **Payment Fraud:** Use of stolen payment methods, chargeback abuse, and money laundering attempts trigger automated holds and manual review.
*   **Vote Manipulation:** Sybil attacks, bot voting, and incentivized voting rings will result in vote invalidation and account suspension.

### 2.4 Protection of Minors
*   **Age Requirements:** Minimum age for account creation is 13 (or higher per local law). Minimum age for monetization, real-money wagering, and cash-out is strictly 18 (or higher per jurisdiction).
*   **Age Verification:** Required for access to mature content, monetization features, and specific competitive divisions.
*   **Interaction Limits:** Accounts identified as minors have restricted direct messaging and visibility settings by default.

### 2.5 Staff Accountability
*   **Principle of Least Privilege:** Staff access to user data, moderation tools, and financial ledgers is strictly role-based.
*   **Auditability:** Every staff action (viewing sensitive data, applying penalties, modifying state) is logged immutably.
*   **Separation of Duties:** Financial overrides and severe account bans require multi-party approval (maker-checker).

## 3. Actors and Permissions

| Role | Permissions |
| :--- | :--- |
| **User / Creator** | Submit reports, file rights claims, submit appeals, view case status. |
| **Moderator (L1)** | Review standard reports (spam, basic safety), apply temporary suspensions, remove content, escalate complex cases. |
| **Trust Analyst (L2)** | Investigate fraud, collusion, complex harassment, and AI division violations. Can apply permanent bans and initiate financial holds. |
| **Rights Specialist** | Process DMCA notices, counter-notices, and likeness disputes. |
| **Finance Operator** | Review financial holds, process chargebacks, approve/deny cash-out requests based on fraud signals. |
| **Admin / Policy Manager** | Configure moderation rules, manage staff roles, review audit logs, handle high-profile escalations. |

## 4. Domain Boundaries and Entities

### 4.1 Domain Boundaries
The Moderation and Trust Operations domain interacts with:
*   **Identity & Access Management (IAM):** For user roles, age verification status, and account suspension enforcement.
*   **Content & Media:** To flag, hide, or remove media assets and metadata.
*   **Competition & Judging:** To invalidate votes, disqualify entries, or pause battles during investigations.
*   **Economy & Ledger:** To freeze funds, reverse transactions, or apply penalties.
*   **Blockchain/Ledger:** To anchor dispute records, moderation hashes, and finality states.

### 4.2 Key Entities
*   `Report`: A user-generated or system-generated flag regarding content, behavior, or a transaction.
*   `Case`: A consolidated investigation container linking multiple reports, entities, and evidence.
*   `Action`: A specific penalty or remediation applied to an entity (e.g., Content Takedown, Account Suspension, Ledger Hold).
*   `Appeal`: A user request to review and reverse an `Action`.
*   `RightsClaim`: A formal legal notice of copyright or likeness infringement.
*   `Evidence`: Immutable records (screenshots, logs, transaction hashes) attached to a `Case`.

## 5. State Machines

### 5.1 Case State Machine
*   `OPEN`: Case created, awaiting assignment.
*   `IN_REVIEW`: Assigned to a moderator/analyst.
*   `ESCALATED`: Sent to a higher tier or specialized team.
*   `ACTION_PENDING`: Decision made, awaiting multi-party approval (if required).
*   `RESOLVED_ACTION_TAKEN`: Case closed with penalties applied.
*   `RESOLVED_NO_ACTION`: Case closed, no violation found.

### 5.2 Rights Claim State Machine
*   `RECEIVED`: Claim submitted.
*   `VALIDATING`: Staff verifying completeness and legal standing.
*   `ACCEPTED_TAKEDOWN`: Content removed, user notified.
*   `REJECTED`: Claim invalid or incomplete.
*   `COUNTER_NOTICE_RECEIVED`: User submitted counter-notice.
*   `RESTORED`: Content restored after counter-notice (and legal waiting period).

### 5.3 Appeal State Machine
*   `SUBMITTED`: Appeal filed by user.
*   `UNDER_REVIEW`: Staff reviewing appeal.
*   `GRANTED`: Original action reversed or modified.
*   `DENIED`: Original action upheld.

## 6. Workflows

### 6.1 Content Moderation Workflow
1.  **Ingestion:** User submits a report OR automated system (e.g., hash matching, text analysis) flags content.
2.  **Triage:** System prioritizes the report based on severity (e.g., CSAM is highest priority).
3.  **Review:** Moderator views content and context in the Moderation Tool.
4.  **Decision:** Moderator selects violation type and applies standard penalty (e.g., 7-day suspension + content removal).
5.  **Enforcement:** System updates IAM and Content domains.
6.  **Notification:** User receives an in-app and email notification detailing the violation and appeal rights.

### 6.2 Rights Claim and Counter-Notice Workflow
1.  **Submission:** Rights holder submits a claim via web form.
2.  **Review:** Rights Specialist verifies the claim.
3.  **Takedown:** Content is hidden. Uploader is notified and given a strike.
4.  **Counter-Notice:** Uploader submits a counter-notice affirming their rights.
5.  **Forwarding:** Counter-notice is sent to the original claimant.
6.  **Resolution:** If claimant does not provide proof of legal action within X days (e.g., 10-14 days per DMCA), content is restored.

### 6.3 Fraud and Collusion Investigation
1.  **Detection:** System detects anomalous voting patterns or suspicious financial flows (e.g., circular wagering).
2.  **Hold:** System automatically places a temporary hold on associated funds and pauses the relevant battle.
3.  **Investigation:** Trust Analyst reviews logs, IP addresses, device fingerprints, and transaction history.
4.  **Resolution:** Analyst confirms fraud (invalidates votes, seizes funds, bans users) or clears the users (releases holds, resumes battle).

## 7. Evidence Chain of Custody
*   **Immutability:** All evidence (reports, system logs, snapshots of content at the time of the report) must be stored immutably.
*   **Blockchain Anchoring:** Hashes of critical case evidence, moderation decisions, and rights claims must be anchored to the native blockchain/ledger to ensure verifiable history, especially for cases involving financial disputes or permanent bans. Sensitive PII must remain off-chain.
*   **Access Logs:** Every staff access to a case or piece of evidence is logged.

## 8. API and Event Implications

### 8.1 Required APIs (Internal/Admin)
*   `POST /admin/cases`: Create a case.
*   `GET /admin/cases/{id}`: Retrieve case details and evidence.
*   `POST /admin/cases/{id}/actions`: Apply an action (requires appropriate RBAC).
*   `POST /admin/rights-claims`: Submit a rights claim.

### 8.2 Required Events (Async)
*   `ReportSubmittedEvent`: Triggers triage and case creation.
*   `ModerationActionAppliedEvent`: Consumed by IAM (to suspend), Content (to hide), and Economy (to freeze).
*   `AppealSubmittedEvent`: Triggers review workflow.
*   `FraudSignalDetectedEvent`: Triggers automated holds.

## 9. Dependencies
*   **Internal:** IAM (Authentication/Authorization), Content Service, Economy/Ledger Service, Notification Service.
*   **External:** Third-party automated moderation APIs (e.g., for CSAM hashing, toxicity scoring), Identity Verification providers (for age/KYC), Payment Gateways (for chargeback data).

## 10. Security, Privacy, and Economic Impact
*   **Privacy:** Moderation tools must obscure PII where not strictly necessary for the investigation.
*   **Security:** Multi-factor authentication (MFA) is strictly required for all staff roles.
*   **Economic Impact:** Erroneous fraud flags can lock user funds; the system must support rapid SLA for financial holds and clear compensation mechanisms for platform errors. The 1% conversion fee is not applied to seized or refunded amounts.

## 11. Abuse and Failure Modes
*   **Mass Reporting:** Coordinated attacks to silence a creator. *Mitigation:* System must detect report clustering and weigh reporter reputation.
*   **Staff Abuse:** A rogue moderator banning users or releasing funds. *Mitigation:* Maker-checker rules for high-impact actions, strict audit logging, and anomaly detection on staff behavior.
*   **Automated System False Positives:** Over-aggressive AI flagging. *Mitigation:* Human-in-the-loop requirement for permanent bans and financial seizures.

## 12. Observability, Analytics, and Performance
*   **Metrics:** Time-to-resolution (TTR) by severity, report volume by category, false positive rate (measured by successful appeals), staff action volume.
*   **Dashboards:** Real-time queues for L1/L2 teams, SLA tracking, and trending violation types.
*   **Performance:** The reporting ingestion API must handle high burst traffic (e.g., during a live event) without degrading the main application.

## 13. Accessibility
*   Reporting flows and appeal forms must meet WCAG 2.1 AA standards.
*   Users must be able to submit evidence in multiple formats (text, images, audio clips) easily.

## 14. Concrete Tests and Acceptance Criteria

### 14.1 Acceptance Criteria
*   [ ] A user can submit a report on any piece of content or user profile.
*   [ ] A moderator can view the report, assess the content, and apply a predefined penalty.
*   [ ] The system automatically enforces the penalty (e.g., hides content, suspends user) across all domains.
*   [ ] A user can submit an appeal, and a different staff member can review and reverse the action.
*   [ ] A Rights Claim workflow exists supporting notice, takedown, and counter-notice.
*   [ ] High-impact actions (e.g., permanent ban, fund seizure) require two-party (maker-checker) approval.
*   [ ] All moderation actions and evidence hashes are anchored to the blockchain.

### 14.2 Tests
*   **Integration Test:** Simulate a mass reporting attack; verify the system groups reports into a single case and does not auto-ban the target without human review.
*   **E2E Test:** User A reports User B for fraud. Analyst applies a financial hold. Verify User B cannot withdraw funds. Analyst resolves case as false positive. Verify User B can withdraw funds.
*   **Security Test:** Attempt to call `POST /admin/cases/{id}/actions` with a standard User token; verify 403 Forbidden.

## 15. V1 Definition of Done
The Moderation and Trust Operations domain is "Done" for V1 when the full lifecycle of reporting, investigation, action, and appeal is operational. This includes the integration with IAM for enforcement, the Economy domain for financial holds, and the Blockchain domain for evidence anchoring. The system must support the Pure Human, Hybrid, and AI Open division rules, and handle complex rights claims. All staff tools must enforce RBAC and audit logging.

## 16. Dependency-Ordered Work Packages
1.  **Core Data Models:** Define schemas for Reports, Cases, Actions, and Appeals.
2.  **Internal APIs & RBAC:** Implement staff roles and backend endpoints for case management.
3.  **User Reporting Flow:** Build the frontend reporting UI and ingestion API.
4.  **Enforcement Integrations:** Connect Actions to IAM (suspensions) and Content (takedowns).
5.  **Rights Claim System:** Implement the DMCA-style notice and counter-notice workflow.
6.  **Financial Holds:** Integrate Trust Operations with the Economy/Ledger domain.
7.  **Blockchain Anchoring:** Implement evidence and decision hashing to the native chain.
8.  **Appeals & Auditing:** Build the user appeals flow and the staff audit logs.

## 17. Unresolved ADRs
*   **ADR-MOD-001:** Selection of third-party automated moderation vendor (e.g., AWS Rekognition vs. Google Cloud Vision) for initial CSAM/NSFW hashing.
*   **ADR-MOD-002:** Exact retention period for PII associated with permanently banned accounts (pending jurisdiction-specific legal review).

## 18. Detailed Operational Guidelines

### 18.1 Handling Complex Harassment Cases
Harassment in a competitive environment can often blur the line between acceptable "trash talk" and targeted abuse. Trust Analysts must evaluate the context of the interaction, the history between the users, and the severity of the language used.
When evaluating harassment, analysts must consider the division in which the users are competing. While the rules remain consistent, the expectation of professional conduct may vary slightly depending on the specific community norms of a given discipline (e.g., rap battles vs. visual art competitions). However, any language that crosses into hate speech, threats of real-world violence, or sustained, coordinated bullying must result in immediate suspension, regardless of the context. The platform's commitment to safety supersedes any defense of "competitive spirit."

### 18.2 Impersonation and Identity Verification
Impersonation is a critical threat to the integrity of Artist Arena, particularly given the financial stakes involved. The platform employs a multi-tiered approach to identity verification. Standard accounts require basic email verification, while accounts participating in real-money wagering or monetization features must undergo a more rigorous KYC (Know Your Customer) process.
If a user is reported for impersonation, Trust Analysts must cross-reference the reported account with known verified profiles, analyze the account's creation date, IP history, and linked social media accounts. In cases where AI-generated content is used to mimic another creator's style or likeness without consent, the case is escalated to the Rights Specialist team for review against the platform's likeness and consent policies. The system must support rapid freezing of funds associated with suspected impersonator accounts to prevent capital flight before the investigation concludes.

### 18.3 Managing the 1% Conversion Fee in Disputes
The 1% conversion fee, as mandated by the Founder Directive, is a core component of the platform's economic model. However, its application during disputes requires careful handling. If a transaction is reversed due to fraud or a successful appeal, the platform must not retain the 1% fee on the reversed amount. The ledger system must support precise rollback of both the principal amount and the associated fee, ensuring that the user's balance is accurately restored.
Furthermore, in cases where a user's account is permanently banned and their remaining balance is seized (subject to legal constraints), the platform must generate clear, auditable records of the seizure, separating the principal from any fees that were previously collected. This transparency is crucial for regulatory compliance and financial reconciliation.

### 18.4 Escalation Pathways for High-Profile Creators
Cases involving high-profile creators (e.g., those with large followings or significant financial activity) carry a higher risk of reputational damage to the platform. Therefore, any moderation action that would result in a suspension, ban, or significant financial hold for a verified, high-profile creator must automatically escalate to the Admin / Policy Manager tier for review before enforcement.
This escalation pathway does not exempt high-profile creators from the rules; rather, it ensures that the application of the rules is consistent, legally sound, and communicated effectively. The Policy Manager must document the rationale for the decision, and this documentation must be securely archived alongside the case evidence.

### 18.5 Continuous Improvement and Policy Updates
The Moderation and Trust Operations domain is not static. As new forms of abuse emerge (e.g., novel AI generation techniques, new methods of financial fraud), the platform's policies and detection mechanisms must evolve. The Admin team is responsible for conducting monthly reviews of case metrics, false positive rates, and user feedback to identify areas for improvement.
Any significant update to the Acceptable Use Policy or the Moderation Guidelines must be communicated to the user base with a clear summary of the changes and the effective date. The system must require users to acknowledge these updates upon their next login, ensuring that the platform maintains a legally binding record of user consent to the governing rules.
