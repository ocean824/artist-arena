# Owner Directive 0001: Artist Arena V1 Is Build-Complete

- **Directive authority:** Founder/Product Owner Ø
- **Effective date:** 2026-08-30
- **Status:** Governing product and implementation override
- **Applies to:** Product requirements, architecture, schemas, APIs, code, tests, backlogs, milestones, agents, launch planning, and repository documentation
- **Canonical preservation:** The supplied master specification remains preserved verbatim. This directive overrides any source statement that classifies a described Artist Arena capability as later, future, optional, deferred, non-goal, sandbox-only, post-V1, or unavailable for V1 construction.

## Directive

Artist Arena V1 must be designed and built as the **full competitive infrastructure layer for the global creator economy**, not as a reduced social prototype. Every capability described in the product canon—including a native blockchain, credits, cash-in and cash-out, paid battle entry, one-to-one credit wagers, sponsor-funded and participant-funded prize pools, escrow, settlement, creator payments, subscriptions, commissions, marketplace commerce, licensing, revenue splits, tax and compliance records, fraud controls, disputes, chargebacks, and multi-discipline expansion—is mandatory V1 engineering scope.

The repository must contain the production-grade interfaces, state machines, schemas, ledgers, provider adapters, policy engine, audit system, tests, monitoring, operations, and user experiences needed for these capabilities. No feature may be omitted or converted into a documentation-only placeholder because its production activation depends on counsel, identity verification, a payment provider, a jurisdiction, a security audit, or founder approval.

## Construction is mandatory; exposure remains controlled

The program separates **whether a capability is built** from **where and when it is activated**.

| Control | May restrict | Must not restrict |
|---|---|---|
| Jurisdiction policy | Regions, operators, user locations, contest classes, currencies, payout availability, age thresholds | Building the complete capability and exercising it in local, sandbox, simulation, and test environments |
| Identity/compliance policy | Who may deposit, wager, enter paid contests, receive prizes, withdraw, sponsor, judge, or operate | Schemas, services, integrations, tests, administrator tooling, and end-to-end flows |
| Payment/provider approval | Live rails, cash movement, supported currencies, settlement timing, reserves | Provider-neutral adapters, mock providers, ledger posting, holds, refunds, chargebacks, and reconciliation |
| Security/audit gate | Real secrets, production signing, custody, value limits, public activation | Implementation, test keys, adversarial testing, sandbox custody, recovery drills, and operational runbooks |
| Founder approval | Production activation, commercial rates, supported regions, mainnet launch, public terms | Dependency-ordered construction and verification of the full V1 capability set |

A capability may be `DISABLED_BY_POLICY` in a production region while still being complete and tested in the V1 codebase. A gate is never permission to defer the system to V2.

## Mandatory V1 native blockchain scope

Artist Arena must have a native blockchain or sovereign application-chain implementation path in V1. The chain must serve creator provenance, competition evidence, programmable rights, digital assets, creator splits, prize escrow, settlement attestations, and economic auditability without forcing large media files or sensitive identity onto a public ledger.

| Blockchain domain | Required V1 outcome |
|---|---|
| Node and network | Runnable node, peer networking, state sync, telemetry, upgrade, backup, recovery, and production-candidate network |
| Consensus and governance | Selected consensus, validator/operator model, fault simulation, upgrade authority, emergency procedures, and transparent versioning |
| State model | Versioned identities/pseudonyms, creator works, licenses, splits, contest commitments, escrow, results, claims, settlements, and policy references |
| Execution | Deterministic native modules and/or contract runtime with limits, metering, migrations, replay protection, and invariants |
| Wallet integration | Managed and self-custodial paths, purpose-separated keys, trusted confirmations, recovery, activity history, and policy checks |
| Provenance | Content hashes, timestamps, creator declarations, tool/AI disclosures, licenses, consent references, and dispute status |
| Competition evidence | Battle/tournament identity, ruleset hash, submission commitments, judge/audience evidence, result attestation, appeal and finality records |
| Economic settlement | Credits/tokens, holds, entry commitments, prize pools, creator splits, fees, refunds, reversals where legally/technically applicable, and reconciliation anchors |
| Explorer and support | User-safe history, operator diagnostics, privacy-aware indexing, case linking, and audit exports |

The production user experience may abstract blockchain mechanics. Blockchain functionality must nevertheless exist in the V1 architecture and implementation rather than being deferred or replaced by a future promise.

## Mandatory V1 credit, wagering, and cash-value scope

The original credit economy is a locked product requirement. V1 must support users purchasing credits, using credits to enter battles, wagering credits one-to-one against opponents, funding participant and sponsor prize pools, paying creators, earning credits or other value, and converting eligible balances to cash. The Artist Arena conversion fee defaults to **1%**, remains configuration-driven, and is accounted for separately from processor, verification, currency, tax, network, and chargeback costs.

| Economic capability | Mandatory V1 behavior |
|---|---|
| Credit purchase | Quote, user confirmation, provider authorization, ledger posting, fee disclosure, receipt, fraud checks, and failure recovery |
| Battle entry | Eligibility decision, balance reservation, entry commitment, cancellation rules, contest start, and release or settlement |
| One-to-one wager | Matched terms, symmetric commitment, ruleset acceptance, funds reservation, result finality, dispute window, and payout |
| Prize pool | Sponsor, platform, participant, or mixed funding; escrow; published allocation; cancellation/refund; result-based settlement |
| Creator payment | Purchase, tip where allowed, subscription, commission, license, gated access, split distribution, refund, dispute, and tax record |
| Cash-out | Eligible balance calculation, identity and policy check, hold review, provider payout, fee disclosure, reconciliation, failure and retry |
| Conversion fee | Configurable 1% platform default; versioned policy; precise ledger entry; disclosure; reporting; no hardcoded hidden charge |
| Chargeback/reversal | External dispute intake, liability allocation, reserve or negative balance handling, evidence, appeal, and accounting adjustment |
| Responsible participation | Age and identity rules, jurisdiction blocks, user limits, cooling-off/self-exclusion controls where required, fraud and collusion monitoring |

These flows must be testable end to end in V1. Production activation depends on the selected jurisdiction and operating model, but implementation is not postponed.

## Requirement model

All capabilities described in the master specification receive `V1-BUILD-REQUIRED`. Separate fields determine activation and assurance.

| Dimension | Values |
|---|---|
| Build obligation | `V1-BUILD-REQUIRED` |
| Environment | `LOCAL`, `TEST`, `SANDBOX`, `TESTNET`, `STAGING`, `PRODUCTION` |
| Activation | `ENABLED`, `DISABLED_BY_POLICY`, `REGION_LIMITED`, `INVITE_ONLY`, `VALUE_CAPPED`, `PROVIDER_PENDING` |
| Assurance | `PROTOTYPE`, `INTEGRATED`, `VERIFIED`, `AUDITED`, `PRODUCTION_QUALIFIED` |
| Economic effect | `NO_VALUE`, `SIMULATED_VALUE`, `TEST_VALUE`, `REAL_VALUE` |

Source labels such as “future,” “later,” “sandbox,” “non-goal,” or “after approval” remain useful as historical or activation context only. They no longer define the V1 engineering boundary.

## Product breadth in V1

Music remains the recommended first validation wedge, but the architecture and implementation must support the full discipline-agnostic model in V1. Beat, song, rap/freestyle, dance, visual art, film/video, writing, gaming, coding, game-building, AI creation, streaming, digital media, and multimedia competitions must share stable competition primitives while permitting discipline-specific submission, judging, playback, scoring, provenance, and moderation modules.

Native mobile clients, native streaming and livestreaming, the public API and SDK, external search-engine extraction, and all required provider integrations may be sequenced after their foundational contracts within the V1 program, but their contracts, services, clients, implementations, tests, administrative controls, and operational runbooks remain `V1-BUILD-REQUIRED` rather than V2 assumptions.

## Backlog interpretation

A task may be blocked for architecture, integration, security qualification, external provider access, legal activation, or production approval. The team must continue all work that does not require the missing external authority: schemas, APIs, state machines, adapters, mocks, simulations, user interfaces, operational tools, tests, threat models, documentation, and sandbox execution.

“Deferred” is valid only when a later explicit owner directive removes the item from V1. Neither an agent nor an implementation team may infer deferral from risk, complexity, or a source phrase that predates this directive.

## V1 Definition of Done

Artist Arena V1 is build-complete only when the full product loop works across identity, creator profiles, media, battles, challenges, tournaments, rankings, judging, audience participation, discovery, community, sponsorship, scouting, marketplace, creator commerce, native blockchain, credits, paid entry, one-to-one wagers, prize escrow, settlement, conversion, cash-out, disputes, moderation, rights, compliance, analytics, support, and operations.

Production deployment may expose different features by operator and jurisdiction. The underlying V1 platform must not require a later architectural rebuild to activate any capability described above.

## Persistent agent instruction

Manus, CodeSpring, Traycer, Codex, Claude, and every other worker must apply this rule:

> When the preserved source describes an Artist Arena capability as later, future, gated, optional, sandbox-only, or outside V1, retain the activation and risk controls but move the capability into mandatory V1 architecture, implementation, integration, and test scope. Never use a gate to avoid building it.

Any conflict between this directive and the preserved source must be reported explicitly and resolved in favor of this directive for current repository planning and implementation.
