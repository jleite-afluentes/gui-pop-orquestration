#!/usr/bin/env python3
"""Controles locais para a orquestração de POP; sem bloqueio distribuído."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys

TYPES = {'implementa','regido_por','usa_termo','executado_por','consulta','informa','precede','depende_de','substitui','relacionado_a'}

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()
def write_new(p, text):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f: f.write(text)
def save(p, data): write_new(p,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def valid_id(s):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',s): raise ValueError('ID inválido; use letras, números, hífen ou sublinhado')
    return s
def inside(root, relative):
    p=(root/relative).resolve()
    if not p.is_relative_to(root.resolve()): raise ValueError('Caminho fora da pasta autorizada')
    return p
def init_company(a):
    p=Path(a.path); p.mkdir(parents=True,exist_ok=True)
    for name in ('contexto','identidade','processos','decisoes','pops','historico'): (p/name).mkdir(exist_ok=True)
    save(p/'grafo.json',{'nodes':[],'edges':[]})
    write_new(p/'empresa.md',f'# Empresa {a.name}\n\nID: {valid_id(a.id)}\nEstado: inicial\nFontes e validação: pendentes\n')
    write_new(p/'participantes.md','# Participantes\n\nRegistre nome, papel, data e POPs relacionados; identidade informada ou verificada.\n')
    print('Empresa inicializada:',p)
def init_pop(a):
    root=Path(a.company); ident=valid_id(a.id); p=inside(root,'pops/'+ident)
    p.mkdir(parents=True,exist_ok=False)
    (p/'entregas').mkdir()
    write_new(p/'estado.md',f'# Estado {ident}\n\nEstado: preparacao\nOwner: {a.owner}\nIdentidade: informada, não verificada\nPendências: fontes, escopo e gates\n')
    write_new(p/'pop.md',f'# {a.title}\n\nID: {ident}\nVersão: rascunho\n\n## Alterações\n\nEmissão inicial em elaboração.\n\n## Fontes e conteúdo\n\nPendente de investigação.\n')
    write_new(p/'historico.md',f'# Histórico {ident}\n\n- {now()}: iniciado por {a.owner}; identidade informada.\n')
    write_new(p/'sipoc.md',f'# SIPOC {ident}\n\nEstado: pendente\n\n| Fornecedores | Entradas | Processo e limites | Saídas | Clientes ou destinatários |\n|---|---|---|---|---|\n| A confirmar | A confirmar | A confirmar | A confirmar | A confirmar |\n')
    write_new(p/'cenarios.md',f'# Cenários {ident}\n\nEstado: pendente de investigação e validação.\n')
    write_new(p/'faq.md',f'# Perguntas frequentes {ident}\n\nEstado: pendente de investigação e validação. Vincular cada resposta a fontes, versão e atividades.\n')
    print('POP inicializado:',p)
def check(a):
    root=Path(a.company).resolve(); g=json.loads((root/'grafo.json').read_text(encoding='utf-8')); errors=[]; ids=set()
    for n in g['nodes']:
        ident=n.get('id')
        if not isinstance(ident,str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',ident): errors.append('ID inválido: '+str(ident)); continue
        if ident in ids: errors.append('ID duplicado: '+ident)
        ids.add(ident)
        try:
            if not inside(root,n['file']).is_file(): errors.append('Arquivo ausente: '+n['file'])
        except (ValueError,KeyError): errors.append('Caminho inválido: '+str(n.get('file')))
    for e in g['edges']:
        if e.get('from') not in ids or e.get('to') not in ids: errors.append('Relação com nó ausente: '+str(e))
        if e.get('type') not in TYPES: errors.append('Tipo inválido: '+str(e.get('type')))
    for err in errors: print('ERRO:',err)
    print(f'Nós: {len(g["nodes"])}; relações: {len(g["edges"])}; erros: {len(errors)}. Cobertura e semântica não verificadas.')
    return 1 if errors else 0
def manifest(a):
    p=Path(a.pop).resolve(); out=p/'entregas'
    if not out.is_dir(): raise ValueError('Pasta entregas ausente')
    files=[]
    for f in sorted(out.rglob('*')):
        if f.is_symlink(): raise ValueError('Links simbólicos não são aceitos no pacote')
        if f.is_file(): files.append({'path':f.relative_to(p).as_posix(),'size':f.stat().st_size,'sha256':digest(f)})
    if not files: raise ValueError('Nenhuma entrega encontrada')
    data={'schema':1,'pop':a.id,'version':a.version,'created_at':now(),'actor':a.actor,'identity':'informada, não verificada','files':files,'checks':'não declarados por esta ferramenta'}
    target=inside(p,a.output); save(target,data); print('Manifesto criado:',target)
def verify(a):
    p=Path(a.pop).resolve(); m=inside(p,a.manifest); data=json.loads(m.read_text(encoding='utf-8')); errors=[]; expected=set()
    for x in data['files']:
        f=inside(p,x['path']); expected.add(f)
        if not f.is_file() or f.is_symlink() or digest(f)!=x['sha256']: errors.append(x['path'])
    actual={x.resolve() for x in (p/'entregas').rglob('*') if x.is_file()}
    if actual != expected: errors.append('Lista de arquivos da pasta entregas diverge')
    for e in errors: print('DIVERGÊNCIA:',e)
    print('Resultado:', 'alterado' if errors else 'íntegro', '(não verifica conteúdo nem identidade)')
    return bool(errors)
def approve(a):
    if not a.confirm: raise ValueError('Confirmação explícita requerida: --confirm')
    p=Path(a.pop).resolve(); m=inside(p,a.manifest)
    if verify(argparse.Namespace(pop=str(p),manifest=a.manifest)): raise ValueError('Manifesto não corresponde às entregas')
    save(inside(p,a.output),{'approved_at':now(),'owner':a.owner,'identity':'informada, não verificada','manifest':a.manifest,'manifest_sha256':digest(m),'remarks':a.remarks})
    print('Aprovação autodeclarada registrada; não é assinatura digital.')
def reserve(a):
    p=Path(a.pop); save(p/'.reserva.json',{'actor':a.actor,'identity':'informada, não verificada','created_at':now(),'notice':'reserva local, não garante exclusão no Drive'})
    print('Reserva local registrada; sincronização pode gerar conflito.')
def release(a):
    p=Path(a.pop)/'.reserva.json'; data=json.loads(p.read_text(encoding='utf-8'))
    if data['actor'] != a.actor and not a.reason: raise ValueError('Outro usuário: informe --reason para assumir/liberar')
    event={'actor':a.actor,'reason':a.reason or 'liberação pelo responsável','released_at':now(),'reservation':data}
    log=Path(a.pop)/'historico-reservas.jsonl'
    with log.open('a',encoding='utf-8') as f: f.write(json.dumps(event,ensure_ascii=False)+'\n')
    p.unlink(); print('Reserva liberada; evento registrado.')
def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(required=True)
    def cmd(name,func,fields):
        q=sub.add_parser(name); q.set_defaults(func=func)
        for flags,opts in fields: q.add_argument(*flags,**opts)
    req=lambda name: ([name],{'required':True})
    cmd('init-company',init_company,[req('--path'),req('--id'),req('--name')])
    cmd('init-pop',init_pop,[req('--company'),req('--id'),req('--title'),req('--owner')])
    cmd('check',check,[req('--company')])
    cmd('manifest',manifest,[req('--pop'),req('--id'),req('--version'),req('--actor'),(['--output'],{'default':'manifesto.json'})])
    cmd('verify',verify,[req('--pop'),(['--manifest'],{'default':'manifesto.json'})])
    cmd('approve',approve,[req('--pop'),req('--owner'),(['--manifest'],{'default':'manifesto.json'}),(['--output'],{'default':'aprovacao.json'}),(['--remarks'],{'default':''}),(['--confirm'],{'action':'store_true'})])
    cmd('reserve',reserve,[req('--pop'),req('--actor')])
    cmd('release',release,[req('--pop'),req('--actor'),(['--reason'],{'default':''})])
    a=p.parse_args()
    try: return a.func(a) or 0
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError) as e: print('Erro:',e,file=sys.stderr); return 2
if __name__=='__main__': sys.exit(main())
