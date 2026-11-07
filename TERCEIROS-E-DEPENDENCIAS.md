# Terceiros e dependências

A licença MIT da raiz abrange contribuições próprias de João Leite ao projeto; materiais de terceiros mantêm seus próprios avisos e condições. A presença de uma referência não significa que o componente está instalado ou incluído na distribuição.

| Componente | Origem e versão | Situação e condições |
|---|---|---|
| `pd-methods`, `pd-ux-service`, `pd-business-analysis`, `pd-grilling`, `pd-documentation`, `pd-quality-review`, `pd-research`, `pd-presentations` | Cópias locais de `~/.agents/skills`; revisão upstream não identificada. | Incluídas com licença MIT de João Leite, conforme autorização expressa do titular. Recursos originais preservados. `pd-grilling` conserva sua atribuição e licença MIT de Matt Pocock. Algumas capacidades dependem do ambiente, agentes ou outras skills. |
| `pd-orchestrator` | Cópia de `~/.agents/skills/pd-orchestrator`; revisão não identificada. | Incluída sob MIT com autorização do titular; configuração local de runtime excluída. Laya, agentes e dependências externas exigem instalação e validação. |
| `grilling` | Cópia local de `~/.codex/skills`; revisão upstream não identificada. | Cópia local ignorada pelo Git; procedência e condições da cópia instalada precisam ser confirmadas antes da redistribuição. |
| `grill-with-docs` | https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs | Repositório sob MIT, copyright Matt Pocock; não incluída nesta versão. Requer `grilling` e `domain-modeling`; obter versão fixada e preservar licença antes de distribuir. |
| `documents:documents` | Plugin Documents do ambiente Codex, versão observada 26.1104.22356 | A licença instalada restringe cópia e redistribuição; não incluída. Usar o plugin autorizado no ambiente. |
| `presentations:Presentations`, `pdf:pdf` | Plugins Presentations e PDF do ambiente Codex, versão observada 26.1104.22356 | Não incluídos; condições de redistribuição e dependências devem ser verificadas com o fornecedor. Usar os plugins disponíveis e autorizados. |
| BPMN | Ferramenta a selecionar | Nenhuma ferramenta BPMN incluída ou testada; dependência externa para XML editável e verificação. |
| Laya | Opcional | Não incluído, não configurado nem avaliado para este projeto. |

O inventário não constitui confirmação de licença ou autorização para redistribuir. A matriz operacional está em `pacote-pop/skills/orquestrar-pop/references/habilidades.md`.
