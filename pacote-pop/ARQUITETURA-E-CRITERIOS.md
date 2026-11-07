# Arquitetura e critérios de implementação da orquestração de POP

**Estado:** desenho aprovado em princípio; implementação e testes pendentes  
**Data:** 2026-11-07  
**Referência:** ESPECIFICACAO-ORQUESTRACAO-POP.md e recomendações de revisão aprovadas pelo solicitante.

## 1. Decisões de arquitetura

1. O Markdown do POP é a referência do conteúdo operacional; o arquivo BPMN é a referência da representação gráfica e das relações do modelo. Ambos usam IDs compartilhados. Nenhum deles altera o outro silenciosamente. A divergência é registrada e resolvida antes da aprovação.
2. A RACI referencia os mesmos IDs de atividades e papéis. A verificação identifica IDs ausentes, duplicados, relações inválidas e divergências potencialmente semânticas. A última categoria exige revisão, pois igualdade textual não comprova equivalência.
3. O pacote instalável, versões de dependências e dados por empresa são separados. A base da empresa permanece na pasta compartilhada do Google Drive. A distribuição e disponibilidade das skills serão verificadas no ambiente de cada usuário.
4. A máquina de estados e as regras de gate são determinísticas. Laya é opcional e sugere classificações ou rotas; não autoriza ações, modifica regras, decide gates ou aprova artefatos.
5. Saídas são derivadas de um conjunto de entradas versionado. Mudanças geram análise de impacto e uma nova execução proporcional; a versão aprovada anterior permanece identificável.

## 2. Contratos de dados e relações

Cada registro Markdown estruturado deve ter `id`, `tipo`, `titulo`, `empresa_id`, `versao`, `estado`, `atualizado_em`, `responsavel` e `fontes` quando aplicáveis. Datas incluem fuso horário; identidades registram se foram informadas ou verificadas. IDs estáveis e únicos por empresa, sem dados pessoais no identificador. Tipos mínimos: empresa, fonte, política, papel, termo, processo, atividade, decisão operacional, POP, decisão da orquestração e aprovação.

Cada relação tem origem, tipo, destino, fonte ou justificativa, estado e versão. Tipos iniciais: `implementa`, `regido_por`, `usa_termo`, `executado_por`, `consulta`, `informa`, `precede`, `depende_de`, `substitui` e `relacionado_a`. O catálogo deve definir direção e tipos de origem e destino válidos. Uma relação identificada como candidata não é fato validado. Índices e visualizações são derivados dos arquivos e podem ser reconstruídos.

O POP deve referenciar IDs de atividades, decisões e papéis no corpo; o BPMN deve preservar os IDs correspondentes nos elementos e na documentação associada; a RACI deve referenciá-los em suas linhas e colunas. A convenção exata de serialização BPMN deve ser testada com a ferramenta escolhida. Validar referências quebradas, IDs duplicados, esquema, tipos de relação, versão de destino e status. A análise de impacto mostra relações consultadas, limites e cobertura desconhecida.

## 3. Estado e gates

Estados: `preparacao`, `investigacao`, `modelagem`, `validacao_processo`, `redacao_revisao`, `producao_verificacao`, `aguardando_aprovacao`, `aprovado`, `em_revisao` e `bloqueado`. Registros de transição indicam data, ator, motivo, entradas e versões, decisões e evidências. Estado bloqueado descreve impedimento e retomada. Retroceder preserva histórico.

| Gate | Saída mínima e evidência | Impedimentos de passagem |
|---|---|---|
| Preparação | Empresa, POP, owner, identidade informada ou verificada, escopo, fontes e assets disponíveis, lacunas e estado registrados. | Empresa ou owner indefinidos; sem acesso aos materiais indispensáveis para iniciar a tarefa. |
| Investigação | Fontes identificadas; lacunas e conflitos registrados; perguntas necessárias encaminhadas; fatos, hipóteses e propostas distinguidos. | Informação indispensável para modelar uma atividade essencial ausente; conflito crítico não encaminhado. |
| Modelagem | BPMN editável e imagem legível, RACI, IDs e regras principais; fluxo atual e melhorias separados. | Fluxo principal incoerente, responsável essencial ausente, exceção crítica sem tratamento ou arquivo BPMN inválido. |
| Validação do processo | Decisões críticas e melhorias apresentadas ao owner, decisões registradas; incertezas remanescentes identificadas. | Decisão humana necessária em aberto que afete a correção ou segurança do fluxo. |
| Redação e revisão | Markdown estruturado, referências, glossário e histórico; crítica independente com achados e respostas. | Instrução essencial inexequível, conflito crítico, ou achado impeditivo sem resolução. |
| Produção e verificação | DOCX, PDF, PPTX, HTML offline e recursos, BPMN visual e editável, RACI; verificações documentadas e problemas relevantes corrigidos ou registrados. | Saída requerida ausente ou ilegível, divergência operacional relevante, HTML dependente de rede, falha impeditiva de exportação. |
| Aprovação | Manifesto do pacote, síntese de decisões e pendências, identidade do owner, aprovação da versão e ressalvas; registros e vínculos atualizados conforme autorização. | Falta de aprovação explícita ou pendência que impeça execução correta ou afete requisito crítico. |

O owner aprova sozinho; consultas externas e teste de compreensão são recomendados quando disponíveis e não introduzem outro aprovador. Ausência de teste real é registrada. A ferramenta não converte encaminhamento ao owner em resolução: decisão documentada e correção ou tratamento efetivo são necessários para encerrar o impedimento.

## 4. Manifesto, aprovação e mudança

Produzir manifesto em formato legível por máquina e por pessoa contendo empresa e POP, versão, estado, data e fuso, responsável, ferramenta e versões, entradas e versões, arquivo relativo, formato, tamanho e SHA-256 de cada entrega, resultados de verificações, pendências e registro de aprovação. Não incluir o hash do próprio manifesto em si; uma aprovação separada referencia o hash do manifesto final. A identidade do aprovador deve indicar se é autodeclarada ou verificada. Hash comprova igualdade dos bytes, não identidade ou autenticidade.

Ao modificar um arquivo após aprovação, comparar hashes, marcar o pacote como alterado e não apresentar a alteração como aprovada. Mudanças operacionais requerem nova versão e aprovação do owner. Para alterações exclusivamente visuais ou correções sem mudança de sentido, registrar a classificação e submeter a classificação ao owner; até que a empresa defina política diferente, solicitar confirmação antes de redistribuir como aprovado. Nunca sobrescrever silenciosamente a versão aprovada.

## 5. Colaboração e Google Drive

Reserva inclui empresa, objeto, usuário e origem da identidade, instante, sessão, estado e hashes das versões de base. Registrar tomada, renovação, liberação e recuperação. Antes de gravar, comparar hashes observados com a versão atual acessível; se divergirem, não sobrescrever e registrar conflito para resolução. Outra pessoa autorizada pode recuperar reserva interrompida registrando motivo e verificando estado e arquivos.

Esses controles são preventivos, não uma garantia de bloqueio distribuído: sincronização atrasada pode permitir gravações concorrentes. Testar em dois ambientes reais, incluindo edição offline e reconexão. Se não for possível garantir integridade, limitar a colaboração operacional ou adotar serviço de coordenação apropriado antes de uso simultâneo. As permissões efetivas são aplicadas no armazenamento, não nos metadados. Não assumir que o projeto pode conceder ou verificar permissões sem integração testada.

## 6. Estratégia de execução e tokens

- Carregar índice da empresa, estado do POP e apenas trechos e versões pertinentes ao gate. Cada trecho carregado mantém localizador de origem; buscar o original quando a decisão depender do contexto completo.
- Um pacote de tarefa contém objetivo, gate, ação, resultado esperado, arquivos e versões, limites, evidências e critérios; não repassar a conversa inteira por padrão. Resumos são auxiliares, não substituem fontes.
- Ativar especialistas e métodos conforme necessidade; manter autoria e crítica independentes. Reutilizar resultados somente se versões e dependências coincidirem.
- Executar verificações determinísticas de esquema, links, IDs, hashes e presença de arquivos sem chamadas a modelo quando tecnicamente possível. Não substituir avaliação semântica por comparação literal.
- Calcular impacto a partir de vínculos e declarar lacunas de cobertura. Regerar apenas artefatos afetados quando verificável; na dúvida revisar os potencialmente afetados.
- Por execução registrar, quando disponíveis, tokens de entrada/saída, chamadas, tempos, custos, escalonamentos, retrabalho e falhas. Se o ambiente não disponibilizar uma métrica, registrar indisponibilidade, sem estimar como medição real.

### Laya opcional

Candidatos: sugestão de papel, categoria de documento e triagem de possíveis exceções ou impactos. Não usar para autorizar operações, determinar cumprimento legal, classificar sozinho risco crítico, validar fatos ou aprovar gates. Primeiro executar em modo de observação. Política fixa envia tarefas críticas, incertas, truncadas, indisponíveis ou fora de escopo para análise apropriada. Confiança é sinal operacional a calibrar, não prova de acerto. Registrar versão, opções, resultado, contexto mínimo, latência, erro, escalonamento e métricas fornecidas; não registrar segredos nem conteúdo além do necessário.

Experimento pareado: mesmos casos autorizados ou anonimizados para regras, modelo principal e Laya; conjunto de avaliação com respostas esperadas revisadas pelo owner, incluindo português, ambiguidades, casos críticos e dados incompletos. Registrar erro de roteamento, falha de escalonamento crítico, qualidade da saída, latência, consumo e custo total incluindo infraestrutura. Fixar e documentar limiares de aceite e amostra antes do teste; separar ajuste e avaliação. Comparar contra cenário sem Laya e não declarar economia sem medição. Ativação posterior depende de evidência e decisão do owner do projeto. Na falta do Laya, o fluxo permanece funcional.

## 7. Instalação e dependências

Um manifesto de dependências identificará componente, origem, versão ou revisão, licença, finalidade, disponibilidade por usuário e verificação. Antes da instalação e de qualquer uso de dependência externa, inspecionar procedência, código, licença, integridade e requisitos. O diagnóstico inicial verifica acesso à pasta, leitura e gravação autorizadas, runtime, renderização, ferramentas de BPMN e disponibilidade das skills de documentos, PDF e apresentações, com resultados `aprovado`, `falhou` ou `indisponível`.

PPTX: testar efetivamente importação do template, edição, exportação e gravação do arquivo final na pasta compartilhada; a skill disponível pode exigir Spaces e exportação por visualizador. DOCX/PDF: testar preservação de template e renderização. HTML: testar abertura em smartphone ou emulação adequada, links e recursos com rede desabilitada. BPMN: testar XML, diagrama e abertura em editor compatível. Laya: verificar modelo, licença, runtime e recursos locais; é opcional. Versões e procedimento de instalação permanecem escolhas técnicas após esses testes.

## 8. Aceite do piloto

Executar um POP autorizado do início ao fim, incluindo lacuna, exceção, melhoria proposta, vínculo a outro item e pelo menos uma alteração versionada. Evidências mínimas:

- registros de gates e decisão do owner; ao menos uma decisão de agente e um achado de revisor rastreáveis;
- BPMN aberto em ferramenta compatível, papéis e referências consistentes com RACI e Markdown;
- DOCX, PDF e slides inspecionados visualmente e coerentes; PPTX editável e disponível na pasta;
- HTML aberto com rede desabilitada e com recursos locais;
- manifesto e hashes conferidos antes e depois de uma alteração simulada;
- análise de impacto e teste de link quebrado e ID duplicado;
- teste de reserva e conflito entre dois ambientes Drive, inclusive sincronização tardia;
- diagnóstico de instalação em mais de um ambiente ou registro explícito da impossibilidade;
- custo, tempo e consumo disponíveis registrados; comparação Laya somente se houver ambiente e casos suficientes.

Falhas são documentadas com impacto, responsável e correção. Ausência de ambiente ou dados significa teste não executado, nunca aprovação implícita. O owner decide a aceitação do piloto e próximos passos.
