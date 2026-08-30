# Artist Arena V1 Engineering Baseline

## 1. Introduction and Scope

This document establishes the contract-first engineering baseline for Artist Arena V1. It integrates the canonical product specifications [1] with the mandatory directives from Owner Directive 0001 [2]. Artist Arena is designed as the comprehensive competitive infrastructure layer for the global creator economy, encompassing native blockchain capabilities, a fully featured credit economy, multi-discipline support, and a robust architecture ready for production deployment.

All capabilities outlined herein are mandatory for the V1 build. While actual production activation of features such as real-money transactions, cash-out, and public blockchain networks may be governed by compliance, jurisdictional, or founder gates, the underlying architecture, implementation, integration, and testing must be complete in V1. The platform will support music, dance, writing, visual art, film, code, game building, and multimedia work from day one, although the recommended launch wedge focuses on music battles.

## 2. Architecture and Repository Standards

### 2.1 Canonical Identifier Conventions
Identifiers across the platform must be stable, sortable, and globally unique. The standard format is a prefixed ULID or KSUID to ensure chronological sortability and clear domain context.
- **Users/Profiles:** `usr_...`, `prf_...`
- **Battles/Tournaments:** `btl_...`, `trn_...`
- **Submissions/Media:** `sub_...`, `med_...`
- **Ledger/Financial:** `act_...` (account), `txn_...` (transaction), `evt_...` (event)

### 2.2 Time, Money, and Credit Types
Time must be recorded in UTC using ISO 8601 format with microsecond precision.

Financial values must never be represented as floating-point numbers or a single mutable balance field. The system employs a double-entry, append-only ledger using fixed-precision minor units (e.g., cents) [1].

The economic instruments include:
- **Arena Points:** Non-transferable, non-withdrawable points for onboarding and free competition.
- **Purchased Credits:** Fiat-purchased units, activated behind compliance gates.
- **Creator Earnings:** Proceeds from sales, subscriptions, and eligible prizes.
- **Contest Escrow:** Funds reserved during active competitions.
- **Bonus Credits:** Non-withdrawable promotional units.
- **Withdrawable Balance:** Provider-backed eligible funds.
- **Reserve / Hold:** Temporary risk reserves.
- **Platform Revenue:** Fees, including the configurable 1% conversion fee default [1] [2].

### 2.3 HTTP Envelopes, Errors, Pagination, and Concurrency
All REST APIs follow OpenAPI 3.1 standards.

**Error Envelope:**
Errors must be structured, providing actionable details without leaking internal logic [1].
```json
{
  "error": {
    "code": "BATTLE_NOT_ELIGIBLE",
    "message": "This account is not eligible for the selected battle.",
    "requestId": "req_123456789",
    "details": {}
  }
}
```

**Pagination:** Cursor-based pagination is mandatory for all list endpoints.
**Concurrency & Idempotency:** Endpoints mutating state must accept an `Idempotency-Key` header. Concurrent edits must use ETags or version checks [1].

### 2.4 Authentication and Policy Context
Authentication utilizes a Postgres-backed layer (e.g., Better Auth) supporting email/password, social OAuth, passkeys, and MFA [1].
Every sensitive action evaluates a comprehensive policy context, checking account status, age, verification, jurisdiction, feature flags, and conflict-of-interest declarations before proceeding [1] [2].

## 3. API Contracts and OpenAPI Groups

The API is organized into domain-specific groups [1]:
- **Auth:** Registration, login, MFA, session management.
- **Profiles:** User profiles, disciplines, portfolios.
- **Uploads and Media:** Multipart uploads, finalization, media retrieval.
- **Battles:** Creation, publishing, acceptance, submissions, timelines.
- **Judging and Voting:** Assignments, scoring, results, disputes.
- **Tournaments:** Brackets, entries, advancement.
- **Ratings and Rankings:** Glicko-2 ratings, seasons.
- **Social:** Follows, comments, notifications, feeds.
- **Marketplace:** Listings, orders, entitlements, commissions.
- **Wallet:** Balances, conversion quotes, payouts, limits. (Regulated actions return policy-gated responses until enabled).
- **Sponsors and Scouts:** Campaigns, reports, search, lists.
- **Admin and Trust:** Case management, ledger reconciliation, audit logs, feature flags.

## 4. Domain Events and Outbox Pattern

Artist Arena utilizes an event-driven architecture based on the outbox pattern. Business transactions must update canonical state and append an event to the outbox table within the same database transaction [1].

### 4.1 Event Envelope
```json
{
  "eventId": "evt_...",
  "eventType": "battle.settled.v1",
  "schemaVersion": "1.0",
  "aggregateType": "battle",
  "aggregateId": "btl_...",
  "actor": "usr_...",
  "occurredAt": "2026-08-30T12:00:00.000Z",
  "correlationId": "req_...",
  "causationId": "cmd_...",
  "payload": {},
  "privacyClassification": "restricted",
  "retentionClass": "financial"
}
```

### 4.2 Event Registry (Subset)
- `user.created.v1`
- `media.upload_completed.v1`
- `battle.published.v1`
- `battle.submissions_locked.v1`
- `battle.result_finalized.v1`
- `ledger.journal_posted.v1`
- `conversion.settled.v1`
- `escrow.held.v1` [1]

## 5. Webhooks, Archives, and Signatures
External communications and integrations rely on secure webhooks.
- **Signatures:** All outgoing webhooks must be signed (e.g., HMAC-SHA256) to verify origin.
- **Replay Protection:** Webhooks include timestamps and unique identifiers to prevent replay attacks [1].
- **Archives:** Immutable audit logs and financial records are archived to secure object storage (e.g., Cloudflare R2) with strict retention policies.

## 6. Chain Transaction and Finality Contracts
In compliance with Owner Directive 0001, V1 includes native blockchain architecture for provenance, escrow, and settlement [2].
- **State Model:** Versioned identities, licenses, escrow, and results.
- **Execution:** Deterministic native modules with limits and replay protection.
- **Wallet Integration:** Managed and self-custodial paths with purpose-separated keys.
- **Finality:** Escrow is released and settlements are attested on-chain only after the dispute window closes and the result is final [2].

## 7. Versioning, Compatibility, and Deprecation
- **APIs:** Versioned via URL path (e.g., `/v1/`).
- **Events:** Schema versions are embedded in the event envelope.
- **Deprecation:** Endpoints and events must be supported for a minimum of 6 months post-deprecation notice, utilizing `Sunset` and `Deprecation` HTTP headers.

## 8. Database Migration Rules
- Schema changes require reviewed SQL migrations (e.g., Drizzle).
- Migrations must be backwards compatible (e.g., add columns before removing old ones).
- No production schema changes are permitted without a reviewed migration [1].

## 9. Conformance Tests and Deterministic Seed Plan
V1 requires an end-to-end testing gauntlet, including property tests, vertical slice E2E tests, and rollback verifications [1].

### 9.1 Deterministic Seed Data
The system initializes with non-infringing, deterministic seed data to validate the entire lifecycle [1]:
- Personas: 2 beat creators, 1 rapper, 1 singer, 1 judge, 1 organizer, 1 sponsor, 1 scout, 1 moderator.
- Events: 1 free battle, 1 completed judged battle, 1 open challenge, 1 tournament.
- Submissions: 1 Pure Human, 1 Hybrid, 1 AI Open.
- Commerce: 1 marketplace listing, 1 commission request, Arena Points ledger entries, mock conversion quotes, and escrow settlements.

### 9.2 Property-Based Tests
To ensure the integrity of the system, strict property tests must be enforced [1]:
- **Ledger:** Debits must always equal credits. Reversals net the original amount. Idempotent replays do not duplicate value.
- **Escrow:** Funds released cannot exceed funds held. Double settlement is prohibited. Voided events return funds according to rules.
- **Ratings:** Voided battles do not impact ratings. Recalculation is deterministic.
- **Voting:** One eligible vote per ballot. Idempotent keys prevent duplicate votes.

### 9.3 E2E Vertical-Slice Test
A complete vertical-slice test must demonstrate the following flow [1]:
1. Creators register and select disciplines.
2. Creator creates a free ranked battle; another accepts.
3. Both upload audio and finalize submissions.
4. Submissions lock, and voting/judging opens.
5. Votes and scores are recorded, result is calculated.
6. Dispute window expires, result becomes final.
7. Ratings update, notifications are sent.
8. No cash ledger entries occur in this free test.
A secondary sandbox test must validate escrow and the 1% conversion fee accounting using mock funds.

## 10. Architecture Decision Records (ADR) Register
Unresolved decisions are preserved as ADRs to guide CodeSpring execution without blocking implementation [1]:
- **ADR-0001:** Monorepo and modular-monolith approach.
- **ADR-0002:** Cloudflare Workers web/API deployment.
- **ADR-0009:** Double-entry ledger.
- **ADR-0010:** Separate economic instruments.
- **ADR-0012:** AI division and disclosure model.
- **ADR-0016:** *Override Noted* - Original spec stated "No blockchain dependency in V1", but Owner Directive 0001 mandates blockchain implementation in V1. This conflict is resolved in favor of Directive 0001.
- **ADR-0018:** Feature flags and jurisdiction policy engine.

## 11. CodeSpring Contract Baseline
The initial CodeSpring handoff package must focus on establishing the core architecture without triggering compliance gates prematurely [1].

**Ticket ID:** CS-001
**Objective:** Implement the non-financial music battle vertical slice.
**User Story:** As a creator, I can create an account, upload a beat, enter a free battle using Arena Points, receive a judge score, and see my rating update.
**Domain Context:** Profiles, Media, Battles, Judging, Ratings.
**Acceptance Criteria:**
1. User registration and profile creation succeed.
2. Media upload completes with mock processing.
3. Battle state machine progresses from DRAFT to SETTLED.
4. Arena Points are accurately deducted and refunded/awarded.
5. Glicko-2 rating updates upon finalization.
6. Full audit events are generated.
**Tests:** E2E coverage of the vertical slice, property tests for the state machine, and ledger invariants.

## 12. Scoring Templates and Integrity
The scoring engine must be configurable by discipline and event.

**Recommended Initial Templates:**
- **Beat Production:** Musicality, originality, sound selection, arrangement, mix, response to brief [1].
- **Dance:** Technique, choreography, musicality, execution, originality, camera-rule compliance [1].
- **Code / Game Building:** Functionality, test performance, architecture, UX, performance, security [1].

**Voting Integrity:**
Voting must be strictly controlled to prevent manipulation:
- One eligible vote per account per ballot.
- Rate limits and bot challenges.
- Account-age and trust signals.
- Duplicate-device and network anomaly signals.
- No public exposure of private fraud signals [1].

## 13. AI Divisions, Disclosure, and Provenance
Competitions support clearly separated divisions: Pure Human, Hybrid, and AI Open [1] [2].

**Disclosure Labels:**
- `HUMAN_MADE`
- `AI_ASSISTED`
- `AI_HYBRID`
- `FULLY_GENERATIVE` [1]

**Process Evidence:**
Depending on event level, creators may need to submit DAW project screenshots, stems, raw vocal takes, screen recordings, prompt logs, or camera originals [1].

**Rights and Training Consent:**
Default policy: No AI training unless the creator opts in through specific, informed permission. Platform display rights are limited to operating and promoting the service [1].

## 14. Data Model and Core Entities
The system utilizes a relational data model managed via Postgres. Key entities include:

- **Identity:** `users`, `profiles`, `user_roles`, `organizations`, `teams`, `verification_records`.
- **Media:** `media_assets`, `media_versions`, `provenance_records`, `ai_disclosures`.
- **Competitions:** `arenas`, `battles`, `submissions`, `tournaments`, `result_attestations`, `disputes`.
- **Judging:** `scoring_templates`, `judges`, `judge_scores`, `votes`.
- **Ratings:** `ratings`, `rating_events`, `leaderboard_snapshots`.
- **Marketplace:** `listings`, `orders`, `entitlements`, `service_contracts`.
- **Ledger:** `ledger_accounts`, `ledger_journals`, `ledger_postings`, `escrow_holds`, `payouts`, `chargebacks`.
- **Audit:** `audit_events`, `security_events`, `outbox_events` [1].

This extensive data model ensures that all V1 capabilities—including native blockchain elements and complex financial transactions—are fully supported at the schema level, even if certain features remain inactive pending policy approval.

## 15. Security, Privacy, and Compliance Posture
Security and compliance are built into the foundation of Artist Arena V1 [1].

**Authentication & App Security:**
- Secure, HTTP-only cookies and CSRF protection.
- Passkeys, 2FA, and step-up authentication for sensitive actions.
- OWASP ASVS-informed controls, CSP, and secure headers.
- Webhook signature verification and rate limiting.

**Financial Security:**
- Immutable append-only ledger with no client-authoritative balances.
- Webhook replay defense and rigorous reconciliation processes.
- Dual control for manual adjustments and payout holds.

**Privacy & Compliance:**
- Data inventory and purpose classification.
- Deletion workflows, retention schedules, and legal holds.
- Regional controls and strict minor protections.
- Regulated features default to disabled (`REGULATED_FEATURES_DISABLED=true`), ensuring no hidden production bypasses exist.

## 16. Creator Profiles and Portfolios
Creator profiles are the central hub for discovery and professional representation on Artist Arena [1].

**Profile Fields:**
Profiles must include display name, unique handle, profile image/banner, bio, disciplines, roles, division participation, optional location, links, availability, portfolio, competitive record, current ratings, and verification badges.

**Privacy and Verification:**
Users have granular control over the visibility of their legal name, contact information, earnings, and private portfolio items. KYC data is strictly separated from public profiles. Verification badges must clearly indicate what was verified (e.g., email, phone, identity, age, professional credential) [1].

## 17. Discovery, Feeds, Live, and Community
Artist Arena's discovery engine focuses on meaningful connections and event completion [1].

**Discover Surface:**
The discovery feed highlights live battles, open challenges, tournaments, rising creators, and sponsor briefs. Users can filter by discipline and division (Pure Human, Hybrid, AI Open).

**Recommendation Principles:**
Recommendations prioritize new creators for controlled exploration exposure, avoiding the reinforcement of existing follower dominance. Sponsored placements are clearly labeled, and protected attributes are excluded from ranking algorithms [1].

**Social Capabilities:**
V1 includes follows, comments, threaded replies, bookmarks, shares, and activity feeds. Direct messaging is deferred until robust moderation, blocking, and reporting workflows are established.

**Live and Replay:**
V1 supports embedded external livestreams, live scoring updates, chat with moderation, and replay links. Native live streaming is planned as a later capability via a provider adapter [1].

## References
[1] ARTIST-ARENA-V1-Master-Specification.md
[2] 0001-v1-build-complete.md
