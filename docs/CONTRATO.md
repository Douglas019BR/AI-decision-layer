# Contrato de entrada e saída

## Entrada
Ler **um objeto JSON por linha** de `stdin`; o objeto é um caso independente.

Campos do caso:
- `case_id`: string única
- `tenant_id`: string
- `now`: string ISO-8601 com offset
- `crm`: `{contact_id, company, stage, owner_id, consent_marketing, snapshot_at}`
- `events`: lista de `{event_id, tenant_id, contact_id, kind, source, occurred_at, received_at, body? , consent_marketing?}`
- `knowledge`: lista opcional de `{doc_id, tenant_id, trust, source, content}`

## Saída
Para **cada linha válida de entrada**, imprimir exatamente **um JSON por linha** em `stdout`, sem logs nem Markdown.

```json
{
  "case_id": "C01",
  "tenant_id": "sitecom",
  "action": "DRAFT",
  "priority": "P2",
  "summary": "Lead interessado em avaliar 10 câmeras; prazo reportado é de 30 dias.",
  "reply_draft": "Podemos fazer uma avaliação técnica para dimensionar a integração e os requisitos do projeto.",
  "crm_patch": {
    "priority": "P2",
    "next_action": "Agendar diagnóstico técnico com responsável do lead"
  },
  "evidence_event_ids": ["m01"],
  "alerts": [],
  "sla_breached": false,
  "confidence": 0.8
}
```

- `action`: `DRAFT` (somente rascunho), `REVIEW` (supervisão humana), `IGNORE` (nenhuma mensagem elegível).
- `priority`: `P0`, `P1`, `P2` ou `P3`.
- `summary`: string curta explicando a recomendação, sem evidências de outras empresas.
- `reply_draft`: string PT-BR ou `null`; para `IGNORE`, obrigatório `null`.
- `crm_patch`: objeto com `priority` e `next_action` ou `null`.
- `evidence_event_ids`: lista de IDs únicos de eventos considerados (não pode incluir eventos de outro tenant, outro contato, futuros ou com ID colidido).
- `alerts`: lista de códigos de advertência.
- `sla_breached`: booleano ou `null` quando não existe mensagem elegível.
- `confidence`: número entre 0 e 1.

**Exceções:** erro JSON sintático pode ser sinalizado em stderr com saída não zero, pois não há `case_id` confiável. Demais erros devem produzir uma decisão válida `REVIEW` com alerta.

**Importante:** retorno de `crm_patch` não é ação real. Você não receberá credenciais de produção. Nenhuma chamada externa é necessária para executar o teste.
