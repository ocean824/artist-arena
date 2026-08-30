ARTIST ARENA

Manus → GitHub → CodeSpring → Traycer Master Repository Specification

Version: 1.0
Founder / Product Owner: Ø
Document status: Governing product-and-repository brief
Repository target: artist-arena
Primary product thesis: The competitive infrastructure layer for the global creator economy.

────────

0. MANUS: READ THIS FIRST

You are not being asked to produce a generic social-media mockup, a landing page, or a loose collection of product ideas.

You are being asked to create a private, GitHub-ready, implementation-ready Artist Arena repository that Ø can hand directly to CodeSpring and continue building through Traycer.

The repository must contain:

1. A normalized product specification.
2. A clear distinction between:
  • locked founder decisions;
  • recommended defaults;
  • compliance-gated capabilities;
  • unresolved decisions.
3. A production-minded monorepo scaffold that installs, type-checks, tests, and builds.
4. Stable domain boundaries and interfaces.
5. Database schemas and migrations sufficient for the first vertical slice.
6. API contracts sufficient for CodeSpring to implement without guessing.
7. Security, privacy, moderation, ledger, rights, and compliance architecture from the beginning.
8. A phased backlog with dependencies, acceptance criteria, and tests.
9. Persistent agent instructions for Manus, Traycer, CodeSpring, Codex, Claude, and other workers.
10. GitHub issues, milestones, labels, project-board structure, CI workflows, branch protections, and ownership rules wherever your GitHub permissions allow.

Do not silently redesign the concept. Do not remove the original credit economy merely because it is regulated. Preserve it as a first-class product capability, but place all cash-convertible credits, paid entry, wagering, prize settlement, and cash-out behind explicit compliance, jurisdiction, identity, provider, and founder-approval gates.

Do not enable production real-money functionality. Build the abstractions, schemas, sandbox flows, feature flags, policy engine, auditability, and tests required to activate it later after counsel and payment-provider approval.

Do not invent credentials, API keys, legal clearance, licenses, or completed integrations. Never commit secrets. Never expose secrets to model prompts or logs.

If a repository already exists, inspect it fully before changing it. If no repository exists, create a new private repository named artist-arena. If the exact name is unavailable, preserve artist-arena as the project slug and report the repository-name conflict instead of silently renaming the product.

GitHub is the source of truth for code, approved specifications, schemas, architectural decisions, issues, pull requests, milestones, changelogs, release tags, and CI evidence.

────────

1. RECOVERED PRODUCT CANON

1.1 Locked founder decisions

The following requirements come from Ø’s prior Artist Arena direction and must be treated as product canon unless Ø later changes them.

Product identity

• The product is named Artist Arena.
• Artist Arena began as an app for beat battles and song battles.
• It has since expanded into a much larger creator-economy platform connecting competition, discovery, community, commerce, sponsorship, scouting, and creator infrastructure.
• Its long-term position is: the competitive infrastructure layer for the global creator economy.

Original battle economy

Artist Arena must be architected to support:

• users buying credits;
• users using credits to enter battles;
• users wagering credits one-to-one against opponents;
• users paying creators for access to their work;
• users converting eligible credits or earnings back into cash;
• Artist Arena charging a 1% fee on credit-to-cash and cash-to-credit conversion;
• battle funds being reserved before a paid battle begins;
• settlement only after the result is final;
• disputes, refunds, reversals, chargebacks, payout holds, and audit trails.

The 1% conversion fee is a locked product default, but it must be configuration-driven rather than hardcoded. Third-party payment-processing, identity-verification, tax, currency-conversion, chargeback, or regulated-provider costs must be represented separately and disclosed transparently.

Creator disciplines

The platform vision spans:

• music;
• beat production;
• songs and songwriting;
• rap and freestyle;
• vocal performance;
• dance;
• visual art and design;
• film and video;
• writing;
• gaming and interactive creation;
• coding;
• game-building competitions;
• AI creators;
• producers;
• streamers;
• digital media;
• multimedia work.

The architecture must be discipline-agnostic, even though the recommended launch wedge is music-first.

Platform capabilities already associated with Artist Arena

Artist Arena must be able to grow into a platform for:

• creator profiles;
• portfolio and work discovery;
• one-to-one battles;
• open challenges;
• ranked ladders;
• brackets and tournaments;
• seasons;
• livestream and replay integrations;
• audience voting and participation;
• judge panels;
• rankings and competitive records;
• sponsorships;
• sponsored challenges and prize pools;
• subscriptions and premium memberships;
• creator commissions;
• creator marketplaces;
• creator services;
• digital events;
• creator analytics;
• audience-growth infrastructure;
• scouting and talent discovery;
• creator monetization;
• community engagement.

AI creator policy

Artist Arena must not ban AI creators.

Competitions must support three clearly separated and transparently labeled divisions:

1. Pure Human
  • Prestige and craftsmanship division.
  • Generative creation is not allowed.
  • Ordinary non-generative production, editing, mixing, mastering, color correction, cleanup, and accessibility tools may be allowed when the discipline rulebook permits them.
2. Hybrid
  • AI-assisted work is allowed.
  • Human direction, selection, editing, performance, assembly, or transformation remains material.
  • Tools, workflow categories, and the role of AI must be disclosed.
3. AI Open
  • Broad generative and automated workflows are allowed.
  • Rights, consent, provenance, impersonation, and platform-safety rules still apply.
  • “Open” does not mean exempt from copyright, likeness, fraud, or abuse rules.

AI must supplement rather than replace human judging. Detection systems may produce signals, request evidence, or flag inconsistencies, but must not be presented as infallible proof.

Strategic ecosystem role

Artist Arena is the consumer-network and creator-acquisition layer in Ø’s broader technology ecosystem. It should be able to connect over time with creative tools such as Sonara/Orpheus, gaming infrastructure such as REAI/AXIOM, and model-agnostic agent infrastructure, while remaining independently usable and not making those other systems mandatory dependencies for V1.

────────

1.2 Recommended launch interpretation

The following are recommended product decisions for V1. They are not allowed to contradict the locked canon.

Launch wedge

Launch with a music-first vertical slice:

• beat battles;
• song battles;
• rap/freestyle battles;
• music-focused creator profiles;
• audio uploads;
• community and judged competition;
• rankings;
• basic discovery;
• a basic creator marketplace;
• sandbox credits and ledger.

Dance and video-heavy categories should follow once the media pipeline, moderation, playback, and cost controls are proven. Visual art, film, writing, code, and game-building then plug into the same competition primitives through discipline-specific rule and scoring templates.

Platform order

Build in this order:

1. Prove the battle loop.
2. Prove fair adjudication.
3. Prove creator identity, profiles, and discovery.
4. Prove rankings and retention.
5. Prove marketplace commerce.
6. Prove sponsored challenges.
7. Prove the regulated wallet and real-money contest flow only after external approval.
8. Expand disciplines.
9. Add native livestreaming and native mobile applications later.

Client strategy

• V1 should be a responsive web application and installable PWA.
• Architect shared contracts and design tokens so native iOS/Android clients can be added without rewriting the backend.
• Do not make mobile app-store distribution a V1 launch dependency.
• External livestream embeds or integrations may precede native streaming.

────────

2. PRODUCT VISION

2.1 Vision statement

Artist Arena is where creators compete, prove skill, build a public record, earn, get discovered, find collaborators, win opportunities, and turn audience attention into durable economic value.

It combines elements normally scattered across creator subscriptions, livestreaming, community platforms, short-form discovery, tournament infrastructure, freelance marketplaces, portfolio networks, and talent scouting—but centers them around a verified competitive record.

Artist Arena should feel like a legitimate arena for creativity, not a popularity contest wearing tournament graphics.

2.2 Core promise

For creators:

> Your work should be able to compete, accumulate proof, attract opportunity, and earn without requiring preexisting industry access.

For audiences:

> Discover talent through meaningful creative competition, not only follower counts and opaque algorithms.

For sponsors and scouts:

> Find creators through structured evidence—discipline, consistency, results, rankings, originality, reliability, audience response, and verified work.

2.3 Product pillars

1. Compete — battles, challenges, tournaments, seasons, and ladders.
2. Prove — transparent records, ratings, judge feedback, provenance, and process evidence.
3. Discover — feeds, search, categories, rising talent, live events, and curator channels.
4. Earn — prizes, marketplace sales, subscriptions, commissions, services, licensing, and sponsorship.
5. Connect — follows, comments, teams, collaborators, judges, scouts, sponsors, and organizers.
6. Protect — rights controls, consent metadata, secure submissions, fraud controls, moderation, disputes, and appeals.
7. Include the future — Pure Human, Hybrid, and AI Open competition without pretending the three are identical.

2.4 Non-goals for V1

V1 is not:

• a generic TikTok clone;
• a generic Discord clone;
• a full DAW;
• a full video editor;
• a native blockchain economy;
• an NFT marketplace;
• a global unlicensed wagering operation;
• an automated AI judge;
• a fully native livestreaming provider;
• a replacement for every creator storefront;
• a permissionless peer-to-peer money-transfer service;
• a platform where paid promotion can buy skill ranking;
• a platform that trains models on creator work by default.

────────

3. USERS, ROLES, AND PERMISSIONS

3.1 Primary personas

Competitor creator

Creates a profile, uploads work, enters battles, accepts challenges, receives ratings and feedback, earns prizes, sells work, and builds a competitive portfolio.

Audience member / fan

Follows creators, watches or listens, votes where eligible, comments, shares, buys access or products, subscribes, and attends digital events.

Buyer / client

Purchases digital products, licenses work, orders services, commissions creators, or pays for gated access.

Judge / curator

Scores submissions against disclosed criteria, leaves structured feedback, declares conflicts, and builds a judge reputation.

Organizer

Creates battles, tournaments, seasons, rule sets, eligibility rules, judge panels, schedules, and prize structures.

Sponsor / brand

Creates branded briefs and sponsored competitions, funds prizes, supplies official rules, selects judges, receives campaign analytics, and discovers creators.

Scout / recruiter / A&R

Searches talent by discipline, division, rating, consistency, location where voluntarily shared, availability, verified work, and other permitted attributes; creates private shortlists and sends contact requests.

Team / collective

Operates a shared identity, roster, portfolio, tournament entries, permissions, and revenue splits.

Moderator / trust analyst

Reviews reports, rights claims, fraud signals, vote anomalies, identity issues, appeals, and disputes.

Finance / compliance operator

Reviews payout holds, verification, chargebacks, reconciliation, restricted jurisdictions, sanctions results, tax records, and ledger exceptions.

Administrator

Manages platform configuration, feature flags, discipline templates, policies, staff permissions, and audit review. No administrator should be able to alter the financial ledger silently.

3.2 RBAC and ABAC

Implement role-based access control with attribute and policy checks.

Roles include:

• user
• creator
• verified_creator
• judge
• organizer
• sponsor_member
• scout
• team_member
• team_admin
• moderator
• trust_analyst
• finance_operator
• compliance_operator
• support_agent
• admin
• super_admin

Sensitive actions must also evaluate:

• account status;
• age status;
• verification status;
• jurisdiction;
• contest eligibility;
• organization membership;
• resource ownership;
• conflict-of-interest declarations;
• moderation restrictions;
• wallet restrictions;
• feature flags;
• policy profile.

────────

4. PRODUCT SURFACES AND INFORMATION ARCHITECTURE

4.1 Primary desktop navigation

• Discover
• Battles
• Tournaments
• Rankings
• Live
• Marketplace
• Search
• Notifications
• Wallet
• Profile

A persistent primary action should allow eligible users to:

• create a battle;
• issue a challenge;
• enter an open event;
• upload a work;
• create a listing.

4.2 Recommended routes

```text
/
 /discover
 /discover/[discipline]
 /arena
 /battles
 /battles/new
 /battles/[battleId]
 /battles/[battleId]/submit
 /battles/[battleId]/judge
 /tournaments
 /tournaments/[tournamentId]
 /seasons
 /rankings
 /rankings/[discipline]
 /live
 /marketplace
 /marketplace/[listingId]
 /commissions
 /studio
 /studio/uploads
 /studio/submissions
 /studio/listings
 /studio/analytics
 /teams
 /teams/[teamSlug]
 /sponsors
 /sponsors/campaigns
 /scout
 /profile/[handle]
 /settings
 /wallet
 /wallet/activity
 /wallet/verification
 /support
 /rules
 /admin
```

4.3 Mobile navigation

Recommended bottom navigation:

• Home
• Battles
• Create
• Live
• Profile

Wallet, rankings, marketplace, search, and notifications remain one tap away through the header or profile sheet.

4.4 UI direction

Create a premium, cinematic, creator-forward interface with competitive energy.

Avoid:

• generic “AI SaaS” gradients;
• a casino visual language;
• misleading win animations around financial activity;
• oversaturated gamer neon everywhere;
• template-looking cards with no editorial hierarchy;
• follower counts dominating skill evidence.

The visual system should balance:

• high-end music and fashion editorial design;
• tournament clarity;
• strong motion and live-state feedback;
• accessible contrast;
• dense desktop utility;
• clean mobile interaction;
• discipline-specific art direction without fragmenting the product.

Create a tokenized design system supporting:

• dark default theme;
• accessible light theme;
• discipline accents;
• sponsor themes constrained by accessibility and brand-safety rules;
• reduced-motion preferences;
• keyboard and screen-reader use;
• WCAG 2.2 AA.

────────

5. THE CORE COMPETITION MODEL

5.1 Canonical vocabulary

Discipline

A creative field such as beat production, songwriting, rap, dance, visual art, film, writing, code, or game building.

Division

The allowed creation-method class:

• Pure Human
• Hybrid
• AI Open

Format

The media and submission structure:

• audio;
• video;
• image;
• text;
• code repository;
• playable build;
• live performance;
• mixed media.

Battle

A direct competitive event, usually one-to-one, producing a result.

Challenge

A brief-based competition that may be one-to-one, open-entry, sponsor-funded, or bounty-based.

Tournament

A multi-participant event with brackets, groups, Swiss rounds, ladders, or judged rounds.

Season

A bounded competitive period with ratings, divisions, qualification, rewards, and reset or carryover rules.

Arena

A configured competitive context combining discipline, division, rules, eligibility, scoring, and ranking policy.

Submission

A version-locked work entered into a battle or event.

Result attestation

The final signed record of entrants, rules, scores, winner, evidence, disputes, settlement, and rating effects.

5.2 Competition types

V1 domain architecture must support:

1. Direct challenge
  • Creator A challenges Creator B.
  • Public or private.
  • Ranked or unranked.
  • Free, points-based, sponsored, or compliance-gated paid mode.
2. Open one-to-one battle
  • A creator posts a challenge.
  • An eligible opponent accepts.
3. Community battle
  • Audience-led outcome.
  • Usually unranked or lower-stakes.
4. Ranked battle
  • Uses approved rules, adjudication, anti-fraud controls, and rating impact.
5. Judge-panel battle
  • Structured scoring by approved judges.
6. Hybrid judged battle
  • Judge score plus eligible audience vote.
7. Open challenge
  • Multiple creators answer a brief.
  • Finalists may be selected before a final round.
8. Bracket tournament
  • Single elimination, double elimination, round robin, groups-to-bracket, or Swiss.
9. Sponsored challenge
  • Brand or partner supplies the brief and secured prize pool.
10. Bounty
  • A client or sponsor pays for the best qualifying solution under explicit rights terms.
11. Exhibition
  • No ranking or financial consequence.
12. Team battle
  • Collective entries and approved split definitions.

5.3 Battle lifecycle

Implement a validated state machine. No client may assign states directly.

```text
DRAFT
  → PUBLISHED
  → MATCHING
  → ACCEPTED
  → FUNDING_PENDING       [only when applicable]
  → FUNDED                [only when applicable]
  → SUBMISSION_OPEN
  → SUBMISSIONS_LOCKED
  → REVIEW_PENDING
  → VOTING_OPEN and/or JUDGING_OPEN
  → SCORING
  → PROVISIONAL_RESULT
  → DISPUTE_WINDOW
  → FINAL
  → SETTLEMENT_PENDING    [only when applicable]
  → SETTLED
  → ARCHIVED
```

Exceptional terminal or side states:

```text
CANCELLED
EXPIRED
VOIDED
DISPUTED
UNDER_REVIEW
REFUND_PENDING
REFUNDED
PAYOUT_HELD
```

Every transition must include:

• actor;
• timestamp;
• previous state;
• next state;
• reason code;
• policy evaluation;
• idempotency key where relevant;
• audit event;
• resulting jobs/events.

5.4 Submission fairness

• Entrants must not see an opponent’s hidden submission before both submissions lock unless the rule set explicitly allows sequential response.
• Record content hash, object version, upload completion time, and finalization time.
• An entrant may save drafts but only the final locked version is judged.
• Late submission rules must be explicit.
• Replacements after lock require a documented administrator action and visible audit reason.
• Private unreleased work must use short-lived signed access and access logging.
• Public previews may be watermarked or transcoded separately from master files.
• Original masters must never be used for model training without explicit opt-in.

5.5 Rule templates

Every event must use a versioned rule set containing:

• discipline;
• division;
• format;
• prompt or brief;
• allowed tools;
• prohibited tools;
• duration or size limits;
• required source/process evidence;
• eligibility;
• entry mode;
• stake or prize mode;
• submission window;
• judging window;
• voting window;
• scoring dimensions;
• tie policy;
• conflict-of-interest policy;
• rights and license terms;
• conduct rules;
• dispute window;
• settlement conditions;
• jurisdiction policy;
• version number.

Published events must snapshot the rule version. Later edits must not retroactively change an active event without a formal amendment visible to entrants.

5.6 Scoring templates

The scoring engine must be configurable by discipline and event.

Recommended initial templates:

Beat production

• musicality;
• originality;
• sound selection and design;
• arrangement;
• mix/presentation;
• response to brief.

Song

• songwriting;
• performance;
• production;
• originality;
• emotional impact;
• response to brief.

Rap / freestyle

• writing or improvisation;
• flow;
• delivery;
• originality;
• performance;
• response to prompt.

Dance

• technique;
• choreography;
• musicality;
• execution;
• originality;
• camera-rule compliance.

Visual art

• concept;
• craft;
• composition;
• originality;
• communication;
• response to brief.

Film / video

• story;
• direction;
• cinematography;
• editing;
• sound;
• originality;
• response to brief.

Writing

• concept;
• structure;
• language;
• voice;
• originality;
• brief compliance.

Code / game building

• functionality;
• automated test performance where applicable;
• architecture and maintainability;
• UX or gameplay;
• performance;
• originality;
• brief compliance;
• security.

Scoring dimensions must use integer or fixed-precision values. Never use floating-point money. Store raw scores, normalized scores, weights, judge identity, conflicts, comments, timestamps, and calculation version.

5.7 Recommended adjudication profiles

Do not hardcode one universal formula.

Provide system templates:

• COMMUNITY_100
• JUDGES_100
• HYBRID_70_30
• HYBRID_60_40
• OBJECTIVE_PLUS_JUDGES
• SPONSOR_PANEL
• PLATFORM_FINALS

Recommended defaults:

• Casual community battle: audience vote.
• Ranked battle: verified judges with a limited trust-weighted audience component.
• High-value final: judge panel plus fraud-reviewed audience component.
• Code/game challenge: automated validation plus human scoring.
• Sponsor event: organizer-defined within platform policy limits.

5.8 Voting integrity

Implement:

• one eligible vote per account per ballot;
• email verification minimum;
• stronger verification for high-impact votes;
• rate limits;
• bot challenges;
• account-age and trust signals;
• duplicate-device and network anomaly signals;
• vote velocity analysis;
• collusion-graph signals;
• no public exposure of private fraud signals;
• append-only vote records;
• recount tooling;
• invalidation reason codes;
• human review and appeal for material outcomes.

Do not secretly turn follower count, spend, or subscription level into vote weight.

5.9 Ties and finality

Each rule set must define:

• tie-break dimension;
• head judge or runoff policy;
• overtime/resubmission policy;
• random selection prohibition for ranked skill outcomes unless legally and explicitly approved;
• final dispute deadline;
• result finality timestamp.

A financial settlement cannot execute before result finality and required hold windows.

────────

6. RATINGS, RANKS, REPUTATION, AND LEADERBOARDS

6.1 Separate skill from popularity

Artist Arena must not collapse every signal into one opaque number.

Maintain separate systems:

1. Skill rating
  • Based on approved ranked results.
  • Recommended initial algorithm: Glicko-2 or an equivalent uncertainty-aware rating model.
  • Separate by discipline, division, format, and season where appropriate.
2. Competitive record
  • Wins, losses, draws, placements, judge-score history, opponent strength, event tier.
3. Reputation
  • Completion rate, cancellations, disputes, upheld violations, on-time delivery, marketplace reliability, judge reliability.
4. Audience
  • Followers, views, saves, shares, engagement.
5. Commerce
  • Sales, repeat buyers, fulfillment quality, review quality.
6. Credential / verification
  • Identity, role, judge approval, sponsor status, organization status, skill verification.

Paid promotion may increase visibility only in clearly labeled placements. It must never directly increase skill rating.

6.2 Rating requirements

• placement period for new competitors;
• rating deviation or uncertainty;
• inactivity handling;
• provisional rating;
• seasonal carryover/reset policy;
• minimum match count for public rank;
• anti-smurf checks;
• voided results excluded;
• disputed results held;
• event-tier multipliers only through approved policy;
• no direct administrator editing without a corrective ledger-style event and audit reason;
• rating recalculation tools;
• deterministic algorithm versioning.

6.3 Leaderboards

Support:

• global;
• regional where voluntarily shared and legally permitted;
• discipline;
• division;
• format;
• season;
• rising creators;
• teams;
• judges;
• sponsor-event standings.

“Rising” must use an explainable formula that resists manipulation and does not simply restate total followers.

────────

7. AI DIVISIONS, DISCLOSURE, AND PROVENANCE

7.1 Disclosure labels

At minimum support:

• HUMAN_MADE
• AI_ASSISTED
• AI_HYBRID
• FULLY_GENERATIVE

For each submission, optionally collect:

• tools used;
• model names;
• generation type;
• estimated workflow share;
• automation depth;
• human performance elements;
• human editing elements;
• source ownership;
• training/voice/likeness consent assertions;
• process notes;
• evidence bundle.

Do not present a self-reported percentage as scientific fact. Store it as creator disclosure.

7.2 Process evidence

Depending on event level and discipline, request:

• DAW project screenshots or exported session manifest;
• stems;
• MIDI or score;
• raw vocal or performance takes;
• screen recording;
• edit timeline;
• source files;
• layer history;
• source-control history;
• build logs;
• prompt/workflow log;
• model and seed metadata;
• camera originals;
• content credentials where available.

Evidence may be private to reviewers. Create a secure evidence vault with:

• least-privilege access;
• time-limited review;
• access logs;
• retention rules;
• hashes;
• redaction support;
• deletion policy.

7.3 Detection policy

AI and provenance detection:

• may generate risk signals;
• may request more evidence;
• may prioritize human review;
• may compare disclosure to metadata;
• may identify obvious inconsistencies.

It must not:

• claim perfect accuracy;
• automatically confiscate funds solely from a probabilistic detector;
• publish an accusation without review;
• penalize a creator for using permitted tools;
• replace the appeal process.

7.4 Rights and training consent

Every uploaded asset must include creator-controlled metadata for:

• public display;
• download;
• remix permission;
• derivative permission;
• commercial licensing;
• platform promotional use;
• AI training permission;
• third-party model training permission;
• voice/likeness use;
• expiration or revocation where legally supported.

Default:

• No AI training unless the creator opts in through a specific, informed permission.
• Platform display rights must be limited to operating and promoting the service under the terms.
• Sponsor usage rights must be explicit in the event rules before entry.

────────

8. CREATOR PROFILES AND PORTFOLIOS

8.1 Profile fields

• display name;
• unique handle;
• profile image and banner;
• bio;
• disciplines;
• creator roles;
• division participation;
• optional location;
• languages;
• links;
• availability;
• commission status;
• collaboration status;
• portfolio;
• featured work;
• competitive record;
• current ratings;
• season ranks;
• trophies and placements;
• judge feedback summaries;
• marketplace listings;
• subscriptions;
• teams and affiliations;
• verification badges;
• AI disclosure summary;
• rights preferences;
• contact-request settings.

8.2 Profile privacy

Users choose visibility for:

• legal name;
• location;
• contact information;
• earnings;
• private portfolio items;
• evidence bundles;
• team membership where permitted;
• marketplace availability.

KYC data must never appear in public profile tables.

8.3 Verification

Separate:

• email verified;
• phone verified;
• identity verified;
• payout verified;
• age verified;
• professional credential verified;
• organization verified;
• judge verified.

Never show “verified” without identifying what was verified.

────────

9. DISCOVERY, FEEDS, LIVE, AND COMMUNITY

9.1 Discover surface

Include:

• live battles;
• upcoming battles;
• open challenges;
• tournaments;
• rising creators;
• top-ranked creators;
• new work from followed creators;
• sponsor briefs;
• marketplace releases;
• curated collections;
• Pure Human, Hybrid, and AI Open filters;
• discipline filters;
• local or regional filters only when opted in.

9.2 Recommendation principles

• optimize for meaningful discovery and event completion, not only watch time;
• give new creators controlled exploration exposure;
• avoid reinforcing existing follower dominance;
• provide “why am I seeing this?” explanations;
• label sponsored placement;
• allow content and discipline controls;
• record recommendation version for experiments;
• exclude protected attributes from ranking;
• audit for manipulation and disparate effects.

9.3 Social capabilities

V1:

• follow/unfollow;
• comments;
• threaded replies;
• reactions;
• bookmarks;
• shares;
• reports;
• event chat only if moderation is ready;
• notifications;
• activity feed.

Later:

• direct messages;
• group chats;
• guilds/collectives;
• watch parties;
• collaboration rooms;
• native live streaming.

Do not ship direct messages before blocking, reporting, rate limits, attachment safety, and moderation workflows exist.

9.4 Live and replay

V1 may support:

• embedded external livestreams;
• scheduled live event pages;
• live scoring updates;
• chat with moderation;
• replay links;
• clips and highlights;
• battle timeline;
• judge commentary.

Native live streaming is a later provider-adapter capability. The core domain must not assume one video vendor.

────────

10. MARKETPLACE, ACCESS, SERVICES, AND LICENSING

10.1 Marketplace purpose

The original vision includes paying creators for access to their work. Implement this through a general entitlement and commerce system, not an ambiguous transfer field.

Supported listing classes should include:

• digital download;
• gated stream or view access;
• subscription access;
• beat or instrumental license;
• stems;
• sample packs;
• presets;
• artwork and design assets;
• video assets;
• code templates;
• game assets;
• tickets and event access;
• commission/service;
• consultation;
• custom deliverable;
• sponsorship package;
• approved commercial license.

10.2 Orders and entitlements

Each purchase must create:

• order;
• order line;
• payment intent/reference;
• entitlement or service contract;
• tax metadata;
• creator split;
• platform fee;
• refund policy;
• delivery state;
• audit events.

Do not grant access from a client-side “paid” flag. Grant from verified server-side settlement or approved provisional policy.

10.3 Commissions and services

Support:

```text
INQUIRY
→ QUOTED
→ ACCEPTED
→ FUNDED
→ IN_PROGRESS
→ DELIVERED
→ REVISION
→ ACCEPTED_BY_BUYER
→ SETTLED
```

Exceptional states:

```text
CANCELLED
DISPUTED
REFUND_PENDING
REFUNDED
PAYOUT_HELD
```

Model:

• brief;
• scope;
• milestones;
• price;
• due dates;
• included revisions;
• deliverables;
• rights/license;
• private files;
• acceptance window;
• dispute evidence;
• split recipients.

10.4 Revenue configuration

Known:

• 1% conversion fee on eligible cash/credit conversion.

Open and configuration-driven:

• marketplace commission;
• subscription plans;
• premium creator tools;
• organizer fees;
• sponsored-event service fees;
• advertising/promoted placement;
• ticketing fee;
• payout fee;
• optional analytics products.

Do not invent final rates. Create a versioned fee-policy table and an ADR documenting each provisional default.

────────

11. WALLET, CREDITS, ESCROW, AND FINANCIAL LEDGER

11.1 Critical design rule

Never represent money by updating a single mutable user.balance field.

Implement a double-entry, append-only ledger with:

• accounts;
• journal entries;
• postings;
• asset/currency code;
• fixed-precision minor units;
• idempotency keys;
• references to source events;
• reversals rather than deletion;
• reconciliation status;
• provider references;
• audit metadata.

Cached balance projections are allowed, but the ledger remains canonical.

11.2 Separate economic instruments

Do not commingle every unit under one “credits” balance.

Model at minimum:

1. Arena Points
  • Promotional or earned.
  • Non-transferable.
  • Non-withdrawable.
  • Useful for onboarding, free competition, progression, and testing.
2. Purchased Credits
  • Only activated where legally and operationally approved.
  • Rules must define redemption and transfer restrictions.
  • Cannot be enabled by a developer toggling a UI flag.
3. Creator Earnings
  • Proceeds from marketplace sales, services, subscriptions, sponsor payments, and eligible prizes.
  • Subject to holds, refunds, tax, verification, and payout rules.
4. Contest Escrow
  • Reserved entry/stake/prize funds.
  • Cannot be spent while held.
  • Released only through result and policy settlement.
5. Bonus Credits
  • Non-withdrawable.
  • Clear expiration and use rules.
  • Never misrepresented as cash equivalent.
6. Withdrawable Balance
  • Provider-backed eligible amount after holds and verification.
  • Not the same as gross creator earnings.
7. Reserve / Chargeback Hold
  • Temporary risk reserve where policy permits.
8. Platform Revenue
  • Conversion fees, marketplace fees, organizer fees, subscription revenue, and other platform accounts.

11.3 Conversion

The conversion engine must support:

• cash to eligible credits;
• eligible credits or earnings to cash;
• founder default platform fee: 1%;
• separate provider/network fees;
• exchange rate;
• minimum and maximum;
• daily/monthly limits;
• user verification requirements;
• jurisdiction requirements;
• quote expiration;
• confirmation;
• idempotency;
• settlement state;
• cancellation;
• reversal;
• chargeback handling;
• reconciliation.

Recommended conversion state machine:

```text
QUOTED
→ USER_CONFIRMED
→ POLICY_APPROVED
→ PROVIDER_PENDING
→ SETTLED
```

Exceptional states:

```text
REJECTED
EXPIRED
FAILED
REVERSED
CHARGEBACK
UNDER_REVIEW
```

11.4 One-to-one wager flow

Preserve the founder’s intended product flow as a compliance-gated module:

```text
1. Battle created with a stake amount and approved rule profile.
2. Policy engine checks both users, jurisdiction, age, identity, limits, and event type.
3. Challenger stake is reserved.
4. Opponent accepts and matching stake is reserved.
5. Funds move into contest escrow.
6. Submissions lock.
7. Judging/voting completes.
8. Result enters dispute window.
9. Result becomes final.
10. Escrow settles to winner or refunds/voids according to the rule set.
11. Platform fees post as separate ledger entries.
12. Reconciliation and tax records update.
```

No free-form peer-to-peer credit transfer is required for V1. Value should move only through approved commerce, contest, refund, payout, or adjustment workflows.

11.5 Compliance gates

Cash-convertible or paid competition features must require:

• approved legal classification;
• jurisdiction profile;
• geolocation and residency policy;
• minimum age;
• identity verification;
• sanctions screening where required;
• payment-provider approval;
• official rules;
• responsible-play controls;
• limits;
• self-exclusion;
• fraud review;
• chargeback controls;
• tax-reporting readiness;
• customer-support escalation;
• audit logging;
• founder approval;
• production feature flag.

All must default to off.

11.6 Payment-provider separation

Create distinct interfaces:

Standard commerce provider

For ordinary subscriptions, marketplace purchases, services, and non-wager commerce, subject to provider approval.

Regulated contest / wallet provider

For paid entry, cash prizes, cash-convertible credits, escrow, or wager-like functionality, selected only after legal and underwriting review.

Internal sandbox provider

For deterministic testing with no real funds.

Never route a paid creator battle through a standard commerce provider merely because its SDK is convenient.

11.7 Reconciliation

Create:

• provider transaction import;
• daily reconciliation job;
• ledger-to-provider diff;
• unresolved exception queue;
• payout reconciliation;
• chargeback reconciliation;
• immutable reconciliation report;
• finance dashboard;
• manual adjustment workflow requiring dual control and reason code.

────────

12. SPONSORSHIP, ORGANIZERS, AND SCOUTING

12.1 Sponsored challenges

A sponsor campaign includes:

• sponsor organization;
• authorized members;
• creative brief;
• discipline and division;
• eligibility;
• geography;
• timeline;
• prize pool;
• secured-funds evidence;
• judge panel;
• rights and usage terms;
• disclosure requirements;
• brand-safety requirements;
• deliverables;
• reporting;
• official rules;
• contact and escalation.

Prize funds must be secured before an event is represented as funded.

12.2 Sponsor dashboard

• campaign status;
• entries;
• moderation status;
• shortlist;
• judge progress;
• audience reach;
• qualified views;
• completion;
• creator demographics only in privacy-safe aggregates;
• spend;
• prize settlement;
• downloadable audit/report.

12.3 Scouting

Scout tools:

• search by discipline;
• division;
• rating;
• consistency;
• event tier;
• verified skill;
• portfolio tags;
• availability;
• optional location;
• team;
• judge feedback;
• sponsor performance;
• marketplace reliability.

Scouts can:

• create private lists;
• add notes;
• compare creators;
• request contact;
• invite creators to private opportunities.

Do not sell hidden personal data. Creators control contact preferences and know when a formal opportunity request is made.

────────

13. MODERATION, RIGHTS, TRUST, DISPUTES, AND APPEALS

13.1 Moderation domains

Separate but coordinated enforcement for:

• content;
• comments/community;
• competition integrity;
• marketplace;
• financial/wallet;
• identity;
• rights/IP;
• sponsorship;
• account safety.

A comment suspension must not silently freeze funds. A wallet restriction must not automatically erase a competitive record. Cross-domain actions require explicit policy.

13.2 Report categories

• harassment;
• hate or abuse;
• sexual content;
• violence;
• self-harm;
• impersonation;
• copyright;
• trademark;
• unauthorized sample or asset;
• voice/likeness misuse;
• AI disclosure fraud;
• vote manipulation;
• collusion;
• plagiarism;
• stolen work;
• spam;
• scam;
• marketplace non-delivery;
• contest-rule violation;
• underage user;
• financial fraud.

13.3 Rights claims

Create:

• rights-claim intake;
• claimant identity and contact;
• target asset;
• basis;
• evidence;
• status;
• counter-notice where applicable;
• access restriction;
• repeat-infringer tracking;
• decision;
• appeal;
• audit retention.

Do not let agents adjudicate legal ownership conclusively.

13.4 Competition disputes

State machine:

```text
OPEN
→ TRIAGE
→ EVIDENCE_REQUESTED
→ UNDER_REVIEW
→ DECIDED
→ APPEAL_WINDOW
→ FINAL
```

Possible outcomes:

• uphold result;
• rescore;
• invalidate votes;
• disqualify submission;
• void battle;
• refund;
• settle;
• hold payout;
• suspend competitive access;
• require resubmission;
• refer to rights process.

Material money or account sanctions require a human escalation path.

13.5 Admin auditability

Every privileged action records:

• staff identity;
• role;
• reason;
• case;
• previous value;
• new value;
• affected resources;
• timestamp;
• source IP/device where appropriate;
• approval;
• evidence link.

High-risk actions should require step-up authentication and, where practical, dual approval.

────────

14. ANALYTICS AND SUCCESS METRICS

14.1 North-star metric

Recommended north-star:

Completed, verified creator competitions that generate a meaningful creator outcome.

A meaningful outcome may include:

• rating movement;
• qualified discovery;
• prize;
• sale;
• commission lead;
• sponsor shortlist;
• scout contact;
• follower conversion;
• repeat participation.

14.2 Core metrics

Acquisition:

• visitor-to-signup;
• creator onboarding completion;
• source/channel;
• referral conversion.

Activation:

• time to first upload;
• time to first battle;
• first challenge acceptance;
• first vote;
• first follow;
• first purchase.

Competition:

• battle fill rate;
• submission completion rate;
• no-show rate;
• event completion time;
• judge completion;
• dispute rate;
• void rate;
• ranked participation;
• repeat battle rate.

Discovery:

• unique creators discovered per user;
• rising-creator exposure;
• follow conversion;
• qualified listen/watch completion;
• search success.

Commerce:

• gross marketplace volume;
• creator earnings;
• sponsor spend;
• conversion volume;
• take rate;
• refund rate;
• payout failure;
• repeat buyers.

Trust:

• fraud flags;
• invalid votes;
• chargeback rate;
• upheld reports;
• appeal overturn rate;
• moderation response time;
• rights-claim response time.

Retention:

• D1, D7, D30;
• creator weekly active;
• audience weekly active;
• event cohort retention;
• discipline retention;
• paid conversion.

14.3 Analytics constraints

• no secret user profiling;
• no selling private creator data;
• consent and opt-out support;
• event schema versioning;
• avoid collecting raw data without a use and retention policy;
• separate product analytics from security/fraud telemetry;
• redact sensitive financial and identity data.

────────

15. TECHNICAL ARCHITECTURE

15.1 Architecture doctrine

Build a modular monolith with event-driven boundaries, not a premature microservice maze.

The system should be deployable as a small number of applications while maintaining domain separation sufficient to extract services later.

Core principles:

• strict TypeScript;
• contract-first APIs;
• immutable financial records;
• event/outbox pattern;
• provider adapters;
• clear trust boundaries;
• no business logic in React components;
• no critical state transitions from the client;
• no secrets in source or model context;
• testable domain services;
• deterministic policy evaluation;
• portable infrastructure where practical;
• separate development, staging, and production resources.

15.2 Recommended stack

Monorepo

• pnpm
• Turborepo
• TypeScript
• shared lint, formatting, test, and build configuration

Web and admin

• latest stable Next.js version compatible with Cloudflare Workers;
• Cloudflare’s current recommended vinext path for a new Workers deployment;
• React;
• Tailwind CSS;
• Radix primitives and/or shadcn-based owned components;
• TanStack Query for client server-state where needed;
• React Hook Form;
• Zod;
• PWA support;
• Storybook or an equivalent component workshop.

If a required feature is not compatible with the recommended Cloudflare adapter, create an ADR comparing:

• vinext/Next.js;
• TanStack Start;
• a split static web client plus Hono API.

Do not silently move the entire platform to another cloud.

API

• Hono on Cloudflare Workers;
• REST/JSON with OpenAPI 3.1;
• typed client generation;
• webhook endpoints with signature verification;
• idempotency middleware;
• policy middleware;
• rate limiting;
• structured errors.

GraphQL is not required for V1. It may be evaluated later for discovery/scouting complexity, but must not block the first vertical slice.

Database

• Neon Postgres;
• Drizzle ORM and SQL migrations;
• separate schemas where useful:
  • auth
  • app
  • ledger
  • moderation
  • audit
  • analytics
• Postgres row-level constraints and transactions;
• outbox table;
• point-in-time recovery;
• branch/database strategy for preview environments;
• no production schema change without a reviewed migration.

Authentication

• self-hosted Better Auth or an equivalent open, Postgres-backed auth layer selected by ADR;
• email/password or passwordless;
• social OAuth;
• passkeys;
• email verification;
• optional phone verification;
• two-factor authentication;
• organization/team support;
• session revocation;
• device/session management;
• step-up auth for sensitive actions.

Do not make a closed identity vendor the only source of identity truth.

Object storage and media

• Cloudflare R2;
• direct client upload through short-lived presigned URLs;
• multipart/resumable upload for large media;
• checksum validation;
• quarantine prefix/bucket;
• malware and content validation workflow;
• derived preview assets separate from originals;
• short-lived download URLs;
• signed playback access for private work;
• lifecycle rules;
• deletion workflow;
• media provenance metadata.

Realtime

• Cloudflare Durable Objects with WebSocket hibernation for:
  • battle rooms;
  • live scoring;
  • event presence;
  • live chat where enabled;
  • tournament updates.

Canonical results and financial state remain in Postgres. Durable Objects coordinate realtime sessions; they do not become the only ledger or result store.

Background jobs

• Cloudflare Queues;
• Workers consumers;
• scheduled jobs for:
  • deadlines;
  • result finalization;
  • notifications;
  • reconciliation;
  • retention;
  • analytics rollups;
  • ranking updates;
  • fraud review;
  • media jobs.

Heavy media transcoding must use a provider abstraction. Do not pretend edge request CPU is a full media farm. Support Cloudflare Stream or a containerized media-worker provider through an adapter.

Search

V1:

• Postgres full-text search;
• pg_trgm;
• structured filters;
• materialized or indexed ranking views.

Later:

• Typesense, OpenSearch, or another search service through an adapter when scale and relevance requirements justify it.

Cache and coordination

Use Cloudflare platform primitives carefully:

• Durable Objects for strongly coordinated realtime state;
• KV only for appropriate eventually consistent configuration/cache;
• Cache API for public responses;
• Postgres remains canonical for domain records.

Email and messaging

Create provider interfaces:

• transactional email;
• SMS/phone verification;
• push notifications;
• web push.

Do not hardwire the domain to one email or SMS vendor.

Payments

Create three provider adapters:

• standard commerce;
• regulated contest/wallet;
• internal sandbox.

Stripe may be integrated only for product classes it explicitly approves. Do not assume it can process entry-fee competitions or cash-prize skill contests.

Observability

• OpenTelemetry;
• structured JSON logs;
• trace IDs;
• request IDs;
• Sentry or equivalent error tracking;
• Cloudflare observability/log export;
• uptime checks;
• alerting;
• dashboards;
• redaction;
• no raw secrets, identity documents, or full payment payloads in logs.

Product analytics

• PostHog or an equivalent adapter;
• server-side authoritative events for financial and competition completion;
• consent-aware client analytics;
• versioned event registry.

Infrastructure as code

• Wrangler configuration;
• OpenTofu/Terraform where it adds value;
• separate Cloudflare, Neon, and third-party resource modules;
• environment-specific state;
• no secrets in state committed to Git.

15.3 Trust zones

At minimum define:

1. public client;
2. authenticated client;
3. edge API;
4. realtime coordination;
5. database;
6. object storage;
7. background workers;
8. payment providers;
9. identity/KYC providers;
10. admin/trust console;
11. analytics;
12. agent/development tooling.

Create a threat model and data-flow diagram for each high-risk flow.

15.4 Event and outbox architecture

Business transactions that require downstream events must:

1. update canonical state;
2. append an outbox event in the same database transaction;
3. publish asynchronously;
4. record delivery attempts;
5. be idempotently consumed.

Never publish “battle settled” before the ledger transaction commits.

────────

16. REPOSITORY TOPOLOGY

Create this structure or a justified equivalent documented in an ADR:

```text
artist-arena/
├── .agents/
│   ├── roles/
│   ├── workflows/
│   └── policies/
├── .analysis/
├── .claude/
├── .codex/
├── .cursor/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   ├── dependabot.yml
│   ├── labels.yml
│   └── workflows/
│       ├── ci.yml
│       ├── security.yml
│       ├── e2e.yml
│       ├── migration-check.yml
│       ├── openapi-check.yml
│       ├── preview.yml
│       ├── staging.yml
│       └── release.yml
├── apps/
│   ├── web/
│   ├── admin/
│   ├── api/
│   ├── realtime/
│   └── workers/
├── packages/
│   ├── auth/
│   ├── config/
│   ├── contracts/
│   ├── db/
│   ├── domain/
│   ├── events/
│   ├── feature-flags/
│   ├── ledger/
│   ├── media/
│   ├── notifications/
│   ├── observability/
│   ├── policy/
│   ├── ratings/
│   ├── security/
│   ├── testing/
│   ├── ui/
│   └── validation/
├── db/
│   ├── migrations/
│   ├── seeds/
│   ├── fixtures/
│   └── diagrams/
├── docs/
│   ├── product/
│   ├── architecture/
│   ├── adr/
│   ├── api/
│   ├── data/
│   ├── design/
│   ├── security/
│   ├── privacy/
│   ├── compliance/
│   ├── moderation/
│   ├── operations/
│   ├── testing/
│   ├── decisions/
│   └── backlog/
├── infra/
│   ├── cloudflare/
│   ├── neon/
│   ├── monitoring/
│   └── terraform/
├── scripts/
├── tests/
│   ├── contract/
│   ├── e2e/
│   ├── integration/
│   ├── load/
│   ├── security/
│   └── smoke/
├── AGENTS.md
├── ARCHITECTURE.md
├── CAPABILITIES.md
├── CHANGELOG.md
├── CLAUDE.md
├── CODESPRING.md
├── CODEX.md
├── COMPLIANCE.md
├── CONTRIBUTING.md
├── DECISIONS.md
├── LICENSE
├── MANUS.md
├── OPEN_DECISIONS.md
├── PRIVACY.md
├── PRODUCT.md
├── PROJECT_MEMORY.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── THREAT_MODEL.md
├── TRAYCER.md
├── .env.example
├── .gitignore
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── turbo.json
└── tsconfig.base.json
```

16.1 Root document responsibilities

README.md

• product summary;
• status;
• prerequisites;
• local setup;
• commands;
• architecture map;
• environment model;
• links to governing docs;
• warning that real-money features are disabled.

PRODUCT.md

• product canon;
• personas;
• scope;
• journeys;
• rules;
• phase boundaries.

ARCHITECTURE.md

• system context;
• container/component diagrams;
• data flows;
• module boundaries;
• dependency rules;
• provider adapters;
• event model.

AGENTS.md

• global operating rules;
• instruction hierarchy;
• planning requirements;
• file-claim protocol;
• secrets rules;
• testing requirements;
• prohibited actions;
• definition of done.

MANUS.md

• Manus repository-creation duties;
• output checklist;
• open-decision preservation;
• no false completion claims.

TRAYCER.md

• task decomposition;
• dependency graphs;
• parallel-safe work;
• checkpoints;
• review gates;
• context-loading order.

CODESPRING.md

• implementation contract;
• stable interfaces;
• acceptance criteria;
• required tests;
• migration discipline;
• output evidence.

SECURITY.md

• secure-development rules;
• vulnerability reporting;
• secret management;
• auth/session policy;
• upload security;
• dependency policy;
• incident severity.

COMPLIANCE.md

• feature classification;
• jurisdiction policy;
• cash-feature activation gates;
• KYC/AML responsibilities;
• app-store constraints;
• privacy controls;
• responsible-play controls;
• “not legal clearance” notice.

DECISIONS.md

Approved decisions only.

OPEN_DECISIONS.md

Every unresolved product, legal, economic, technical, or brand choice with:

• decision ID;
• question;
• context;
• options;
• recommendation;
• impact;
• owner;
• deadline;
• status.

PROJECT_MEMORY.md

Durable project state for future agent sessions:

• current milestone;
• completed work;
• active branches;
• decisions;
• known risks;
• next actions;
• unresolved blockers.

────────

17. CORE DATA MODEL

Use UUIDv7 or another sortable, collision-resistant ID strategy selected in an ADR. Use created_at, updated_at, and where appropriate deleted_at, but do not soft-delete immutable financial or audit records.

17.1 Identity and organizations

• users
• profiles
• user_handles
• user_emails
• user_phones
• sessions
• passkeys
• user_roles
• role_assignments
• organizations
• organization_members
• teams
• team_members
• verification_records
• contact_preferences
• user_consents
• user_restrictions

17.2 Creator taxonomy and portfolios

• disciplines
• discipline_formats
• creator_disciplines
• skills
• creator_skills
• portfolio_items
• portfolio_assets
• work_rights_profiles
• creator_availability
• creator_links
• badges
• user_badges

17.3 Media and provenance

• media_assets
• media_versions
• media_derivatives
• upload_sessions
• upload_parts
• media_checksums
• media_scan_results
• provenance_records
• ai_disclosures
• creation_tools
• evidence_bundles
• evidence_items
• asset_access_logs
• rights_assertions
• consent_grants

17.4 Competitions

• arenas
• rule_sets
• rule_set_versions
• battles
• battle_participants
• battle_state_events
• battle_rounds
• submissions
• submission_assets
• submission_finalizations
• challenges
• tournaments
• tournament_entries
• tournament_rounds
• bracket_nodes
• seasons
• season_memberships
• eligibility_decisions
• result_attestations
• result_participants
• result_amendments
• disputes
• dispute_evidence
• appeals

17.5 Judging and voting

• scoring_templates
• scoring_dimensions
• event_scoring_configs
• judges
• judge_assignments
• judge_conflicts
• judge_scores
• judge_score_items
• ballots
• votes
• vote_risk_signals
• vote_invalidations
• score_calculations
• tie_breaks

17.6 Ratings and rankings

• rating_pools
• ratings
• rating_events
• rating_algorithm_versions
• leaderboard_snapshots
• competitive_records
• reputation_events
• reputation_snapshots

17.7 Social and discovery

• follows
• comments
• comment_reactions
• bookmarks
• shares
• feeds
• feed_items
• recommendation_impressions
• search_documents
• notifications
• notification_preferences
• event_presence
• live_sessions
• chat_messages
• blocks
• mutes

17.8 Marketplace

• listings
• listing_versions
• listing_assets
• prices
• orders
• order_lines
• entitlements
• licenses
• subscriptions
• commission_requests
• service_contracts
• service_milestones
• deliverables
• reviews
• refunds
• royalty_splits
• split_recipients

17.9 Sponsors and scouting

• sponsor_organizations
• sponsor_campaigns
• campaign_briefs
• campaign_prizes
• campaign_reports
• scout_profiles
• scout_lists
• scout_list_items
• opportunities
• opportunity_invites
• contact_requests

17.10 Ledger and payments

• ledger_accounts
• ledger_journals
• ledger_postings
• ledger_balances
• ledger_reversals
• money_instruments
• fee_policies
• conversion_quotes
• conversion_orders
• escrow_holds
• escrow_releases
• payment_customers
• payment_methods
• payment_transactions
• provider_events
• payout_accounts
• payouts
• chargebacks
• reserves
• reconciliation_runs
• reconciliation_items
• tax_profiles
• tax_documents
• wallet_restrictions
• responsible_play_limits
• self_exclusions

17.11 Trust, support, and audit

• reports
• moderation_cases
• moderation_actions
• rights_claims
• counter_notices
• support_tickets
• fraud_signals
• risk_reviews
• policy_profiles
• policy_rules
• feature_flags
• admin_actions
• audit_events
• security_events
• incidents

17.12 Analytics and event delivery

• analytics_events
• outbox_events
• event_deliveries
• webhook_endpoints
• webhook_deliveries
• experiment_assignments

────────

18. API CONTRACTS

Create OpenAPI 3.1 specifications and generated types.

18.1 API standards

• versioned path or media type;
• request and response schemas;
• Zod validation;
• consistent error envelope;
• request ID;
• trace ID;
• cursor pagination;
• idempotency keys for mutations with financial or state consequences;
• ETag/version checks for concurrent edits;
• rate-limit headers;
• permission documentation;
• event side effects;
• no leaking internal fraud logic.

Recommended error shape:

```json
{
  "error": {
    "code": "BATTLE_NOT_ELIGIBLE",
    "message": "This account is not eligible for the selected battle.",
    "requestId": "req_...",
    "details": {}
  }
}
```

18.2 Endpoint groups

Auth

```text
POST   /v1/auth/register
POST   /v1/auth/login
POST   /v1/auth/logout
POST   /v1/auth/verify-email
POST   /v1/auth/2fa/challenge
POST   /v1/auth/2fa/verify
GET    /v1/auth/sessions
DELETE /v1/auth/sessions/:sessionId
```

Profiles

```text
GET    /v1/profiles/:handle
PATCH  /v1/me/profile
GET    /v1/me/profile
POST   /v1/me/disciplines
DELETE /v1/me/disciplines/:disciplineId
GET    /v1/profiles/:handle/record
GET    /v1/profiles/:handle/portfolio
```

Uploads and media

```text
POST   /v1/uploads
POST   /v1/uploads/:uploadId/parts
POST   /v1/uploads/:uploadId/complete
POST   /v1/uploads/:uploadId/abort
GET    /v1/media/:mediaId
POST   /v1/media/:mediaId/finalize
DELETE /v1/media/:mediaId
```

Battles

```text
POST   /v1/battles
GET    /v1/battles
GET    /v1/battles/:battleId
PATCH  /v1/battles/:battleId
POST   /v1/battles/:battleId/publish
POST   /v1/battles/:battleId/accept
POST   /v1/battles/:battleId/withdraw
POST   /v1/battles/:battleId/submissions
POST   /v1/battles/:battleId/submissions/:submissionId/finalize
POST   /v1/battles/:battleId/cancel
GET    /v1/battles/:battleId/timeline
```

Judging and voting

```text
GET    /v1/judge/assignments
POST   /v1/judge/assignments/:assignmentId/scores
POST   /v1/battles/:battleId/votes
GET    /v1/battles/:battleId/results
POST   /v1/battles/:battleId/disputes
POST   /v1/disputes/:disputeId/evidence
POST   /v1/disputes/:disputeId/appeal
```

Tournaments

```text
POST   /v1/tournaments
GET    /v1/tournaments
GET    /v1/tournaments/:tournamentId
POST   /v1/tournaments/:tournamentId/publish
POST   /v1/tournaments/:tournamentId/enter
GET    /v1/tournaments/:tournamentId/bracket
POST   /v1/tournaments/:tournamentId/advance
```

Ratings and rankings

```text
GET    /v1/ratings/:profileId
GET    /v1/rankings
GET    /v1/seasons
GET    /v1/seasons/:seasonId
```

Social

```text
POST   /v1/profiles/:profileId/follow
DELETE /v1/profiles/:profileId/follow
POST   /v1/comments
PATCH  /v1/comments/:commentId
DELETE /v1/comments/:commentId
POST   /v1/comments/:commentId/report
GET    /v1/feed
GET    /v1/notifications
POST   /v1/notifications/read
```

Marketplace

```text
POST   /v1/listings
GET    /v1/listings
GET    /v1/listings/:listingId
PATCH  /v1/listings/:listingId
POST   /v1/listings/:listingId/publish
POST   /v1/orders
GET    /v1/orders/:orderId
GET    /v1/me/entitlements
POST   /v1/commissions
POST   /v1/service-contracts/:contractId/deliverables
POST   /v1/service-contracts/:contractId/accept
POST   /v1/service-contracts/:contractId/dispute
```

Wallet

```text
GET    /v1/wallet
GET    /v1/wallet/activity
POST   /v1/wallet/conversion-quotes
POST   /v1/wallet/conversions
POST   /v1/wallet/payouts
GET    /v1/wallet/payouts/:payoutId
POST   /v1/wallet/limits
POST   /v1/wallet/self-exclusion
```

The production handlers for regulated actions must return a policy-gated response until enabled.

Sponsors and scouts

```text
POST   /v1/sponsor/campaigns
GET    /v1/sponsor/campaigns
POST   /v1/sponsor/campaigns/:campaignId/publish
GET    /v1/sponsor/campaigns/:campaignId/report
GET    /v1/scout/search
POST   /v1/scout/lists
POST   /v1/scout/lists/:listId/creators
POST   /v1/opportunities/:opportunityId/invite
POST   /v1/contact-requests
```

Admin and trust

```text
GET    /v1/admin/cases
GET    /v1/admin/cases/:caseId
POST   /v1/admin/cases/:caseId/actions
GET    /v1/admin/ledger/reconciliation
POST   /v1/admin/ledger/adjustments
GET    /v1/admin/audit
POST   /v1/admin/feature-flags
POST   /v1/admin/policies/evaluate
```

────────

19. DOMAIN EVENTS

Create a versioned event registry.

Initial events:

```text
user.created.v1
user.email_verified.v1
profile.updated.v1
creator.discipline_added.v1
media.upload_started.v1
media.upload_completed.v1
media.scan_failed.v1
submission.created.v1
submission.finalized.v1
battle.created.v1
battle.published.v1
battle.accepted.v1
battle.funded.v1
battle.submission_window_opened.v1
battle.submissions_locked.v1
battle.voting_opened.v1
battle.judging_opened.v1
vote.cast.v1
judge_score.submitted.v1
battle.provisional_result_created.v1
battle.disputed.v1
battle.result_finalized.v1
battle.settled.v1
rating.updated.v1
tournament.created.v1
tournament.entry_added.v1
tournament.bracket_generated.v1
listing.published.v1
order.created.v1
order.paid.v1
entitlement.granted.v1
service.delivered.v1
ledger.journal_posted.v1
conversion.quoted.v1
conversion.settled.v1
escrow.held.v1
escrow.released.v1
payout.requested.v1
payout.completed.v1
chargeback.opened.v1
report.created.v1
moderation.action_taken.v1
rights_claim.created.v1
notification.requested.v1
```

Each event schema includes:

• event ID;
• event type;
• schema version;
• aggregate type;
• aggregate ID;
• actor;
• occurred time;
• correlation ID;
• causation ID;
• payload;
• privacy classification;
• retention class.

────────

20. SECURITY, PRIVACY, AND COMPLIANCE BASELINE

20.1 Secrets

• no secrets in Git;
• no secrets in screenshots;
• no secrets in generated examples;
• no secrets in prompts;
• no secrets in logs;
• .env only for local non-committed development;
• .env.example contains names and safe descriptions only;
• OS keychain or secret manager for local credentials;
• encrypted GitHub environment secrets;
• separate dev/staging/prod credentials;
• scoped, short-lived tokens for agents;
• rotation and revocation;
• automatic secret scanning;
• pre-commit detection;
• redaction tests.

20.2 Authentication security

• secure, HTTP-only, same-site cookies;
• CSRF protection;
• session rotation;
• session revocation;
• password hashing with a modern memory-hard algorithm when passwords are enabled;
• passkeys;
• 2FA;
• step-up auth;
• brute-force protection;
• credential-stuffing controls;
• email-change confirmation;
• recovery codes;
• device/session view;
• high-risk login alerts.

20.3 Application security

• OWASP ASVS-informed controls;
• authorization tested server-side;
• CSP;
• secure headers;
• SSRF protection;
• SQL injection prevention;
• XSS prevention;
• file type sniffing;
• archive-bomb protection;
• malware scan;
• webhook signature verification;
• idempotency;
• rate limiting;
• bot controls;
• dependency pinning;
• SBOM;
• SAST;
• DAST;
• dependency scanning;
• license scanning;
• signed release artifacts;
• least privilege.

20.4 Financial security

• append-only ledger;
• no client-authoritative balance;
• immutable provider event archive;
• webhook replay defense;
• reconciliation;
• dual control for adjustments;
• payout holds;
• velocity limits;
• device/account risk;
• chargeback workflow;
• no silent deletion;
• penny/minor-unit precision tests;
• property-based accounting tests.

20.5 Privacy

Implement:

• data inventory;
• purpose classification;
• consent/notice hooks;
• download/export;
• deletion workflow;
• retention schedules;
• legal holds;
• encryption;
• privileged-access audit;
• regional controls;
• child/minor protections;
• telemetry opt-out where required;
• cookie controls;
• separation of KYC data from public application data.

20.6 Compliance posture

• Design the hosted platform/backend for SOC 2 readiness.
• Do not claim SOC 2 certification until an actual audit is completed.
• HIPAA is not a default Artist Arena requirement because the intended product does not require protected health information.
• If a future workflow processes PHI, isolate and reassess it rather than labeling the entire platform “HIPAA compliant” in advance.
• Maintain a control matrix mapping policies to implementation and evidence.
• Create evidence collection hooks compatible with Vanta or an equivalent compliance platform.
• Maintain incident response, vendor inventory, access review, change management, backup, and business-continuity documentation.

20.7 Regulated-money posture

Create a REGULATED_FEATURES_DISABLED=true default.

The codebase may contain:

• interfaces;
• schemas;
• sandbox flows;
• tests;
• policy checks;
• mock provider;
• admin review tooling.

It must not contain:

• a hidden production bypass;
• automatic global activation;
• fake KYC;
• fake geolocation;
• fake legal clearance;
• a production “test” payment key committed to source.

20.8 Minors and age gating

• age-appropriate onboarding;
• block regulated financial participation by minors;
• parental/guardian hooks where appropriate;
• prevent public exposure of sensitive minor information;
• stronger messaging/contact restrictions;
• configurable country/state age policy;
• report and escalation flow.

────────

21. TESTING AND QUALITY GAUNTLET

21.1 Required test layers

• formatting;
• lint;
• TypeScript;
• unit;
• domain tests;
• property-based tests;
• database integration;
• migration tests;
• API contract tests;
• event schema tests;
• WebSocket/realtime tests;
• end-to-end browser tests;
• accessibility;
• visual regression;
• load/performance;
• security;
• dependency/license;
• secret scan;
• smoke deploy;
• rollback;
• backup/restore;
• reconciliation;
• fault injection for critical jobs.

21.2 Critical property tests

Ledger

For every valid journal:

• debits equal credits;
• no money is created or destroyed except through defined external/source accounts;
• reversal nets the original;
• idempotent repeat does not duplicate value;
• concurrent settlement cannot double-pay;
• balance projection equals ledger sum.

Escrow

• cannot release more than held;
• cannot settle twice;
• void returns funds according to rule;
• dispute prevents settlement;
• final result and settlement references match.

Ratings

• voided battle has no rating impact;
• repeat event processing is idempotent;
• algorithm version is recorded;
• rating changes are deterministic for identical input;
• no rating change for exhibition events.

Voting

• one eligible vote per ballot;
• duplicate idempotency key does not create duplicate vote;
• invalidated votes leave audit evidence;
• final score uses the snapshotted scoring policy.

21.3 E2E vertical-slice test

A complete test must prove:

1. Creator A registers.
2. Creator B registers.
3. Both create profiles and select Beat Production.
4. Creator A creates a free ranked-compatible test battle.
5. Creator B accepts.
6. Both upload audio through presigned R2 URLs.
7. Uploads pass validation.
8. Both finalize submissions.
9. Submissions remain private until locked.
10. Voting/judging opens.
11. Eligible votes and judge scores are recorded.
12. Result is calculated.
13. Dispute window expires in test time.
14. Result becomes final.
15. Ratings update once.
16. Notifications are delivered.
17. The timeline and audit record are complete.
18. No cash ledger entry occurs.
19. The full flow passes on a clean environment.

A second sandbox test must prove escrow and 1% conversion fee accounting with mock money only.

────────

22. PERFORMANCE AND RELIABILITY TARGETS

Create measurable service-level objectives.

Recommended initial targets:

• public page p95 server response under 500 ms where not media-bound;
• authenticated API p95 under 750 ms under expected beta load;
• realtime update p95 under 1 second;
• battle state transition correctness over raw speed;
• upload resumability for large media;
• no lost finalization jobs;
• no duplicate settlement;
• RPO and RTO documented for each service;
• graceful queue retries and dead-letter handling;
• backpressure;
• circuit breakers for external providers;
• degraded mode when recommendation or analytics systems are unavailable;
• wallet and result operations fail closed, not open.

Create load profiles for:

• battle launch spike;
• tournament final;
• voting close;
• sponsor event;
• large upload;
• notification burst;
• leaderboard refresh.

────────

23. ACCESSIBILITY, LOCALIZATION, AND CONTENT DESIGN

• WCAG 2.2 AA;
• full keyboard operation;
• visible focus;
• captions/transcripts where supplied;
• text alternatives;
• reduced motion;
• accessible audio player;
• waveform not required for navigation;
• color never the only status indicator;
• plain-language money and eligibility explanations;
• dates/times localized;
• currency localized;
• timezone explicit;
• translation-ready message catalogs;
• no hardcoded user-facing copy in domain logic;
• error messages explain recovery without exposing security internals.

────────

24. DEVELOPMENT WORKFLOW

24.1 Instruction hierarchy

Agents must read instructions in this order:

1. founder/governing specification;
2. workspace instructions;
3. repository AGENTS.md;
4. tool-specific root instruction;
5. directory-specific instruction;
6. issue/ticket;
7. current task plan.

Lower-level instructions cannot override higher-level security, product canon, or founder decisions.

24.2 Required agent workflow

```text
ASK / INSPECT
→ NORMALIZE REQUIREMENT
→ IDENTIFY LOCKED DECISIONS AND OPEN QUESTIONS
→ PLAN
→ DEFINE ACCEPTANCE CRITERIA
→ DEFINE TESTS
→ IDENTIFY SECURITY / RIGHTS / MONEY IMPACT
→ CLAIM FILES / MODULES
→ IMPLEMENT ON WORKING BRANCH
→ RUN GAUNTLET
→ REVIEW DIFF
→ UPDATE DOCUMENTATION AND PROJECT MEMORY
→ OPEN PR
→ HUMAN / AUTHORIZED MERGE
```

24.3 Parallel work

• agents work in isolated branches/worktrees;
• each task lists owned files/modules;
• shared contracts are changed through a coordination ticket;
• no worker overwrites concurrent work;
• no agent force-pushes shared branches;
• no agent merges main;
• no agent deploys production;
• no agent accesses master secrets;
• no agent changes financial rules without an ADR and review.

24.4 Prompt optimization

Before acting, agents must translate founder intent into:

• objective;
• constraints;
• non-goals;
• assumptions;
• dependencies;
• outputs;
• acceptance criteria;
• tests;
• risks;
• reversible plan.

Agents must not “improve” the prompt by removing difficult requirements.

24.5 Definition of done for a code change

• scope complete;
• acceptance criteria pass;
• tests added;
• lint/typecheck/build pass;
• migrations reviewed;
• security impact documented;
• privacy impact documented where relevant;
• money/ledger impact documented where relevant;
• API contract updated;
• docs updated;
• telemetry added;
• rollback documented;
• no secrets;
• project memory updated;
• PR evidence attached.

────────

25. GIT AND GITHUB OPERATING MODEL

25.1 Branches

Protected long-lived branches:

• main — production-ready source;
• staging — release-candidate integration;
• develop — active integration.

Short-lived branches:

```text
feature/<issue>-<slug>
fix/<issue>-<slug>
chore/<issue>-<slug>
docs/<issue>-<slug>
security/<issue>-<slug>
spike/<issue>-<slug>
```

25.2 Merge flow

```text
working branch
→ pull request into develop
→ release PR into staging
→ validated release PR into main
```

Emergency fixes require an explicit hotfix workflow and must be back-merged.

25.3 Required PR checks

• install with frozen lockfile;
• formatting;
• lint;
• typecheck;
• unit tests;
• integration tests;
• build;
• migration validation;
• OpenAPI diff;
• event-schema compatibility;
• secret scan;
• dependency scan;
• license scan;
• SBOM;
• security tests;
• relevant E2E;
• preview smoke test.

25.4 GitHub configuration

Create:

• CODEOWNERS;
• PR template;
• bug template;
• feature template;
• security issue route;
• decision template;
• ADR template;
• risk template;
• labels;
• milestones;
• project board;
• branch protection;
• environment protection;
• required reviewers;
• Dependabot/Renovate configuration;
• release notes/changelog automation.

Recommended labels:

```text
area:auth
area:profile
area:media
area:battle
area:tournament
area:judging
area:ratings
area:social
area:marketplace
area:ledger
area:payments
area:sponsor
area:scout
area:moderation
area:security
area:infra
area:design
type:feature
type:bug
type:chore
type:docs
type:adr
type:spike
risk:low
risk:medium
risk:high
risk:critical
status:blocked
status:ready
status:in-progress
status:review
status:done
compliance-gated
founder-decision
```

────────

26. PHASED DELIVERY PLAN

Phase 0 — Repository and architecture foundation

Deliver:

• private GitHub repo;
• branch model;
• monorepo scaffold;
• current stable dependencies;
• root instructions;
• product docs;
• ADRs;
• architecture diagrams;
• threat model;
• data classification;
• OpenAPI skeleton;
• event registry;
• database baseline;
• CI;
• test harness;
• local development;
• demo seed system;
• feature flags;
• mock providers;
• no real money.

Exit gate:

• fresh clone installs, type-checks, tests, and builds;
• docs are internally consistent;
• CodeSpring can start ticketed implementation without product guessing.

Phase 1 — Music battle vertical slice

Deliver:

• auth;
• creator profiles;
• disciplines;
• audio upload;
• battle create/accept;
• submission lock;
• community vote;
• judge scoring;
• result calculation;
• Glicko-2 rating;
• timeline;
• notifications;
• admin basics;
• audit;
• free/Arena Points only.

Exit gate:

• complete two-creator beat battle E2E passes.

Phase 2 — Music beta

Deliver:

• discovery feed;
• follows/comments/bookmarks;
• leaderboards;
• seasons;
• tournament bracket;
• organizer tools;
• AI divisions and disclosures;
• evidence vault;
• moderation;
• rights claims;
• basic marketplace;
• sponsor challenge sandbox;
• creator analytics.

Exit gate:

• a moderated beta season and sponsor-style mock challenge can run end to end.

Phase 3 — Commerce

Deliver:

• standard marketplace payments subject to provider approval;
• creator earnings ledger;
• subscriptions;
• commissions;
• entitlements;
• refunds;
• creator splits;
• payout verification;
• tax profile;
• reconciliation.

Exit gate:

• ordinary non-wager purchase, refund, creator earning, and payout sandbox/approved flow reconciles exactly.

Phase 4 — Regulated competition readiness

Deliver:

• jurisdiction policy engine;
• age/identity gates;
• geolocation;
• responsible-play controls;
• contest escrow;
• purchased-credit conversion;
• 1% fee engine;
• wager flow;
• regulated provider adapter;
• compliance console;
• app-store policy profiles;
• legal-document hooks;
• external security and financial review.

Exit gate:

• no production activation until counsel, provider, founder, security, and operational gates are all recorded as approved.

Phase 5 — Discipline expansion

Add:

• dance;
• visual art;
• film/video;
• writing;
• code;
• game building;
• multimedia;
• team competitions;
• category-specific media and evidence.

Phase 6 — Scale and ecosystem

• native mobile;
• native live streaming;
• advanced sponsor/scout tools;
• creator teams/collectives;
• deeper Sonara/Orpheus integrations;
• REAI/AXIOM game-competition adapters;
• external developer API;
• organizer marketplace;
• internationalization;
• advanced recommendations.

────────

27. FIRST IMPLEMENTATION BACKLOG

Create GitHub issues with dependencies, acceptance criteria, tests, risk, and owner type.

Epic A — Repository

1. Create monorepo and package boundaries.
2. Configure pnpm and Turborepo.
3. Add shared TypeScript, lint, format, and test config.
4. Configure Cloudflare Workers and local emulator.
5. Create GitHub workflows.
6. Add secret scanning, dependency scanning, and SBOM.
7. Add root instruction and memory files.
8. Add ADR template and initial ADRs.

Epic B — Product contracts

9. Define discipline schema.
10. Define division and disclosure schema.
11. Define battle state machine.
12. Define rule-set version schema.
13. Define submission and media schema.
14. Define judging/voting schema.
15. Define result attestation schema.
16. Define rating event schema.
17. Publish OpenAPI v1 skeleton.
18. Publish event registry v1.

Epic C — Identity and profile

19. Implement auth foundation.
20. Implement email verification.
21. Implement session/device management.
22. Implement profile CRUD.
23. Implement handle reservation.
24. Implement creator disciplines.
25. Implement profile public page.
26. Add 2FA/passkey path.

Epic D — Media

27. Create R2 upload-session API.
28. Add presigned upload.
29. Add multipart flow.
30. Add checksum and MIME validation.
31. Add quarantine and scan status.
32. Add private signed playback.
33. Add media derivative job contract.
34. Add upload E2E.

Epic E — Battle loop

35. Implement battle create.
36. Implement publish/accept.
37. Implement eligibility policy.
38. Implement submission create/finalize.
39. Implement lock/reveal rules.
40. Implement battle timeline.
41. Implement state transition audit.
42. Implement cancellation/expiration.
43. Implement battle E2E.

Epic F — Judging and ratings

44. Implement scoring templates.
45. Implement judge assignments.
46. Implement audience ballots.
47. Implement anti-duplicate voting.
48. Implement score calculation.
49. Implement provisional/final result.
50. Implement dispute window.
51. Implement Glicko-2 rating events.
52. Implement rankings.

Epic G — Social and discovery

53. Implement follow.
54. Implement comments/replies.
55. Implement blocks/reports.
56. Implement discover query.
57. Implement feed events.
58. Implement notifications.

Epic H — Admin and trust

59. Implement admin RBAC.
60. Implement case management.
61. Implement moderation actions.
62. Implement rights-claim intake.
63. Implement audit search.
64. Implement feature-flag console.

Epic I — Ledger sandbox

65. Implement double-entry schema.
66. Implement journal service.
67. Implement Arena Points.
68. Implement mock purchased credits.
69. Implement conversion quote and 1% fee.
70. Implement escrow hold/release.
71. Implement reversal.
72. Implement reconciliation.
73. Add property-based ledger tests.
74. Keep regulated production flags disabled.

Epic J — Marketplace sandbox

75. Implement listings.
76. Implement orders.
77. Implement entitlements.
78. Implement creator split schema.
79. Implement commission request.
80. Implement service delivery/acceptance.
81. Implement refund sandbox.

Epic K — Sponsorship

82. Implement sponsor organizations.
83. Implement campaign briefs.
84. Implement secured-prize status.
85. Implement sponsor challenge.
86. Implement sponsor report.
87. Implement scout search and lists.

────────

28. FIRST VERTICAL-SLICE ACCEPTANCE CRITERIA

The repository is ready for CodeSpring implementation when:

• product canon is preserved;
• V1 scope is clear;
• regulated and non-regulated flows are separated;
• module boundaries are documented;
• architecture diagrams exist;
• database relationships exist;
• the battle state machine exists;
• the ledger design exists;
• the AI division rules exist;
• API contracts exist;
• events exist;
• CI exists;
• the repo builds cleanly;
• the first issues are dependency-ordered;
• every issue has acceptance criteria and tests;
• secrets are absent;
• real-money features are disabled;
• open decisions are visible;
• all scaffold placeholders are labeled;
• no mock is represented as a completed production integration.

The first implemented vertical slice is complete when:

• two users can register;
• create public creator profiles;
• select a discipline;
• create and accept a beat battle;
• upload and lock audio;
• vote/judge;
• finalize a result;
• update ratings once;
• show the result on both profiles;
• create complete audit evidence;
• perform the same flow in an automated E2E test;
• perform a mock escrow and conversion test without real money.

────────

29. OPEN DECISIONS MANUS MUST RECORD, NOT HIDE

Create entries for:

1. Legal operating entity and IP owner.
2. Launch country and approved U.S. states/territories.
3. Minimum age for ordinary accounts.
4. Minimum age for creator commerce.
5. Whether 1% applies to each direction independently as the current default or is displayed as a round-trip total.
6. Credit exchange rate and denomination.
7. Whether purchased credits can ever be transferred outside approved contests/commerce.
8. Marketplace commission.
9. Subscription tiers and pricing.
10. Organizer fee.
11. Sponsor service fee.
12. Prize-funding structure.
13. Responsible-play limits.
14. Regulated payment/wallet provider.
15. KYC/AML provider.
16. Tax provider.
17. Geolocation provider.
18. Standard commerce provider.
19. Email/SMS provider.
20. Native streaming provider.
21. Initial judging profile.
22. Judge recruitment and compensation.
23. Appeal fee, if any.
24. Exact launch disciplines.
25. Whether dance is launch or phase 2.
26. Rights terms for sponsored briefs.
27. Creator default license templates.
28. Brand identity, logo, typography, and domain.
29. Public API timing.
30. Native mobile timing.
31. Final repository organization/account.
32. Final software license for proprietary code.
33. Data residency requirements.
34. Retention periods.
35. Whether creator teams can receive direct split payouts in first commerce release.

Do not block the repository on decisions that can remain configurable. Mark them explicitly.

────────

30. INITIAL ADRS

Create at least:

• ADR-0001: Monorepo and modular-monolith approach.
• ADR-0002: Cloudflare Workers web/API deployment.
• ADR-0003: Next.js + vinext compatibility and fallback.
• ADR-0004: Neon Postgres and Drizzle.
• ADR-0005: Better Auth/self-hosted identity.
• ADR-0006: R2 upload and media architecture.
• ADR-0007: Durable Objects realtime coordination.
• ADR-0008: Event outbox.
• ADR-0009: Double-entry ledger.
• ADR-0010: Separate economic instruments.
• ADR-0011: Glicko-2 rating.
• ADR-0012: AI division and disclosure model.
• ADR-0013: Standard versus regulated payment providers.
• ADR-0014: PWA-first, native-mobile-later.
• ADR-0015: Postgres search before external search engine.
• ADR-0016: No blockchain dependency in V1.
• ADR-0017: Provider-agnostic heavy media processing.
• ADR-0018: Feature flags and jurisdiction policy engine.
• ADR-0019: Human-reviewed material enforcement.
• ADR-0020: No training on creator uploads without opt-in.

────────

31. SEED AND DEMO DATA

Create deterministic seed data with clearly fictional, non-infringing content:

• two beat creators;
• one rapper;
• one singer/songwriter;
• one judge;
• one organizer;
• one sponsor organization;
• one scout;
• one moderator;
• one free beat battle;
• one completed judged battle;
• one open challenge;
• one tournament;
• one Pure Human submission;
• one Hybrid submission;
• one AI Open submission;
• one marketplace listing;
• one commission request;
• one mock sponsor campaign;
• Arena Points ledger;
• mock conversion quote;
• mock escrow settlement.

Do not use copyrighted commercial audio, celebrity likenesses, copied UI, or unlicensed assets.

────────

32. MANUS GITHUB EXECUTION CHECKLIST

Perform the following in order.

Step 1 — Inspect

• Inspect connected GitHub organization/account.
• Confirm whether artist-arena exists.
• Inspect any relevant existing template repo.
• Read all available instructions.
• Do not assume permissions.

Step 2 — Create

If authorized:

• create private repository artist-arena;
• add description: “Competitive infrastructure for the global creator economy”;
• initialize main;
• create staging;
• create develop;
• keep main as default;
• add repository topics;
• do not add a public license unless Ø has selected one.

Step 3 — Scaffold

• create the complete repository structure;
• create compilable apps/packages;
• create safe .env.example;
• create local setup;
• create deterministic seed;
• create mock providers;
• create initial schemas;
• create OpenAPI skeleton;
• create tests;
• create CI.

Step 4 — Document

• populate all governing docs;
• create Mermaid diagrams;
• create ADRs;
• create threat model;
• create data classification;
• create compliance gating;
• create roadmap;
• create backlog;
• create open decisions.

Step 5 — Configure GitHub

Where permissions allow:

• branch protections;
• required checks;
• CODEOWNERS;
• labels;
• milestones;
• project board;
• environments;
• environment approvals;
• issue templates;
• PR template;
• security policy;
• dependency automation.

Step 6 — Validate

Run from a clean checkout:

```bash
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

Also run:

• migration validation;
• OpenAPI validation;
• secret scan;
• dependency scan;
• license scan;
• SBOM generation;
• relevant E2E smoke test.

Step 7 — Commit

Use focused commits. Suggested initial history:

1. chore: initialize artist arena monorepo
2. docs: add governing product and architecture specifications
3. feat: add domain contracts and database baseline
4. test: add vertical slice and ledger test scaffolds
5. ci: add quality security and preview workflows
6. chore: add github planning and agent operations

Step 8 — Report

Return:

• repository URL;
• default branch;
• commit hashes;
• created branches;
• build/test status;
• GitHub settings applied;
• issues/milestones created;
• open decisions;
• permission limitations;
• unimplemented integrations;
• exact next CodeSpring ticket;
• no claims of deployment or legal approval.

If GitHub write access is unavailable, produce a complete repository bundle and exact push/configuration commands, and state clearly that the GitHub repository was not created.

────────

33. CODESPRING HANDOFF PACKAGE

The first CodeSpring task must not be “build Artist Arena.”

Create an implementation package containing:

• ticket ID;
• objective;
• user story;
• domain context;
• files/modules;
• dependencies;
• API changes;
• schema changes;
• event changes;
• security impact;
• privacy impact;
• financial impact;
• edge cases;
• acceptance criteria;
• required tests;
• commands;
• evidence;
• rollback.

Recommended first CodeSpring ticket:

> Implement the non-financial music battle vertical slice from account creation through final result and rating update, using mock media and Arena Points only, with complete audit events and E2E coverage.

No paid-entry, cash conversion, cash-out, or production payment provider should be included in the first ticket.

────────

34. FINAL MANUS DIRECTIVE

Create Artist Arena as a serious platform foundation, not a disposable prototype.

Preserve the original idea:

• beat and song battles;
• one-to-one credit competition;
• creator access and commerce;
• credit-to-cash conversion;
• Ø’s 1% conversion fee.

Also preserve what Artist Arena has become:

• multi-discipline creative esports;
• creator discovery;
• rankings;
• tournaments;
• streaming;
• community;
• sponsorship;
• scouting;
• subscriptions;
• marketplace;
• analytics;
• Pure Human, Hybrid, and AI Open divisions;
• the competitive infrastructure layer for the global creator economy.

The first repository must make the simple music battle loop buildable now while keeping the larger system possible later.

Architect the money system correctly without pretending it is already cleared to launch. Architect AI participation transparently without banning it or pretending detection is perfect. Architect creator rights so uploads are not silently treated