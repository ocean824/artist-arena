# Contributing to Artist Arena

This is a private, proprietary repository. Contributions are accepted only from authorized collaborators and remain subject to the repository’s ownership and confidentiality terms.

## Required workflow

Begin with a dependency-valid `AA-####` ticket from [`docs/backlog/v1-160-tickets.md`](docs/backlog/v1-160-tickets.md). Read the owner directive, canonical source, linked requirements, domain specifications, affected ADRs, `CODESPRING.md`, `AGENTS.md`, and current project memory. Create a short-lived branch from `develop` and use an isolated worktree for parallel agent work.

| Change | Required branch pattern |
|---|---|
| Feature | `feature/AA-####-short-description` |
| Fix | `fix/AA-####-short-description` |
| Security | `security/AA-####-short-description` |
| Documentation | `docs/AA-####-short-description` |
| Experiment | `spike/AA-####-short-description` |

Do not commit directly to `main`, `staging`, or `develop`; force-push a shared branch; rewrite another contributor’s changes; or merge your own consequential change without independent review.

## Work-package minimum

Every pull request states objective, requirements, dependencies, scope/exclusions, affected files, states, APIs/schemas/events/migrations, security/privacy/rights/economic impact, activation effect, observability, acceptance criteria, tests, evidence, migration, rollback, and residual risk. The pull-request template is mandatory.

## Engineering rules

Use strict TypeScript for web packages. Preserve module dependency direction. Keep domain logic out of transport handlers and UI. Use typed IDs, UTC instants, integer money/credit units, explicit instruments, immutable double-entry journals, idempotent mutations, transactional outbox/inbox, server authorization, provider adapters, versioned states/contracts, and forward-compatible migrations.

The native blockchain, wallet, credits, 1% conversion fee, paid entry, one-to-one credit wagers, prize pools, escrow, settlement, cash-out, mobile, streaming, public API, all disciplines, and providers are V1 build scope. Do not replace them with future TODOs because activation is restricted.

## Verification

Run `pnpm validate:repo`, `pnpm lint`, `pnpm typecheck`, `pnpm test`, and `pnpm build`, plus every domain-relevant Gauntlet stage. Economic, chain, wallet, competition, policy, rights, privacy, and moderation work requires failure, concurrency, idempotency, authorization-negative, recovery, and reconciliation tests.

Attach reproducible evidence. Update requirements, ADRs/RFCs, schemas, OpenAPI, events, migrations, risk, runbooks, and `.agents/PROJECT_MEMORY.md` when affected.

## Reviews

Shared contracts require domain-owner review. Financial, chain, wallet, signing, consensus, paid-contest, identity/location, minors, rights, moderation, security, privacy, production-policy, and public-release changes require named independent human review. No agent approves its own exception or production activation.

## Confidentiality and provenance

Do not copy unlicensed code, media, likeness, UI, or proprietary material. Record source, license, modifications, generated content, model/tool use, and redistribution rights. Do not put secrets or personal data into commits, issues, tests, fixtures, or logs. Use deterministic fictional content for development and tests.
