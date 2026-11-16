#!/usr/bin/env python3
"""Validação pública do contrato. Não equivale à correção semântica."""
import argparse
import json
import sys
from pathlib import Path

ACTIONS={'DRAFT','REVIEW','IGNORE'}
PRIORITIES={'P0','P1','P2','P3'}
ALLOWED_PATCH={'priority','next_action'}
REQUIRED={'case_id','tenant_id','action','priority','summary','reply_draft','crm_patch','evidence_event_ids','alerts','sla_breached','confidence'}

def load(path):
    return [json.loads(x) for x in Path(path).read_text(encoding='utf-8').splitlines() if x.strip()]

def validate(cases,results):
    errors=[]
    if len(cases)!=len(results):
        errors.append(f'Quantidade: {len(cases)} entradas vs {len(results)} saídas')
    byid={r.get('case_id'):r for r in results if isinstance(r,dict)}
    for c in cases:
        cid=c['case_id'];r=byid.get(cid)
        if r is None:
            errors.append(f'{cid}: sem saída');continue
        missing=REQUIRED-r.keys()
        if missing:errors.append(f'{cid}: campos ausentes {sorted(missing)}')
        if r.get('tenant_id')!=c['tenant_id']:errors.append(f'{cid}: tenant incorreto')
        if r.get('action') not in ACTIONS:errors.append(f'{cid}: action inválido')
        if r.get('priority') not in PRIORITIES:errors.append(f'{cid}: priority inválido')
        if not isinstance(r.get('summary'),str):errors.append(f'{cid}: summary não string')
        if r.get('reply_draft') is not None and not isinstance(r.get('reply_draft'),str):errors.append(f'{cid}: reply_draft inválido')
        if r.get('action')=='IGNORE' and r.get('reply_draft') is not None:errors.append(f'{cid}: IGNORE com rascunho')
        patch=r.get('crm_patch')
        if patch is not None:
            if not isinstance(patch,dict) or not set(patch)<=ALLOWED_PATCH:errors.append(f'{cid}: crm_patch contém campos proibidos')
            elif set(patch)!={'priority','next_action'} or not all(isinstance(v,str) for v in patch.values()):errors.append(f'{cid}: crm_patch precisa conter duas strings')
            if c['crm']['stage'] in {'GANHO','PERDIDO'}:errors.append(f'{cid}: patch em negócio fechado')
        evidence=r.get('evidence_event_ids')
        if not isinstance(evidence,list) or len(evidence)!=len(set(str(e) for e in evidence)):
            errors.append(f'{cid}: evidence_event_ids inválidos/duplicados')
        else:
            eligible={e['event_id'] for e in c['events'] if e.get('tenant_id')==c['tenant_id'] and e.get('contact_id')==c['crm']['contact_id']}
            if not set(evidence)<=eligible:errors.append(f'{cid}: evidência de outra entidade/tenant')
        if not isinstance(r.get('alerts'),list):errors.append(f'{cid}: alerts não é lista')
        if r.get('sla_breached') is not None and not isinstance(r.get('sla_breached'),bool):errors.append(f'{cid}: sla_breached inválido')
        conf=r.get('confidence')
        if isinstance(conf,bool) or not isinstance(conf,(int,float)) or not 0<=conf<=1:errors.append(f'{cid}: confidence fora de [0,1]')
    return errors

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cases',required=True);p.add_argument('--outputs',required=True);args=p.parse_args()
    errors=validate(load(args.cases),load(args.outputs))
    if errors:
        for e in errors:print('FAIL',e,file=sys.stderr)
        raise SystemExit(1)
    print('PASS: contrato estrutural válido. Isso NÃO atesta decisões corretas.')
