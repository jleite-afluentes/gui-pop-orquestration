# Especificação do projeto — Orquestração de POP

**Estado:** proposta para validação  
**Data:** 2026-11-07  
**Fonte:** decisões Q1–Q63 registradas na conversa de discovery e síntese confirmada pelo solicitante.  
**Finalidade:** orientar a implementação posterior; esta especificação não aprova POPs nem autoriza a publicação de artefatos.

**Complemento arquitetural:** [Arquitetura e critérios de implementação](ARQUITETURA-E-CRITERIOS.md) detalha contratos, critérios de gate, aprovação, colaboração, economia de tokens, Laya e aceite do piloto, conforme recomendações aprovadas. Quando houver maior detalhe operacional no complemento, aplicá-lo em conjunto com esta especificação.

## 1. Objetivo e escopo

Criar um pacote instalável e reutilizável no Codex para apoiar a elaboração e manutenção de Procedimentos Operacionais Padrão (POPs) de múltiplas organizações. Cada organização mantém uma base própria em pasta compartilhada no Google Drive. Mais de um usuário poderá trabalhar no projeto, com instalação ou configuração da orquestração em seus respectivos ambientes.

Cada POP terá uma referência de conteúdo em Markdown, documento formal DOCX e PDF, apresentação PPTX para treinamento e onboarding, e guia HTML para smartphone. O guia deverá ser legível offline, incluindo seus recursos; a integração e a disponibilidade offline no PWA dependem do aplicativo de destino e não incluem a construção do PWA nesta fase. O conjunto incluirá BPMN editável e representação visual, além de matriz RACI.

## 2. Princípios

- A base de contexto da organização inclui, quando disponíveis, documentos de cultura, políticas, compliance, processos, glossário e identidade visual. Ausências são registradas e investigadas com perguntas; orientações não são inventadas.
- A orquestração separa o processo existente das melhorias propostas. A incorporação de melhorias depende de decisão humana explícita.
- A autoria, a crítica e a aprovação são responsabilidades distintas. Revisores registram achados e podem contestar autores; personas sintéticas não substituem observação ou validação humana.
- O usuário que escreve ou é owner do POP é o único responsável pela aprovação final. Outras pessoas podem ser consultadas; não há exigência de segundo aprovador.
- O conteúdo operacional aprovado é coerente entre os formatos; cada formato adapta apresentação e detalhe a seu público.
- Hipóteses e pendências permanecem identificadas. Apenas informações validadas e autorizadas para reutilização são consolidadas como conhecimento compartilhado.

## 3. Papéis

| Papel | Responsabilidade |
|---|---|
| Usuário / owner | Fornecer e validar informações, participar de decisões de alta complexidade ou criticidade, decidir melhorias e aprovar os artefatos finais. |
| Orquestrador | Conduzir etapas e perguntas, atribuir trabalho, manter estado, fontes, decisões e dependências. |
| Investigação e contexto | Identificar fontes, cultura, lacunas e conflitos; preparar perguntas e registrar respostas. |
| Analista de processos | Separar processo atual e melhoria proposta; modelar BPMN, regras, papéis e RACI. |
| Redator | Elaborar instruções em linguagem simples, natural, objetiva e cordial, com glossário; aplicar comunicação assertiva e storytelling adequados ao conteúdo e ao público. |
| Produção de artefatos | Adaptar o conteúdo aprovado para documento, treinamento e guia móvel, respeitando a marca. |
| Revisor independente | Criticar conteúdo, rastreabilidade, fluxo, linguagem, identidade, acessibilidade e coerência entre entregas; registrar achados. |
| Gestão do conhecimento | Manter identificadores, vínculos, histórico e análise de impacto entre POPs e contexto. |

Papéis de agentes podem ser combinados quando adequado, preservando a independência entre autoria e crítica. A arquitetura e o uso de agentes separados serão definidos na implementação.

## 4. Gates e fluxo

1. **Preparação:** identificar empresa, usuário/owner, objetivo do POP, fontes disponíveis, modelos e assets; confirmar identidade informada e estado do trabalho.
2. **Investigação:** examinar documentos; levantar lacunas e conflitos; realizar perguntas em rodadas; registrar decisões e fontes progressivamente.
3. **Modelagem:** distinguir situação atual e melhorias; produzir BPMN e RACI coerentes, identificando início, fim, papéis, atividades, decisões e exceções conhecidas.
4. **Validação do processo:** envolver o usuário nas decisões críticas ou complexas e nas melhorias; apresentar fluxo e questões abertas. Decisões de baixa e média complexidade poderão ser tomadas pelos agentes conforme seção 5; a validação final permanece com o owner.
5. **Redação e crítica:** elaborar Markdown estruturado, revisar linguagem e rastreabilidade, registrar e tratar achados.
6. **Produção e verificação:** gerar os demais formatos; conferir conteúdo, diagrama, legibilidade e funcionamento real, inclusive HTML sem rede.
7. **Aprovação e registro:** apresentar ao owner o conjunto versionado, síntese de decisões e pendências; registrar sua aprovação e ressalvas; atualizar a base autorizada e preparar o pacote final.

Qualquer etapa pode retornar a uma anterior se surgir informação relevante. Mudanças no fluxo exigem rever BPMN, RACI e artefatos afetados; pedir ao usuário confirmação da parte alterada conforme sua criticidade e a validação final acordada. Lacunas que afetem segurança, regra obrigatória ou execução correta impedem a aprovação da parte afetada até sua resolução efetiva. Encaminhar ao responsável não equivale a resolver. Não marcar como resolvido o que permanece pendente.

## 5. Autonomia e revisão

Agentes podem decidir questões de baixa ou média complexidade com evidência suficiente e entendimento seguro. Registrar agente ou papel, decisão, justificativa, fontes, classificação e artefatos afetados. Na incerteza, encaminhar ao usuário. Decisões que afetem segurança, conformidade, responsabilidades, regras obrigatórias ou etapas essenciais exigem participação humana antes da decisão; a empresa pode ampliar critérios.

Divergências de baixa ou média complexidade entre autor e revisor podem ser resolvidas pelos agentes quando houver evidência suficiente. Divergências críticas, complexas ou sem evidência suficiente são apresentadas ao usuário com alternativas e justificativas. Antes da aprovação, todo achado deve estar resolvido ou registrado como pendente com impacto; o owner recebe síntese das decisões dos agentes e pendências.

## 6. Base de conhecimento e grafo

A base é isolada por empresa e tem duas camadas: contexto compartilhado e documentação específica de cada POP. Arquivos Markdown usam identificadores estáveis, metadados e links explícitos para representar relações entre POPs, processos, políticas, fontes, papéis, termos e decisões. Uma visualização do grafo ou banco de grafos é uma possibilidade futura, não requisito inicial.

Cada item compartilhado deve indicar fonte, responsável pela validação, data e estado. Cada decisão relevante registra usuário ou agente, data, decisão, justificativa, fonte e papel de quem elaborou, revisou e aprovou. Identidades fornecidas pelo usuário devem ser distinguidas de identidades verificadas pelo ambiente.

Ao criar ou revisar um POP, atualizar registros e relações pertinentes, respeitando validação e autorização. Divergências entre fontes devem ser apresentadas e alinhadas com o responsável; registrar entendimento correto e apontar correções necessárias. Gerar proposta de correção para outros documentos e obter autorização de seus responsáveis antes de alterá-los. Quando um item compartilhado mudar, listar POPs vinculados, razão da possível afetação e responsável pela avaliação; um vínculo não prova, por si só, necessidade de mudança.

## 7. Estrutura inicial proposta

```text
orquestracao-pop/                 # pacote separado dos dados
  SKILL.md                       # ponto de entrada proposto
  referencias/                   # gates, papéis, critérios e métodos
  modelos/                       # modelos genéricos e esquemas
  ferramentas/                   # validação e geração, conforme decisão técnica
  instalacao/                    # instruções e dependências
empresas/<empresa>/              # pasta compartilhada da organização
  contexto/                      # cultura, políticas, fontes e glossário
  identidade/                    # logomarca, manual, fontes e templates autorizados
  processos/                     # processos e relações compartilhadas
  decisoes/                      # decisões e rastreabilidade
  pops/<id-pop>/
    estado.md
    pop.md
    processo.bpmn
    processo.svg
    raci.md
    historico.md
    entregas/                    # DOCX, PDF, PPTX, HTML e recursos
  historico/                     # alterações da base e impactos
```

Nomes e esquema são propostas sujeitas a teste. Não guardar dados de empresa nas skills instaladas. Definir convenções de IDs, metadados, links, versões, armazenamento de fontes e compatibilidade com sincronização na implementação.

## 8. Conteúdo e apresentação

O POP contém identificação e versão; resumo inicial das alterações da última versão, ou emissão inicial; objetivo e abrangência; responsabilidades; pré-requisitos; passos; decisões e exceções; registros; referências; glossário; e aprovação. O histórico detalhado registra data, responsável e justificativa. Mudanças operacionais após aprovação geram nova versão submetida ao owner.

### Redação, storytelling e comunicação assertiva

O redator organiza o conteúdo em uma sequência compreensível: contexto e finalidade, momento de uso, responsáveis, preparação, ações em ordem, pontos de decisão e resultado esperado. Storytelling significa conectar essas partes e, quando útil, apresentar exemplos ou situações breves identificadas como ilustrativas; não inventar fatos, regras, incidentes ou evidências. O PPTX pode recorrer a uma narrativa visual para onboarding, mantendo vínculo com o procedimento aprovado.

Aplicar comunicação assertiva: frases diretas e cordiais, verbos de ação, sujeito responsável explícito, uma instrução por passo quando possível, condições e consequências claras, e orientação concreta para exceções. Explicar termos específicos no primeiro uso e vinculá-los ao glossário. Adaptar linguagem e apresentação ao público sem pressupor capacidade de compreensão a partir da escolaridade. Não sacrificar precisão, avisos necessários ou condições operacionais para simplificar o texto.

Na crítica independente, verificar se a pessoa consegue localizar o que precisa, identificar quem age, entender quando e como executar cada passo e saber o que fazer diante de uma exceção. Avaliações de agentes são inspeções; compreensão real depende de verificação com pessoas quando disponível. Registrar limitações e submetê-las ao owner.

Solicitar logomarca, cores, fontes, manual, modelos DOCX/PPTX e demais orientações disponíveis. Reutilizar templates fornecidos como referência prioritária e apontar adaptações necessárias. Caso faltem assets, registrar lacunas e submeter uma solução provisória ao owner. Conflitos entre marca e legibilidade são apresentados com alternativa para decisão. O PPTX é guia visual para treinamento, referência e onboarding; o HTML é consulta em smartphone e deve incluir recursos necessários ao uso offline.

## 9. Colaboração e controle

Uma pessoa por vez edita o mesmo POP ou item compartilhado. Registrar responsável, estado e reserva; outra pessoa autorizada pode assumir uma reserva interrompida após verificar arquivos e registrar o motivo. A implementação deve considerar conflitos de sincronização: uma reserva baseada em arquivo não garante exclusão mútua sem mecanismo testado.

Ao retomar, consultar estado, responsável, decisões, pendências e último gate. Manter histórico legível de alterações, autoria, data e motivo, sem exigir conhecimento de Git. Prever restrições de acesso conforme a organização, utilizando permissões do ambiente; não presumir que links ou metadados ofereçam controle de acesso.

## 10. Capacidades e dependências a investigar

- Reutilizar, conforme disponibilidade e distribuição: análise de processos e regras, documentação, revisão independente e criação de skills.
- **Redação e comunicação — `pd-documentation`:** candidata para documentação e rastreabilidade; avaliar também as capacidades de escrita executiva e técnica disponíveis e a necessidade de instruções específicas para storytelling, linguagem simples e comunicação assertiva. Verificar compatibilidade e distribuição antes da incorporação.
- **Seleção de métodos — `pd-methods`:** selecionar métodos por decisão, incerteza, gate, evidências e condições disponíveis; registrar protocolo, resultados, limites e motivos de escolha. Investigar disponibilidade e distribuição para os usuários.
- **Design de serviços — `pd-ux-service`:** apoiar análise de atores, jornadas, pontos de contato, transferências, esperas, falhas, recuperação e acessibilidade, quando pertinentes ao processo.
- **DOCX — `documents:documents`:** produzir e editar o documento formal, aproveitando o modelo da empresa quando aplicável; renderizar as páginas e inspecionar o resultado, corrigindo quebras, tabelas, cabeçalhos e legibilidade. Validar preservação de estilos e editabilidade no piloto.
- **PDF — `pdf:pdf`:** inspecionar e verificar visualmente o PDF final; sempre que viável, derivá-lo da versão DOCX final para manter conteúdo e paginação coerentes. Conferir texto, páginas, fontes, imagens e eventuais perdas na conversão.
- **PPTX — `presentations:Presentations`:** conceber o roteiro visual de treinamento, aplicar o template da empresa e produzir apresentação editável; renderizar e inspecionar os slides. A skill instalada atualmente encaminha apresentações para Spaces e prevê exportação pelo visualizador; é necessário testar se esse fluxo atende à entrega de um arquivo PPTX na pasta compartilhada. Não presumir exportação direta nem disponibilidade idêntica em todos os ambientes.
- **Reconhecimento dos modelos e identidade:** criar uma etapa especializada de análise visual e estrutural de DOCX, PPTX, PDF, manual de marca e logomarca fornecidos. Inspecionar páginas e slides renderizados e, quando disponível, estrutura editável (estilos, temas, layouts mestres, fontes, cores, cabeçalhos, rodapés, dimensões e assets). Produzir um registro de identidade por empresa com origem, versão, grau de certeza e exceções; reaproveitar os originais autorizados e não presumir regras de marca a partir de um único exemplo. Conflitos ou elementos incertos vão ao owner. Avaliar se uma skill própria de análise e aplicação de identidade é necessária após o piloto.
- **Templates reutilizáveis — `template-creator:template-creator`:** candidata para extrair um template pessoal reutilizável de uma referência DOCX ou PPTX. A skill atual gerencia templates pessoais e não publica plugins compartilhados; não deve ser considerada mecanismo de distribuição para toda a equipe sem solução adicional. Avaliar retenção da referência e permissões antes de usá-la com material empresarial.
- **HTML móvel:** prever capacidade específica de autoria e verificação de HTML responsivo, acessível e autocontido; identificar e testar a ferramenta ou skill adequada. A análise visual de documentos não substitui o teste do guia em tela de smartphone e sem rede.
- Avaliar [Grill-with-docs](https://github.com/mattpocock/skills/blob/main/docs/engineering/grill-with-docs.md), suas dependências, licenças e adaptação ao registro de entrevistas; sua documentação informa que a instalação isolada é insuficiente.
- Avaliar a [skill BPMN](https://github.com/architawr/claude-bpmn-skill/blob/main/skills/bpmn/SKILL.md), que declara gerar e editar XML e layout e requer Node.js e dependências npm. Verificar licença, código, segurança, validação e exportação antes de incorporar. Comparar com [Camunda BPMN](https://github.com/camunda/skills/blob/main/skills/camunda-bpmn/SKILL.md), voltada a processos executáveis e com dependências específicas.
- Testar arquivo BPMN editável em editor compatível, validação estrutural e legibilidade visual; não confundir validação técnica com confirmação do processo pelo owner.
- Verificar instalação e distribuição entre usuários Codex, versionamento do pacote, permissões, comportamento do Drive, fontes e licenças dos assets, e geração e teste offline do HTML.

Nenhuma skill externa foi instalada ou testada nesta etapa. Escolha técnica, licenças e versões permanecem abertas.

## 11. Verificação e piloto

Testar um POP piloto real autorizado ou exemplo: coleta de contexto e identidade; perguntas e registro de decisões; modelagem com raias e RACI; revisão independente; quatro entregas; aprovação; atualização dos vínculos e análise de impacto. Conferir visualmente PDF, slides e demais elementos relevantes; abrir HTML sem rede; verificar links e arquivos editáveis; comparar versões e conteúdo entre saídas. Sempre que possível, uma pessoa do público real verifica a compreensão; se não houver teste, registrar a limitação para decisão do owner, sem exigir outro aprovador.

Critérios de conclusão do piloto, dados de teste, ferramentas, ambiente e evidências de execução serão definidos antes de sua realização. O piloto não equivale à aprovação da solução para todas as empresas.

## 12. Questões técnicas em aberto

1. Formato e mecanismo de instalação e atualização do pacote em cada ambiente Codex.
2. Esquema verificável para grafo, versionamento e auditoria e eventual integração com controle de versões.
3. Mecanismo de reserva, recuperação de sessão e detecção de conflitos de sincronização no Google Drive.
4. Identificação dos usuários e aplicação efetiva das permissões de acesso.
5. Escolha, licenças e testes das skills e ferramentas; portabilidade das dependências.
6. Convenções e limites de revisão para alterações puramente visuais ou sem mudança de sentido.
7. Requisitos de integração com o PWA e armazenamento offline pelo aplicativo.
8. Seleção do POP piloto e critérios específicos de aceite.

## 13. Métodos para investigação, modelagem e validação

As cinco capacidades abaixo devem estar disponíveis à orquestração. A seleção e a profundidade de aplicação dependem do problema, criticidade, evidências, acesso a pessoas e recursos. Registrar método, objetivo, fontes, hipóteses, achados, limitações e decisão; não afirmar execução ou validação de um método sem evidência. Personas sintéticas e análises de agentes não substituem observação ou testes reais.

| Capacidade | Investigação e modelagem | Validação e resultados |
|---|---|---|
| Design Thinking | Entender necessidades e contexto, formular o problema e explorar alternativas. Usar entrevistas, observação e protótipos quando disponíveis e adequados. | Submeter propostas relevantes ao owner; registrar aprendizado e evidência. A aplicação é proporcional ao problema, sem impor oficinas em todo POP. |
| Design de Serviços | Identificar atores, canais, pontos de contato, transferências, esperas, ações de suporte e recuperação de falhas; usar jornada ou blueprint quando útil. | Verificar interfaces com outros processos e a experiência de quem executa ou recebe o serviço; conectar achados ao BPMN, à RACI e a propostas. |
| Design Robusto | Identificar variações, condições de operação, falhas possíveis e medidas de prevenção ou recuperação; quando aplicável, investigar fatores controláveis e fatores de ruído. | Registrar cenários e limites; propor testes adequados antes de afirmar robustez. Experimentos quantitativos exigem desenho e dados suficientes. O significado exato pretendido pelo solicitante, inclusive eventual referência a Taguchi, permanece a confirmar. |
| Teoria das Restrições | Investigar hipóteses sobre a restrição do sistema, filas, capacidade, dependências e efeito no resultado global; usar dados quando disponíveis. | Diferenciar hipótese de restrição identificada por evidência. Propor melhorias com impacto esperado e validação pelo owner, sem tratar toda demora como gargalo do sistema. |
| Problem Solving | Definir problema, efeito e contexto; distinguir sintomas de causas; avaliar alternativas e riscos. Utilizar métodos como 5 porquês ou diagrama de causa e efeito quando adequados. | Registrar evidências e incertezas das causas; propor ação, responsável, medida e acompanhamento. Não declarar causa comprovada apenas por consenso ou análise sintética. |

Na investigação, aplicar perguntas orientadas às necessidades, variações, problemas e interfaces; na modelagem, refletir achados pertinentes em fluxos, regras, exceções e responsabilidades; na validação, testar consistência e apresentar melhorias como propostas separadas do processo vigente. Decisões críticas e melhorias continuam sujeitas ao envolvimento e à decisão do owner previstos nesta especificação.
