# Artist Arena V1: Sponsorship and Organizer Domain Specification

## 1. Domain Overview

The Sponsorship and Organizer domain is a core pillar of Artist Arena V1, empowering brands, agencies, and third-party organizers to discover talent, fund competitions, and engage with the creator economy. This specification outlines the architecture, rules, and implementation requirements for sponsorships, organizer marketplaces, branded campaigns, prize pools, and talent scouting, fully compliant with Owner Directive 0001 [1].

This domain encompasses the creation of branded briefs, the management of sponsor-funded and mixed prize pools, the execution of campaign operations, and the provision of analytics and reporting. It also covers the organizer marketplace, scout search capabilities, contact requests, and the handling of conflicts and rights terms.

All capabilities described herein, including those previously marked as future or sandbox-only, are mandatory V1 engineering scope [2]. Activation of real-money features and public campaigns remains subject to policy, compliance, and founder approval gates.

The goal is to create a robust, secure, and transparent ecosystem where sponsors can confidently invest in creator competitions, organizers can build sustainable businesses, and creators can discover and monetize their talent through fair, verifiable processes.

## 2. Product Rules and Core Mechanics

### 2.1 Sponsorship and Branded Briefs
*   **Branded Briefs:** Sponsors can create structured briefs detailing campaign goals, required disciplines, submission criteria, and brand guidelines. These briefs serve as the foundational contract for the campaign, outlining exactly what is expected from participating creators. The brief must include specific deliverables, timelines, and any required brand assets (e.g., logos, specific audio stems, or thematic elements).
*   **Sponsored Challenges:** Briefs can be instantiated as sponsored challenges, battles, or tournaments. A sponsor might launch a global beat-making competition or a localized rap battle, tailoring the format to their target audience and marketing objectives. The system must support various competition formats seamlessly.
*   **Rights Terms:** Every sponsored event must explicitly define the rights terms (e.g., exclusive licensing, non-exclusive usage, buyout) for submitted and winning works. These terms must be accepted by creators upon entry. The platform must provide standardized rights templates to simplify this process while allowing for custom agreements when necessary. The acceptance of these terms is cryptographically anchored to ensure non-repudiation.
*   **Brand Safety:** Sponsors can define brand safety rules, including disallowed content themes and mandatory moderation review before submissions are visible to the public or the sponsor. This includes automated scanning for inappropriate content, copyright infringement, and adherence to the specific guidelines outlined in the brief.

### 2.2 Prize Pools (Sponsor, Participant, and Mixed)
*   **Sponsor-Funded Pools:** Sponsors can fund prize pools using fiat currency or credits. Funds must be escrowed before the competition begins. This guarantees that the advertised prize money is available and will be distributed upon the successful completion of the event, building trust within the creator community.
*   **Participant-Funded Pools:** Organizers can configure entry fees (in credits) that contribute to the prize pool. This enables community-driven events where the stakes are determined by the participants themselves. The platform must handle the secure collection and escrow of these entry fees.
*   **Mixed Pools:** Competitions can feature a base prize funded by a sponsor, augmented by participant entry fees or audience contributions. This hybrid model allows sponsors to amplify their impact while encouraging active community participation. The logic for distributing mixed pools must be transparent and clearly communicated to all participants.
*   **Settlement:** Prize distribution is strictly tied to the finalized, attested results of the competition. The platform's 1% conversion fee applies to credit-to-cash conversions [1]. The settlement process must be automated, secure, and auditable, ensuring that winners receive their funds promptly and accurately.
*   **Escrow and Blockchain Anchoring:** All prize commitments, whether sponsor or participant-funded, must be recorded and escrowed. Settlement attestations must be anchored to the native blockchain [2]. This provides an immutable record of the transaction, protecting all parties involved and ensuring compliance with financial regulations.

### 2.3 Organizer Marketplace
*   **Marketplace Access:** Verified organizers can list their services, past event portfolios, and available sponsorship inventory. This creates a vibrant ecosystem where experienced event managers can connect with brands looking to host competitions. The marketplace must support rich profiles, including reviews, ratings, and detailed case studies of past events.
*   **Sponsor-Organizer Matching:** Sponsors can browse the marketplace to find experienced organizers to run their campaigns. The platform should offer search and filtering tools based on the organizer's expertise, past performance, and availability.
*   **Commission Structures:** Organizers can charge flat fees or take a percentage of the sponsor's budget, handled transparently through the platform's payment routing. The system must support flexible commission models, ensuring that organizers are compensated fairly for their work while providing sponsors with clear visibility into the costs involved.

### 2.4 Scout Search and Opportunities
*   **Talent Discovery:** Scouts and A&R representatives can search the creator database using advanced filters (discipline, division, rating, consistency, verified work, and location where voluntarily shared). This powerful search capability allows industry professionals to pinpoint the exact talent they need, based on a comprehensive set of criteria. The search engine must be highly performant and capable of handling complex queries across a large dataset.
*   **Shortlists:** Scouts can create private, organized lists of prospective talent. These shortlists can be used to track promising creators over time, collaborate with team members, and manage the talent acquisition pipeline.
*   **Contact Requests:** Verified scouts can send structured contact requests or direct opportunity offers to creators. Creators can configure their inbound request settings (e.g., minimum offer size, required information). This ensures that creators are only contacted with relevant and valuable opportunities, protecting them from spam and unwanted solicitations.

### 2.5 Conflicts of Interest
*   **Judge Conflicts:** Judges selected for sponsored events must declare any conflicts of interest regarding the sponsor or known participants. This is critical for maintaining the integrity of the competition and ensuring that the judging process is fair and unbiased. The platform must provide a formal mechanism for judges to declare conflicts and for organizers to review and address them.
*   **Organizer Independence:** Organizers managing mixed pools must adhere to strict neutrality rules, verifiable via audit logs. They must not have any financial interest in the outcome of the competition beyond their agreed-upon commission. The system must track all organizer actions to ensure compliance with these rules.

## 3. Actors and Permissions

| Actor | Description | Key Permissions |
| :--- | :--- | :--- |
| **Sponsor Member** | Representative of a brand or agency. | Create briefs, fund escrow, view campaign analytics, access scout search, approve final deliverables. |
| **Organizer** | Third-party event creator and manager. | Create events, configure prize pools, select judges, manage marketplace profile, moderate submissions, finalize results. |
| **Scout / A&R** | Talent discovery professional. | Advanced search, create shortlists, send contact requests, view detailed creator analytics. |
| **Competitor Creator** | Platform creator participating in events. | View briefs, accept rights terms, submit work, receive prizes, manage contact preferences, view personal analytics. |
| **Compliance Operator** | Platform staff overseeing legal and financial rules. | Approve sponsor accounts, verify escrow funds, audit mixed pools, review rights disputes, manage platform-wide safety settings. |
| **Trust Analyst** | Platform staff focused on moderation and safety. | Review flagged content, investigate fraud reports, enforce community guidelines, manage user bans and suspensions. |

## 4. Domain Boundaries and Entities

### 4.1 Key Entities

*   `Campaign`: The overarching sponsor initiative. It contains metadata such as the campaign name, description, start and end dates, overall budget, and target audience.
*   `Brief`: The specific requirements, rules, and rights terms for a campaign. It details the creative prompt, required deliverables, brand guidelines, and any specific constraints or limitations.
*   `PrizePool`: The financial construct holding escrowed funds (sponsor, participant, or mixed). It tracks the total amount, the source of the funds, the distribution rules, and the current state of the escrow.
*   `OrganizerProfile`: The marketplace listing for an organizer. It includes their name, bio, contact information, portfolio of past events, ratings, and reviews.
*   `ScoutList`: A private collection of creator profiles maintained by a scout. It allows scouts to organize and track promising talent, with notes and tags for easy reference.
*   `ContactRequest`: A structured message initiating a professional opportunity. It includes the sender's details, the nature of the opportunity, any proposed compensation, and a clear call to action for the creator.
*   `RightsAgreement`: The immutable record of terms accepted by a creator for a specific submission. It details the specific rights granted to the sponsor, the duration of the agreement, and any compensation or royalties involved.

### 4.2 State Machines

**PrizePool State Machine:**
`DRAFT` (Initial creation) -> `FUNDING_PENDING` (Waiting for funds to clear) -> `ESCROWED` (Funds secured) -> `LOCKED` (Competition active, funds cannot be withdrawn) -> `SETTLEMENT_PENDING` (Results finalized, waiting for distribution) -> `DISTRIBUTED` (Funds sent to winners) | `REFUNDED` (Event cancelled, funds returned)

**ContactRequest State Machine:**
`DRAFT` (Being written by scout) -> `SENT` (Dispatched to creator) -> `DELIVERED` (Received by creator's inbox) -> `READ` (Opened by creator) -> `ACCEPTED` (Creator agrees to terms) | `DECLINED` (Creator rejects offer) | `EXPIRED` (Offer time limit reached)

**Campaign State Machine:**
`DRAFT` (Initial setup) -> `REVIEW_PENDING` (Waiting for compliance approval) -> `APPROVED` (Ready to launch) -> `ACTIVE` (Accepting submissions) -> `JUDGING` (Submissions closed, under review) -> `COMPLETED` (Results announced, prizes distributed) | `CANCELLED` (Campaign aborted)

## 5. User and Operator Workflows

### 5.1 Sponsor Campaign Creation
1.  **Initiation:** Sponsor logs into the platform and initiates the creation of a new `Campaign`. They provide basic details such as the campaign name, goals, and target audience.
2.  **Brief Development:** Sponsor drafts a detailed `Brief`, outlining the creative requirements, brand guidelines, and specific deliverables expected from the creators. They also define the rights terms that creators must accept.
3.  **Prize Pool Configuration:** Sponsor defines the `PrizePool` structure, including the total amount, the distribution among winners (e.g., 1st place, 2nd place, honorable mentions), and the funding source (fiat or credits).
4.  **Escrow Funding:** Sponsor initiates the funding process. The platform securely processes the payment and places the funds into escrow, changing the `PrizePool` state to `ESCROWED`.
5.  **Organizer Selection (Optional):** Sponsor can choose to manage the event directly or select an `Organizer` from the marketplace to handle the logistics, judging, and community engagement.
6.  **Compliance Review:** If the campaign involves real-money prizes or has high visibility, a `Compliance Operator` reviews the campaign details, brief, and rights terms to ensure adherence to platform policies and legal regulations.
7.  **Launch:** Once approved, the campaign goes live. Creators can view the brief, accept the `RightsAgreement`, and submit their work.
8.  **Monitoring:** Throughout the campaign, the sponsor can monitor submissions, engagement metrics, and audience feedback via the analytics dashboard.
9.  **Finalization:** After the judging period, the results are finalized, and the `PrizePool` state transitions to `SETTLEMENT_PENDING` and then `DISTRIBUTED`.

### 5.2 Talent Scouting
1.  **Search and Discovery:** Scout uses the advanced search interface to find creators matching specific criteria. They might filter by discipline (e.g., beat production), division (e.g., Pure Human), rating (e.g., top 10%), and consistency (e.g., active in the last 30 days).
2.  **Shortlisting:** Scout identifies promising creators and adds them to a custom `ScoutList` for future reference and tracking. They can add private notes and tags to each profile.
3.  **Opportunity Drafting:** Scout decides to reach out to a specific creator with an opportunity (e.g., a record deal, a collaboration, a sponsored post). They draft a structured `ContactRequest` detailing the offer, compensation, and required next steps.
4.  **Request Dispatch:** Scout sends the request. The system checks the creator's inbound request settings to ensure the offer meets their minimum criteria before delivering it.
5.  **Creator Review:** Creator receives the request, reviews the terms, and decides whether to accept or decline. If accepted, the platform facilitates the next steps, which may involve signing a formal contract or initiating a secure communication channel.

### 5.3 Organizer Marketplace Engagement
1.  **Profile Creation:** An experienced event manager creates an `OrganizerProfile` on the marketplace, detailing their expertise, past successes, and available services.
2.  **Verification:** A `Compliance Operator` reviews the profile and verifies the organizer's credentials before making the listing public.
3.  **Sponsor Discovery:** A sponsor browsing the marketplace finds the organizer's profile and reviews their portfolio.
4.  **Negotiation:** The sponsor contacts the organizer to discuss a potential collaboration. They negotiate the scope of work, timeline, and commission structure.
5.  **Contracting:** Once terms are agreed upon, the platform facilitates the formalization of the agreement, linking the organizer to the specific `Campaign`.
6.  **Execution:** The organizer manages the campaign, handling everything from promoting the event to moderating submissions and coordinating the judging panel.

## 6. API and Event Implications

### 6.1 Core APIs
*   `POST /api/v1/sponsors/campaigns`: Create a new campaign. Requires campaign metadata, brief details, and prize pool configuration.
*   `GET /api/v1/sponsors/campaigns/{id}`: Retrieve detailed information about a specific campaign, including its current state and associated brief.
*   `PUT /api/v1/sponsors/campaigns/{id}`: Update campaign details (only allowed in `DRAFT` state).
*   `POST /api/v1/sponsors/campaigns/{id}/fund`: Initiate escrow funding. Triggers the payment processing integration.
*   `GET /api/v1/organizers/marketplace`: Browse available organizers. Supports complex filtering and pagination.
*   `POST /api/v1/scouts/search`: Execute advanced talent search. Requires a structured query object defining the search criteria.
*   `POST /api/v1/scouts/requests`: Send a contact request. Requires the target creator ID, the opportunity details, and the proposed terms.
*   `GET /api/v1/creators/{id}/requests`: Retrieve a list of inbound contact requests for a specific creator.

### 6.2 Key Events
*   `CampaignCreated`: Fired when a new campaign is successfully created. Triggers notifications to compliance operators for review.
*   `PrizePoolEscrowed`: Fired when funds are successfully secured in escrow. Triggers the transition of the campaign state to `APPROVED` or `ACTIVE`.
*   `SubmissionReceived`: Fired when a creator submits work to a campaign. Triggers moderation workflows and updates campaign analytics.
*   `RightsAccepted`: Fired when a creator explicitly agrees to the rights terms. Triggers the anchoring of the agreement hash to the blockchain.
*   `PrizeDistributed`: Fired when prize funds are successfully transferred to the winners. Triggers the finalization of the campaign and updates the ledger.
*   `ContactRequestSent`: Fired when a scout dispatches a request. Triggers delivery mechanisms and updates the scout's tracking dashboard.
*   `ContactRequestAccepted`: Fired when a creator accepts an offer. Triggers notifications to the scout and initiates the next steps in the workflow.

## 7. Security, Privacy, and Abuse Modes

### 7.1 Security
*   **Escrow Fraud:** Mitigation: All prize funds must be cryptographically verified in escrow before an event status changes to `LOCKED`. The system must integrate with secure, audited payment providers and utilize multi-signature wallets where appropriate.
*   **Data Breaches:** Mitigation: Strict access controls (RBAC/ABAC) must be enforced across all APIs and data stores. Sensitive information, such as financial details and private communications, must be encrypted at rest and in transit.
*   **Account Takeover:** Mitigation: Mandatory multi-factor authentication (MFA) for all sponsor, organizer, and scout accounts. Continuous monitoring for suspicious login activity.

### 7.2 Privacy
*   **Scout Search Privacy:** Scout search must respect creator privacy settings; location data is only searchable if voluntarily shared by the creator. Creators must have granular control over what information is visible to scouts and sponsors.
*   **Data Minimization:** The platform should only collect and store the data necessary for the execution of campaigns and the facilitation of opportunities.
*   **GDPR/CCPA Compliance:** The system must support data subject access requests (DSARs), allowing users to view, export, or delete their personal data.

### 7.3 Abuse Modes
*   **Scout Spam:** Mitigation: Rate-limiting on `ContactRequests`; requirement for verified scout status; creator-defined inbound filters (e.g., minimum offer size). The platform must also monitor for repetitive or abusive messaging patterns.
*   **Rights Exploitation:** Mitigation: `RightsAgreements` must be clearly presented, requiring explicit opt-in. The agreement hash is anchored to the blockchain to prevent retroactive changes. The platform should provide educational resources to help creators understand the terms they are agreeing to.
*   **Fake Submissions/Bots:** Mitigation: Implementation of robust CAPTCHA, device fingerprinting, and behavioral analysis to detect and block automated submissions. Integration with the AI detection system to ensure compliance with the chosen division (Pure Human, Hybrid, AI Open).

## 8. Observability, Analytics, and Reporting

### 8.1 Sponsor Analytics
Sponsors require deep insights into the performance of their campaigns to measure ROI and optimize future initiatives. The platform must provide real-time dashboards showing:
*   **Reach and Engagement:** Total views, unique visitors, submission volume, and audience interaction rates (likes, comments, shares).
*   **Demographics:** Aggregated, anonymized data on the audience and participants, including age, location, and interests.
*   **Content Performance:** Analysis of the top-performing submissions, highlighting trends and identifying the most effective creative approaches.
*   **Financial Reporting:** Detailed breakdown of prize pool distribution, platform fees, and any associated costs.

### 8.2 Organizer Performance
To maintain the quality of the marketplace, the platform must track and display verified metrics for organizers:
*   **Track Record:** Number of events successfully completed, total prize money distributed, and average event duration.
*   **Creator Satisfaction:** Ratings and reviews from creators who have participated in the organizer's events.
*   **Sponsor Satisfaction:** Ratings and reviews from sponsors who have hired the organizer.

### 8.3 System Observability
The engineering team requires comprehensive monitoring to ensure the stability and performance of the platform:
*   **Financial Health:** Monitor escrow lock/release times, ledger reconciliation rates, and payment gateway error rates.
*   **Workflow Efficiency:** Track the time taken for compliance reviews, the acceptance rates of contact requests, and the average duration of the judging process.
*   **System Performance:** Monitor API latency, database query times, and error rates across all core services.

## 9. V1 Definition of Done and Acceptance Criteria

The Sponsorship and Organizer domain is considered "Done" for V1 when the following criteria are met:

*   **Sponsorships:** Sponsors can successfully create detailed briefs, fund escrow accounts securely, and launch events that are visible to the target audience.
*   **Prize Pools:** The system correctly handles sponsor-only, participant-only, and mixed prize pools, accurately calculating and deducting the 1% conversion fee where applicable. All funds are securely escrowed and distributed according to the finalized results.
*   **Marketplace:** Verified organizers can list their profiles, and sponsors can browse, filter, and select organizers for their campaigns. The platform facilitates the connection and tracks the engagement.
*   **Scouting:** Scouts can execute complex searches across the creator database, create and manage shortlists, and send structured contact requests that respect the creators' inbound filters.
*   **Blockchain Integration:** All prize pool commitments, rights agreement hashes, and settlement attestations are successfully anchored to the native chain (or a robust simulation environment), providing an immutable audit trail.
*   **Divisions:** Search filters, campaign configurations, and moderation workflows correctly respect and enforce the rules for Pure Human, Hybrid, and AI Open divisions.
*   **Testing:** Comprehensive end-to-end tests cover all critical workflows, including campaign creation, escrow funding, submission processing, and prize distribution. All tests pass consistently in the staging environment.
*   **Documentation:** API documentation is complete, accurate, and accessible to internal developers and external partners (if applicable).

## 10. Dependency-Ordered Work Packages

The implementation of this domain should proceed in the following order to manage dependencies effectively:

1.  **Core Entities and Schemas (Sprint 1):** Define and implement the database schemas for `Campaign`, `Brief`, `OrganizerProfile`, `ScoutList`, and `ContactRequest`. Establish the basic CRUD operations for these entities.
2.  **Financial Engine Integration (Sprint 2):** Connect the `PrizePool` logic to the core platform ledger and external escrow services. Implement the state machine for prize pools and ensure secure funding and distribution mechanisms.
3.  **Search Infrastructure (Sprint 3):** Build the advanced indexing and querying capabilities required for the scout search feature. Optimize for performance and scalability, ensuring that complex filters (including division and verified work) operate efficiently.
4.  **Workflow Engines and State Machines (Sprint 4):** Implement the robust state machines for `Campaigns` and `ContactRequests`. Ensure that state transitions trigger the appropriate events and notifications.
5.  **Blockchain Anchoring (Sprint 5):** Integrate the rights agreements and settlement attestations with the native blockchain module. Develop the mechanisms for hashing documents and verifying their integrity on-chain.
6.  **Analytics and Reporting (Sprint 6):** Build the sponsor reporting dashboards and the organizer performance metrics. Implement the data pipelines required to aggregate and visualize this information in real-time.
7.  **UI/UX Implementation (Sprint 7):** Develop the frontend interfaces for sponsors, organizers, and scouts, ensuring a seamless and intuitive user experience across all workflows.
8.  **Security and Compliance Review (Sprint 8):** Conduct comprehensive security audits, penetration testing, and compliance reviews to ensure the system meets all regulatory requirements and platform standards.

## 11. Unresolved ADRs (Architecture Decision Records)

The following decisions remain unresolved and require further discussion and analysis before final implementation:

*   **ADR-SPO-01: Scout Request Bounties:** Should contact requests require a micro-escrow (bounty) to guarantee a response from high-profile creators? This could reduce spam and ensure that creators are compensated for their time reviewing offers, but it adds complexity to the workflow and may deter legitimate scouts.
*   **ADR-SPO-02: Rights Agreement Templates:** What is the exact structure and legal language of the standardized `RightsAgreement` templates? We need to define the default options (e.g., standard buyout, revenue share, non-exclusive license) and determine how much customization sponsors are allowed to make without triggering a manual legal review.
*   **ADR-SPO-03: Mixed Pool Distribution Logic:** In mixed prize pools (sponsor + participant funded), how are the funds distributed if the event is cancelled or fails to reach a minimum participant threshold? We need clear rules for refunding participants versus returning funds to the sponsor.

---
**References:**
[1] Owner Directive 0001: Artist Arena V1 Is Build-Complete
[2] ARTIST-ARENA-V1-Master-Specification.md
