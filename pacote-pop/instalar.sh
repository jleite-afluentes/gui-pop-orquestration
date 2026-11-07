#!/bin/sh
set -eu
ORIGEM=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DESTINO="${CODEX_HOME:-$HOME/.codex}/skills/orquestrar-pop"
if [ -e "$DESTINO" ]; then
  printf 'Já existe uma instalação em %s. Nenhum arquivo foi alterado.\n' "$DESTINO" >&2
  exit 1
fi
mkdir -p "$(dirname "$DESTINO")"
cp -R "$ORIGEM/skills/orquestrar-pop" "$DESTINO"
printf 'Skill instalada em %s\nReinicie o Codex se ela não aparecer.\n' "$DESTINO"
