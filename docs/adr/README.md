# Artist Arena V1 Architecture Decision Register

This register contains forty-five explicit decisions. It preserves the twenty decision areas requested by the source, records the owner directive’s blockchain/mobile/streaming/API scope changes, and adds the economic, chain, wallet, compliance, rights, security, and operations decisions required by the build-complete V1.

**Important:** `Directed` means the founder settled the stated product requirement. It does not silently approve a framework, provider, legal position, denomination, custody model, or production rollout. `Proposed` decisions require named review and approval. `Superseded` records remain for history.

| ID | Decision | Status | Primary owner | Blocking scope |
|---|---|---|---|---|
| ADR-0001 | [Monorepo and modular-monolith boundaries](0001-monorepo-and-modular-monolith-boundaries.md) | Proposed | Architecture | Repository/package boundaries and future service extraction |
| ADR-0002 | [Cloudflare edge web and API deployment](0002-cloudflare-edge-web-and-api-deployment.md) | Proposed | Platform | Web/API runtime, limits, regional behavior, and fallback |
| ADR-0003 | [Next.js and vinext compatibility/fallback](0003-next-js-and-vinext-compatibility-fallback.md) | Proposed | Web | Framework build, routing, SSR, and portability |
| ADR-0004 | [Neon Postgres and Drizzle data layer](0004-neon-postgres-and-drizzle-data-layer.md) | Proposed | Data | Canonical relational store, migrations, pooling, and transactions |
| ADR-0005 | [Self-hosted identity and authentication stack](0005-self-hosted-identity-and-authentication-stack.md) | Proposed | Identity and Security | Accounts, sessions, passkeys, 2FA, organizations, and recovery |
| ADR-0006 | [R2 upload, quarantine, and media architecture](0006-r2-upload-quarantine-and-media-architecture.md) | Proposed | Media and Security | Originals, derivatives, signed access, scan, retention, and CDN |
| ADR-0007 | [Durable Objects realtime coordination](0007-durable-objects-realtime-coordination.md) | Proposed | Realtime | Battle rooms, presence, voting coordination, chat, and failover |
| ADR-0008 | [Transactional outbox and idempotent consumers](0008-transactional-outbox-and-idempotent-consumers.md) | Proposed | Architecture and Data | Domain events, jobs, retries, inboxes, and auditability |
| ADR-0009 | [Immutable double-entry ledger](0009-immutable-double-entry-ledger.md) | Proposed | Finance and Data | Journals, postings, balances, holds, reversals, and reconciliation |
| ADR-0010 | [Separation of economic instruments](0010-separation-of-economic-instruments.md) | Proposed | Finance | Arena Points, purchased credits, cash, chain assets, entitlements, and payables |
| ADR-0011 | [Versioned rating algorithm and pools](0011-versioned-rating-algorithm-and-pools.md) | Proposed | Competition | Glicko-2 baseline, parameters, pool partitioning, and migrations |
| ADR-0012 | [Pure Human, Hybrid, and AI Open divisions](0012-pure-human-hybrid-and-ai-open-divisions.md) | Directed | Product, Rights, and Trust | Disclosure, evidence, judging, enforcement, and appeals |
| ADR-0013 | [Standard-commerce and regulated-value provider boundaries](0013-standard-commerce-and-regulated-value-provider-boundaries.md) | Proposed | Finance and Compliance | Provider isolation, routing, ledger interfaces, and failure behavior |
| ADR-0014 | [PWA-first delivery order with native mobile in V1](0014-pwa-first-delivery-order-with-native-mobile-in-v1.md) | Superseded-in-part | Product and Client | Web/PWA baseline remains; native mobile may not be deferred beyond V1 |
| ADR-0015 | [Postgres search baseline and V1 extraction path](0015-postgres-search-baseline-and-v1-extraction-path.md) | Proposed | Discovery and Platform | Full-text/trigram search, ranking, indexing, external-engine extraction |
| ADR-0016 | [No blockchain dependency in V1](0016-no-blockchain-dependency-in-v1.md) | Superseded | Architecture | Owner Directive 0001 requires a native blockchain and sovereign application-chain path in V1 |
| ADR-0017 | [Provider-neutral heavy media processing](0017-provider-neutral-heavy-media-processing.md) | Proposed | Media and Platform | Transcode, waveform, moderation, livestream, portability, and cost |
| ADR-0018 | [Feature flags and jurisdiction policy engine](0018-feature-flags-and-jurisdiction-policy-engine.md) | Proposed | Compliance and Platform | Build/assurance/activation status, policies, approvals, and evidence |
| ADR-0019 | [Human-reviewed material enforcement](0019-human-reviewed-material-enforcement.md) | Directed | Trust and Safety | AI/rules provide signals; material sanctions and rights decisions retain accountable review |
| ADR-0020 | [No training on creator uploads without opt-in](0020-no-training-on-creator-uploads-without-opt-in.md) | Directed | Rights and Privacy | Consent, purpose, dataset provenance, revocation, and audit |
| ADR-0021 | [Native Artist Arena chain framework](0021-native-artist-arena-chain-framework.md) | Directed-Scope / Proposed-Technology | Blockchain | Sovereign chain implementation is required; framework and license require approval |
| ADR-0022 | [Consensus and finality model](0022-consensus-and-finality-model.md) | Proposed | Blockchain and Security | Safety/liveness, validator faults, finality, upgrades, recovery, and operations |
| ADR-0023 | [Validator, governance, and emergency authority](0023-validator-governance-and-emergency-authority.md) | Proposed | Blockchain and Governance | Admission, removal, keys, voting, upgrades, pause, and accountability |
| ADR-0024 | [Chain state, native modules, and contract runtime](0024-chain-state-native-modules-and-contract-runtime.md) | Proposed | Blockchain | Deterministic execution, metering, migrations, capabilities, and third-party contracts |
| ADR-0025 | [Credit/token denomination, supply, and treasury](0025-credit-token-denomination-supply-and-treasury.md) | Proposed | Economy and Blockchain | Atomic units, issuance, burn, reserves, transferability, limits, and disclosures |
| ADR-0026 | [Wallet custody, trusted signing, and recovery](0026-wallet-custody-trusted-signing-and-recovery.md) | Proposed | Wallet and Security | Managed, self-custodial, organization, key separation, recovery, and compromise |
| ADR-0027 | [Chain/off-chain bridge and reconciliation](0027-chain-off-chain-bridge-and-reconciliation.md) | Proposed | Finance and Blockchain | Mint/burn, journal linkage, finality, mismatch handling, limits, and recovery |
| ADR-0028 | [Paid-contest operator and jurisdiction model](0028-paid-contest-operator-and-jurisdiction-model.md) | Proposed | Compliance, Competition, and Finance | Contest classification, operator, regions, age, identity, limits, exclusions, and terms |
| ADR-0029 | [Native iOS and Android applications in V1](0029-native-ios-and-android-applications-in-v1.md) | Directed-Scope / Proposed-Technology | Product and Client | Native clients are required; framework, store, security, and rollout remain decisions |
| ADR-0030 | [Native livestreaming in V1](0030-native-livestreaming-in-v1.md) | Directed-Scope / Proposed-Technology | Media and Product | Owned live path, provider adapter, moderation, recording, captions, and scale |
| ADR-0031 | [Public API, SDK, and partner access in V1](0031-public-api-sdk-and-partner-access-in-v1.md) | Directed-Scope / Proposed-Technology | API and Partnerships | Contract groups, auth, scopes, limits, developer policy, compatibility, and rollout |
| ADR-0032 | [Configuration-driven one-percent conversion fee](0032-configuration-driven-one-percent-conversion-fee.md) | Directed | Founder, Finance, and Product | Each enabled conversion direction uses the founder default; display and accounting details remain configurable |
| ADR-0033 | [Geolocation and location-integrity provider strategy](0033-geolocation-and-location-integrity-provider-strategy.md) | Proposed | Compliance and Security | Signals, consent, anti-spoofing, fail-closed behavior, retention, and provider portability |
| ADR-0034 | [KYC, KYB, AML, and sanctions provider strategy](0034-kyc-kyb-aml-and-sanctions-provider-strategy.md) | Proposed | Compliance and Privacy | Provider result model, step-up tiers, webhooks, cases, retention, and replacement |
| ADR-0035 | [Payment, payout, tax, and app-store providers](0035-payment-payout-tax-and-app-store-providers.md) | Proposed | Finance and Legal | Provider matrix, regions, instruments, reserves, tax records, failure, and reconciliation |
| ADR-0036 | [Creator rights, licenses, consent, and provenance](0036-creator-rights-licenses-consent-and-provenance.md) | Proposed | Rights and Legal | Ownership assertions, grants, training consent, collaborators, disputes, and chain anchoring |
| ADR-0037 | [Marketplace, subscriptions, commissions, and fees](0037-marketplace-subscriptions-commissions-and-fees.md) | Proposed | Commerce and Finance | Products, services, milestones, entitlements, refunds, ratings, splits, and pricing |
| ADR-0038 | [Sponsor, organizer, prize, and scouting model](0038-sponsor-organizer-prize-and-scouting-model.md) | Proposed | Partnerships and Competition | Contracts, funding, rights, reports, lists, contact consent, and conflicts |
| ADR-0039 | [Moderation, appeals, rights claims, and minor safety](0039-moderation-appeals-rights-claims-and-minor-safety.md) | Proposed | Trust, Rights, and Safety | Reports, cases, evidence, actions, counter-notice, appeals, child controls, and audit |
| ADR-0040 | [Data classification, retention, residency, and deletion](0040-data-classification-retention-residency-and-deletion.md) | Proposed | Privacy and Data | Purpose, retention, regions, export/delete, legal holds, immutable records, and chain privacy |
| ADR-0041 | [Observability, analytics, and experiment governance](0041-observability-analytics-and-experiment-governance.md) | Proposed | Operations and Product | Telemetry, redaction, event quality, metrics, guardrails, experiments, and access |
| ADR-0042 | [Security, secrets, signing, and supply-chain baseline](0042-security-secrets-signing-and-supply-chain-baseline.md) | Proposed | Security | Threat model, secret isolation, build provenance, SBOM, dependencies, vulnerabilities, and response |
| ADR-0043 | [SLOs, incidents, business continuity, and disaster recovery](0043-slos-incidents-business-continuity-and-disaster-recovery.md) | Proposed | Reliability and Operations | Targets, on-call, degraded modes, backups, restore, failover, exercises, and evidence |
| ADR-0044 | [Tournament, judging, voting, and result-finality profiles](0044-tournament-judging-voting-and-result-finality-profiles.md) | Proposed | Competition and Trust | Templates, conflicts, weighting, tie breaks, fraud, disputes, appeals, and ratings |
| ADR-0045 | [Explorer, indexer, and on-chain privacy presentation](0045-explorer-indexer-and-on-chain-privacy-presentation.md) | Proposed | Blockchain, Privacy, and Product | Canonical projections, reprocessing, public views, sensitive-linkage controls, and audit export |

## Decision workflow

An ADR begins Proposed, may become Accepted or Rejected through named approval, and can later be Superseded. Directed and Superseded statuses cite the controlling owner directive. Every accepted ADR records context, compared options, decision, consequences, security/privacy/rights/economic impact, migration, rollback, evidence, date, and approver.

Open ADRs cannot be guessed. They also cannot be used to move a mandatory V1 capability into a later version. Teams continue interface-neutral, mock, simulation, testnet, local, and test work until the decision permits deeper integration or production activation.

## Template

Use [`0000-template.md`](0000-template.md) for new decisions. Never edit a past Accepted ADR to conceal a change; add a superseding ADR and migration plan.
