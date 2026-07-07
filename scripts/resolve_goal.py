#!/usr/bin/env python3
"""Resolve a human-friendly goal alias to a goal file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_index(root: Path) -> dict[str, Any]:
    index_path = root / "goals" / "index.json"
    with index_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or not isinstance(data.get("goals"), dict):
        raise SystemExit(f"invalid goal index: {index_path}")
    return data


def resolve_goal(root: Path, name: str) -> tuple[str, dict[str, Any]]:
    goals = load_index(root)["goals"]
    if name in goals:
        entry = goals[name]
        if not isinstance(entry, dict):
            raise SystemExit(f"invalid goal entry for {name}")
        return name, entry

    matches = []
    for alias, entry in goals.items():
        if not isinstance(entry, dict):
            continue
        path = str(entry.get("path", ""))
        rel_path = Path(path)
        stem = rel_path.stem
        if name in {
            stem,
            stem.removesuffix("-goal"),
            rel_path.name,
            rel_path.as_posix(),
            path,
        } or stem.startswith(name):
            matches.append((alias, entry))

    if len(matches) == 1:
        return matches[0]
    if matches:
        names = ", ".join(alias for alias, _ in matches)
        raise SystemExit(f"ambiguous goal alias {name!r}: {names}")

    available = ", ".join(sorted(goals)) or "none"
    raise SystemExit(f"unknown goal alias {name!r}; available: {available}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("alias", help="goal alias, for example: codex")
    parser.add_argument(
        "--field",
        choices=("path", "relative-path", "repository", "branch", "resume-prompt", "json"),
        default="path",
    )
    args = parser.parse_args()

    root = repo_root()
    alias, entry = resolve_goal(root, args.alias)
    rel_path = Path(str(entry.get("path", "")))
    abs_path = root / rel_path
    if not abs_path.is_file():
        raise SystemExit(f"goal file not found for {alias}: {abs_path}")

    if args.field == "path":
        print(abs_path)
    elif args.field == "relative-path":
        print(rel_path)
    elif args.field == "repository":
        print(entry.get("repository", ""))
    elif args.field == "branch":
        print(entry.get("branch", ""))
    elif args.field == "resume-prompt":
        print(f"/goal resume {rel_path.name}")
    else:
        print(json.dumps({"alias": alias, **entry, "absolute_path": str(abs_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
