# Artist Arena V1 Native Blockchain Architecture

**Authority:** This document derives from the preserved Artist Arena master specification and Owner Directive 0001. The directive makes native blockchain functionality a mandatory V1 architecture, implementation, integration, and test obligation. Consensus technology, denomination, validator composition, custody provider, and mainnet launch remain explicit decisions; this document does not invent their approval.

## 1. Mission and boundaries

Artist Arena’s native blockchain is the sovereign evidence and settlement layer for creator provenance, programmable rights, competition commitments, prize escrow, result attestations, credits/tokens, creator splits, and auditable economic finality. It is not a replacement for the web application database, media storage, compliance record store, or real-time battle coordination.

The chain records compact, durable protocol facts. Large media remains in controlled object storage. Authentication credentials, identity documents, tax records, private contact details, fraud signals, support evidence, and unnecessary personal information stay off-chain. The relational application remains authoritative for product workflows until an approved transaction commits; the chain becomes authoritative for the state transitions assigned to its modules.

## 2. Design principles

| Principle | Required consequence |
|---|---|
| Sovereign control | Artist Arena owns the protocol, module contracts, upgrade process, operational evidence, and data model rather than depending on an unrelated token network for core product behavior |
| Deterministic execution | Identical valid state and transaction input produces identical state transition and events across nodes |
| Native modules first | Identity references, provenance, rights, assets, credits, escrow, competition commitments, settlement, and governance use tightly bounded native modules before general third-party programmability |
| Explicit finality | Product and financial systems know whether a transaction is pending, finalized, failed, replaced, or subject to recovery procedures |
| Privacy minimization | Personal, confidential, mutable, and large data remains off-chain; hashes and opaque references are used only when necessary and policy-safe |
| Ledger separation | On-chain assets, off-chain credits/liabilities, fiat/provider settlement, entitlements, and creator payables remain distinct and reconcile through explicit bridges |
| Defense in depth | Policy checks exist before transaction construction, during application authorization, inside chain module validation, and during settlement/reconciliation |
| Build versus activation | Local network, deterministic simulation, sandbox, testnet, modules, wallet, indexer, explorer, and operations are mandatory V1 construction; real-value mainnet exposure remains separately approved |
| No invented economics | Supply, denomination, transferability, fees, treasury, validator rewards, and governance parameters require approved ADRs and versioned policy |

## 3. System context

The web/API modular monolith owns user experience, authentication, profile, media, competition workflow, marketplace workflow, moderation, support, provider integration, and operator policy. Neon Postgres contains canonical off-chain domain records and the immutable financial journal. Cloudflare R2 stores original and derived media. Durable Objects coordinate real-time rooms. Queues and workers process the outbox, chain submissions, finality, indexing, notifications, and reconciliation.

The native chain comprises node/network, consensus, deterministic runtime, native modules, validator/governance operations, wallet/signing services, indexer, explorer, testnet, simulations, backup/recovery, and monitoring. The application submits transactions through a versioned adapter and consumes finalized chain events through an idempotent indexer/outbox bridge.

```text
Web / Native Clients
        │
        ▼
API + Policy + Domain Services ──── Postgres Ledger / Outbox
        │                                  │
        ├── Trusted Wallet/Signer          ├── Queue Consumers
        │                                  │
        ▼                                  ▼
Chain Transaction Gateway ─────── Native Artist Arena Network
                                           │
                         ┌─────────────────┼─────────────────┐
                         ▼                 ▼                 ▼
                    Validators       Native Modules    Indexer/Explorer
                                                               │
                                                               ▼
                                                   Postgres Read Models
```

No client directly declares a balance, eligibility result, competition result, or settlement outcome. No game or user-supplied interface may replace the trusted signing surface.

## 4. Node, network, and consensus decision surface

The node must provide peer discovery, authenticated networking, transaction propagation, deterministic block/state execution, state synchronization, persistent storage, pruning/snapshot policy, telemetry, upgrades, backups, restore, and operator diagnostics. The production-candidate network must run as a reproducible artifact with signed provenance.

Consensus remains an ADR. Candidate implementations must be compared against safety and liveness assumptions, deterministic finality, validator operations, fault tolerance, performance under the expected workload, upgrade/recovery behavior, implementation maturity, language/runtime fit, license, auditability, and operational cost. The repository must not hard-code a favored framework before the ADR is approved.

V1 requires a deterministic simulator that exercises honest faults, Byzantine behavior, partitions, delayed messages, validator loss, invalid blocks, conflicting proposals, restart, state sync, snapshot restore, and upgrade boundaries. Test results identify the exact build, seed, topology, timing model, and hardware profile.

## 5. State and execution model

Every transaction uses a versioned envelope containing network, chain, transaction, actor/signing authority, nonce or replay-protection value, expiry, command type/version, payload hash, fee/resource limit, policy/authorization reference, and signature set. Validation occurs before execution and again at module boundaries.

The runtime must provide deterministic serialization, bounded computation and storage, explicit errors, no ambient network or clock access inside execution, versioned migrations, event emission, transaction atomicity, and state-root verification. A general contract runtime is mandatory V1 construction, but unrestricted deployment remains disabled until capability, metering, security, upgrade, and audit controls pass.

## 6. Native modules

| Module | State and responsibilities |
|---|---|
| Identity reference | Pseudonymous chain identity, approved public key relationships, status references, and rotation/revocation without storing legal identity |
| Provenance | Work/content hash, creator reference, timestamp, evidence root, tool/AI disclosure, source/license references, and dispute status |
| Rights and licenses | Versioned rights grant, permitted uses, territory/duration where applicable, attribution, training consent, transfer limits, and revocation/amendment semantics |
| Digital assets | Mint, ownership, transfer, burn, freeze only where policy and terms permit, metadata reference, entitlement link, provenance, and license association |
| Credits/token | Issuance/burn, atomic units, treasury, balances, holds, transferability class, supply limits, conversion references, emergency controls, and audit events |
| Competition | Ruleset/build hash, participant commitments, submission commitment roots, evidence roots, authority set, result and dispute references |
| Escrow | Pool/funding sources, participant/sponsor commitments, holds, release conditions, cancellation/refund rules, dispute freeze, and settlement status |
| Settlement | Final result reference, allocation, platform fee, creator/team split, tax/withholding reference, recipient postings, idempotency, and completion proof |
| Governance | Parameter versions, validator/operator authority, upgrades, module pause, emergency procedure, transparent proposals/decisions, and audit trail |

Modules use stable identifiers shared with application contracts. No module stores arbitrary personal profiles or media. Mutable off-chain URLs are not treated as permanent provenance; content hashes, storage commitments, and availability policy are distinct.

## 7. Competition commitments and result attestation

Publishing a value-bearing competition commits an immutable ruleset version, software/build profile where relevant, discipline, division, eligibility policy, funding structure, allocation, dispute window, cancellation rules, result-authority profile, and settlement module version. Participants accept those terms before funds are held.

Submission finalization creates an off-chain immutable snapshot and a chain commitment containing only required hashes and references. Authoritative battle/tournament services produce result evidence linked to replay, judge, audience, integrity, and calculation records. The attestation identifies event, participants, ruleset, submission commitments, result, authority/signatures, calculation version, dispute state, and evidence root.

A provisional result cannot settle. The finality service verifies that the dispute window expired or all disputes/appeals resolved, then submits the final attestation. Chain and application modules reject an attestation that refers to the wrong event, participants, rules, build, funds, authority, or prior final result.

## 8. Credits, token, and economic boundaries

The source requires purchased credits, earned value, battle entry, one-to-one wagers, creator payments, and cash conversion. The chain must support these capabilities without pretending every accounting fact belongs on-chain.

| Boundary | Canonical responsibility |
|---|---|
| Fiat/provider settlement | External authorizations, captures, payouts, refunds, chargebacks, processor fees, reserves, and bank settlement |
| Off-chain double-entry ledger | Legal/platform liabilities, credit balances where off-chain, creator payables, fees, taxes, holds, reversals, provider reconciliation, and statements |
| Native chain | On-chain credit/token balances, digital assets, escrow commitments, settlement proofs, provenance/rights, and governance |
| Entitlements | Access to content, products, services, events, and installations independent of the payment or asset rail |

An approved bridge operation links one off-chain journal and one on-chain transaction. Minting follows confirmed funding and policy approval. Burning precedes or atomically coordinates a payout request so value cannot be spent twice. Every bridge action has idempotency, correlation, actor, policy, quote, fee, provider, chain transaction, journal, and reconciliation identifiers.

The 1% founder conversion fee is configuration-driven and applies to each approved cash-to-credit or credit-to-cash conversion according to the versioned fee policy. It is separate from processor, network, foreign exchange, identity, tax, reserve, chargeback, and payout costs. Denomination and supply are open ADRs; no conversion constant is invented here.

## 9. Escrow and settlement

A pool can be sponsor-funded, platform-funded, participant-funded, or mixed. Funding records identify instrument, contributor, amount, source ledger/transaction, refund rule, and availability. Escrow states are `PROPOSED`, `FUNDING`, `FUNDED`, `LOCKED`, `DISPUTED`, `SETTLEMENT_READY`, `SETTLED`, `REFUNDING`, `REFUNDED`, or `INCIDENT_HOLD`.

Invariants include: released value never exceeds confirmed funding; one source commitment funds one pool position; locked funds cannot be spent elsewhere; settlement occurs once; disputed pools cannot settle; cancellation follows the committed rule; every recipient allocation plus fees, withholding, refunds, and remainder equals the pool; the final result and settlement refer to the same event and version; retries return the original result; and Chain and off-chain projections reconcile.

A blockchain transaction cannot reverse an external chargeback. The economic architecture therefore includes reserve and negative-balance policy, affected account restrictions, claims and evidence, recovery, and compensating off-chain/on-chain actions where technically and legally valid. History is never silently rewritten.

## 10. Wallet and signing architecture

Wallet supports managed custody, self-custody, and organization/team treasury modes. The final custody technology and provider remain ADRs. Keys are purpose-separated for authentication, ordinary wallet transactions, high-value operations, treasury, validator, governance, bridge, and recovery. Platform keys use isolated signing infrastructure, least privilege, dual control, rotation, and tested compromise response.

The trusted confirmation surface displays action, source/destination, asset or credit instrument, amount, all fee categories, contest or marketplace context, permissions, irreversible effects, policy status, expiry, and recovery/support path. Untrusted media, creator content, games, plugins, and web views cannot draw over, script, or imitate this surface.

Managed recovery uses verified account recovery plus step-up authentication and risk review; it must not make possession of an email alone equivalent to custody authority. Self-custody recovery cannot rely on an undisclosed administrator override. Social, guardian, multisignature, or hardware recovery options require explicit user configuration and security analysis. Court or policy restrictions are represented as separately authorized module/account controls with audit evidence.

## 11. Indexer, explorer, and reconciliation

The indexer consumes finalized blocks, verifies chain continuity and state roots, applies versioned projections, and records checkpoints. Reprocessing is idempotent. Reorganization behavior, if possible under the selected consensus, is explicit. Explorer views cover transactions, assets, provenance, licenses, competitions, pools, settlements, validators, governance, and module versions while respecting privacy and avoiding public linkage of compliance identity.

Reconciliation compares chain state, indexer projections, off-chain journals, escrow records, provider events, payouts, entitlements, and application state. Every mismatch becomes a classified reconciliation item with owner, amount/state delta, evidence, resolution, and incident linkage. No automated correction may mutate immutable history without an authorized compensating action.

## 12. Privacy, rights, and compliance

On-chain data must pass a permanence review. Direct personal identifiers, identity documents, date of birth, address, private contact, tax data, full payment payloads, device fingerprints, private evidence, unreleased submissions, and moderation notes are prohibited. Even hashes can become identifying when inputs are predictable; the design uses opaque references, keyed commitments, salted structures, or off-chain proof services where necessary.

Creator provenance is evidence, not automatic ownership adjudication. Rights claims and counter-notices can mark a record disputed or superseded without deleting the original. AI division disclosures are anchored through versioned declarations and evidence roots. Detection systems may contribute risk signals but cannot autonomously rewrite a creator’s provenance or competition result.

The application policy service evaluates operator, jurisdiction, location, age, identity, sanctions/risk result, self-exclusion, limits, wallet restrictions, contest or commerce class, instrument, provider, value, and assurance. Chain modules also enforce non-bypassable structural restrictions. A local/testnet transaction does not imply real-world legal approval.

## 13. Security and failure modes

Threats include stolen keys, signer compromise, validator collusion, consensus failure, replay, double spend, bridge mismatch, malicious contract/module input, resource exhaustion, indexer corruption, false result attestation, compromised authority, rights fraud, privacy leakage, and governance abuse.

Required controls include hardware-backed or isolated platform keys, multisignature/threshold policy for high-risk authority, nonce/expiry/domain separation, least privilege, deterministic limits, signed builds, reproducible artifacts, SBOM, dependency/license review, static analysis, fuzzing, differential tests, fault injection, module audits, validator monitoring, pause boundaries, backup/restore, state verification, and incident runbooks.

During provider outage, deposits/payouts pause while unaffected chain functions may continue. During finality uncertainty, dependent settlement remains pending. During indexer outage, chain truth remains available but user-facing projections clearly degrade. During consensus safety concern, governance pauses affected modules and preserves forensic state. Recovery never fabricates missing finality.

## 14. Environments and operations

| Environment | Purpose |
|---|---|
| Local deterministic network | Unit, property, developer, migration, replay, and CI scenarios |
| Sandbox network | End-to-end application, provider mock, wallet, contest, marketplace, and operator testing |
| Persistent testnet | Multi-node operations, upgrades, fault tests, external audit, validator rehearsals, indexer/explorer, and integrations |
| Production-candidate network | Final configuration, controlled pilot, disaster recovery, security and economic limits |
| Mainnet/production | Only after founder, legal/operator, provider, security, operational, and policy authorization for the defined activation profile |

Node and validator runbooks cover provisioning, identity, key ceremonies, monitoring, rotation, upgrade, rollback limits, snapshot, restore, peer incidents, liveness/safety incidents, evidence retention, and decommissioning. Dashboards track finality, block production, peer health, state sync, transaction failure, module errors, queue depth, bridge lag, indexer checkpoint, reconciliation variance, signer health, and policy denials without leaking sensitive data.

## 15. Test and audit Gauntlet

Tests include deterministic transition/property tests, invalid transaction corpus, replay and duplicate rejection, concurrency, supply and escrow invariants, migration/upgrade, module pause, permission negatives, wallet recovery, signer failure, consensus faults, partition, state sync, snapshot restore, indexer rebuild, bridge idempotency, provider retries, contest settlement, marketplace royalty, refund/chargeback, privacy review, load/soak, and disaster recovery.

The minimum end-to-end scenarios are: creator work provenance and license anchoring; digital-asset mint/list/purchase/transfer/royalty; cash-to-credit quote with separate 1% fee and mock funding; paid one-to-one competition entry, evidence, dispute, final result, settlement, credit-to-cash payout; cancellation/refund; chargeback after creator or winner earning; managed-wallet recovery; self-custody signing; validator/node restore; chain upgrade; and reconciliation from genesis/checkpoint to application statements.

Independent reviews are required before production qualification of consensus, modules, wallet/custody, signing, bridge, economic settlement, and public explorer privacy.

## 16. V1 Definition of Done

The domain is V1 build-complete when runnable nodes, selected consensus, deterministic runtime, native modules, general contract path, validator/governance operations, local/sandbox/testnet/production-candidate networks, managed/self/organization wallet modes, trusted signing, recovery, provenance, rights, digital assets, credits/token, competition commitments, escrow, settlement, indexer, explorer, provider bridges, reconciliation, monitoring, incidents, backup/restore, tests, and independent-review packages exist and integrate with the Artist Arena product.

Production activation may remain restricted by operator, region, identity, age, provider, limit, or audit. No blockchain capability may remain a paper-only future promise or an unlabeled placeholder.

## 17. Dependency-ordered work packages

1. Approve protocol scope, stable IDs, serialization, transaction/event envelopes, and state ownership.
2. Build deterministic runtime, state store, node skeleton, simulator, and network interfaces.
3. Evaluate and select consensus; implement fault, sync, upgrade, snapshot, and recovery behavior.
4. Implement identity, provenance, rights, and digital-asset native modules.
5. Implement credits/token, supply, treasury, policy, escrow, competition, settlement, and governance modules.
6. Implement managed, self-custodial, and organization wallet contracts plus trusted signing and recovery.
7. Implement application transaction gateway, outbox bridge, finality worker, indexer, explorer, and reconciliation.
8. Integrate marketplace, creator splits/royalties, paid entry, one-to-one stakes, pools, results, disputes, payouts, refunds, and chargebacks.
9. Operate persistent testnet, complete adversarial/load/recovery testing, external audits, and remediation.
10. Produce production-candidate network and activation dossier with explicit residual risk and approvals.

## 18. Open ADRs

Required ADRs cover chain framework and license; consensus/finality; validator and governance model; state/storage/pruning; deterministic serialization; native modules versus contract runtime; contract language and capability model; credit/token necessity and denomination; supply and treasury; transferability; bridge and reconciliation; wallet custody and recovery; key/signing infrastructure; privacy commitments; result-attestation authority; indexer/explorer architecture; upgrade/emergency pause; provider integration; fee/gas/resource metering; and mainnet/operator activation.
