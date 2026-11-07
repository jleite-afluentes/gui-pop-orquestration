#!/bin/sh
set -eu
ORIGEM=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DESTINO="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$DESTINO"
for origem in "$ORIGEM"/skills/*; do
  nome=$(basename "$origem")
  if [ -e "$DESTINO/$nome" ]; then
    printf 'Preservada instalação existente: %s (versão não verificada)\n' "$nome"
  else
    cp -R "$origem" "$DESTINO/"
    printf 'Instalada: %s\n' "$nome"
  fi
done
printf 'Destino: %s\nReinicie o Codex se as skills não aparecerem.\n' "$DESTINO"
