# Master Product Specification: Artist Arena V1

## 1. Product Vision and Core Promise

Artist Arena is the competitive infrastructure layer for the global creator economy. It is where creators compete, prove skill, build a public record, earn, get discovered, find collaborators, win opportunities, and turn audience attention into durable economic value. The platform combines elements from creator subscriptions, livestreaming, community platforms, short-form discovery, tournament infrastructure, freelance marketplaces, portfolio networks, and talent scouting, centering them around a verified competitive record.

For creators, the core promise is that their work should be able to compete, accumulate proof, attract opportunity, and earn without requiring preexisting industry access. For audiences, it offers talent discovery through meaningful creative competition, rather than opaque algorithms and follower counts. For sponsors and scouts, Artist Arena provides a structured environment to find creators based on discipline, consistency, results, rankings, originality, reliability, audience response, and verified work.

## 2. Product Pillars

The Artist Arena platform is built upon seven foundational pillars:
1. **Compete:** Engage in battles, challenges, tournaments, seasons, and ladders.
2. **Prove:** Establish transparent records, ratings, judge feedback, provenance, and process evidence.
3. **Discover:** Navigate feeds, search, categories, rising talent, live events, and curator channels.
4. **Earn:** Accumulate prizes, marketplace sales, subscriptions, commissions, services, licensing, and sponsorship.
5. **Connect:** Interact through follows, comments, teams, collaborators, judges, scouts, sponsors, and organizers.
6. **Protect:** Enforce rights controls, consent metadata, secure submissions, fraud controls, moderation, disputes, and appeals.
7. **Include the Future:** Support Pure Human, Hybrid, and AI Open competition divisions with clear separation and transparency.

## 3. Personas and Roles

Artist Arena serves a diverse ecosystem of users, each with distinct goals and capabilities.

| Persona | Primary Activities |
|---|---|
| **Competitor Creator** | Creates a profile, uploads work, enters battles, accepts challenges, receives ratings and feedback, earns prizes, sells work, and builds a competitive portfolio. |
| **Audience Member / Fan** | Follows creators, watches or listens, votes where eligible, comments, shares, buys access or products, subscribes, and attends digital events. |
| **Buyer / Client** | Purchases digital products, licenses work, orders services, commissions creators, or pays for gated access. |
| **Judge / Curator** | Scores submissions against disclosed criteria, leaves structured feedback, declares conflicts, and builds a judge reputation. |
| **Organizer** | Creates battles, tournaments, seasons, rule sets, eligibility rules, judge panels, schedules, and prize structures. |
| **Sponsor / Brand** | Creates branded briefs and sponsored competitions, funds prizes, supplies official rules, selects judges, receives campaign analytics, and discovers creators. |
| **Scout / Recruiter / A&R** | Searches talent by permitted attributes, creates private shortlists, and sends contact requests. |
| **Team / Collective** | Operates a shared identity, roster, portfolio, tournament entries, permissions, and revenue splits. |
| **Moderator / Trust Analyst** | Reviews reports, rights claims, fraud signals, vote anomalies, identity issues, appeals, and disputes. |
| **Finance / Compliance Operator** | Reviews payout holds, verification, chargebacks, reconciliation, restricted jurisdictions, sanctions results, tax records, and ledger exceptions. |
| **Administrator** | Manages platform configuration, feature flags, discipline templates, policies, staff permissions, and audit review. |

## 4. Role-Based and Attribute-Based Access Control (RBAC/ABAC)

Access control combines explicit roles with dynamic policy evaluation. Roles include user, creator, verified_creator, judge, organizer, sponsor_member, scout, team_member, team_admin, moderator, trust_analyst, finance_operator, compliance_operator, support_agent, admin, and super_admin.

Sensitive actions must dynamically evaluate account status, age status, verification status, jurisdiction, contest eligibility, organization membership, resource ownership, conflict-of-interest declarations, moderation restrictions, wallet restrictions, feature flags, and policy profiles. No administrator should be able to alter the financial ledger silently.

## 5. Information Architecture and Client Strategy

The V1 product is delivered as a responsive web application and installable Progressive Web App (PWA). The architecture uses shared contracts and design tokens to ensure native iOS and Android clients can be added without backend rewrites. Native mobile applications and native livestreaming are mandatory V1 engineering scope, though they may be sequenced after the web/PWA path.

The primary desktop navigation includes Discover, Battles, Tournaments, Rankings, Live, Marketplace, Search, Notifications, Wallet, and Profile. A persistent primary action allows eligible users to create a battle, issue a challenge, enter an open event, upload a work, or create a listing. The UI direction emphasizes a premium, cinematic, creator-forward interface with competitive energy, avoiding generic SaaS gradients or casino visual languages.

## 6. Complete V1 Scope and Reinterpreted Non-Goals

Pursuant to Owner Directive 0001, Artist Arena V1 is the complete competitive infrastructure layer. Every capability described in the product canon is mandatory V1 engineering scope. This includes native blockchain, credits, cash-in and cash-out, paid battle entry, one-to-one credit wagers, sponsor-funded and participant-funded prize pools, escrow, settlement, creator payments, subscriptions, commissions, marketplace commerce, licensing, revenue splits, tax and compliance records, fraud controls, disputes, chargebacks, and multi-discipline expansion.

The program strictly separates whether a capability is built from where and when it is activated. Capabilities previously labeled as "later," "sandbox-only," or "non-goal" are mandatory for V1 architecture, implementation, integration, and test scope. Gates control activation, operator/jurisdiction exposure, provider access, and assurance, but never construction. For example, real-money features must be fully built, tested, and verifiable in sandbox environments, even if they remain disabled by policy in production pending legal and provider approval.

## 7. Domain Boundaries and Entities

The system is architected as a modular monolith with event-driven boundaries.

### 7.1 Identity and Organizations
Manages users, profiles, roles, teams, organizations, verification records, and consents.

### 7.2 Creator Taxonomy and Portfolios
Handles disciplines, skills, portfolio items, rights profiles, availability, and badges.

### 7.3 Media and Provenance
Manages assets, uploads, checksums, provenance records, AI disclosures, evidence bundles, and rights assertions.

### 7.4 Competitions
Coordinates arenas, rule sets, battles, submissions, challenges, tournaments, seasons, result attestations, and disputes.

### 7.5 Judging and Voting
Handles scoring templates, judges, assignments, scores, ballots, votes, invalidations, and tie-breaks.

### 7.6 Ratings and Rankings
Manages rating pools, rating events, leaderboards, competitive records, and reputation snapshots.

### 7.7 Social and Discovery
Handles follows, comments, feeds, recommendations, search, notifications, live sessions, blocks, and mutes.

### 7.8 Marketplace
Coordinates listings, prices, orders, entitlements, licenses, subscriptions, commissions, deliverables, and royalty splits.

### 7.9 Sponsors and Scouting
Manages sponsor campaigns, briefs, prizes, scout profiles, lists, opportunities, and contact requests.

### 7.10 Ledger and Payments
Handles accounts, journals, postings, balances, money instruments, fee policies, conversions, escrow, transactions, payouts, chargebacks, reconciliation, and tax profiles.

### 7.11 Trust, Support, and Audit
Coordinates reports, moderation cases, rights claims, support tickets, fraud signals, policy profiles, feature flags, and audit events.

## 8. State Machines and User Workflows

### 8.1 Battle Lifecycle
The battle lifecycle follows a validated state machine. Clients cannot assign states directly.
`DRAFT → PUBLISHED → MATCHING → ACCEPTED → FUNDING_PENDING → FUNDED → SUBMISSION_OPEN → SUBMISSIONS_LOCKED → REVIEW_PENDING → VOTING_OPEN / JUDGING_OPEN → SCORING → PROVISIONAL_RESULT → DISPUTE_WINDOW → FINAL → SETTLEMENT_PENDING → SETTLED → ARCHIVED`

Exceptional states include `CANCELLED`, `EXPIRED`, `VOIDED`, `DISPUTED`, `UNDER_REVIEW`, `REFUND_PENDING`, `REFUNDED`, and `PAYOUT_HELD`. Every transition requires actor, timestamp, state changes, reason code, policy evaluation, audit event, and resulting jobs.

### 8.2 Commission and Service Lifecycle
`INQUIRY → QUOTED → ACCEPTED → FUNDED → IN_PROGRESS → DELIVERED → REVISION → ACCEPTED_BY_BUYER → SETTLED`

### 8.3 Conversion State Machine
`QUOTED → USER_CONFIRMED → POLICY_APPROVED → PROVIDER_PENDING → SETTLED`

## 9. API and Event Implications

APIs follow OpenAPI 3.1 standards with generated types, Zod validation, structured error envelopes, request/trace IDs, cursor pagination, and rate limiting. Idempotency keys are required for mutations with financial or state consequences.

The system uses an event/outbox architecture. Business transactions update canonical state and append an outbox event in the same database transaction. These events are published asynchronously and consumed idempotently.

## 10. Financial Ledger and Economic Impact

Artist Arena uses a double-entry, append-only ledger for all financial transactions. The ledger is canonical, and money is never represented by a single mutable balance field. The system supports multiple economic instruments, including Arena Points, Purchased Credits, Creator Earnings, Contest Escrow, Bonus Credits, Withdrawable Balance, Reserve Holds, and Platform Revenue.

The conversion fee is a locked product requirement, defaulting to 1%. It is configuration-driven and accounted for separately from processor, verification, currency, tax, network, and chargeback costs. All cash-convertible or paid competition features require comprehensive compliance gates, including jurisdiction checks, identity verification, and payment-provider approval, though they must be fully implemented in V1.

## 11. Security, Privacy, and Rights

Every uploaded asset includes creator-controlled metadata for public display, download, remix permission, commercial licensing, AI training permission, and voice/likeness use. The default is no AI training unless explicitly opted in.

Moderation domains are separate but coordinated, covering content, community, competition integrity, marketplace, financial, identity, IP, sponsorship, and account safety. Rights claims follow a structured intake, review, and appeal process. All privileged administrative actions are logged with comprehensive audit metadata.

## 12. Blockchain Anchoring

Artist Arena V1 includes a native blockchain or sovereign application-chain implementation path. The chain serves creator provenance, competition evidence, programmable rights, digital assets, creator splits, prize escrow, settlement attestations, and economic auditability. Large media files and sensitive identity data are not stored on-chain. The blockchain integration provides a verifiable, immutable record of competitive outcomes and economic settlements.

## 13. Observability, Analytics, and Performance

The platform uses OpenTelemetry, structured JSON logs, trace IDs, and Sentry for observability. Analytics track acquisition, activation, competition metrics, discovery, commerce, trust, and retention. The north-star metric is "completed, verified creator competitions that generate a meaningful creator outcome." Analytics constraints prohibit secret user profiling, selling private creator data, and collecting raw data without a use policy.

## 14. Acceptance Criteria and Definition of Done

Artist Arena V1 is build-complete only when the full product loop works across identity, creator profiles, media, battles, challenges, tournaments, rankings, judging, audience participation, discovery, community, sponsorship, scouting, marketplace, creator commerce, native blockchain, credits, paid entry, one-to-one wagers, prize escrow, settlement, conversion, cash-out, disputes, moderation, rights, compliance, analytics, support, and operations.

The V1 codebase must contain the production-grade interfaces, state machines, schemas, ledgers, provider adapters, policy engine, audit system, tests, monitoring, operations, and user experiences needed for these capabilities.

## 15. Dependency-Ordered Work Packages

1. **Foundation:** Monorepo setup, core database schemas (identity, profiles, media), authentication, and basic RBAC.
2. **Competition Primitives:** Arenas, rule sets, battle state machine, submissions, and evidence handling.
3. **Judging and Voting:** Scoring templates, judge assignments, voting integrity controls, and result attestations.
4. **Economic Ledger:** Double-entry ledger, economic instruments, escrow, and mock payment providers.
5. **Marketplace and Commerce:** Listings, orders, entitlements, commissions, and revenue splits.
6. **Blockchain Integration:** Node setup, state model, provenance anchoring, and settlement attestations.
7. **Social and Discovery:** Feeds, search, notifications, and creator portfolios.
8. **Trust and Moderation:** Reporting, rights claims, dispute resolution, and audit logging.
9. **Compliance Gates:** Jurisdiction policies, verification workflows, and feature flags.
10. **Analytics and Observability:** Telemetry, event tracking, and finance dashboards.

## 16. Unresolved ADRs and Open Decisions

- **Database ID Strategy:** Selection between UUIDv7 or another sortable, collision-resistant ID format.
- **Authentication Provider:** Evaluation of self-hosted Better Auth versus other Postgres-backed open auth layers.
- **Blockchain Consensus and Framework:** Selection of the specific consensus mechanism and framework for the native application chain.
- **Search Infrastructure:** Timeline for migrating from Postgres full-text search to a dedicated service like Typesense or OpenSearch.
- **Fee Policy Configuration:** Finalizing the initial versioned fee-policy table beyond the 1% conversion fee default.
