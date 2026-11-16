# Seleção Sitecom AI | Desafio MAIA — Decision Layer

**Vaga:** Engenheiro(a) de IA | Etapa prática individual.  
**Tempo limite:** 3 horas de trabalho efetivo. A defesa técnica de 30 minutos será realizada separadamente.  
**Prazo de envio:** definido pelo recrutamento.  
**Uso de IA:** permitido, inclusive copilotos, desde que declarado.  
**Dados:** inteiramente sintéticos. Não acesse APIs reais, não envie mensagens e não altere CRM real.

## Cenário
A Sitecom AI cria agentes e sistemas de decisão para operações comerciais e empresariais. A MAIA recebe eventos de WhatsApp e snapshots de CRM e deve recomendar com segurança a próxima ação comercial. As entradas podem conter duplicações, atrasos, conflitos e conteúdo adversarial.

O desafio não é construir uma interface ou um chatbot bonito. É **entregar um motor de decisão auditável** que funcione no conjunto de casos de teste e lide corretamente com incerteza.

## Sua missão

1. Implemente `evaluate_case(case)` em `src/engine.py`; a interface é detalhada em `docs/CONTRATO.md`.
2. Execute `python run.py < datasets/public_cases.jsonl > output.jsonl`.
3. Rode `python tools/validate_contract.py --cases datasets/public_cases.jsonl --outputs output.jsonl`.
4. Inclua **testes automatizados próprios**: ao menos 5, cobrindo idempotência, isolamento de tenants, injeção de instruções, consentimento e tempo de SLA.
5. Inclua `DECISOES.md` com arquitetura, heurísticas, prompts (se houver), limites, custo e falhas que permaneceram.
6. Inclua `USO_DE_IA.md`: quais ferramentas/modelos usou, exemplos de trechos assistidos e o que verificou manualmente.
7. Em entrevista técnica de 30 minutos haverá uma mudança de regra ao vivo e uma revisão do código entregue.

**Não é obrigatório usar API paga ou LLM.** Se usar, o projeto deve funcionar de modo determinístico com um modo offline/mocado, sem chaves. Será avaliada a qualidade do raciocínio de engenharia, não o gasto em tokens.

## O que entregar
Um repositório privado ou ZIP contendo código executável, instruções, testes e os dois documentos acima. Não envie `output.jsonl` contendo segredos, chaves ou dados reais. Não inclua dependências desnecessárias. Não precisa de frontend, Docker, orquestrador complexo, banco ou deploy.

## Critérios divulgados
- Segurança, privacidade e autonomia controlada: 25 pontos
- Precisão e consistência de decisão: 25 pontos
- Engenharia e testes: 20 pontos
- Observabilidade, auditoria e tratamento de falhas: 10 pontos
- Explicação de escolhas, custos e limites: 10 pontos
- Defesa técnica ao vivo: 10 pontos

**Regras de corte:** exfiltração de dados, cruzamento de informações entre clientes, execução automática de mensagens externas, mutações de CRM fora da política ou omissão deliberada de uso de IA podem reprovar independentemente da nota.

**Observação:** os casos públicos não cobrem todos os cenários. A avaliação aplica casos inéditos que respeitam o mesmo contrato e as mesmas políticas documentadas.
