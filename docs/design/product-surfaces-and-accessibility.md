# Artist Arena V1: Product Surfaces, Design System, and UX Architecture Specification

## 1. Introduction and Product Vision

This document provides the complete, implementation-grade domain specification for the product surfaces, design system, and UX architecture of Artist Arena V1. Artist Arena is not merely a social media mockup or a loose collection of product ideas; it is the competitive infrastructure layer for the global creator economy. It connects competition, discovery, community, commerce, sponsorship, scouting, and creator infrastructure [1].

The V1 release is strictly build-complete. Every capability described in the product canon—including native mobile applications, native livestreaming, real-money transactions, one-to-one wagers, and a native blockchain—must be fully architected, implemented, integrated, and tested [2]. While gates may control activation, operator exposure, and assurance, they never delay construction [2]. The system separates whether a capability is built from where and when it is activated, ensuring that the V1 codebase contains the full suite of features even if some are initially disabled by policy in certain regions [2].

## 2. Design System and Visual Language

The visual system of Artist Arena must project a premium, cinematic, and creator-forward interface that embodies competitive energy without resorting to cheap gimmicks.

### 2.1 Visual Language Principles

The design system must explicitly avoid:
- Generic “AI SaaS” gradients that dilute the brand's unique identity.
- A casino visual language that implies gambling rather than skill-based competition.
- Misleading win animations around financial activity that could violate compliance or trust.
- Oversaturated gamer neon everywhere, which detracts from the professional aesthetic.
- Template-looking cards with no editorial hierarchy.
- Follower counts dominating skill evidence, as Artist Arena prioritizes verified competitive records over mere popularity [1].

Instead, the visual system must balance:
- High-end music and fashion editorial design.
- Tournament clarity, ensuring that brackets, ladders, and results are instantly legible.
- Strong motion and live-state feedback to convey the excitement of real-time competition.
- Accessible contrast across all themes.
- Dense desktop utility for power users and creators managing their portfolios.
- Clean mobile interaction for on-the-go consumption and participation.
- Discipline-specific art direction without fragmenting the overall product experience [1].

### 2.2 Theming and Tokenization

Create a comprehensive, tokenized design system supporting:
- A dark default theme that aligns with the premium, cinematic vision.
- An accessible light theme for users who prefer or require higher contrast.
- Discipline accents that subtlely differentiate music, visual art, code, etc.
- Sponsor themes that allow brands to customize their sponsored challenges, strictly constrained by accessibility and brand-safety rules.
- Reduced-motion preferences for users sensitive to animations [1].

## 3. Accessible Content Design

Accessibility is a fundamental requirement, integrated from the beginning, not a post-launch add-on. The platform must target WCAG 2.2 AA compliance [3].

### 3.1 Core Accessibility Requirements

- **Keyboard and Screen Reader Operation**: The entire platform must support full keyboard operation and provide visible focus states. Screen readers must be fully supported across all interactive elements [1] [3].
- **Media Accessibility**: Provide captions and transcripts where supplied by creators or sponsors. Ensure text alternatives exist for all meaningful images [3].
- **Audio Player**: The audio player must be accessible, ensuring that waveforms are not required for navigation or comprehension [3].
- **Status Indicators**: Color must never be the only status indicator. Use icons, text, and patterns to convey state changes [3].
- **Clarity and Plain Language**: Use plain-language explanations for money, eligibility, rules, and outcomes to ensure all users understand the stakes and requirements [3].

## 4. Internationalization (i18n), Currency, and Timezone

Artist Arena is a global platform, and its interface must reflect the local context of its users.

### 4.1 Localization Rules

- **Dates and Times**: All dates and times must be localized to the user's current setting [3].
- **Currency**: Currency values must be localized and clearly indicate the underlying asset (e.g., USD, EUR, or specific credits) [3].
- **Timezones**: Timezones must be explicit, especially for live events, submission deadlines, and dispute windows [3].
- **Implementation Strategy**: Use translation-ready message catalogs for all user-facing text. Do not hardcode user-facing copy in domain logic. This ensures that the platform can scale to new languages seamlessly [3].

## 5. Product Surfaces and Information Architecture

### 5.1 Responsive Web and PWA

V1 must be delivered as a responsive web application and an installable Progressive Web App (PWA) [1].

The primary desktop navigation includes:
- **Discover**: The hub for finding new talent, open challenges, and trending content.
- **Battles**: The core competitive arena for one-to-one matches.
- **Tournaments**: Brackets, ladders, and larger competitive structures.
- **Rankings**: Leaderboards separated by discipline, division, and season.
- **Live**: Ongoing events, live scoring, and streams.
- **Marketplace**: Where creators sell access, services, and digital goods.
- **Search**: Comprehensive discovery across users, disciplines, and events.
- **Notifications**: Alerts for challenges, results, and social interactions.
- **Wallet**: The financial hub for managing credits, earnings, and escrow.
- **Profile**: The user's portfolio, competitive record, and settings [1].

A persistent primary action button must allow eligible users to quickly create a battle, issue a challenge, enter an open event, upload a work, or create a listing [1].

### 5.2 Native Mobile V1 Path

Native mobile applications for iOS and Android are mandatory V1 obligations [2]. The architecture must use shared contracts and design tokens so native clients can be added without rewriting the backend [1].

Recommended bottom navigation for mobile:
- **Home**: A personalized feed of discovery and followed creators.
- **Battles**: Quick access to active and upcoming matches.
- **Create**: The primary upload and challenge interface.
- **Live**: Access to ongoing streams and real-time events.
- **Profile**: The user's identity and portfolio [1].

Secondary surfaces such as Wallet, Rankings, Marketplace, Search, and Notifications remain one tap away through the header or a profile sheet [1].

### 5.3 Native Live-Streaming V1 Path

Native livestreaming is a mandatory V1 obligation, even if external embeds are used initially [2].

The V1 live surface must support:
- Embedded external livestreams.
- Scheduled live event pages with countdowns and RSVP functionality.
- Live scoring updates synchronized with the backend.
- Real-time chat with robust moderation tools.
- Replay links available immediately after the event.
- Clips and highlights generated from the stream.
- A battle timeline showing key moments and submissions.
- Judge commentary integrated into the live feed [1].

### 5.4 Admin Console and Trust Operations

The admin console is critical for platform governance and must not be an afterthought.

Administrators must be able to manage:
- Platform configuration and feature flags.
- Discipline templates and scoring rubrics.
- Global and regional policies.
- Staff permissions and role-based access control (RBAC).
- Comprehensive audit reviews [1].

The console must include dedicated tools for moderation, trust analysis, rights claims, and financial/compliance operations. Every privileged action must record staff identity, role, reason, case, previous value, new value, affected resources, timestamp, and approval [1].

## 6. Trusted Money, Escrow, and Financial Ledger

The financial infrastructure is a core component of Artist Arena, governed by strict rules to ensure trust and compliance.

### 6.1 Wallet and Financial Ledger Architecture

Never represent money by updating a single mutable user balance field. Implement a double-entry, append-only ledger with accounts, journal entries, postings, asset/currency codes, fixed-precision minor units, idempotency keys, and reconciliation status [1].

Separate economic instruments must be modeled:
- **Arena Points**: Promotional, non-transferable, and non-withdrawable.
- **Purchased Credits**: Activated where legally approved, with strict redemption rules.
- **Creator Earnings**: Proceeds from sales, services, subscriptions, and eligible prizes.
- **Contest Escrow**: Reserved entry/stake/prize funds that cannot be spent while held.
- **Bonus Credits**: Non-withdrawable with clear expiration rules.
- **Withdrawable Balance**: Provider-backed eligible amount after holds and verification.
- **Reserve / Chargeback Hold**: Temporary risk reserve.
- **Platform Revenue**: Conversion fees, marketplace fees, and other platform accounts [1].

### 6.2 Conversion and Wagering Flows

The conversion engine must support cash to eligible credits and eligible credits/earnings to cash. The founder default platform fee is 1%, which must be configuration-driven and accounted for separately from processor, verification, and network costs [1] [2].

The one-to-one wager flow is a compliance-gated module that must be built in V1:
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
12. Reconciliation and tax records update [1].

### 6.3 Blockchain Anchoring and Provenance

V1 must include a native blockchain or sovereign application-chain implementation. This chain serves creator provenance, competition evidence, programmable rights, digital assets, creator splits, prize escrow, settlement attestations, and economic auditability [2].

Crucially, the architecture must not force large media files or sensitive identity data onto a public ledger. Hashes, commitments, and policy references are stored on-chain, while the actual media and PII remain in secure, compliant off-chain storage [2].

### 6.4 Error and Recovery UX

Error messages, particularly those related to financial transactions, authentication, and permissions, must explain recovery options clearly. They must never expose security internals, stack traces, or underlying provider details to the user [3].

## 7. AI Creator Policy and Divisions

Artist Arena embraces the future of creation while maintaining clear boundaries to protect human craftsmanship. The platform must not ban AI creators but must enforce transparent disclosure [1].

Competitions must support three clearly separated and transparently labeled divisions:
1. **Pure Human**: The prestige and craftsmanship division. Generative creation is strictly prohibited. Ordinary non-generative production tools are allowed when the discipline rulebook permits them [1].
2. **Hybrid**: AI-assisted work is allowed, but human direction, selection, editing, performance, assembly, or transformation remains material. Tools and workflows must be disclosed [1].
3. **AI Open**: Broad generative and automated workflows are allowed. However, “Open” does not mean exempt from copyright, likeness, fraud, or abuse rules. All rights and consent rules still apply [1].

AI must supplement rather than replace human judging. Detection systems may produce signals or request evidence, but they must not be presented as infallible proof or automatically confiscate funds [1].

## 8. User Roles, Permissions, and State Machines

### 8.1 Primary Personas

The UX must cater to distinct personas, each with specific workflows:
- **Competitor Creator**: Uploads work, enters battles, receives ratings, and earns prizes.
- **Audience Member / Fan**: Follows creators, votes, comments, and buys access.
- **Buyer / Client**: Purchases digital products, licenses work, or commissions creators.
- **Judge / Curator**: Scores submissions against disclosed criteria and leaves structured feedback.
- **Organizer**: Creates battles, tournaments, and prize structures.
- **Sponsor / Brand**: Creates sponsored competitions, funds prizes, and discovers creators.
- **Scout / Recruiter**: Searches talent by discipline, rating, and verified work.
- **Moderator / Trust Analyst**: Reviews reports, rights claims, and disputes [1].

### 8.2 Battle Lifecycle State Machine

The battle lifecycle must be governed by a validated state machine. No client may assign states directly.

Standard flow:
`DRAFT → PUBLISHED → MATCHING → ACCEPTED → FUNDING_PENDING → FUNDED → SUBMISSION_OPEN → SUBMISSIONS_LOCKED → REVIEW_PENDING → VOTING_OPEN/JUDGING_OPEN → SCORING → PROVISIONAL_RESULT → DISPUTE_WINDOW → FINAL → SETTLEMENT_PENDING → SETTLED → ARCHIVED` [1].

Exceptional states include `CANCELLED`, `EXPIRED`, `VOIDED`, `DISPUTED`, `UNDER_REVIEW`, `REFUND_PENDING`, `REFUNDED`, and `PAYOUT_HELD` [1]. Every transition must record the actor, timestamp, previous state, next state, reason code, and policy evaluation [1].

## 9. Definition of Done (V1)

Artist Arena V1 is considered build-complete only when the full product loop operates seamlessly across identity, creator profiles, media, battles, challenges, tournaments, rankings, judging, audience participation, discovery, community, sponsorship, scouting, marketplace, creator commerce, native blockchain, credits, paid entry, one-to-one wagers, prize escrow, settlement, conversion, cash-out, disputes, moderation, rights, compliance, analytics, support, and operations [2].

Production deployment may expose different features by operator and jurisdiction, but the underlying V1 platform must not require a later architectural rebuild to activate any of these capabilities [2].

## 10. References

[1] ARTIST-ARENA-V1-Master-Specification.md
[2] 0001-v1-build-complete.md
[3] ARTIST-ARENA-V1-Master-Specification.md (Lines 2880-2897)
