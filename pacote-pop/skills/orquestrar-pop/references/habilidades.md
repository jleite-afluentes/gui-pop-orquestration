# Habilidades por gate

As skills `gui-*` são incluídas neste pacote e instaladas junto com `orquestrar-pop`. Para cada gate, priorize as skills originais disponíveis e autorizadas abaixo, lendo seus SKILL.md e dependências; use as `gui-*` para os contratos específicos de POP ou como instruções locais de apoio quando a skill original não estiver disponível. As skills `gui-*` não substituem as originais e não provam equivalência funcional. A skill principal coordena e o owner aprova.

| Gate | Skills originais a localizar e verificar |
|---|---|
| Preparação e investigação | `pd-research`, `pd-methods`, `pd-ux-service`, `pd-grilling` e `grilling` |
| Modelagem e melhoria | `pd-business-analysis`, `pd-methods`, `pd-ux-service` |
| Redação e crítica | `pd-documentation`, `pd-quality-review`, `pd-grilling` |
| Produção e verificação | `pd-presentations`, `documents:documents`, `pdf:pdf`, `presentations:Presentations` |
| Aprovação e registro | `pd-quality-review`, `pd-business-analysis` |

As cópias de desenvolvimento `pd-*` podem depender de `pd-orchestrator`, seu CLI, agentes e contexto de projeto; verificar o contrato e não afirmar integração funcional até testá-la. Não altere essas skills para omitir dependências. A disponibilidade é específica de cada ambiente.

| Gate | Skills incluídas | Responsabilidade | Dependências externas |
|---|---|---|---|
| Preparação | `gui-conhecimento`, `gui-investigacao` | Identidade, base, fontes, cultura e marca | Acesso autorizado ao Drive |
| Investigação | `gui-investigacao`, `gui-melhoria` | Perguntas, SIPOC, Design Thinking, serviços, DMAIC e análise de problemas quando cabível | Entrevistas e fontes reais quando necessárias |
| Modelagem | `gui-processos`, `gui-melhoria` | BPMN, RACI, regras, exceções, restrições e robustez | Ferramenta de BPMN XML e visualização ainda a selecionar e testar |
| Validação do processo | `gui-revisao`, `gui-processos`, `gui-conhecimento` | Crítica independente, vínculos e decisões do owner | Editor BPMN para verificar abertura |
| Redação e crítica | `gui-redacao`, `gui-revisao` | Linguagem simples, storytelling, cenários, FAQ e crítica | Fontes e ferramentas de leitura pertinentes |
| Produção e verificação | `gui-entregas`, `gui-revisao` | Identidade visual, documentos, slides, HTML e inspeção | `documents:documents`, `pdf:pdf`, `presentations:Presentations` ou alternativas verificadas; ferramentas de HTML e BPMN |
| Aprovação e registro | `gui-conhecimento`, `gui-revisao` | Manifesto, rastreabilidade e apresentação ao owner | Acesso à base e ferramentas de verificação |

Grill-with-docs e Laya são candidatos opcionais externos, não inclusos nem automaticamente instalados. As skills incluídas trazem método de perguntas e triagem humana, sem alegar incorporar o código desses projetos. Nunca afirmar que uma dependência externa está disponível sem conferência. Caso uma capacidade seja indispensável e indisponível, registrar bloqueio e uma alternativa viável; não tratar artefatos não produzidos como concluídos.
