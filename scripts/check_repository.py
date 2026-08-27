#!/usr/bin/env python3
"""Repository validation for CIC Station documentation and safety invariants."""
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
    "VERSION",
    "BUILD_NUMBER",
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
    "config/task.example.yaml",
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
REQ = re.compile(r"MC-REQ-\d{4}")
REQ_TOKEN = re.compile(r"\bMC-REQ-[A-Za-z0-9_-]+\b")
REQ_DEFINITION = re.compile(r"(?m)^- \*\*(MC-REQ-[A-Za-z0-9_-]+)\b")
ADR_FILE = re.compile(r"ADR-(\d{4})-[a-z0-9-]+\.md$")
ADR_INDEX_ENTRY = re.compile(r"(?m)^- `(ADR-\d{4}-[a-z0-9-]+\.md)`")
SEMVER = re.compile(
    r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)
BUILD_ID = re.compile(r"\d{4,}$")


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required canonical document: {rel}")
    for rel in RETIRED_PATHS:
        if (ROOT / rel).exists():
            failures.append(f"retired document still present: {rel}")

    version_path = ROOT / "VERSION"
    if version_path.is_file() and not SEMVER.fullmatch(version_path.read_text(encoding="utf-8").strip()):
        failures.append("VERSION must contain a valid Semantic Versioning version")

    build_path = ROOT / "BUILD_NUMBER"
    if build_path.is_file() and not BUILD_ID.fullmatch(build_path.read_text(encoding="utf-8").strip()):
        failures.append("BUILD_NUMBER must contain a numeric build identifier of at least four digits")

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

    requirements_path = ROOT / "docs/REQUIREMENTS.md"
    if requirements_path.is_file():
        requirements_text = requirements_path.read_text(encoding="utf-8")

        invalid_ids = sorted({token for token in REQ_TOKEN.findall(requirements_text) if not REQ.fullmatch(token)})
        for req_id in invalid_ids:
            failures.append(f"invalid requirement identifier: {req_id}")

        definitions = REQ_DEFINITION.findall(requirements_text)
        valid_definitions = [req_id for req_id in definitions if REQ.fullmatch(req_id)]
        seen: set[str] = set()
        duplicate_definitions: set[str] = set()
        for req_id in valid_definitions:
            if req_id in seen:
                duplicate_definitions.add(req_id)
            seen.add(req_id)
        for req_id in sorted(duplicate_definitions):
            failures.append(f"duplicate requirement definition: {req_id}")

    adr_index_path = ROOT / "docs/decisions/README.md"
    if adr_index_path.is_file():
        indexed_names = ADR_INDEX_ENTRY.findall(adr_index_path.read_text(encoding="utf-8"))
        counts: dict[str, int] = {}
        for name in indexed_names:
            counts[name] = counts.get(name, 0) + 1
        for name, count in sorted(counts.items()):
            if count > 1:
                failures.append(f"duplicate ADR index entry: {name}")

        actual_names = {path.name for path in adr_numbers.values()}
        indexed_set = set(indexed_names)
        for name in sorted(actual_names - indexed_set):
            failures.append(f"ADR missing from index: {name}")
        for name in sorted(indexed_set - actual_names):
            failures.append(f"ADR index references missing file: {name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("CIC Station canonical document/link/requirement/ADR/version/build/credential checks: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
