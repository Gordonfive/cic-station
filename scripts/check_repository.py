#!/usr/bin/env python3
"""Repository validation for Mission Control documentation and safety invariants."""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/README.md",
    "docs/PRODUCT.md",
    "docs/REQUIREMENTS.md",
    "docs/ARCHITECTURE.md",
    "docs/PROGRAM_ROADMAP.md",
    "docs/ROADMAP.md",
    "docs/STATUS.md",
    "docs/decisions/README.md",
]
RETIRED_PATHS = [
    "MISSION_CONTROL.md",
    "docs/PROJECT_START_HERE.md",
    "docs/CONTINUATION_HANDOFF.md",
    "docs/PLANNED_FEATURES.md",
    "docs/coordination/decisions.md",
]
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----"),
    "GitHub classic token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REQ = re.compile(r"\bMC-REQ-\d{4}\b")
ADR_FILE = re.compile(r"ADR-(\d{4})-[a-z0-9-]+\.md$")


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required canonical document: {rel}")
    for rel in RETIRED_PATHS:
        if (ROOT / rel).exists():
            failures.append(f"retired document still present: {rel}")

    requirement_definitions: dict[str, list[pathlib.Path]] = {}
    adr_numbers: dict[str, pathlib.Path] = {}

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"credential pattern {name}: {path.relative_to(ROOT)}")

        if path == ROOT / "docs/REQUIREMENTS.md":
            for req_id in REQ.findall(text):
                requirement_definitions.setdefault(req_id, []).append(path)

        if path.parent == ROOT / "docs/decisions" and path.name != "README.md":
            match = ADR_FILE.fullmatch(path.name)
            if not match:
                failures.append(f"invalid ADR filename: {path.relative_to(ROOT)}")
            else:
                number = match.group(1)
                if number in adr_numbers:
                    failures.append(
                        f"duplicate ADR number {number}: {adr_numbers[number].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                    )
                adr_numbers[number] = path

        if path.suffix == ".md":
            for raw in LINK.findall(text):
                target = raw.strip().split()[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if target and not (path.parent / target).resolve().exists():
                    failures.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")

    for req_id, locations in requirement_definitions.items():
        if len(locations) != 1:
            failures.append(f"duplicate requirement definition: {req_id}")

    requirements_text = (ROOT / "docs/REQUIREMENTS.md").read_text(encoding="utf-8")
    ids = REQ.findall(requirements_text)
    if len(ids) != len(set(ids)):
        failures.append("duplicate MC-REQ identifier in docs/REQUIREMENTS.md")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("Mission Control canonical document/link/requirement/ADR/credential checks: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
