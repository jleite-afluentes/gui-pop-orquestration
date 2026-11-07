# Pacote de orquestração de POP — Gui 0.3.0

Skill para Codex com instruções, referências e controles locais em Python 3.9+. O pacote não contém dados de empresas, nem instala ferramentas externas ou modelos de IA. Não é necessário Laya para usá-lo.

## Instalação por participante

1. Descompacte o pacote em local de sua escolha.
2. No terminal, execute `./instalar.sh`. O script instala a skill principal e sete skills especializadas em `${CODEX_HOME:-~/.codex}/skills` e não sobrescreve instalações existentes.
3. Reinicie o Codex se necessário e invoque `$orquestrar-pop`, indicando a pasta da empresa no Google Drive. A skill solicitará os insumos e conduzirá os gates.

Cada participante precisa de acesso autorizado à pasta da empresa e das ferramentas de criação de DOCX, PDF, PPTX e BPMN. O instalador não fornece essas ferramentas; sua disponibilidade e capacidade de gerar os formatos na pasta devem ser verificadas no ambiente. Laya, se escolhido futuramente, requer instalação e avaliação independentes.

O Gui se apresenta e confirma a pessoa e a empresa; apoia investigação com SIPOC e, quando pertinente, DMAIC; e orienta a manutenção de cenários e FAQ versionada. Mudanças da skill constam em `skills/orquestrar-pop/references/versoes.md`. Para atualizar uma instalação existente, faça uma cópia de segurança, remova da pasta de skills as versões antigas das skills deste pacote e execute o instalador; ele não sobrescreve instalações.

## Controles

`python3 skills/orquestrar-pop/scripts/pop.py --help` apresenta os comandos locais. Eles criam estruturas, validam referências declaradas, geram e verificam manifestos, registram aprovação autodeclarada e reservas locais. Não criam automaticamente os documentos finais, não validam semântica ou BPMN e não garantem bloqueio distribuído na sincronização do Drive. Não inclua dados sensíveis em argumentos de comandos compartilhados.

O arquivo `ARQUITETURA-E-CRITERIOS.md` acompanha o pacote como referência de projeto. A implementação é inicial: geração de artefatos depende das skills e ferramentas disponíveis; não há grafo automático, máquina de estados executável, análise semântica, detecção garantida de conflitos distribuídos ou integração Laya. O piloto posterior deverá verificar o fluxo integral e os limites de cada ambiente.

## Habilidades por gate

A matriz em `skills/orquestrar-pop/references/habilidades.md` relaciona investigação, modelagem, melhoria, redação, revisão, entregas e gestão do conhecimento aos gates. As sete skills especializadas acompanham o pacote; os mecanismos externos de produção de DOCX, PDF, PPTX e BPMN não estão incluídos.
