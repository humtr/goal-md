#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
skill_name="goal-md"
profile=""

usage() {
  cat <<USAGE
Usage: $(basename "$0") [--profile NAME]

Installs goal-md into ~/.codex/skills/goal-md by default.
Use --profile NAME to install into ~/.codex-profiles/NAME/skills/goal-md.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile)
      profile="${2:-}"
      if [[ -z "$profile" ]]; then
        echo "error: --profile requires a name" >&2
        exit 1
      fi
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -n "$profile" ]]; then
  target_root="$HOME/.codex-profiles/$profile/skills"
else
  target_root="$HOME/.codex/skills"
fi

target="$target_root/$skill_name"
mkdir -p "$target_root"
rm -rf "$target"

if ln -s "$repo_root" "$target" 2>/dev/null; then
  echo "installed $skill_name via symlink at $target"
else
  mkdir -p "$target"
  cp -a "$repo_root"/. "$target"/
  echo "installed $skill_name via copy at $target"
fi
