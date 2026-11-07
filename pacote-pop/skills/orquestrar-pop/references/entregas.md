# Entregas e identidade

Markdown contém identificação, versão, alterações da última versão, objetivo, abrangência, responsabilidades, pré-requisitos, etapas, decisões e exceções, registros, referências, glossário e aprovação. Use sujeito responsável, verbos diretos, uma ação por passo quando possível e linguagem cordial. Storytelling dá sequência e contexto sem inventar fatos. Explicar termos no primeiro uso.

Mantenha cenários e FAQ em Markdown próprio, com IDs, versão, fontes, status e ligações ao POP, às atividades e às respostas aprovadas. Questões comuns podem ficar na base da empresa com responsável e versão e ser vinculadas a vários POPs; avalie impactos ao alterá-las. Inclua a FAQ completa no DOCX e no HTML. No PPTX, inclua perguntas prioritárias para o treinamento e indique onde consultar a FAQ completa; apresente a seleção ao owner. A FAQ operacional acompanha a aprovação e a versão do POP. Respostas desconhecidas ficam pendentes.

Solicite manual de marca, logomarca, fontes e templates. Inspecione estrutura e renderização para identificar layouts, estilos, cores, temas, cabeçalhos e assets; registre origem, certeza e lacunas. Não altere originais. Aponte conflitos de legibilidade ao owner.

Use, quando disponíveis, skills `documents:documents`, `pdf:pdf` e `presentations:Presentations` e siga suas instruções vigentes. A apresentação é referência visual e onboarding, não substitui o POP detalhado. Examine páginas e slides renderizados; verifique conteúdo, editabilidade, acessibilidade e marca. Um modelo ou habilidade indisponível é limitação explícita. Para BPMN produza XML editável e imagem e verifique em ferramenta compatível; não presumir que uma sintaxe Mermaid é BPMN XML. HTML deve incluir recursos necessários e ser testado sem rede; PWA fica fora do escopo.

Depois de revisar o conjunto, gere manifesto com `pop.py manifest`; apresente o conteúdo e o hash do manifesto ao owner. Registre aprovação explícita com `pop.py approve`; após qualquer mudança a verificação do manifesto deve acusar divergência. O hash confirma igualdade de arquivos, não identidade ou validade do POP. Preserve arquivos aprovados antes de alterá-los e regenere os afetados.
