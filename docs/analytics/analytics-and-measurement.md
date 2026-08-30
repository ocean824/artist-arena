# Analytics and Measurement Specification

## 1. Domain Overview
This document specifies the Analytics and Measurement domain for Artist Arena V1. It defines the implementation requirements for the event registry, funnels, metrics, experiments, privacy controls, authoritative server events, dashboards, SLOs, and data quality. The specification conforms to the mandatory V1 build scope directed by Owner Directive 0001, meaning all capabilities—even those gated or labeled as future—are required in the V1 architecture and implementation. The analytics system is designed to provide deep insights into user behavior, platform health, and economic activity while strictly adhering to privacy, consent, and data security standards. It serves as the foundational layer for understanding how creators and audiences interact within the competitive infrastructure of the global creator economy.

## 2. Product Rules and North-Star Metric
The primary objective of the analytics system is to measure and optimize the core value of Artist Arena. This involves tracking user journeys, evaluating the success of competitions, and monitoring the economic health of the platform, all while maintaining strict privacy, consent, and data quality controls.

### 2.1 North-Star Metric
The guiding north-star metric for Artist Arena is the number of completed, verified creator competitions that generate a meaningful creator outcome. A meaningful outcome is defined as any event that significantly advances a creator's career or standing on the platform. This includes positive movement in their Glicko-2 rating, qualified discovery by new audiences, winning a prize pool, making a sale in the marketplace, generating a commission lead, being shortlisted by a sponsor, receiving contact from a talent scout, converting viewers into followers, or demonstrating repeat participation in competitive events.

### 2.2 Core Metrics
The analytics system is responsible for tracking a comprehensive set of core metrics across various stages of the user lifecycle and platform activity.

| Category | Metrics Tracked | Description |
|---|---|---|
| **Acquisition** | Visitor-to-signup conversion, creator onboarding completion rate, source/channel attribution, referral conversion rate. | Measures the effectiveness of marketing efforts and the initial user onboarding experience. |
| **Activation** | Time to first upload, time to first battle, first challenge acceptance, first vote cast, first follow, first purchase. | Evaluates how quickly new users engage with core platform features. |
| **Competition** | Battle fill rate, submission completion rate, no-show rate, event completion time, judge completion rate, dispute rate, void rate, ranked participation volume, repeat battle rate. | Assesses the health, fairness, and engagement levels of the competitive ecosystem. |
| **Discovery** | Unique creators discovered per user, rising-creator exposure, follow conversion rate, qualified listen/watch completion rate, search success rate. | Tracks how effectively audiences find and engage with new talent. |
| **Commerce** | Gross marketplace volume, total creator earnings, total sponsor spend, conversion volume, platform take rate, refund rate, payout failure rate, repeat buyer frequency. | Monitors the economic activity and financial health of the platform. |
| **Trust** | Fraud flags generated, invalid votes detected, chargeback rate, upheld moderation reports, appeal overturn rate, moderation response time, rights-claim response time. | Measures the integrity of the platform and the efficiency of trust and safety operations. |
| **Retention** | D1, D7, and D30 retention rates, creator weekly active users (WAU), audience weekly active users (WAU), event cohort retention, discipline-specific retention, paid user conversion rate. | Evaluates long-term user engagement and platform stickiness. |

## 3. Funnels
The analytics system must support the definition and tracking of several critical funnels to understand user progression and identify drop-off points.

| Funnel Type | Stages | Purpose |
|---|---|---|
| **Product Funnel** | Visitor -> Signup -> Onboarding -> First Action (Upload/Vote/Follow). | Tracks the general user acquisition and activation journey. |
| **Competition Funnel** | Battle Creation -> Acceptance -> Submission -> Judging -> Final Result. | Monitors the lifecycle of a competitive event from inception to conclusion. |
| **Creator Funnel** | Profile Creation -> Discipline Selection -> First Upload -> First Battle -> First Meaningful Outcome. | Evaluates the success of creators in establishing themselves on the platform. |
| **Marketplace Funnel** | Listing View -> Add to Cart/Initiate Purchase -> Checkout -> Payment Success -> Entitlement Granted. | Analyzes the e-commerce purchasing process. |
| **Sponsor Funnel** | Campaign Creation -> Brief Published -> Challenge Accepted -> Result Settled -> Sponsor Report Generated. | Tracks the effectiveness of sponsored campaigns and challenges. |
| **Economic Funnel** | Deposit/Earn -> Balance Accrual -> Wager/Purchase -> Escrow -> Settlement -> Cash-out Request -> Cash-out Complete. | Follows the flow of value through the platform's economic systems. |

## 4. Event Registry
To ensure consistent tracking across all services and platforms, the system must maintain a strictly versioned event registry. This registry serves as the single source of truth for all analytics events generated by the application.

### 4.1 Required Event Envelope Fields
Every event emitted by the system, regardless of its origin or purpose, must conform to a standard envelope structure. This envelope provides necessary context for routing, processing, and analyzing the event data. The required fields include `event_id` (a unique identifier for the event), `event_type` (the specific action that occurred), `schema_version` (the version of the event schema being used), `aggregate_type` (the domain entity involved, e.g., 'battle', 'user'), `aggregate_id` (the unique identifier of the domain entity), `actor` (the user or system that initiated the event), `occurred_time` (the exact timestamp of the event), `correlation_id` (used to trace related events across services), `causation_id` (the ID of the event that caused this event), `payload` (the specific data associated with the event), `privacy_classification` (indicates the sensitivity of the data for compliance purposes), and `retention_class` (determines how long the event data should be stored).

### 4.2 Initial Event Registry
The following core domain events are required for the V1 implementation. This list is not exhaustive but represents the minimum necessary events for tracking platform activity.

| Domain | Event Types |
|---|---|
| **User & Profile** | `user.created.v1`, `user.email_verified.v1`, `profile.updated.v1`, `creator.discipline_added.v1` |
| **Media** | `media.upload_started.v1`, `media.upload_completed.v1`, `media.scan_failed.v1` |
| **Competition** | `submission.created.v1`, `submission.finalized.v1`, `battle.created.v1`, `battle.published.v1`, `battle.accepted.v1`, `battle.funded.v1`, `battle.submission_window_opened.v1`, `battle.submissions_locked.v1`, `battle.voting_opened.v1`, `battle.judging_opened.v1`, `battle.provisional_result_created.v1`, `battle.disputed.v1`, `battle.result_finalized.v1`, `battle.settled.v1`, `tournament.created.v1`, `tournament.entry_added.v1`, `tournament.bracket_generated.v1` |
| **Judging & Rating** | `vote.cast.v1`, `judge_score.submitted.v1`, `rating.updated.v1` |
| **Commerce & Ledger** | `listing.published.v1`, `order.created.v1`, `order.paid.v1`, `entitlement.granted.v1`, `service.delivered.v1`, `ledger.journal_posted.v1`, `conversion.quoted.v1`, `conversion.settled.v1`, `escrow.held.v1`, `escrow.released.v1`, `payout.requested.v1`, `payout.completed.v1`, `chargeback.opened.v1` |
| **Trust & Social** | `report.created.v1`, `moderation.action_taken.v1`, `rights_claim.created.v1`, `notification.requested.v1` |

## 5. Experiment Rules
The system must robustly support controlled experiments, commonly known as A/B testing, to facilitate data-driven product development. User assignments to specific experiment variants must be persistently recorded in the `experiment_assignments` table to ensure consistent experiences across sessions. These assignments must be deterministic, calculated based on stable identifiers such as user ID or device ID, to prevent users from fluctuating between variants. The analytics infrastructure must be capable of segmenting all core metrics by experiment variant, allowing for precise impact analysis. Furthermore, the experiment framework must support gradual rollouts to mitigate risk, as well as immediate rollback capabilities in the event of negative outcomes or critical failures.

## 6. Privacy and Consent
The analytics system is designed with privacy as a foundational principle, adhering to strict controls to protect user data and comply with global regulations.

The platform explicitly prohibits secret user profiling and the sale of private creator data to third parties. All client-side analytics collection must be governed by robust consent hooks, allowing users to explicitly opt-in or opt-out of tracking. Before any data is transmitted to external analytics systems or long-term storage, sensitive financial information and personally identifiable information (PII) must be rigorously redacted. Data retention is strictly managed; all stored data must follow defined retention schedules dictated by the `retention_class` specified in the event envelope, ensuring data is not held longer than necessary or legally required. Crucially, product analytics data is kept entirely separate from security and fraud telemetry, preventing cross-contamination and ensuring that essential security monitoring is not compromised by user opt-outs.

## 7. Authoritative Server Events
To guarantee the accuracy and integrity of critical platform data, the system relies exclusively on authoritative server events for specific domains. Client-side events are inherently unreliable and easily manipulated, making them unsuitable for tracking financial transactions or competition outcomes.

All financial events, including ledger entries, currency conversions, escrow holds and releases, and payout requests, must be generated authoritatively by the backend server. Similarly, the completion of competitions, the finalization of battle results, and all subsequent rating updates must be exclusively server-driven. This approach ensures that the economic and competitive records of the platform remain incorruptible and auditable.

## 8. Dashboards
The analytics data must be surfaced through role-specific dashboards, providing actionable insights tailored to the needs of different user personas.

| Persona | Dashboard Focus |
|---|---|
| **Admin/Operator** | System health, real-time fraud flags, financial reconciliation status, platform-wide core metrics, and operational alerts. |
| **Creator** | Profile views, detailed battle history and performance, earnings breakdowns, audience growth trends, and engagement metrics. |
| **Sponsor** | Campaign performance, return on investment (ROI), engagement metrics, challenge completion rates, and audience demographics. |
| **Organizer** | Tournament participation levels, voting engagement, dispute rates, and overall event success metrics. |

## 9. SLOs and Performance
The analytics infrastructure must operate within strict Service Level Objectives (SLOs) to ensure it does not degrade the core user experience.

The application architecture must support a degraded mode, ensuring that core functionalities, such as battle participation and media playback, continue to operate seamlessly even if the analytics or recommendation systems experience outages. While analytics event delivery should aim for high reliability, it must never block critical user flows; for example, a payment processing action must not fail simply because the analytics endpoint is temporarily unreachable. Performance-wise, the event tracking mechanisms must be highly optimized, ensuring they do not significantly impact server response times. The target p95 server response time remains under 500 milliseconds for public pages and under 750 milliseconds for authenticated APIs, inclusive of any synchronous analytics processing.

## 10. Cost Controls and Data Quality
Managing the cost of data storage and processing is critical, as is ensuring the high quality of the data collected. The system strictly avoids collecting raw data without a clearly defined use case and an associated retention policy, preventing uncontrolled storage cost inflation.

Data quality is enforced at the point of ingestion. All incoming event schemas must be rigorously validated against the established registry, utilizing tools such as Zod validation. Events that fail validation must be rejected or routed to a dedicated dead-letter queue for investigation, preventing malformed data from corrupting the analytics warehouse. Furthermore, event schema compatibility and delivery mechanisms must be continuously tested as an integral part of the Continuous Integration (CI) pipeline.

## 11. Actors and Permissions
Access to analytics data is strictly governed by Role-Based Access Control (RBAC), ensuring that users only see information relevant and permissible to their role.

Administrators and Super Admins possess broad access, able to view all aggregated analytics and comprehensive system health dashboards. Trust Analysts and Moderators are granted access specifically to fraud and trust metrics necessary for their investigative duties. Finance Operators have visibility into financial and commerce metrics for reconciliation and reporting purposes. Creators, Sponsors, and Organizers are restricted to viewing only the analytics directly related to their own entities, such as their specific profiles, campaigns, or managed tournaments, ensuring data privacy across the platform ecosystem.

## 12. State Machines and Workflows
The reliable delivery of domain events is managed through a robust outbox workflow. When a domain state change occurs, the corresponding domain event is written to the `outbox_events` table within the exact same database transaction. This guarantees that the event is recorded if and only if the state change is successful. A dedicated background worker continuously polls the outbox table and is responsible for delivering these events to the `analytics_events` table and any external systems, such as PostHog. The status of these deliveries is meticulously recorded in the `event_deliveries` table, allowing for retries and auditing of the event pipeline.

## 13. API/Event Implications
The platform's API must provide dedicated endpoints to support the querying of aggregated analytics data, which powers the creator and sponsor dashboards. These endpoints must be heavily optimized for read performance, strictly rate-limited to prevent abuse, and rigorously permission-checked to ensure data is only exposed to authorized users.

## 14. Dependencies
The analytics and measurement domain relies on several key external dependencies. PostHog, or an equivalent product analytics platform, is utilized for deep product analytics and user journey mapping. OpenTelemetry is employed for distributed tracing, providing visibility into requests as they traverse the microservices architecture. Sentry, or a comparable service, is integrated for real-time error tracking and exception monitoring. Finally, Cloudflare is leveraged for edge observability and the export of access logs.

## 15. Security/Privacy/Rights/Economic Impact
The design of the analytics system carries significant implications across security, privacy, and platform economics.

From a security perspective, it is an absolute requirement that no raw secrets, identity documents, or full payment payloads are ever written to logs or transmitted to analytics systems. Privacy is maintained through strict adherence to user consent preferences and opt-out mechanisms. Economically, the reliance on authoritative server events is crucial; it ensures the accurate tracking and auditing of the 1% conversion fee, creator splits, and overall platform revenue, preventing financial discrepancies caused by client-side manipulation.

## 16. Abuse and Failure Modes
The system is designed to anticipate and mitigate potential abuse and failure modes. In the event of an analytics outage, the system must degrade gracefully, ensuring that core platform functionality remains uninterrupted. To combat event spam and malicious data injection, strict rate limiting and payload size limits must be enforced on all analytics ingestion endpoints, protecting the integrity of the data warehouse and the stability of the ingestion pipeline.

## 17. Acceptance Criteria and Definition of Done
The Analytics and Measurement domain is considered complete when the following criteria are met:
- A comprehensive event registry is defined, versioned, and documented.
- The transactional outbox pattern is fully implemented and tested for reliable event delivery.
- Authoritative server events are implemented and verified for all financial transactions and competition state changes.
- Privacy controls, including data redaction and client-side consent hooks, are active and functioning correctly.
- The Continuous Integration (CI) pipeline includes automated tests for event schema compatibility.
- Role-specific dashboards for core metrics can be successfully populated from the primary analytics data store.

## 18. Dependency-Ordered Work Packages
The implementation of this domain should proceed in the following ordered phases:
1. Define the initial event schemas and establish the versioned event registry.
2. Implement the database outbox pattern and the background event delivery worker.
3. Integrate OpenTelemetry and establish structured logging practices across all services.
4. Implement authoritative server events for all core financial and competition flows.
5. Integrate PostHog (or the chosen equivalent) and implement client-side consent hooks.
6. Build and secure the API endpoints required for creator and sponsor analytics dashboards.

## 19. Unresolved ADRs
The following Architectural Decision Records (ADRs) remain unresolved and require finalization:
- The final selection of the specific product analytics provider (e.g., confirming PostHog versus evaluating alternatives like Mixpanel).
- The definition of specific, legally compliant retention periods for different classes of analytics data.
