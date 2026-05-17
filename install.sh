#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$ROOT_DIR/skills"
DEST_DIR="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"

usage() {
  cat <<'USAGE'
Usage:
  ./install.sh                 Install every skill
  ./install.sh skill-name      Install one skill
  ./install.sh skill-a skill-b Install selected skills

Set CODEX_SKILLS_DIR to install somewhere other than ~/.codex/skills.
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Missing skills directory: $SKILLS_DIR" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"

if [[ "$#" -gt 0 ]]; then
  skill_names=("$@")
else
  skill_names=()
  for skill_dir in "$SKILLS_DIR"/*; do
    [[ -d "$skill_dir" ]] || continue
    skill_names+=("$(basename "$skill_dir")")
  done
fi

if [[ "${#skill_names[@]}" -eq 0 ]]; then
  echo "No skills found in $SKILLS_DIR" >&2
  exit 1
fi

valid_skill_name() {
  [[ "$1" =~ ^[a-z0-9][a-z0-9-]{0,63}$ ]]
}

installed=0
skipped=0

for name in "${skill_names[@]}"; do
  if ! valid_skill_name "$name"; then
    echo "Invalid skill name: $name" >&2
    exit 1
  fi

  skill_dir="$SKILLS_DIR/$name"
  target="$DEST_DIR/$name"

  if [[ ! -d "$skill_dir" ]]; then
    echo "Missing skill: $name" >&2
    exit 1
  fi

  if [[ -L "$target" ]]; then
    current_target="$(readlink "$target")"
    if [[ "$current_target" == "$skill_dir" ]]; then
      echo "Already installed: $name"
    else
      echo "Skipped existing symlink: $target -> $current_target" >&2
      skipped=$((skipped + 1))
    fi
    continue
  fi

  if [[ -e "$target" ]]; then
    echo "Skipped existing path: $target" >&2
    skipped=$((skipped + 1))
    continue
  fi

  ln -s "$skill_dir" "$target"
  echo "Installed: $name"
  installed=$((installed + 1))
done

echo
echo "Installed $installed skill(s); skipped $skipped existing path(s)."
echo "Restart Codex to pick up installed skills."
