# Artist Arena V1 Competition Domain Specification

**Authority:** Derived from the preserved Artist Arena master specification and governed by Owner Directive 0001. All battle, challenge, tournament, season, ladder, team, prize, paid-entry, and wagering-compatible capabilities are mandatory V1 construction. Policy may restrict real-value activation, but it may not remove implementation or end-to-end testing.

## 1. Domain purpose

Competition is Artist Arena’s central product domain. It turns creative work into a structured, reviewable competitive record rather than a popularity contest. The domain owns the lifecycle of one-to-one battles, open challenges, ranked and unranked events, exhibitions, brackets, tournaments, seasons, ladders, team competitions, sponsored events, and participant-funded events across every supported discipline.

Music remains the first validation wedge, but the domain model is discipline-agnostic. Beat production, songs, rap/freestyle, vocals, dance, visual art, film/video, writing, gaming, coding, game-building, AI creation, streaming, digital media, and multimedia use common competition primitives with discipline-specific submission, media, evidence, judging, and scoring modules.

## 2. Non-negotiable rules

| Rule | Required behavior |
|---|---|
| Versioned rules | Every event points to an immutable ruleset version; publishing snapshots eligibility, scoring, timing, funding, disclosures, dispute terms, and tie-break rules |
| Locked software/content context | Event results reference the exact rules, submissions, media versions, disclosures, and system versions used to calculate them |
| Three AI divisions | Pure Human, Hybrid, and AI Open remain separate and transparently labeled; detection produces review signals, not automatic proof |
| Fair adjudication | Judge, audience, or mixed scoring uses a snapshotted scoring policy; conflicts, invalid votes, tie breaks, amendments, and appeals remain auditable |
| Private-before-reveal | Where blind judging or simultaneous reveal applies, one participant cannot inspect another participant’s submission before lock/reveal |
| Result before settlement | Money or credit settlement cannot occur until the result is final under the event’s dispute policy |
| Exact economic linkage | Every entry commitment, prize contribution, escrow hold, refund, release, payout, fee, and reversal references the event and ledger/chain records |
| Human authority | Automated systems may calculate and flag; material enforcement, disputed rights, and final high-risk actions retain authorized human review |
| No bought ranking | Paid promotion, sponsorship, and marketplace spend may not silently alter skill ratings or competitive records |

## 3. Actors and authorization

Competitors create or accept events, submit work, declare tools and rights, receive results, dispute outcomes, and earn eligible prizes. Organizers configure rules, schedules, divisions, judging profiles, prizes, and operational staff. Judges score only assigned submissions after declaring conflicts. Audience members vote only when the event policy permits them. Sponsors fund approved prize structures and receive campaign reporting without gaining undisclosed control over ratings. Moderators and trust analysts investigate reports, manipulation, rights, and integrity signals. Finance and compliance operators review holds, identity, jurisdiction, payouts, chargebacks, and reconciliation. Administrators manage configuration but cannot silently rewrite results or ledger history.

Every sensitive command evaluates RBAC plus attributes: account status, age status, identity level, jurisdiction, location confidence, contest eligibility, organization/team role, resource ownership, conflict declaration, moderation restrictions, wallet restrictions, self-exclusion, limits, feature activation, policy profile, and event state.

## 4. Canonical model

| Aggregate/entity | Responsibility |
|---|---|
| `Arena` | Logical competition venue or organizer context with policy and branding references |
| `RuleSet` / `RuleSetVersion` | Immutable event rules, eligibility, division, format, timing, scoring, funding, disclosure, cancellation, tie-break, and dispute policy |
| `Battle` | One-to-one or bounded-participant contest with lifecycle and participant slots |
| `Challenge` | Directed or open invitation that becomes a battle after acceptance and eligibility |
| `Tournament` | Multi-round event with entries, bracket nodes, seeding, advancement, and tournament-wide rules |
| `Season` | Time-bounded grouping of events, rating eligibility, memberships, and leaderboards |
| `BattleParticipant` / `TournamentEntry` | User/team participation, slot, eligibility result, acceptance, funding, and status |
| `Submission` | Creator work entry with media versions, finalization, disclosures, rights profile, and evidence references |
| `JudgeAssignment` / `JudgeConflict` | Authorized judging work and conflict declarations |
| `Ballot` / `Vote` / `JudgeScore` | Versioned evaluation input with eligibility and risk status |
| `ScoreCalculation` / `TieBreak` | Deterministic calculation inputs, algorithm version, intermediate results, and selected outcome |
| `ResultAttestation` | Provisional/final result, participants, evidence, signatures, ruleset/build references, and finality status |
| `Dispute` / `Appeal` | Reason, evidence, owner, deadlines, decision, amendment, and economic hold linkage |
| `RatingEvent` / `CompetitiveRecord` | Idempotent rating and public-record changes derived from an eligible final result |
| `EscrowHold` / `PrizePool` | Entry and prize funds reserved for the event across sponsor, platform, participant, or mixed sources |

All durable identifiers use the repository’s sortable-ID ADR. Events, rules, scoring algorithms, rating algorithms, and policy profiles carry explicit versions. Immutable financial, audit, vote, score, and result history is never soft-deleted; corrections use invalidation, amendment, or compensating records.

## 5. Competition classifications

An event declares its discipline, format, division, ranking effect, participation model, adjudication model, and economic profile.

| Dimension | V1 values |
|---|---|
| Format | One-to-one battle, open challenge, bracket tournament, ladder match, season event, team event, exhibition |
| Ranking | Ranked, unranked, exhibition; void events never update ratings |
| Division | Pure Human, Hybrid, AI Open |
| Adjudication | Judge-only, audience-only where allowed, mixed weighted, organizer panel, automated calculation with human review |
| Funding | Free, Arena Points, sponsor-funded, platform-funded, participant-funded, one-to-one stake, mixed prize pool |
| Entry | Invite, direct challenge, open entry, qualification, organizer selection, bracket advancement |
| Visibility | Public, unlisted, private/invite, embargoed until reveal |

The ruleset defines discipline-specific media, duration, file constraints, originality evidence, allowed tools, AI disclosure, submission deadline, reveal mode, score dimensions, judge qualifications, audience eligibility, tie break, dispute window, cancellation, disconnect, no-show, and settlement behavior.

## 6. Battle and challenge state machine

```text
DRAFT
→ PUBLISHED | CANCELLED
PUBLISHED
→ AWAITING_ACCEPTANCE | ENTRY_OPEN | CANCELLED | EXPIRED
AWAITING_ACCEPTANCE
→ ACCEPTED | DECLINED | WITHDRAWN | EXPIRED
ACCEPTED / ENTRY_OPEN
→ FUNDING_PENDING | SUBMISSION_OPEN | CANCELLED
FUNDING_PENDING
→ FUNDED | FUNDING_FAILED | CANCELLED
FUNDED
→ SUBMISSION_OPEN
SUBMISSION_OPEN
→ SUBMISSIONS_LOCKED | WITHDRAWN | CANCELLED | EXPIRED
SUBMISSIONS_LOCKED
→ REVEALED | JUDGING_OPEN | VOTING_OPEN
JUDGING_OPEN / VOTING_OPEN
→ CALCULATION_PENDING
CALCULATION_PENDING
→ PROVISIONAL_RESULT | MANUAL_REVIEW
PROVISIONAL_RESULT
→ DISPUTED | FINAL_RESULT
DISPUTED
→ UPHELD | AMENDED | VOID
UPHELD / AMENDED
→ FINAL_RESULT
FINAL_RESULT
→ SETTLEMENT_PENDING | SETTLED (non-value)
SETTLEMENT_PENDING
→ SETTLED | SETTLEMENT_REVIEW
```

Every transition records actor, time, prior/new state, command, correlation/causation IDs, policy/ruleset version, request ID, and reason. The server owns transitions. Client requests are commands, never authoritative state changes.

Cancellation and void rules are explicit by state. A pre-funding cancellation releases no money because no hold exists. A funded pre-start cancellation releases participant and sponsor holds according to policy. A mid-event failure may reschedule, refund, split, or escalate; it cannot silently settle. A dispute freezes affected settlement until resolution.

## 7. Tournament, season, and ladder behavior

Tournament publication snapshots format, entry policy, bracket size, seeding, byes, advancement, tie resolution, schedule, prize allocation, and cancellation plan. Bracket generation is deterministic from committed inputs and algorithm version. A node cannot advance until its source result is final or an authorized override creates a recorded amendment.

Seasons group rating pools, eligible events, membership, timeframe, and leaderboard rules. Leaderboards are reproducible snapshots, not mutable cached truth. Ladders use rating and eligibility policies while constraining repeated opponents, smurfing, latency, parties, region, queue time, and integrity risk. Matchmaking outputs the reasons and policy version without exposing internal fraud thresholds.

## 8. Submission, lock, reveal, and evidence

A submission begins as a draft linked to the participant and event. Media uploads use short-lived presigned URLs, multipart/resumable transfer, checksum verification, quarantine, scan, validation, and derived previews separate from originals. Finalization validates required assets, file/format rules, rights assertion, consent, division disclosure, tool disclosure, evidence bundle, and deadline.

Finalization creates an immutable snapshot of the submission and asset versions. After lock, edits require a new version only if the rules allow correction; prior versions remain retained. Blind events encrypt or authorization-gate access so competitors, public clients, and unauthorized staff cannot inspect content before reveal. Blockchain anchoring records hashes and compact commitments, not large media or private evidence.

Evidence may include creation-process artifacts, stems, source files, screen recordings, tool logs, consent records, licenses, and timestamps. Access is purpose-limited, logged, retained according to policy, and available to authorized review—not automatically public.

## 9. Judging, voting, scoring, and finality

Scoring templates define named dimensions, descriptions, range, weight, required feedback, and algorithm version. Event scoring config snapshots the template, judge/audience weighting, minimum ballot count, invalidation policy, tie-break sequence, and rounding rules.

Judge assignment requires authorization, conflict declaration, availability, and deadline. Scores are immutable after submission; permitted correction creates a superseding record with reason. Audience ballots enforce eligibility and one accepted vote per ballot/user while retaining duplicate, invalidated, and risk-marked attempts for audit. Fraud signals may reduce visibility or trigger review but do not erase history.

Calculation consumes the snapshotted policy and accepted inputs. It records each intermediate value, excluded input with reason, tie-break invocation, and algorithm version. The provisional result opens the configured dispute window. Finality requires the window to expire or all disputes to resolve. Rating and settlement consumers operate idempotently from the final result event.

## 10. Ratings, records, and reputation

Ratings are partitioned by discipline, format, division, and other approved pool dimensions. Glicko-2 is the source-recommended baseline, but the algorithm and parameters remain versioned. A rating event records before/after values, inputs, event result, pool, algorithm version, and idempotency key.

Free, paid, and sponsored status does not itself determine ranking eligibility. The event’s ranking classification and integrity profile do. Exhibition and void events never change ratings. Result amendments create compensating rating events rather than editing history. Public records distinguish wins/losses/draws, division, format, rating pool, opponent, finality, and void/amendment status.

Reputation is separate from skill. Reliability, judge quality, organizer operations, marketplace conduct, rights disputes, and policy compliance cannot be collapsed into a hidden score that changes competitive rank.

## 11. Paid entry, prizes, and one-to-one stakes

The competition domain requests economic actions but never writes balances directly. Before a funded event starts, the policy service evaluates operator, jurisdiction, location, age, identity, sanctions/risk results, self-exclusion, limits, wallet status, contest classification, funding source, currency/instrument, and ruleset. Approved participant and sponsor amounts become immutable escrow holds.

Prize pools support sponsor, platform, participant, and mixed contributions. Allocation is published before entry closes. One-to-one stake contests require symmetric or explicitly disclosed terms accepted by both participants. The system does not invent sportsbook odds; it implements skill-contest commitments governed by event and jurisdiction policy.

Settlement receives the final attestation, verifies event/rules/build/participants, confirms no active dispute or hold, calculates winner/prize/platform/creator/tax/provider postings, and commits one balanced journal. Idempotency and database/chain invariants prevent double payment. Cancellations, voids, refunds, reversals, chargebacks, payout holds, and negative-balance/reserve cases are explicit paths.

## 12. APIs and domain events

The source endpoint groups remain valid: battle create/list/get/update/publish/accept/withdraw/submit/finalize/cancel/timeline; judge assignments/scores; votes; results; disputes/evidence/appeal; tournament create/list/get/publish/enter/bracket/advance; ratings/rankings/seasons. The complete V1 adds explicit entry quote/commitment, pool status, contest policy evaluation, escrow status, attestation, settlement status, and chain-proof queries.

Representative events include `battle.created.v1`, `battle.published.v1`, `battle.accepted.v1`, `battle.funded.v1`, `submission.finalized.v1`, `battle.submissions_locked.v1`, `vote.cast.v1`, `judge_score.submitted.v1`, `battle.provisional_result_created.v1`, `battle.disputed.v1`, `battle.result_finalized.v1`, `battle.settled.v1`, `rating.updated.v1`, `tournament.bracket_generated.v1`, `escrow.held.v1`, and `escrow.released.v1`.

State mutation and outbox append occur in one database transaction. Consumers are idempotent and record delivery. `battle.settled` cannot publish before the authoritative ledger transaction commits.

## 13. Failure, abuse, and degraded modes

| Scenario | Required response |
|---|---|
| Duplicate command/webhook | Return the original result; do not repeat entry, score, rating, or settlement |
| Realtime service unavailable | Preserve canonical Postgres state; degrade live updates to polling; never move financial/result truth into ephemeral coordination |
| Media scan delayed | Keep submission unavailable and event in a bounded waiting/review state |
| Judge missing/deadline failure | Apply snapshotted replacement/quorum policy and disclose the operational change |
| Voting manipulation | Retain votes, mark risk/invalidation, recalculate transparently, and preserve appeal evidence |
| Integrity anomaly | Pause finality/settlement, retain replay and telemetry, open case, and require authorized review |
| Provider/chain outage | Preserve holds and pending state; retry idempotently; expose status; reconcile before completion |
| Conflicting result | Reject settlement, open incident/manual review, and protect the earlier canonical version |
| Harassment or rights claim | Limit visibility/contact as policy permits while preserving evidence and due process |

## 14. Observability and privacy

Metrics cover event creation-to-publication, acceptance, entry/funding, submission completion, no-show, judging time, vote validity, disputes, finalization, settlement, queue time, match quality, retention, and discipline/division health. Financial and final-result events are server authoritative. Logs contain correlation and state-transition identifiers but exclude raw identity documents, secrets, full payment payloads, private evidence, and unreleased submissions.

Dashboards separate product health from integrity. Growth never overrides invalid-vote rate, dispute rate, rights complaints, collusion, payout failure, minor safety, or reconciliation variance.

## 15. Test Gauntlet

The domain requires unit and property tests for transition legality, score determinism, rating determinism, bracket advancement, tie breaks, entry/escrow invariants, cancellation refunds, and duplicate processing. Integration tests cover Postgres transactions/outbox, policy, media, ledger, chain, notifications, and realtime. E2E tests cover free, Arena Points, sponsor-funded, participant-funded, mixed-pool, and one-to-one stake events.

Required adverse cases include concurrent acceptance, deadline races, duplicate votes, conflict disclosure, malformed media, late finalization, judge loss, insufficient quorum, tie, disconnect, no-show, suspected cheating, rights claim, dispute, appeal, amended result, void, provider timeout, chain finality delay, duplicate settlement message, and chargeback after payout.

## 16. V1 Definition of Done

Competition is V1 build-complete when every format and division has executable workflows; discipline templates cover the entire product taxonomy; all states and transitions are server-authoritative and audited; media lock/reveal works; judging/voting/results/ratings are deterministic and versioned; tournaments/seasons/ladders/teams operate; free and every value-bearing funding profile completes end to end in safe environments; blockchain commitments and attestations reconcile; moderation, rights, fraud, disputes, appeals, notifications, observability, and operations are integrated; and the applicable Gauntlet evidence is approved.

Activation may remain region-, operator-, provider-, age-, identity-, limit-, or assurance-restricted. No described competition capability may remain an unlabeled stub or be moved to a later product version.

## 17. Dependency-ordered work packages

1. Define stable IDs, ruleset versions, policy context, event envelopes, and audit schema.
2. Implement battle/challenge aggregates and transition engine.
3. Implement media submission, finalization, lock, reveal, and evidence access.
4. Implement scoring templates, judge assignments/conflicts, ballots, votes, and calculation.
5. Implement provisional/final results, disputes, appeals, amendments, and voids.
6. Implement rating pools/events, records, leaderboards, ladders, and seasons.
7. Implement tournament brackets, advancement, teams, rosters, and organizer operations.
8. Integrate realtime rooms, presence, live scoring, chat policy, streaming, replay, and notifications.
9. Integrate eligibility, credits, entry commitments, prize pools, one-to-one stakes, escrow, settlement, and reconciliation.
10. Integrate provenance, blockchain commitments, result attestations, indexer/explorer, and operator evidence.
11. Complete anti-cheat, vote/fraud/collusion controls, moderation, rights, support, and compliance console.
12. Run full functional, economic, security, load, fault, recovery, and production-readiness Gauntlet.

## 18. Open ADRs

Open decisions include the exact launch and per-discipline templates; rating parameters and pool partitioning; judge/audience weighting profiles; bracket/seeding algorithms; tie-break order; blind/reveal rules; replay/integrity evidence; native streaming architecture; paid-contest legal/operator profiles; geolocation/KYC/payment providers; responsible-participation limits; credit denomination and transferability; entry/prize fee policies; settlement finality; chain attestation format; and appeal fees or deposits. These decisions remain configurable and visible; they do not remove implementation work.
