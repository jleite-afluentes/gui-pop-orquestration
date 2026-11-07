# Habilidades por gate

As skills `gui-*` são incluídas neste pacote e instaladas junto com `orquestrar-pop`. Ao executá-las, leia o SKILL.md da skill correspondente no diretório de skills instalado. A skill principal coordena e o owner aprova.

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
