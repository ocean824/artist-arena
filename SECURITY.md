# Artist Arena Security Policy

## Security posture

Artist Arena combines untrusted media and social content, real-time competition, creator rights, a financial ledger, credits, paid and wagering-compatible contests, payouts, wallets, and a native blockchain. Security, privacy, integrity, and economic correctness are release requirements rather than post-launch additions.

## Reporting a vulnerability

Do not disclose suspected vulnerabilities publicly through issues, discussions, social media, or competition content. Report them privately to the repository owner through an approved private channel. Include affected commit/version, environment, reproduction steps, expected and actual behavior, impact, and any safe supporting evidence. Do not include real credentials, identity documents, payment data, wallet secrets, unreleased media, or third-party personal information.

If the repository later enables GitHub private vulnerability reporting, use that mechanism. No public bug bounty, testing authorization, safe-harbor promise, response-time commitment, or payment program is created by this document.

## Prohibited handling

Production secrets, signing keys, custody keys, validator keys, payment credentials, identity-provider secrets, private user evidence, and personal data must never be committed, placed in prompts, pasted into issues, exposed in logs, or used in ordinary CI. Security testing uses local/sandbox/testnet environments and synthetic data unless the named owner explicitly authorizes a controlled alternative.

Do not probe production users, move value, access accounts, bypass authorization, exfiltrate data, perform destructive tests, publish exploit details, or attack providers without explicit written authorization defining scope and time.

## Required controls

| Boundary | Minimum control |
|---|---|
| Authentication and sessions | Passkeys/2FA where appropriate, secure cookies/tokens, rotation, revocation, step-up auth, recovery controls, device/session audit |
| Authorization | Server-side RBAC plus attributes, resource ownership, account state, age, jurisdiction, organization role, and policy version |
| Media and user content | Presigned upload, quarantine, checksum, scanning, validated types, bounded processing, derivative separation, signed reads, moderation and rights checks |
| API/provider webhooks | Schema validation, signature and timestamp verification, replay protection, idempotency, archived originals, normalized events, rate limits |
| Ledger and value | Integer units, immutable balanced journals, holds, compensating reversals, dual control, exact fee separation, reconciliation, audit |
| Blockchain and wallet | Deterministic modules, key separation, trusted signing, consensus/module audits, replay protection, upgrade/pause control, backup/restore |
| Supply chain | Locked dependencies, provenance, SBOM, license review, secret scan, vulnerability management, signed/reproducible artifacts |
| Agents and automation | Least privilege, isolated branches/worktrees, untrusted-content handling, no production keys, independent evidence and human review |

## Triage and response

Reports are classified by exploitability and impact to confidentiality, integrity, availability, user safety, competition fairness, rights, funds, custody, signing, consensus, or production control. Response preserves evidence; contains exposure; protects users and value; rotates/revokes affected authority; repairs and verifies; reconciles financial/chain state; restores service; communicates through authorized channels; and tracks corrective actions.

Immutable history is not rewritten to conceal an incident. Corrections use new audit records, ledger compensations, chain governance/recovery procedures, and documented data-remediation mechanisms.

## Release gates

Unresolved critical findings block the affected production activation. A blocked activation does not remove V1 construction: implementation, simulations, local/sandbox/testnet tests, audit preparation, and remediation continue. Security exceptions require a named approver, exact scope, expiration, compensating control, monitoring, and rollback.
