# Artist Arena V1 Creator Identity, Community, Discovery, and Scouting Specification

**Authority:** Derived from the preserved master specification and governed by Owner Directive 0001. Creator identity, portfolios, discovery, community, teams, scouting, native mobile, and live surfaces are all mandatory V1 construction; activation and rollout may be staged without deferring architecture or implementation.

## 1. Purpose

This domain turns an account into a durable creator identity and makes creative achievement discoverable through work, discipline, competitive evidence, collaboration, and reputation. It owns public profiles, handles, disciplines and skills, portfolios, creator availability, links, badges, teams and collectives, follows, comments, reactions, bookmarks, shares, feeds, search, notifications, presence, live-session discovery, blocks, mutes, scouting visibility, and opportunity contact.

The domain must not reduce discovery to follower count or paid reach. Competition outcomes, consistency, verified work, division, discipline, judge feedback, provenance, reliability, and audience response can inform discovery, but ranking logic must remain explainable and cannot allow paid promotion to buy skill standing.

## 2. Identity boundaries

Public creator identity is separate from authentication, compliance identity, wallet custody, and private contact information.

| Boundary | Owned data | Data it may reference but not expose |
|---|---|---|
| Authentication | Credentials, sessions, passkeys, email verification, 2FA, recovery | Public handle and profile ID |
| Public profile | Handle, display identity, bio, disciplines, skills, portfolio, public record, badges, availability, approved links | Verification state as a coarse badge; never raw documents |
| Compliance identity | Legal name, date of birth, address, verification/provider results, tax and sanctions status | Public profile ID and policy-safe status only |
| Wallet | Addresses, custody mode, restrictions, trusted signing, activity | Public identity link chosen by policy/user |
| Scouting | Public/consented creator fields, private lists, contact requests, opportunities | Contact data only after consent and authorization |
| Moderation/trust | Reports, restrictions, blocks, cases, actions, evidence | Public restriction effects without leaking internal fraud logic |

Stable IDs prevent a handle change from breaking competitive records, rights, ledger references, or blockchain provenance. Handle history and reservation prevent impersonation and unsafe reuse.

## 3. Actors and permissions

Creators manage their profiles, disciplines, portfolios, availability, links, notification preferences, privacy, blocks, team memberships, scouting visibility, and contact consent. Fans follow, bookmark, comment, react, share, vote where eligible, and attend live events. Team admins manage a collective identity, roster, roles, shared portfolio, permissions, competition entry, and revenue splits. Scouts search permitted attributes, create private lists, invite creators to opportunities, and send consent-based contact requests. Sponsors and organizers can discover creators only through allowed fields. Moderators enforce safety and privacy. Administrators configure taxonomy and policy but cannot silently alter competitive or financial history.

RBAC is combined with resource ownership, account state, age, region, team role, visibility, block/mute relationships, contact consent, moderation restrictions, opportunity policy, and purpose limitation.

## 4. Canonical entities

| Entity | Required behavior |
|---|---|
| `Profile` | Stable user-owned public identity with versioned public fields and privacy settings |
| `UserHandle` | Unique normalized handle, reservation/history, impersonation and abuse controls |
| `Discipline` / `DisciplineFormat` | Platform taxonomy and supported submission/competition formats |
| `CreatorDiscipline` / `CreatorSkill` | Declared or verified creative focus and proficiency evidence |
| `PortfolioItem` / `PortfolioAsset` | Public or controlled work showcase with media, provenance, rights, division, and access policy |
| `WorkRightsProfile` | Ownership, license, collaborators, consent, display/promotion, training, and dispute status |
| `CreatorAvailability` | Commission, collaboration, employment, event, and contact preferences |
| `CreatorLink` | Approved external presence with validation and safety policy |
| `Badge` / `UserBadge` | Versioned achievement or verification indicator with issuer and evidence |
| `Team` / `TeamMember` | Collective identity, roster, roles, permissions, portfolio, competition and payout references |
| `Follow`, `Bookmark`, `Share` | User-intent social relationships with privacy and abuse controls |
| `Comment`, `Reaction` | Threaded community interaction with editing history, moderation, blocks, and reports |
| `Feed`, `FeedItem`, `RecommendationImpression` | Explainable delivery, source, ranking version, reason, and measurement |
| `SearchDocument` | Privacy-safe indexed projection of profile, work, event, and marketplace facts |
| `Notification` | Versioned user-facing event with channel, preference, delivery, read, and retry status |
| `LiveSession`, `EventPresence`, `ChatMessage` | Live discovery and participation linked to event policy and moderation |
| `ScoutProfile`, `ScoutList`, `Opportunity`, `ContactRequest` | Authorized talent search, private shortlists, opportunity terms, and consented contact |

Immutable competition, rating, ledger, chain, rights, moderation, and audit records are referenced rather than rewritten by profile changes.

## 5. Profile lifecycle

```text
ACCOUNT_CREATED
→ PROFILE_DRAFT
→ HANDLE_RESERVED
→ PROFILE_ACTIVE
→ PROFILE_LIMITED | PROFILE_SUSPENDED | PROFILE_DEACTIVATED
PROFILE_ACTIVE / PROFILE_LIMITED
→ PROFILE_UPDATED
PROFILE_DEACTIVATED
→ RESTORED where retention and policy permit
```

Profile activation requires an eligible account, reserved handle, minimum display fields, privacy defaults, and age-appropriate policy. Verification is a separate record and badge, not a mutable client-controlled boolean. Deactivation hides public surfaces while preserving records that must remain for safety, disputes, finance, legal holds, or audit. Deletion follows the data-retention and legal-obligation matrix rather than cascading into immutable history.

## 6. Portfolio and work discovery

A portfolio item references creator, discipline, title, description, division/disclosure, media versions, rights profile, provenance record, competition entries/results, marketplace listing where relevant, visibility, and moderation state. Original media remains in protected storage; public previews and derivatives are separately controlled. Blockchain anchoring stores content hashes, provenance and license references, not large media or private evidence.

Creators decide whether a work is public, unlisted, private, available to scouts, licensable, for sale, commission-related, or competition-only. The system must prevent a private submission from becoming discoverable through search, feeds, analytics, object-storage URLs, cache, or blockchain metadata.

## 7. Search and discovery

Search supports discipline, format, division, skill, rating/record, verified work, availability, team, language, location only when voluntarily shared and legally permitted, event participation, marketplace category, and freshness. Postgres full-text search and trigram matching are the first implementation path; an external search engine remains behind an adapter and is still a V1 workstream under the owner directive.

Ranking combines explicit query relevance, freshness, competitive evidence, portfolio quality signals, relationship/context, safety, and controlled exploration. It records algorithm version and impression reason. The platform must measure exposure concentration and avoid making follower count or historical popularity an irreversible advantage.

Paid promotion may label and place sponsored content, but it cannot change skill ratings, win/loss records, judge outcomes, or organic rank without transparent policy. Users can distinguish editorial, algorithmic, followed, trending, sponsored, live, and competition-derived recommendations.

## 8. Feed and community behavior

Feed items can represent work, battle/tournament activity, final results, live sessions, portfolio updates, marketplace items, sponsorship challenges, creator announcements, and editorial collections. Every item has source, eligibility, visibility, moderation, ranking reason, and expiration where appropriate.

Comments support replies, editing history, deletion policy, reporting, blocking, moderation, rate limits, and notification controls. A blocked relationship prevents direct contact and hides interaction according to policy without erasing necessary evidence. Muting is a user-experience preference and does not notify the muted party. Shares and bookmarks respect the source object’s access policy; a share cannot make private media public.

## 9. Teams and collectives

Teams own a public identity, roster, portfolio, competition entries, organization links, roles, permissions, and optional revenue-split references. Membership states include invited, active, suspended, removed, and departed. Roles distinguish owner/admin, roster manager, competitor, creator, finance viewer/operator, and public editor. Sensitive actions require step-up authentication and, where configured, multi-party approval.

Team content and competition entries identify contributing humans/AI tools, rights, consent, and split recipients. Removing a member does not rewrite historical authorship, competition participation, provenance, or earned payables. Direct team payouts are implemented in V1 behind policy and provider controls even if a launch profile routes early payouts through individually verified recipients.

## 10. Scouting and opportunities

Scouts create role-specific profiles and organizations, accept platform conduct and data-use terms, search public/consented attributes, maintain private lists, create opportunities, invite creators, and send contact requests. Private lists are never visible to creators or other scouts unless shared explicitly within an authorized organization.

An opportunity records organization, role or brief, discipline, compensation range or structure where supplied, rights requested, location/remote requirements, dates, eligibility, contact method, status, and moderation state. Contact requests do not reveal private email or phone until the creator consents. Bulk outreach, scraping, discrimination, harassment, and use outside the stated purpose are restricted and audited.

Scouting filters involving sensitive or location attributes require legal and policy review and clear creator control. The platform logs searches and exports at an appropriate risk tier without exposing hidden security signals to ordinary scouts.

## 11. Live and native-client surfaces

Live discovery includes upcoming, active, replay, followed-creator, tournament, sponsor, and discipline channels. V1 builds native livestreaming and provider-embed paths behind a common session contract. A live session has host/event, stream provider/runtime, access, recording/replay, moderation, chat, captions, rights, age, geographic, sponsorship, and retention policy.

The responsive web app and PWA establish the shared contract. Native iOS and Android clients are mandatory V1 construction under the owner directive and consume the same API, event, design-token, media, notification, policy, and trusted economic-confirmation contracts. Native apps may roll out to controlled cohorts after store, security, and performance qualification; they are not a separate later-version architecture.

## 12. Privacy, minors, and safety

Profile defaults minimize exposure. Exact location, legal identity, identity documents, date of birth, private contact information, wallet recovery data, tax details, and internal trust signals are never public. Minors receive age-appropriate profiles, stricter discoverability and messaging, no regulated-value participation, guardian hooks where required, and rapid report/escalation paths.

Users can export profile, portfolio, social, and preference data; request deletion where permitted; manage consent and notification channels; review sessions/devices; block, mute, and report; and control scouting/contact visibility. Retention exceptions for disputes, financial records, rights claims, safety evidence, fraud, and legal holds are transparent and purpose-limited.

## 13. APIs and events

Core APIs include profile get/update, discipline add/remove, record/portfolio, handle reservation, portfolio CRUD/publish, availability, links, follows, comments/reactions, reports, bookmarks/shares, feed, search, notifications/read/preferences, teams/roster/roles, live sessions/presence/chat, scout search/lists, opportunities/invites, and contact requests.

Mutations use validated schemas, server authorization, request/trace IDs, idempotency when side effects matter, optimistic version checks for profile edits, consistent errors, rate-limit headers, and documented event side effects.

Events include `profile.updated.v1`, `creator.discipline_added.v1`, `portfolio.published.v1`, `follow.created.v1`, `comment.created.v1`, `notification.requested.v1`, `team.member_added.v1`, `live.session_started.v1`, `opportunity.published.v1`, and `contact_request.accepted.v1`. Privacy and retention class are mandatory in the envelope.

## 14. Failure and abuse modes

| Scenario | Required response |
|---|---|
| Handle race or impersonation | Transactional reservation, normalization/confusable checks, appeal, and auditable reassignment |
| Feed/search outage | Degrade to indexed or chronological safe queries; profiles and direct links remain available |
| Notification outage | Queue/retry with dead-letter handling; in-product canonical status remains |
| Privacy-policy change | Recompute projections and revoke cached/indexed access; retain decision evidence |
| Block evasion or harassment | Device/account risk, rate limit, messaging restriction, case escalation, and appeal |
| Private media leak attempt | Deny access, rotate signed URLs, invalidate cache, open incident, and preserve evidence |
| Scout misuse | Restrict search/export/contact, investigate organization, and notify affected users where required |
| Moderation false positive | Preserve content/evidence, enable appeal, and reverse by a new action rather than deleting history |

## 15. Observability and analytics

Metrics cover profile completion, portfolio publication, discipline coverage, search success, follows and meaningful engagement, creator discovery diversity, contact acceptance, opportunity conversion, team activity, notification delivery, live attendance/replay, blocks/reports, safety response, and privacy requests. Guardrails include harassment, unwanted contact, minor exposure, recommendation concentration, rights disputes, spam, appeal reversals, and sensitive-data access.

Authoritative events are server-side for access, moderation, opportunity, and economic outcomes. Client analytics are consent-aware and never include raw private content, identity documents, contact data, wallet secrets, or unredacted evidence.

## 16. Test Gauntlet

Tests cover handle normalization and concurrency, profile ownership/authorization, privacy projections, export/delete/retention, portfolio access, signed media, search filters, feed ranking version, block/mute semantics, comment moderation, team roles and member removal, scout purpose and contact consent, notification idempotency, live presence/chat moderation, accessibility, localization, load, security, and cache invalidation.

End-to-end scenarios include a new creator completing a music profile and portfolio; gaining a battle result and badge; appearing in permitted search/feed surfaces; joining a team; receiving and consenting to a scout request; blocking harassment; exporting data; and deactivating while immutable competition, rights, and financial records remain correctly retained.

## 17. V1 Definition of Done

The domain is V1 build-complete when public/private creator identities, profiles, handles, full discipline taxonomy, portfolios, provenance/rights, teams, social graph, comments, feeds, search, notifications, live discovery/streaming, native clients, scouting, opportunities, consented contact, reputation separation, privacy/minor controls, moderation, analytics, observability, and operator tools are executable and integrated. Every access decision is server-authoritative, every sensitive exposure is testable, and every public claim links to canonical evidence.

## 18. Dependency-ordered work packages

1. Stable identity/profile IDs, privacy classes, handles, auth references, and policy context.
2. Disciplines, skills, creator profile, portfolio, rights/provenance, and media access.
3. Follows, blocks, mutes, comments, reactions, bookmarks, shares, and notifications.
4. Search documents, filters, ranking versions, feeds, impressions, and diversity guardrails.
5. Teams/collectives, roster roles, team portfolio, competition and split references.
6. Scout profiles, lists, opportunities, invitations, contact consent, and abuse controls.
7. Live sessions, presence, chat, provider adapter, native streaming, replay, captions, and moderation.
8. Native mobile clients, shared design/contracts, push, offline/deep-link, and app-policy profiles.
9. Privacy export/delete/retention/legal hold, minors, data-access auditing, and incidents.
10. Full E2E, accessibility, security, load, moderation, discovery-quality, and operational readiness.

## 19. Open decisions

Open ADRs cover legal entity and IP owner, account and commerce age thresholds, public location fields, verification badge semantics, handle reuse, initial taxonomy, team payout model, search/recommendation implementation, ranking explainability, sponsored discovery boundaries, native streaming provider and moderation, native client rollout, scout verification and export limits, opportunity terms, contact relay, retention periods, data residency, and public API timing. All remain configurable and visible; none removes V1 construction.
