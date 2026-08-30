#!/usr/bin/env python3
"""Validate Artist Arena repository invariants without network access."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "docs/source/ARTIST-ARENA-V1-Master-Specification.md"
EXPECTED_SHA256 = "6fe9ba6637165d43d3ab606e54aaed07104aff69e2b5717046ae26b4d4d18fa5"

REQUIRED_FILES = [
    "README.md", "CODESPRING.md", "AGENTS.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md", "CODEOWNERS",
    "artist-arena-bootstrap.json",
    "docs/owner-directives/0001-v1-build-complete.md",
    "docs/source/ARTIST-ARENA-V1-Master-Specification.md", "docs/source/README.md",
    "docs/requirements/requirements-register.md", "docs/backlog/v1-160-tickets.md", "docs/adr/README.md",
    "docs/architecture/01-system-architecture.md", "docs/architecture/state-machines.md",
    "docs/architecture/native-blockchain.md", "docs/data/domain-model.md",
    "docs/api/contracts-and-events.md", "docs/api/contract-first-engineering-baseline.md",
    "docs/domains/competition-domain.md", "docs/domains/creator-community.md",
    "docs/economy/ledger-and-accounting.md", "docs/economy/credits-wallet-conversions-and-payouts.md",
    "docs/economy/paid-competition-and-wagers.md", "docs/economy/marketplace-and-creator-settlement.md",
    "docs/blockchain/escrow-attestation-and-settlement.md", "docs/compliance/activation-policy-engine.md",
    "docs/security/security-and-privacy-architecture.md", "docs/testing/quality-gauntlet.md",
    "docs/validation/repository-readiness.md", ".agents/PROJECT_MEMORY.md", "packages/contracts/openapi.yaml",
    "docs/schemas/domain-event.schema.json", "docs/schemas/work-package.schema.json",
]

REQUIRED_DIRECTORIES = [
    "apps/web", "apps/admin", "apps/api", "apps/realtime", "apps/workers",
    "packages/auth", "packages/config", "packages/contracts", "packages/db", "packages/domain",
    "packages/events", "packages/feature-flags", "packages/ledger", "packages/media",
    "packages/notifications", "packages/observability", "packages/policy", "packages/ratings",
    "packages/security", "packages/testing", "packages/ui", "packages/validation", "packages/chain",
    "packages/wallet", "packages/economy", "packages/contests", "packages/provenance", "packages/compliance",
    "chain/node", "chain/runtime", "chain/modules", "chain/indexer", "chain/explorer", "chain/testnet",
    "db/migrations", "db/seeds", "tests/contract", "tests/e2e", "tests/chain", "tests/ledger",
]

REQUIRED_V1_TERMS = [
    "native blockchain", "wallet", "one-to-one", "wager", "escrow", "cash-out",
    "1%", "native mobile", "native streaming", "public API", "V1-BUILD-REQUIRED",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def add(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def table_first_column_ids(path: Path, pattern: re.Pattern[str]) -> list[str]:
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        columns = [part.strip() for part in line.split("|")[1:-1]]
        if columns and pattern.fullmatch(columns[0]):
            ids.append(columns[0])
    return ids


def validate() -> list[str]:
    errors: list[str] = []

    add(errors, MASTER.is_file(), "Missing canonical master specification")
    if MASTER.is_file():
        add(errors, sha256(MASTER) == EXPECTED_SHA256, "Canonical master specification checksum mismatch")

    for relative in REQUIRED_FILES:
        add(errors, (ROOT / relative).is_file(), f"Missing required file: {relative}")
    for relative in REQUIRED_DIRECTORIES:
        add(errors, (ROOT / relative).is_dir(), f"Missing required directory: {relative}/")

    for relative in ["README.md", "CODESPRING.md", "docs/owner-directives/0001-v1-build-complete.md"]:
        path = ROOT / relative
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for term in REQUIRED_V1_TERMS:
                add(errors, term.lower() in text, f"{relative} does not state mandatory V1 term: {term}")

    requirements_path = ROOT / "docs/requirements/requirements-register.md"
    requirement_pattern = re.compile(r"AA-[A-Z]+-[0-9]{3}")
    requirement_ids: list[str] = []
    if requirements_path.is_file():
        requirement_ids = table_first_column_ids(requirements_path, requirement_pattern)
        add(errors, len(requirement_ids) == 120, f"Expected 120 requirement rows, found {len(requirement_ids)}")
        add(errors, len(set(requirement_ids)) == 120, "Requirement IDs are not unique")
        text = requirements_path.read_text(encoding="utf-8")
        add(errors, text.count("V1-BUILD-REQUIRED") >= 120, "Every requirement must be V1-BUILD-REQUIRED")

    backlog_path = ROOT / "docs/backlog/v1-160-tickets.md"
    ticket_pattern = re.compile(r"AA-[0-9]{4}")
    if backlog_path.is_file():
        ticket_ids = table_first_column_ids(backlog_path, ticket_pattern)
        expected = [f"AA-{number:04d}" for number in range(1, 161)]
        add(errors, ticket_ids == expected, "Backlog must contain AA-0001 through AA-0160 exactly once and in order")
        backlog_text = backlog_path.read_text(encoding="utf-8")
        referenced = set(re.findall(r"\bAA-[A-Z]+-[0-9]{3}\b", backlog_text))
        unresolved = sorted(referenced.difference(requirement_ids))
        add(errors, not unresolved, f"Backlog references unknown requirement IDs: {', '.join(unresolved)}")
        add(errors, "..." not in backlog_text and "Skipping detailed" not in backlog_text, "Backlog contains placeholder omissions")

    adr_files = [p for p in (ROOT / "docs/adr").glob("[0-9][0-9][0-9][0-9]-*.md") if not p.name.startswith("0000-")]
    add(errors, len(adr_files) == 45, f"Expected 45 individual ADR records, found {len(adr_files)}")
    adr_index = ROOT / "docs/adr/README.md"
    if adr_index.is_file():
        add(errors, len(re.findall(r"^\| ADR-[0-9]{4} ", adr_index.read_text(encoding="utf-8"), re.MULTILINE)) == 45,
            "ADR index must contain 45 decision rows")

    for json_path in list(ROOT.rglob("package.json")) + list((ROOT / "docs/schemas").glob("*.json")) + [ROOT / "artist-arena-bootstrap.json"]:
        try:
            parsed_json = json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in {json_path.relative_to(ROOT)}: {exc}")
            continue
        if json_path.name == "artist-arena-bootstrap.json":
            add(errors, parsed_json.get("canonical_source", {}).get("sha256") == EXPECTED_SHA256,
                "Bootstrap manifest contains the wrong canonical source checksum")
            counts = parsed_json.get("counts", {})
            add(errors, counts.get("build_complete_v1_requirements") == 120,
                "Bootstrap manifest must declare 120 requirements")
            add(errors, counts.get("v1_implementation_tickets") == 160,
                "Bootstrap manifest must declare 160 implementation tickets")
            add(errors, counts.get("individual_adrs") == 45,
                "Bootstrap manifest must declare 45 individual ADRs")

    markdown_link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for markdown_path in ROOT.rglob("*.md"):
        if markdown_path == MASTER:
            continue
        text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        for raw in markdown_link.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative = target.split("#", 1)[0]
            if relative:
                resolved = (markdown_path.parent / relative).resolve()
                add(errors, resolved.exists(), f"Broken local link in {markdown_path.relative_to(ROOT)}: {target}")

    scan_suffixes = {".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".ts", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path == MASTER or path.suffix.lower() not in scan_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            add(errors, pattern.search(text) is None, f"Potential secret pattern in {path.relative_to(ROOT)}")

    derived_markdown = [p for p in (ROOT / "docs").rglob("*.md") if p != MASTER]
    total_words = sum(len(p.read_text(encoding="utf-8", errors="ignore").split()) for p in derived_markdown)
    add(errors, total_words >= 50000, f"Expected at least 50,000 words of derived documentation, found {total_words}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Artist Arena repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Artist Arena repository validation passed.")
    print(f"Canonical source SHA-256: {EXPECTED_SHA256}")
    print("Requirements: 120")
    print("Implementation tickets: 160")
    print("Individual ADRs: 45")
    return 0


if __name__ == "__main__":
    sys.exit(main())
