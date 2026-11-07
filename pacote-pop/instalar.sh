#!/bin/sh
set -eu
ORIGEM=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DESTINO="${CODEX_HOME:-$HOME/.codex}/skills"
for origem in "$ORIGEM"/skills/*; do
  nome=$(basename "$origem")
  if [ -e "$DESTINO/$nome" ]; then
    printf 'Já existe uma instalação em %s. Nenhum arquivo foi alterado.\n' "$DESTINO/$nome" >&2
    exit 1
  fi
done
mkdir -p "$DESTINO"
for origem in "$ORIGEM"/skills/*; do
  cp -R "$origem" "$DESTINO/"
done
printf 'Skills instaladas em %s\nReinicie o Codex se não aparecerem.\n' "$DESTINO"
