# Artist Arena: AI Divisions, Provenance, and Trust Specification

## 1. Introduction

This document outlines the architecture, rules, and implementation details for Artist Arena's AI divisions, provenance tracking, and trust systems. It is designed to guide engineering teams, including CodeSpring, in building the complete V1 capabilities required by the product canon and Owner Directive 0001.

Artist Arena embraces AI as a creative tool while maintaining clear boundaries to protect human craftsmanship, ensure fair competition, and respect intellectual property and likeness rights. The system must support Pure Human, Hybrid, and AI Open divisions, with robust provenance, disclosure, and evidence mechanisms backed by blockchain anchoring. The architecture must be discipline-agnostic, supporting music, visual art, writing, and other creative fields from day one.

## 2. AI Divisions and Competition Rules

Competitions in Artist Arena must support three distinct divisions, each with its own rules and evidence requirements. These divisions ensure that creators are evaluated fairly against peers using similar tools and methodologies.

### 2.1 Pure Human Division

The Pure Human division represents the prestige and craftsmanship tier of Artist Arena. In this division, generative AI creation is strictly prohibited. The focus is entirely on human skill, execution, and traditional creative processes. While generative AI is banned, ordinary non-generative production, editing, mixing, mastering, color correction, cleanup, and accessibility tools may be allowed when the specific discipline rulebook permits them.

Evidence requirements in this division are exceptionally high. Competitors may be required to submit raw files, detailed project files such as DAW sessions, comprehensive screen recordings, or other definitive proof of human execution. Enforcement is correspondingly strict. Any submissions flagged by automated detection signals or human judges will immediately require manual review and rigorous evidence validation before being allowed to proceed in the competition.

### 2.2 Hybrid Division

The Hybrid division acknowledges the reality of modern creative workflows where AI-assisted work is common and often necessary. In this division, generative AI tools are permitted for ideation, asset generation, or processing. However, a critical requirement is that human direction, selection, editing, performance, assembly, or transformation must remain material and central to the final output. The AI acts as an assistant or tool, not the primary creator.

To maintain transparency, this division mandates strict disclosure requirements. Creators must explicitly disclose the tools used, the workflow categories involved, and the specific role AI played in the creation process. Evidence requirements are medium; competitors must provide the required disclosures upfront and may need to submit evidence demonstrating the human transformation process if their submission is challenged during the competition.

### 2.3 AI Open Division

The AI Open division is designed for broad generative and automated workflows. Here, creators can leverage any AI or automated tool to produce their submissions. This division celebrates prompt engineering, algorithmic generation, and advanced AI curation.

However, "Open" does not mean exempt from the platform's core rules regarding copyright, likeness, fraud, or abuse. All submissions, regardless of how they were generated, must respect intellectual property rights and consent requirements. While the evidence requirements for the creation process itself are low, the requirements for rights clearance and consent are exceptionally high, especially if the submission utilizes specific likenesses, voices, or protected materials.

## 3. Provenance and Disclosure

Provenance tracking is a foundational capability for establishing the origin, creation process, and authenticity of submissions across all divisions.

### 3.1 Disclosure Workflows

During the upload process, creators must select their target division and complete a comprehensive disclosure form. The platform maintains a dynamic registry of known AI and creation tools. Creators can select tools directly from this registry or manually enter new ones if they are not listed. For Hybrid submissions, creators are required to provide a detailed narrative describing how AI was utilized and the specific extent of human involvement in shaping the final work.

### 3.2 Evidence Bundles

An evidence bundle is a secure collection of files, metadata, and attestations submitted alongside the primary work to definitively prove its origin and compliance with division rules. These bundles may contain raw media files such as audio stems or unedited photographs, complex project files like Ableton Live sets or Premiere Pro projects, continuous screen recordings, creation logs, and cryptographic signatures generated directly by creation tools where available.

Evidence bundles are stored securely using encrypted object storage. Access is strictly controlled via role-based access control (RBAC) and is only granted to authorized judges, trust analysts, or moderators during active disputes, audits, or mandated review processes.

## 4. Human Judging and AI Assistance

A core principle of Artist Arena is that AI must supplement, rather than replace, human judging. The final evaluation of creative work remains a human endeavor.

### 4.1 AI Detection Signals

The platform utilizes advanced AI detection systems to provide judges and moderators with probabilistic indicators of AI generation or manipulation. It is crucial to understand that these detection signals are not infallible proof. They are presented as supplementary data points, complete with confidence scores and clear, human-readable explanations of exactly what anomaly or pattern was detected.

High-confidence signals indicating AI use in a Pure Human division submission may trigger automated workflows. These workflows can automatically request comprehensive evidence bundles from the creator or route the submission for mandatory manual review by a trust analyst before any human judging begins.

### 4.2 Human Judge Role

Judges are responsible for evaluating submissions based on established, discipline-specific criteria. They must incorporate AI detection signals and review evidence bundles as part of their holistic assessment. Judges are required to provide structured, constructive feedback and must formally declare any conflicts of interest before scoring a submission.

## 5. Trust, Rights, and Impersonation

Artist Arena is committed to protecting creators' rights and preventing the unauthorized use of their likeness, voice, or original work.

### 5.1 Impersonation and Likeness

Unauthorized voice cloning, deepfakes, or style mimicry intended to deceive the audience or exploit a specific creator's identity are strictly prohibited across all divisions, including AI Open. Any submission utilizing a recognized creator's likeness or voice must include verifiable consent metadata. If this metadata is absent, the submission will be automatically flagged for immediate manual review and potential disqualification. Enforcement relies on a combination of automated scanning for known protected likenesses, community reporting mechanisms, and dedicated manual review teams.

### 5.2 Rights and Licensing

Creators bear the ultimate responsibility for clearing all samples, assets, and AI training data utilized in their submissions. While the platform secures the necessary rights to host, display, and promote the submissions for the purpose of the competition, creators retain full ownership of their original work. The platform architecture must support programmable representations of licensing terms and revenue splits, ensuring that all contributors are fairly compensated.

## 6. Blockchain Anchoring

Blockchain technology is utilized to create an immutable, auditable record of provenance, rights, and competition outcomes. Crucially, large media files and sensitive personally identifiable information (PII) are never stored directly on the blockchain.

### 6.1 On-Chain Data

The blockchain ledger stores cryptographic hashes of the final submission media and all associated evidence bundles. It records precise timestamps providing proof of existence at the exact moment of submission. Furthermore, it anchors creator declarations, including hashes of the division selection, tool disclosures, and consent attestations. Competition evidence, such as hashes of the governing rulesets, individual judge scores, and the final attested results, are also recorded on-chain. Finally, programmable representations of licensing terms, revenue splits, and the configuration-driven 1% platform conversion fee are managed via smart contracts or native chain modules.

### 6.2 Off-Chain Data

Large media files, including high-resolution audio, video, and images, are stored in traditional cloud object storage. Sensitive PII required for identity verification and compliance is stored in secure, encrypted databases subject to strict data privacy regulations. Detailed project files and raw evidence bundles remain off-chain, with only their cryptographic hashes anchored to the ledger for verification purposes.

## 7. Disputes, Appeals, and Audit

Robust mechanisms are essential for resolving conflicts, handling rules violations, and ensuring the overall integrity of the platform.

### 7.1 Dispute Process

Disputes can be initiated by users, judges, or automated systems flagging a submission for potential rules violations, such as suspected AI use in the Pure Human division or alleged rights infringement. Trust analysts are responsible for reviewing the submission, analyzing the AI detection signals, examining the evidence bundles, and evaluating user reports. Following their investigation, analysts can choose to uphold the submission, request additional evidence from the creator, disqualify the entry entirely, or apply specific penalties as defined by the platform rules.

### 7.2 Appeals

Creators have the right to appeal disqualifications or penalties. The appeal process requires the creator to provide additional, compelling evidence or detailed clarification regarding their submission. Appeals are escalated and reviewed by a senior moderator or a dedicated, independent appeals panel to ensure fairness and objectivity.

### 7.3 Auditability

The platform maintains comprehensive, tamper-evident system logs detailing all moderation actions, judge scoring events, and automated system flags. Because critical data is anchored to the blockchain, anyone can independently verify the integrity of a submission or a competition result. This is achieved by taking the off-chain data, generating its cryptographic hash, and comparing it against the immutable on-chain record.

## 8. Implementation Details

This section details the specific technical implementations required for the V1 build.

### 8.1 State Machines

The lifecycle of a submission and a dispute must be strictly managed by robust state machines.

| Entity | States | Transitions |
| :--- | :--- | :--- |
| Submission | `DRAFT`, `SUBMITTED`, `IN_REVIEW`, `ACCEPTED`, `REJECTED`, `JUDGING`, `FINALIZED`, `DISQUALIFIED` | `DRAFT` -> `SUBMITTED` -> `IN_REVIEW` (optional) -> `ACCEPTED` / `REJECTED`. `ACCEPTED` -> `JUDGING` -> `FINALIZED` / `DISQUALIFIED`. |
| Dispute | `OPEN`, `UNDER_INVESTIGATION`, `EVIDENCE_REQUESTED`, `RESOLVED_UPHELD`, `RESOLVED_REJECTED` | `OPEN` -> `UNDER_INVESTIGATION` -> `EVIDENCE_REQUESTED` -> `RESOLVED_UPHELD` / `RESOLVED_REJECTED`. |

### 8.2 API and Event Implications

The backend architecture must expose specific RESTful endpoints and emit domain events to support these workflows.

| Type | Name | Description |
| :--- | :--- | :--- |
| API | `POST /api/v1/submissions` | Accepts media payloads, division selections, and detailed disclosure data. |
| API | `POST /api/v1/evidence` | Handles the secure upload of large evidence bundles. |
| API | `GET /api/v1/submissions/{id}/provenance` | Aggregates and returns both on-chain and off-chain provenance data for a specific submission. |
| Event | `SubmissionCreated` | Emitted when a new submission is successfully recorded. |
| Event | `EvidenceRequested` | Emitted when a trust analyst or automated system requests an evidence bundle. |
| Event | `DetectionSignalGenerated` | Emitted when the AI detection pipeline completes its analysis of a submission. |
| Event | `DisputeOpened` | Emitted when a new dispute is initiated. |
| Event | `ResultAnchored` | Emitted when competition results are successfully written to the blockchain ledger. |

### 8.3 Security and Privacy

Evidence bundles often contain sensitive intellectual property and must be encrypted at rest using strong cryptographic standards (e.g., AES-256). Access to these bundles must be strictly governed by RBAC, ensuring that only authorized personnel can view them during active investigations. Furthermore, the AI detection models utilized by the platform must be continuously monitored and regularly updated to counter emerging adversarial evasion techniques designed to bypass detection.

## 9. V1 Definition of Done

The V1 implementation of AI Divisions, Provenance, and Trust is considered complete when the following criteria are met:

1. All three divisions (Pure Human, Hybrid, AI Open) are fully functional, featuring division-specific upload flows and mandatory disclosure requirements.
2. The secure upload, encrypted storage, and RBAC-gated retrieval of evidence bundles are fully implemented and tested.
3. AI detection signals are successfully integrated into the platform and are clearly visible to authorized judges and moderators within their respective interfaces.
4. Blockchain anchoring of submission hashes, creator disclosures, and final competition results is active and verifiable on the selected V1 chain or testnet.
5. The complete dispute and appeals workflows are operational, providing trust analysts with the necessary internal dashboards to manage cases.
6. The locked product requirement of a 1% default conversion fee is configurable within the system and correctly applied to any economic transactions related to these divisions.

## 10. Dependency-Ordered Work Packages

The engineering effort should be executed in the following dependency-ordered sequence:

1. **Core Schema & Storage:** Design and implement the relational database schemas for submissions, divisions, disclosures, and evidence metadata. Provision and configure the secure, encrypted object storage for evidence bundles.
2. **Upload & Disclosure Flow:** Develop the user interfaces and supporting APIs enabling creators to select their division, declare tools from the registry, and upload their submissions and evidence.
3. **AI Detection Integration:** Integrate with selected third-party AI detection APIs or deploy internal models. Implement the pipeline to store these signals against the corresponding submissions.
4. **Moderation & Dispute Tools:** Build the internal administrative dashboards required by trust analysts to review detection signals, access evidence bundles, and manage the lifecycle of disputes.
5. **Blockchain Anchoring:** Develop the blockchain adapters required to generate cryptographic hashes of submission data and anchor these records to the chosen blockchain network.
6. **Judging Interface:** Update the existing judging user interface to prominently display creator disclosures, AI detection signals, and provide secure access to evidence bundles based on the judge's RBAC permissions.

## 11. Unresolved Architectural Decision Records (ADRs)

The following architectural decisions remain open and require resolution by the engineering team during the V1 build phase:

- **ADR-015:** Final selection and vendor approval of the specific AI detection providers for both audio and visual content analysis.
- **ADR-016:** Final technical evaluation and selection of the exact blockchain network or Layer 2 scaling solution for V1 data anchoring.
- **ADR-017:** Definition of the data retention policy for large evidence bundles after a competition has officially concluded and all dispute windows have closed.
