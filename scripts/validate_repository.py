from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "README.md", "README.en.md", "docs/install.md", "docs/update.md",
    "docs/uninstall.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "SECURITY.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "llms.txt",
    ".github/FUNDING.yml",
]


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing: {relative}")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\nname:" not in skill or "\ndescription:" not in skill:
        errors.append("SKILL.md frontmatter is invalid")
    if re.search(r"[A-Z]:\\Users\\(?!<[^>]+>\\)[^\\\r\n]+\\|[A-Z]:\\(?:Codex|Godot)\\", skill, re.I):
        errors.append("SKILL.md contains a private absolute path")
    if errors:
        print("\n".join(errors))
        return 1
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
