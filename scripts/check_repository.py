#!/usr/bin/env python3
"""Repository-only validation for Mission Control migration state."""
from __future__ import annotations
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = ["AGENTS.md", "README.md", "MISSION_CONTROL.md", "docs/PROJECT_START_HERE.md", "docs/ROADMAP.md", "docs/CONTINUATION_HANDOFF.md"]
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----"),
    "GitHub classic token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def main() -> int:
    failures = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required recovery document: {rel}")
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
        if path.suffix == ".md":
            for raw in LINK.findall(text):
                target = raw.strip().split()[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if target and not (path.parent / target).resolve().exists():
                    failures.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Mission Control recovery-document/link/credential checks: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
