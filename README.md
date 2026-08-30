# Artist Arena V1

> **Competitive infrastructure for the global creator economy.**

Artist Arena is a private, build-complete V1 platform for creator identity, multi-discipline creative competition, human judging, transparent AI participation, discovery, community, sponsorship, scouting, subscriptions, marketplace commerce, creator services, a native blockchain, credits, paid entry, one-to-one credit competition, prize pools, escrow, settlement, cash conversion, payouts, and auditable creator economics.

**Current status:** The repository is a documentation-rich, compilable implementation scaffold. It preserves the complete founder specification, defines product and engineering contracts, and creates the full monorepo, requirements, ADR, backlog, testing, agent, security, economic, blockchain, and operations structure. It does not falsely claim that runtime applications, providers, legal approvals, production infrastructure, custody, or real-value activation are complete.

## 1. Product vision

Artist Arena treats creative excellence as something that can be demonstrated, judged, discovered, recorded, and rewarded across disciplines. The platform begins with a simple music battle loop but is not limited to music. It uses common competition primitives for beat production, songs, rap and freestyle, vocals, dance, visual art, film and video, writing, gaming, coding, game-building, AI creation, streaming, digital media, and multimedia.

The product connects six loops:

| Loop | User outcome |
|---|---|
| **Create identity** | A creator builds a durable profile, disciplines, portfolio, team membership, availability, rights, and provenance record |
| **Compete** | Creators challenge one another or enter battles, tournaments, seasons, ladders, exhibitions, and team events under versioned rules |
| **Judge and prove** | Human judges and eligible audiences score transparent submissions; results, ratings, evidence, disputes, and appeals remain auditable |
| **Discover and connect** | Fans, collaborators, sponsors, organizers, and scouts discover creators through work and competitive evidence rather than popularity alone |
| **Earn and transact** | Creators sell products, subscriptions, services, commissions, licenses, access, and sponsorship while receiving transparent splits and statements |
| **Commit and settle** | The native chain, wallet, credits, holds, escrow, result attestations, settlement, conversions, and payouts provide verifiable economic finality |

Artist Arena’s north star is not raw screen time. It is **meaningful creator opportunity grounded in credible work, fair competition, transparent rights, and trustworthy economic outcomes**.

## 2. Canonical source and owner directive

The full founder specification is preserved byte-for-byte at [`docs/source/ARTIST-ARENA-V1-Master-Specification.md`](docs/source/ARTIST-ARENA-V1-Master-Specification.md). Its expected SHA-256 digest is:

```text
6fe9ba6637165d43d3ab606e54aaed07104aff69e2b5717046ae26b4d4d18fa5
```

The founder’s later instruction is preserved at [`docs/owner-directives/0001-v1-build-complete.md`](docs/owner-directives/0001-v1-build-complete.md). It changes how historical maturity and timing labels are interpreted.

| Priority | Authority | Effect |
|---:|---|---|
| 1 | Owner Directive 0001 and later founder directives | Control present scope and may supersede historical deferrals |
| 2 | Verbatim master specification | Governs all product canon and details not superseded by a directive |
| 3 | Accepted ADRs and RFCs | Resolve architecture without weakening product obligations |
| 4 | Requirements, domain, economic, security, testing, and operations documents | Translate canon into implementation obligations |
| 5 | Backlog, code, tests, evidence, and release artifacts | Implement and prove the approved system |

The canonical source is never edited silently. A new source version receives its own checksum and explicit relationship to the prior version.

## 3. Build-complete V1 doctrine

Every capability described in the source is `V1-BUILD-REQUIRED`, including items historically labeled future, later, phase 2, native-mobile-later, no-blockchain-in-V1, sandbox-only, disabled, non-goal, gated, or provider-dependent.

Mandatory V1 includes:

* native Artist Arena blockchain, nodes, consensus, deterministic execution, native modules, governance, indexer, explorer, testnet, and production-candidate network;
* managed, self-custodial, and organization wallet paths, trusted signing, recovery, and activity;
* purchased credits, Arena Points separation, the founder’s configuration-driven **1% cash-to-credit and credit-to-cash conversion fee**, cash-in, cash-out, payouts, provider adapters, reserves, tax records, chargebacks, and reconciliation;
* free, sponsored, participant-funded, mixed-pool, paid-entry, and one-to-one credit-wager competition, with eligibility, limits, escrow, evidence, finality, disputes, settlement, refunds, and appeals;
* subscriptions, gated access, marketplace products, services, commissions, entitlements, rights, licenses, royalties, collaborator/team splits, and creator statements;
* every discipline and division, native mobile clients, native streaming, public API/SDK, extracted search, and all provider interfaces.

The program tracks three independent statuses:

| Dimension | Meaning |
|---|---|
| **Build** | Architecture, executable implementation, integration, tests, operator/admin paths, runbooks, and ownership exist |
| **Assurance** | Prototype, Integrated, Verified, Audited, or Production-Qualified |
| **Activation** | Local, Sandbox, Testnet, Pilot, Region-Limited, Value-Capped, Production-Enabled, or Disabled-by-Policy |

A legal, jurisdiction, identity, age, provider, audit, security, app-store, capital, or founder gate can restrict real-world activation. It **cannot** remove architecture, code, deterministic mocks, simulations, local/testnet environments, integration, complete failure states, end-to-end tests, admin controls, or runbooks from V1.

## 4. Product actors and surfaces

| Actor | Primary capabilities |
|---|---|
| Audience member | Discover, follow, attend live events, react/comment, bookmark/share, vote when eligible, buy access/products, and manage safety/privacy |
| Creator | Build profile/portfolio, declare disciplines and AI division, publish work, compete, collaborate, sell, license, receive earnings, and manage rights/provenance |
| Team/collective | Manage roster, roles, shared identity/portfolio, competition entry, rights, economic splits, and organization permissions |
| Judge | Accept assignments, declare conflicts, review protected submissions, score versioned dimensions, provide feedback, and participate in appeals where permitted |
| Organizer | Configure and operate battles/tournaments/seasons, rules, schedules, judges, participants, streams, prizes, and reports |
| Sponsor | Create campaigns/briefs, fund prizes, monitor approved outcomes, and receive rights/analytics reports without buying undisclosed competitive rank |
| Scout/A&R | Search consented creator data, maintain private lists, publish opportunities, request contact, and record conflicts/purpose |
| Marketplace buyer/client | Purchase products/access, subscribe, request commissions/services, approve deliverables, review, dispute, and manage entitlements |
| Moderator/trust analyst | Review reports, rights claims, integrity signals, fraud, harassment, minors, appeals, and enforcement with attributable actions |
| Finance/compliance operator | Review policy, identity/location results, holds, conversions, payouts, chargebacks, reconciliation, limits, cases, and activation evidence |
| Platform administrator | Manage configuration and operations without silently rewriting competition, rights, chain, or financial history |

The principal product surfaces are Discover, Arenas, Tournaments, Live, Marketplace, profile/portfolio, teams, subscriptions, sponsorship/scouting, Wallet/economy, notifications, settings/privacy, and the authorized admin console.

## 5. Competition architecture

The competition core owns battles, challenges, tournaments, seasons, ladders, teams, rulesets, eligibility, submissions, lock/reveal, judge assignments, audience ballots, score calculations, provisional and final results, ratings, records, disputes, appeals, livestream/replay, and settlement linkage.

Every event snapshots its discipline, format, Pure Human/Hybrid/AI Open division, ranking status, ruleset version, eligibility, permitted tools, AI disclosure, media requirements, deadlines, scoring, judge/audience weighting, funding, prize allocation, cancellation, tie-break, evidence, dispute, and settlement policy.

```text
DRAFT → PUBLISHED → ENTRY/ACCEPTANCE → ELIGIBILITY/FUNDING
→ SUBMISSION OPEN → LOCKED/REVEALED → JUDGING/VOTING
→ PROVISIONAL RESULT → DISPUTE WINDOW → FINAL RESULT
→ SETTLEMENT PENDING → SETTLED
```

Cancellation, expiration, withdrawal, no-show, disconnection, integrity review, dispute, amended result, void, refund, settlement review, and incident hold are first-class states. The server owns transitions. Clients submit commands, never authoritative state.

Human judges remain central. Automated systems can validate formats, calculate scores, identify duplicates, surface anomalies, and triage evidence. They cannot become the sole judge of creativity, hidden AI usage, authorship, rights, fraud, or guilt.

## 6. Pure Human, Hybrid, and AI Open

Artist Arena does not ban AI and does not pretend AI detection is perfect. It creates transparent divisions:

| Division | Product intent |
|---|---|
| Pure Human | Creator asserts no prohibited generative-AI use and supplies the evidence required by the ruleset |
| Hybrid | AI assistance is allowed with material human direction and complete tool/process disclosure |
| AI Open | Broad generative workflows are allowed under safety, consent, likeness, provenance, and rights rules |

Every submission records division, declaration version, tools/models, source materials, human contribution, licenses/consent, evidence root, and dispute status. Detection output is a risk signal. Material enforcement requires review, documented evidence, notice, and appeal. On-chain provenance commitments store hashes and compact references, not private creation evidence or large media.

## 7. Creator identity, discovery, and community

Public creator identity is separated from authentication, compliance identity, private contact details, and wallet recovery. Stable IDs survive handle changes. Profiles combine disciplines, portfolio, verified work, competitive record, badges, availability, team membership, public links, and creator-selected visibility.

Search and discovery support discipline, division, format, rating/record, work, availability, team, language, and voluntarily shared location. Ranking records its version and reason, measures exposure concentration, and keeps sponsored placement distinct from skill rating and organic evidence. Paid promotion cannot buy judge outcomes, wins, or ratings.

Follows, comments, reactions, bookmarks, shares, feeds, notifications, blocks, mutes, reports, teams, live presence, chat, scouting, opportunities, and consent-based contact use server-side policy. Private submissions cannot leak through indexes, recommendations, analytics, object-storage URLs, cache, or chain metadata.

## 8. Marketplace and creator economy

Marketplace supports digital products, subscriptions, gated access, licenses, commissions, services, milestones, deliverables, acceptance, disputes, refunds, reviews, storefronts, royalties, collaborator/team splits, creator payables, statements, and payout eligibility.

Commerce is tied to explicit rights. Buying a file, token, subscription, or digital object does not automatically transfer copyright, likeness, commercial rights, or AI-training permission. Licenses state permitted use, duration, territory where relevant, attribution, modification, redistribution, training, transfer, and revocation/dispute semantics.

Creator earnings are not a single mutable balance. Sales, fees, royalties, reserves, refunds, chargebacks, tax withholding/status, payables, payouts, and chain settlement remain explicit and reconcilable.

## 9. Native blockchain, Wallet, credits, and settlement

Artist Arena’s chain is a sovereign evidence and settlement layer. It anchors creator provenance, rights/licenses, digital assets, competition/rules commitments, submission hashes, result attestations, escrow, settlement, credits/token state, and governance. Consensus framework, validator model, denomination, supply, custody technology, and mainnet activation remain ADRs rather than invented decisions.

| System | Canonical responsibility |
|---|---|
| Neon Postgres | Product workflows, private identity references, immutable off-chain journals, provider events, moderation, compliance, and read models |
| Cloudflare R2 | Original and derived media, evidence, and protected content |
| Native chain | On-chain assets/credits where approved, provenance/rights commitments, event funding commitments, escrow, result attestations, settlement, and governance |
| Provider adapters | Payment, payout, identity, location, tax, messaging, media, and other external boundaries |
| Indexer/reconciliation | Verified chain projection, journal/provider/chain comparison, mismatches, owner, resolution, and incident evidence |

Financial accounting uses immutable double-entry journals. Amounts use integer minor or atomic units plus instrument/currency. Every transaction balances. Balances are projections. Holds cannot be released twice or above funding. Corrections use compensating entries. State-changing retries are idempotent.

The 1% founder fee is configurable and independently recorded for each enabled conversion direction. It is separated from processor, network, FX, identity, tax, payout, reserve, chargeback, or app-store costs.

## 10. Paid entry and one-to-one credit competition

Paid competition is built completely in V1. Before real-value participation, the policy service evaluates operator, contest class, jurisdiction, location confidence, age, identity, sanctions/risk result, self-exclusion, limits, account/wallet status, instrument, value, provider, and ruleset.

Funds are reserved before play. The event locks its rules, build/runtime context where applicable, participants, submissions, scoring, and payout allocation. Authoritative evidence supports a provisional result. Disputes and appeals freeze settlement. Only a final attestation can release escrow. Cancellation, void, refunds, provider outages, chain finality delays, duplicate messages, collusion, cheating suspicion, chargebacks, reserves, and negative-balance restrictions are tested explicitly.

Operator and jurisdiction policies restrict production exposure; they do not remove the code or tests.

## 11. Architecture and repository layout

Artist Arena begins as a strict TypeScript modular monolith with event-driven boundaries. Cloudflare-oriented web/API/realtime/workers, Neon Postgres/Drizzle, R2 media, typed contracts, provider adapters, and a native-chain subtree are the source-recommended shape. Service extraction occurs only when ownership, load, failure isolation, or deployment evidence justifies it.

| Path | Responsibility |
|---|---|
| `apps/web` | Responsive web application and installable PWA |
| `apps/admin` | Trust, rights, support, finance, compliance, and operations console |
| `apps/api` | Contract-first HTTP boundary |
| `apps/realtime` | Battles, presence, chat, voting, and live coordination |
| `apps/workers` | Outbox, deadlines, media, finalization, settlement, reconciliation, and notifications |
| `packages/*` | Auth, config, contracts, DB, domain, events, flags, ledger, media, notifications, observability, policy, ratings, security, UI, validation, chain, wallet, economy, contests, provenance, and compliance |
| `chain/*` | Node, runtime, native modules, indexer, explorer, testnet, simulations, specs, and fixtures |
| `db/*` | Migrations, deterministic seeds, fixtures, and diagrams |
| `docs/*` | Source, directives, product, architecture, domains, API/data, economy/chain, rights/trust, security/privacy, testing, operations, requirements, ADRs, and backlog |
| `.agents/*` | Persistent memory, specialist roles, workflows, and policies |
| `tests/*` | Contract, integration, E2E, load, security, chain, ledger, policy, and reconciliation tests |

## 12. Data, API, and event rules

IDs are opaque and typed. Time is UTC at rest. Persistent states are versioned. APIs use stable envelopes, consistent errors, pagination, authorization, optimistic concurrency where needed, and idempotency for retryable side effects. Provider webhooks are signature/timestamp verified, archived, replay-protected, normalized, and consumed idempotently.

Domain changes and outbox events commit in one database transaction. Consumers maintain inbox/deduplication state. Events carry version, aggregate, actor, request, trace, correlation, causation, policy, privacy, retention, and occurred/recorded times. Public API and generated SDKs use additive compatibility and explicit deprecation.

## 13. Security, privacy, rights, and trust

Trust zones separate public clients, authenticated clients, admin/operator surfaces, APIs, realtime rooms, workers, database, object storage, external providers, chain nodes, indexer/explorer, wallet/signing, and production control. Least privilege and typed authenticated interfaces govern boundaries.

The baseline covers passkeys/2FA and session security, server authorization, upload quarantine/scanning, signed media access, prompt/untrusted-content resistance, secret isolation, supply-chain controls, SBOM and provenance, encryption, audit, rate limits, abuse controls, fraud and anti-collusion, incident response, backup/restore, and disaster recovery.

Privacy minimizes collection and separates public identity from compliance and custody. It supports purpose/retention, consent, export/delete where permitted, legal holds, access audit, minors, blocking, messaging safety, and rights claims/counter-notices/appeals. Sensitive identity, private evidence, and large media are prohibited on-chain.

## 14. Testing and Definition of Done

The Gauntlet covers formatting, linting, typecheck, build, unit/domain/property, database/migration, API/contract, event/outbox, realtime, media, E2E, accessibility, visual, load/soak, security, secret, dependency/license, chain, wallet, ledger, policy, reconciliation, fault injection, provider outage, backup/restore, deployment, and rollback.

No universal coverage percentage is invented. Tests must prove critical invariants, failure branches, concurrency, idempotency, and recovery. Evidence records commit, toolchain, environment, fixture/seed, commands, expected/actual results, unresolved findings, assurance state, activation state, and named review.

V1 is build-complete only when every major source domain has executable integrated code, tests, ownership, runbooks, and evidence. Selective production activation can remain restricted; construction cannot remain a future promise.

## 15. Implementation control plane

| Artifact | Content |
|---|---|
| [`CODESPRING.md`](CODESPRING.md) | Master CodeSpring execution contract |
| [`AGENTS.md`](AGENTS.md) | Persistent rules for all agents |
| [`docs/requirements/requirements-register.md`](docs/requirements/requirements-register.md) | Exactly 120 build-complete V1 requirements |
| [`docs/backlog/v1-160-tickets.md`](docs/backlog/v1-160-tickets.md) | Exactly 160 dependency-ordered tickets |
| [`docs/adr/README.md`](docs/adr/README.md) | Forty-five individual architecture decisions |
| [`docs/architecture/01-system-architecture.md`](docs/architecture/01-system-architecture.md) | System boundaries and deployment context |
| [`docs/architecture/state-machines.md`](docs/architecture/state-machines.md) | Canonical lifecycle contracts |
| [`docs/data/domain-model.md`](docs/data/domain-model.md) | Relational and on-chain entity model |
| [`docs/api/contracts-and-events.md`](docs/api/contracts-and-events.md) | API groups, events, idempotency, webhooks, and compatibility |
| [`docs/architecture/native-blockchain.md`](docs/architecture/native-blockchain.md) | Native chain, wallet, modules, governance, indexer, and operations |
| [`docs/economy/`](docs/economy/) | Ledger, credits, conversion, paid competition, marketplace, and payout specifications |
| [`docs/compliance/activation-policy-engine.md`](docs/compliance/activation-policy-engine.md) | Operator/jurisdiction/identity/age/location/limit activation policy |
| [`docs/testing/quality-gauntlet.md`](docs/testing/quality-gauntlet.md) | Complete quality and evidence standard |
| [`.agents/PROJECT_MEMORY.md`](.agents/PROJECT_MEMORY.md) | Current implementation truth and handoff format |

## 16. Current limitations

Most apps and packages are contract scaffolds, not completed implementation. The technology and product decision register is mostly Proposed. Named maintainers beyond the repository owner are unassigned. No external provider is represented as selected or approved. No production deployment, real-money activation, mainnet, production custody, mobile store release, legal opinion, rights terms, or audit is claimed.

This is deliberate: **the repository writes out the complete destination while distinguishing requirements from evidence and construction from activation**.

## 17. Confidentiality and license

This private repository contains proprietary planning, architecture, and implementation material. No public or open-source license is granted. Do not publish, mirror, redistribute, sublicense, train external models on, or expose the source outside the owner’s authorized collaborators. See [`LICENSE`](LICENSE), [`SECURITY.md`](SECURITY.md), and [`CONTRIBUTING.md`](CONTRIBUTING.md).

## TL;DR — CodeSpring launch sequence

1. Clone the private repository and branch from `develop`.
2. Read [`docs/owner-directives/0001-v1-build-complete.md`](docs/owner-directives/0001-v1-build-complete.md) before interpreting any historical future/gated labels.
3. Read [`CODESPRING.md`](CODESPRING.md), the verbatim source, requirements, architecture/domain documents, ADR register, and project memory.
4. Start with `AA-0001`, `AA-0002`, and `AA-0003`, then choose the lowest dependency-valid ticket.
5. Claim files in an isolated branch/worktree and write the complete work package before implementation.
6. Do not defer blockchain, wallet, conversions, paid entry, wagers, escrow, payout, mobile, streaming, public API, disciplines, or providers beyond V1; keep unsafe activation disabled while building and testing them fully.
7. Use provider-neutral adapters and deterministic mocks until approved providers and credentials exist.
8. Run repository validation and every applicable Gauntlet check; attach reproducible evidence.
9. Update schemas, APIs, events, ADRs, requirements, risks, documentation, and `.agents/PROJECT_MEMORY.md` in the same pull request.
10. Merge through `develop` → `staging` → `main`; production activation is a separate explicitly approved operation.
