from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADR_DIR = ROOT / 'docs' / 'adr'
ADR_DIR.mkdir(parents=True, exist_ok=True)

# Statuses describe decision state, not whether the related capability belongs in V1.
# Owner Directive 0001 settles build scope; implementation choices remain open unless explicitly stated.
ADRS = [
    (1, 'Monorepo and modular-monolith boundaries', 'Proposed', 'Architecture', 'Repository/package boundaries and future service extraction'),
    (2, 'Cloudflare edge web and API deployment', 'Proposed', 'Platform', 'Web/API runtime, limits, regional behavior, and fallback'),
    (3, 'Next.js and vinext compatibility/fallback', 'Proposed', 'Web', 'Framework build, routing, SSR, and portability'),
    (4, 'Neon Postgres and Drizzle data layer', 'Proposed', 'Data', 'Canonical relational store, migrations, pooling, and transactions'),
    (5, 'Self-hosted identity and authentication stack', 'Proposed', 'Identity and Security', 'Accounts, sessions, passkeys, 2FA, organizations, and recovery'),
    (6, 'R2 upload, quarantine, and media architecture', 'Proposed', 'Media and Security', 'Originals, derivatives, signed access, scan, retention, and CDN'),
    (7, 'Durable Objects realtime coordination', 'Proposed', 'Realtime', 'Battle rooms, presence, voting coordination, chat, and failover'),
    (8, 'Transactional outbox and idempotent consumers', 'Proposed', 'Architecture and Data', 'Domain events, jobs, retries, inboxes, and auditability'),
    (9, 'Immutable double-entry ledger', 'Proposed', 'Finance and Data', 'Journals, postings, balances, holds, reversals, and reconciliation'),
    (10, 'Separation of economic instruments', 'Proposed', 'Finance', 'Arena Points, purchased credits, cash, chain assets, entitlements, and payables'),
    (11, 'Versioned rating algorithm and pools', 'Proposed', 'Competition', 'Glicko-2 baseline, parameters, pool partitioning, and migrations'),
    (12, 'Pure Human, Hybrid, and AI Open divisions', 'Directed', 'Product, Rights, and Trust', 'Disclosure, evidence, judging, enforcement, and appeals'),
    (13, 'Standard-commerce and regulated-value provider boundaries', 'Proposed', 'Finance and Compliance', 'Provider isolation, routing, ledger interfaces, and failure behavior'),
    (14, 'PWA-first delivery order with native mobile in V1', 'Superseded-in-part', 'Product and Client', 'Web/PWA baseline remains; native mobile may not be deferred beyond V1'),
    (15, 'Postgres search baseline and V1 extraction path', 'Proposed', 'Discovery and Platform', 'Full-text/trigram search, ranking, indexing, external-engine extraction'),
    (16, 'No blockchain dependency in V1', 'Superseded', 'Architecture', 'Owner Directive 0001 requires a native blockchain and sovereign application-chain path in V1'),
    (17, 'Provider-neutral heavy media processing', 'Proposed', 'Media and Platform', 'Transcode, waveform, moderation, livestream, portability, and cost'),
    (18, 'Feature flags and jurisdiction policy engine', 'Proposed', 'Compliance and Platform', 'Build/assurance/activation status, policies, approvals, and evidence'),
    (19, 'Human-reviewed material enforcement', 'Directed', 'Trust and Safety', 'AI/rules provide signals; material sanctions and rights decisions retain accountable review'),
    (20, 'No training on creator uploads without opt-in', 'Directed', 'Rights and Privacy', 'Consent, purpose, dataset provenance, revocation, and audit'),
    (21, 'Native Artist Arena chain framework', 'Directed-Scope / Proposed-Technology', 'Blockchain', 'Sovereign chain implementation is required; framework and license require approval'),
    (22, 'Consensus and finality model', 'Proposed', 'Blockchain and Security', 'Safety/liveness, validator faults, finality, upgrades, recovery, and operations'),
    (23, 'Validator, governance, and emergency authority', 'Proposed', 'Blockchain and Governance', 'Admission, removal, keys, voting, upgrades, pause, and accountability'),
    (24, 'Chain state, native modules, and contract runtime', 'Proposed', 'Blockchain', 'Deterministic execution, metering, migrations, capabilities, and third-party contracts'),
    (25, 'Credit/token denomination, supply, and treasury', 'Proposed', 'Economy and Blockchain', 'Atomic units, issuance, burn, reserves, transferability, limits, and disclosures'),
    (26, 'Wallet custody, trusted signing, and recovery', 'Proposed', 'Wallet and Security', 'Managed, self-custodial, organization, key separation, recovery, and compromise'),
    (27, 'Chain/off-chain bridge and reconciliation', 'Proposed', 'Finance and Blockchain', 'Mint/burn, journal linkage, finality, mismatch handling, limits, and recovery'),
    (28, 'Paid-contest operator and jurisdiction model', 'Proposed', 'Compliance, Competition, and Finance', 'Contest classification, operator, regions, age, identity, limits, exclusions, and terms'),
    (29, 'Native iOS and Android applications in V1', 'Directed-Scope / Proposed-Technology', 'Product and Client', 'Native clients are required; framework, store, security, and rollout remain decisions'),
    (30, 'Native livestreaming in V1', 'Directed-Scope / Proposed-Technology', 'Media and Product', 'Owned live path, provider adapter, moderation, recording, captions, and scale'),
    (31, 'Public API, SDK, and partner access in V1', 'Directed-Scope / Proposed-Technology', 'API and Partnerships', 'Contract groups, auth, scopes, limits, developer policy, compatibility, and rollout'),
    (32, 'Configuration-driven one-percent conversion fee', 'Directed', 'Founder, Finance, and Product', 'Each enabled conversion direction uses the founder default; display and accounting details remain configurable'),
    (33, 'Geolocation and location-integrity provider strategy', 'Proposed', 'Compliance and Security', 'Signals, consent, anti-spoofing, fail-closed behavior, retention, and provider portability'),
    (34, 'KYC, KYB, AML, and sanctions provider strategy', 'Proposed', 'Compliance and Privacy', 'Provider result model, step-up tiers, webhooks, cases, retention, and replacement'),
    (35, 'Payment, payout, tax, and app-store providers', 'Proposed', 'Finance and Legal', 'Provider matrix, regions, instruments, reserves, tax records, failure, and reconciliation'),
    (36, 'Creator rights, licenses, consent, and provenance', 'Proposed', 'Rights and Legal', 'Ownership assertions, grants, training consent, collaborators, disputes, and chain anchoring'),
    (37, 'Marketplace, subscriptions, commissions, and fees', 'Proposed', 'Commerce and Finance', 'Products, services, milestones, entitlements, refunds, ratings, splits, and pricing'),
    (38, 'Sponsor, organizer, prize, and scouting model', 'Proposed', 'Partnerships and Competition', 'Contracts, funding, rights, reports, lists, contact consent, and conflicts'),
    (39, 'Moderation, appeals, rights claims, and minor safety', 'Proposed', 'Trust, Rights, and Safety', 'Reports, cases, evidence, actions, counter-notice, appeals, child controls, and audit'),
    (40, 'Data classification, retention, residency, and deletion', 'Proposed', 'Privacy and Data', 'Purpose, retention, regions, export/delete, legal holds, immutable records, and chain privacy'),
    (41, 'Observability, analytics, and experiment governance', 'Proposed', 'Operations and Product', 'Telemetry, redaction, event quality, metrics, guardrails, experiments, and access'),
    (42, 'Security, secrets, signing, and supply-chain baseline', 'Proposed', 'Security', 'Threat model, secret isolation, build provenance, SBOM, dependencies, vulnerabilities, and response'),
    (43, 'SLOs, incidents, business continuity, and disaster recovery', 'Proposed', 'Reliability and Operations', 'Targets, on-call, degraded modes, backups, restore, failover, exercises, and evidence'),
    (44, 'Tournament, judging, voting, and result-finality profiles', 'Proposed', 'Competition and Trust', 'Templates, conflicts, weighting, tie breaks, fraud, disputes, appeals, and ratings'),
    (45, 'Explorer, indexer, and on-chain privacy presentation', 'Proposed', 'Blockchain, Privacy, and Product', 'Canonical projections, reprocessing, public views, sensitive-linkage controls, and audit export'),
]

TEMPLATE = '''# ADR-{id:04d}: {title}\n\n**Status:** {status}  \n**Decision owners:** {owner}; founder approval where scope, economics, rights, legal exposure, or irreversible production authority is affected  \n**Blocking scope:** {scope}\n\n## Context\n\nThe preserved master specification requires this decision to be visible. Owner Directive 0001 makes all described capabilities mandatory V1 construction, but it does not approve an unstated technology, provider, legal interpretation, economic parameter, or production activation. The team must compare realistic options without using an open decision as a reason to defer safe implementation, mocks, simulations, contract surfaces, or tests.\n\n## Decision drivers\n\nThe proposal must compare product fit, security, privacy, rights, compliance, determinism, reliability, latency, scale, portability, operational burden, cost, lock-in, licensing, migration, rollback, auditability, accessibility, and the ability to support the complete V1 destination.\n\n## Options considered\n\n1. **Option A — To be completed.** Describe implementation, benefits, limits, risks, cost, migration, and failure behavior.\n2. **Option B — To be completed.** Describe implementation, benefits, limits, risks, cost, migration, and failure behavior.\n3. **Option C — Status quo or hybrid.** State whether retaining or combining existing approaches is valid.\n\n## Decision\n\nNo implementation choice is approved by this scaffold unless the status is `Directed`, and a Directed status approves only the explicit founder requirement described by the title and register. Complete the comparison, name the accountable approver, record the decision date, and link approval evidence before treating a technology or provider choice as accepted.\n\n## Build-versus-activation rule\n\nWhile this ADR is open, teams must implement interface-neutral contracts, deterministic mocks, simulations, fixtures, tests, and other dependency-valid work. They must not expose real money, production signing, sensitive identity, unapproved provider commitments, public-chain authority, or jurisdiction-restricted behavior without separate activation approval.\n\n## Consequences and follow-up\n\nRecord positive and negative consequences, security and privacy impact, economic and rights impact, required migrations, operational ownership, test/evidence requirements, rollout, rollback, and criteria for revisiting the decision. Link affected requirements and backlog tickets.\n\n## Approval evidence\n\nPending unless a founder directive or signed decision is linked here. Repository text generated during bootstrap is not approval evidence.\n'''

for old in ADR_DIR.glob('[0-9][0-9][0-9][0-9]-*.md'):
    old.unlink()

rows = []
for number, title, status, owner, scope in ADRS:
    slug = ''.join(c.lower() if c.isalnum() else '-' for c in title)
    while '--' in slug:
        slug = slug.replace('--', '-')
    slug = slug.strip('-')
    filename = f'{number:04d}-{slug}.md'
    (ADR_DIR / filename).write_text(TEMPLATE.format(id=number, title=title, status=status, owner=owner, scope=scope), encoding='utf-8')
    rows.append(f'| ADR-{number:04d} | [{title}]({filename}) | {status} | {owner} | {scope} |')

index = '''# Artist Arena V1 Architecture Decision Register\n\nThis register contains forty-five explicit decisions. It preserves the twenty decision areas requested by the source, records the owner directive’s blockchain/mobile/streaming/API scope changes, and adds the economic, chain, wallet, compliance, rights, security, and operations decisions required by the build-complete V1.\n\n**Important:** `Directed` means the founder settled the stated product requirement. It does not silently approve a framework, provider, legal position, denomination, custody model, or production rollout. `Proposed` decisions require named review and approval. `Superseded` records remain for history.\n\n| ID | Decision | Status | Primary owner | Blocking scope |\n|---|---|---|---|---|\n''' + '\n'.join(rows) + '''\n\n## Decision workflow\n\nAn ADR begins Proposed, may become Accepted or Rejected through named approval, and can later be Superseded. Directed and Superseded statuses cite the controlling owner directive. Every accepted ADR records context, compared options, decision, consequences, security/privacy/rights/economic impact, migration, rollback, evidence, date, and approver.\n\nOpen ADRs cannot be guessed. They also cannot be used to move a mandatory V1 capability into a later version. Teams continue interface-neutral, mock, simulation, testnet, local, and test work until the decision permits deeper integration or production activation.\n\n## Template\n\nUse [`0000-template.md`](0000-template.md) for new decisions. Never edit a past Accepted ADR to conceal a change; add a superseding ADR and migration plan.\n'''
(ADR_DIR / 'README.md').write_text(index, encoding='utf-8')

(ADR_DIR / '0000-template.md').write_text('''# ADR-XXXX: Decision title\n\n**Status:** Proposed  \n**Decision owners:** Unassigned  \n**Blocking scope:** To be completed\n\n## Context\n\nExplain the problem, source requirement, owner directives, constraints, and why the decision is needed.\n\n## Decision drivers\n\nList measurable product, architecture, security, privacy, rights, compliance, economic, reliability, operational, cost, licensing, and migration criteria.\n\n## Options considered\n\nDescribe each realistic option, including the status quo, with evidence and consequences.\n\n## Decision\n\nState the selected option, date, approver, exact scope, and non-goals.\n\n## Consequences\n\nRecord positive and negative consequences, risks, mitigations, ownership, and follow-up.\n\n## Migration and rollback\n\nExplain compatibility, data/code migration, rollout, rollback limits, and recovery.\n\n## Verification and approval evidence\n\nLink benchmarks, prototypes, tests, audits, legal/provider review where applicable, and the named approval record.\n''', encoding='utf-8')

print(f'Generated {len(ADRS)} ADRs plus index and template')
