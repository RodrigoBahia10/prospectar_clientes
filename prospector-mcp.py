#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prospector de Sites — servidor MCP do CRM (STDIO)
Funciona no ChatGPT (Work/Codex) e no Claude (Desktop/Cowork) ao mesmo tempo,
por cima do MESMO prospector.db do dashboard.

Instalação:  pip install "mcp[cli]<2"   ← ATENÇÃO: mcp>=2 renomeou FastMCP; pin <2 obrigatório
Execução:    python3 prospector-mcp.py            (usa a pasta atual)
             python3 prospector-mcp.py --pasta "/home/usuario/meu-projeto"
Teste local: python3 prospector-mcp.py --teste
"""
import argparse, csv, json, os, sqlite3, sys, datetime, time, urllib.request, urllib.error

parser = argparse.ArgumentParser()
parser.add_argument('--pasta', default=os.environ.get('PROSPECTOR_DIR', '.'),
                    help='Pasta do projeto (onde ficam prospector.db e dashboard.html)')
parser.add_argument('--teste', action='store_true', help='Roda o autoteste e sai')
ARGS, _ = parser.parse_known_args()
PASTA = os.path.abspath(ARGS.pasta)
DB = os.path.join(PASTA, 'prospector.db')

CAMPOS = ['slug','nome','nicho','cidade','nota','avaliacoes','email','telefone','whatsapp',
          'siteAntigo','motivo','status','urlNova','dataProposta','valor','obs',
          'contratoStatus','contratoEm','manutencao','pago','docCliente','endCliente']
CAMPOS_SET = set(CAMPOS)  # whitelist para validação de nomes de coluna
STATUS_VALIDOS = ['novo','redesenhado','publicado','proposta','respondeu','fechado','descartado']

def conexao():
    c = sqlite3.connect(DB)
    c.execute('''CREATE TABLE IF NOT EXISTS leads(
        slug TEXT PRIMARY KEY, nome TEXT, nicho TEXT, cidade TEXT, nota REAL,
        avaliacoes INTEGER, email TEXT, telefone TEXT, whatsapp TEXT, siteAntigo TEXT,
        motivo TEXT, status TEXT DEFAULT 'novo', urlNova TEXT, dataProposta TEXT,
        valor REAL, obs TEXT, contratoStatus TEXT DEFAULT 'pendente', contratoEm TEXT,
        manutencao REAL, pago INTEGER DEFAULT 0, docCliente TEXT, endCliente TEXT,
        atualizado TEXT)''')
    c.commit()
    return c

def _linhas(rows, cols):
    return [dict(zip(cols, r)) for r in rows]

def _agora():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

def _col_valida(nome):
    """Valida nome de coluna contra whitelist. Levanta ValueError se não reconhecido."""
    if nome not in CAMPOS_SET:
        raise ValueError('Coluna inválida: %s' % nome)
    return nome

# ---------- Lógica (compartilhada entre MCP e autoteste) ----------

def f_listar(status=None):
    c = conexao(); cur = c.cursor()
    cols = ','.join(_col_valida(k) for k in CAMPOS)
    if status:
        cur.execute('SELECT %s FROM leads WHERE status=? ORDER BY nome' % cols, (status,))
    else:
        cur.execute('SELECT %s FROM leads ORDER BY status, nome' % cols)
    r = _linhas(cur.fetchall(), CAMPOS); c.close(); return r

def f_obter(slug):
    c = conexao(); cur = c.cursor()
    cols = ','.join(_col_valida(k) for k in CAMPOS)
    cur.execute('SELECT %s FROM leads WHERE slug=?' % cols, (slug,))
    row = cur.fetchone(); c.close()
    return dict(zip(CAMPOS, row)) if row else None

def f_salvar(dados):
    if not dados.get('slug'):
        return {'erro': 'slug é obrigatório (ex.: maria-silva)'}
    if dados.get('status') and dados['status'] not in STATUS_VALIDOS:
        return {'erro': 'status inválido. Use: %s' % ', '.join(STATUS_VALIDOS)}
    atual = f_obter(dados['slug']) or {}
    atual.update({k: v for k, v in dados.items() if k in CAMPOS_SET and v is not None})
    atual.setdefault('status', 'novo'); atual.setdefault('contratoStatus', 'pendente'); atual.setdefault('pago', 0)
    c = conexao()
    c.execute('INSERT OR REPLACE INTO leads (%s,atualizado) VALUES (%s,?)' % (','.join(CAMPOS), ','.join('?'*len(CAMPOS))),
              [atual.get(k) for k in CAMPOS] + [_agora()])
    c.commit(); c.close()
    return {'ok': True, 'lead': atual['slug'], 'status': atual['status']}

def f_status(slug, status, obs_extra=None):
    if status not in STATUS_VALIDOS:
        return {'erro': 'status inválido. Use: %s' % ', '.join(STATUS_VALIDOS)}
    lead = f_obter(slug)
    if not lead: return {'erro': 'lead não encontrado: %s' % slug}
    c = conexao()
    if status == 'proposta' and not lead.get('dataProposta'):
        c.execute('UPDATE leads SET dataProposta=? WHERE slug=?', (datetime.date.today().isoformat(), slug))
    if obs_extra:
        novo_obs = ((lead.get('obs') or '') + ' | ' + obs_extra).strip(' |')
        c.execute('UPDATE leads SET obs=? WHERE slug=?', (novo_obs, slug))
    c.execute('UPDATE leads SET status=?, atualizado=? WHERE slug=?', (status, _agora(), slug))
    c.commit(); c.close()
    return {'ok': True, 'lead': slug, 'novo_status': status}

def f_fechar(slug, valor, manutencao=None):
    lead = f_obter(slug)
    if not lead: return {'erro': 'lead não encontrado: %s' % slug}
    c = conexao()
    c.execute('UPDATE leads SET status=?, valor=?, manutencao=?, atualizado=? WHERE slug=?',
              ('fechado', valor, manutencao, _agora(), slug))
    c.commit(); c.close()
    return {'ok': True, 'lead': slug, 'valor': valor, 'manutencao': manutencao}

def f_followups(dias=3):
    limite = (datetime.date.today() - datetime.timedelta(days=dias)).isoformat()
    c = conexao(); cur = c.cursor()
    cur.execute("SELECT slug,nome,email,dataProposta,obs FROM leads WHERE status='proposta' AND dataProposta<=? ", (limite,))
    r = _linhas(cur.fetchall(), ['slug','nome','email','dataProposta','obs']); c.close()
    return [x for x in r if 'follow-up' not in (x.get('obs') or '').lower()]

def f_financeiro():
    c = conexao(); cur = c.cursor()
    cur.execute("SELECT COALESCE(SUM(valor),0), COALESCE(SUM(CASE WHEN pago=1 THEN valor ELSE 0 END),0), COALESCE(SUM(manutencao),0), COUNT(*) FROM leads WHERE status='fechado'")
    total, recebido, mrr, n = cur.fetchone(); c.close()
    return {'fechados': n, 'total_fechado': total, 'recebido': recebido,
            'a_receber': total - recebido, 'mrr_manutencoes': mrr, 'projecao_12m': total + mrr*12}

def f_dashboard():
    """Regenera o dashboard.html (snapshot) a partir do banco, se houver template na pasta."""
    tpl_path = None
    for cand in ['dashboard-template.html', 'dashboard.html']:
        p = os.path.join(PASTA, cand)
        if os.path.exists(p): tpl_path = p; break
    if not tpl_path: return {'erro': 'dashboard.html/template não encontrado na pasta %s' % PASTA}
    import re
    t = open(tpl_path, encoding='utf-8').read()
    dados = json.dumps({'atualizado': _agora(), 'leads': f_listar()}, ensure_ascii=False)
    if '__DADOS__' in t:
        novo = t.replace('__DADOS__', dados)
    else:
        novo = re.sub(r'(<script id="dados"[^>]*>).*?(</script>)', lambda m: m.group(1)+dados+m.group(2), t, flags=re.S)
    open(os.path.join(PASTA, 'dashboard.html'), 'w', encoding='utf-8').write(novo)
    return {'ok': True, 'leads': len(f_listar())}

def f_exportar_csv(status=None):
    """Exporta leads para CSV na pasta do projeto. Retorna caminho do arquivo gerado."""
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    sufixo = ('-%s' % status) if status else ''
    nome_arquivo = 'prospector-export%s-%s.csv' % (sufixo, ts)
    caminho = os.path.join(PASTA, nome_arquivo)
    leads = f_listar(status)
    if not leads:
        return {'erro': 'Nenhum lead encontrado', 'total': 0}
    with open(caminho, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(leads)
    return {'ok': True, 'arquivo': caminho, 'total': len(leads)}

def f_pontuar_site(url):
    """
    Pré-qualifica um site automaticamente sem abrir o navegador.
    Usa apenas stdlib Python (urllib). Retorna score e lista de problemas.
    score 0 = site parece adequado; score >= 2 = candidato forte para redesign.
    """
    problemas = []
    if not url.startswith('http'):
        url = 'https://' + url

    # 1. Verificar HTTPS e tempo de resposta
    t0 = time.time()
    html = ''
    url_final = url
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; ProspectorBot/1.0)'}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            url_final = resp.url
            html = resp.read(65536).decode('utf-8', errors='ignore')
            tempo_ms = int((time.time() - t0) * 1000)
            if not url_final.startswith('https://'):
                problemas.append('Sem HTTPS — site serve em HTTP (inseguro, penalizado pelo Google)')
            if tempo_ms > 3000:
                problemas.append('Lento — resposta em %dms (>3s penaliza ranking e conversão)' % tempo_ms)
    except urllib.error.URLError as e:
        return {'score': 5, 'classificacao': 'inacessível',
                'problemas': ['Site inacessível: %s' % str(e)], 'url_final': url}
    except Exception as e:
        return {'score': 5, 'classificacao': 'erro',
                'problemas': ['Erro ao acessar o site: %s' % str(e)], 'url_final': url}

    # 2. Redireciona para rede social (não tem site próprio)
    for rede in ['instagram.com', 'facebook.com', 'linktr.ee', 'linktree.com', 'bio.link']:
        if rede in url_final:
            problemas.append('Site redireciona para %s — não tem página própria' % rede)
            break

    html_lower = html.lower()

    # 3. Sem viewport meta (provavelmente não é responsivo)
    if 'name="viewport"' not in html_lower and "name='viewport'" not in html_lower:
        problemas.append('Sem meta viewport — provavelmente não é responsivo no celular')

    # 4. Sem WhatsApp
    if 'wa.me' not in html_lower and 'api.whatsapp.com' not in html_lower and 'whatsapp' not in html_lower:
        problemas.append('Sem link de WhatsApp — nenhum CTA direto de contato')

    # 5. Plataformas gratuitas / subdomínios de terceiros
    for plataforma in ['wixsite.com', 'sites.google.com', 'webnode.com.br', 'jimdo.com',
                       'weebly.com', 'blogspot.com', 'wordpress.com']:
        if plataforma in url_final:
            problemas.append('Plataforma gratuita (%s) — domínio de terceiro' % plataforma)
            break

    score = len(problemas)
    if score >= 2:
        classi = 'site ruim — candidato forte'
    elif score == 1:
        classi = 'site com problema pontual'
    else:
        classi = 'site parece adequado'

    return {'score': score, 'classificacao': classi, 'problemas': problemas, 'url_final': url_final}

# ---------- Autoteste ----------
if ARGS.teste:
    import tempfile
    PASTA = tempfile.mkdtemp(); DB = os.path.join(PASTA, 'prospector.db')
    print('1 salvar:', f_salvar({'slug':'teste-mcp','nome':'Teste MCP','email':'t@t.com','nicho':'nutricionista','cidade':'SP'}))
    print('2 listar:', len(f_listar()), 'lead(s)')
    print('3 status:', f_status('teste-mcp','proposta'))
    import sqlite3 as s3
    c=s3.connect(DB); c.execute("UPDATE leads SET dataProposta=date('now','-5 day') WHERE slug='teste-mcp'"); c.commit(); c.close()
    print('4 followups pendentes:', f_followups())
    print('5 fechar:', f_fechar('teste-mcp', 700, 100))
    print('6 financeiro:', f_financeiro())
    print('7 status inválido (deve dar erro):', f_status('teste-mcp','banana'))
    print('8 exportar_csv:', f_exportar_csv())
    print('9 pontuar_site (wix = ruim):', f_pontuar_site('http://clinica.wixsite.com/saude'))
    print('AUTOTESTE OK')
    sys.exit(0)

# ---------- Servidor MCP ----------
from mcp.server.fastmcp import FastMCP
mcp = FastMCP('prospector-crm')

@mcp.tool()
def listar_leads(status: str = '') -> str:
    """Lista os leads do CRM. Opcional: filtrar por status (novo, redesenhado, publicado, proposta, respondeu, fechado, descartado)."""
    return json.dumps(f_listar(status or None), ensure_ascii=False)

@mcp.tool()
def obter_lead(slug: str) -> str:
    """Retorna todos os dados de um lead pelo slug (ex.: maria-silva)."""
    return json.dumps(f_obter(slug) or {'erro': 'não encontrado'}, ensure_ascii=False)

@mcp.tool()
def salvar_lead(slug: str, nome: str = '', nicho: str = '', cidade: str = '', nota: float = 0,
                avaliacoes: int = 0, email: str = '', telefone: str = '', whatsapp: str = '',
                siteAntigo: str = '', motivo: str = '', urlNova: str = '', obs: str = '') -> str:
    """Cria ou atualiza um lead no CRM (usar após prospectar ou ao corrigir dados). Slug no formato nome-sobrenome."""
    d = {k: v for k, v in locals().items() if v not in ('', 0)}
    return json.dumps(f_salvar(d), ensure_ascii=False)

@mcp.tool()
def atualizar_status(slug: str, status: str, observacao: str = '') -> str:
    """Move o lead no funil: novo → redesenhado → publicado → proposta → respondeu → fechado/descartado. NUNCA use 'fechado' sem confirmação explícita do usuário (para fechar com valor, use registrar_fechamento)."""
    return json.dumps(f_status(slug, status, observacao or None), ensure_ascii=False)

@mcp.tool()
def registrar_fechamento(slug: str, valor: float, manutencao_mensal: float = 0) -> str:
    """Registra um cliente FECHADO com o valor acordado (e manutenção mensal, se houver). Use somente quando o usuário confirmar o fechamento e o valor."""
    return json.dumps(f_fechar(slug, valor, manutencao_mensal or None), ensure_ascii=False)

@mcp.tool()
def followups_pendentes(dias: int = 3) -> str:
    """Lista leads com proposta enviada há N+ dias, sem resposta e sem follow-up registrado — os que precisam de follow-up agora."""
    return json.dumps(f_followups(dias), ensure_ascii=False)

@mcp.tool()
def registrar_followup(slug: str) -> str:
    """Registra que o follow-up foi enviado hoje para o lead (1 por lead, nunca repetir)."""
    return json.dumps(f_status(slug, 'proposta', 'Follow-up enviado em %s' % datetime.date.today().isoformat()), ensure_ascii=False)

@mcp.tool()
def resumo_financeiro() -> str:
    """Painel financeiro: total fechado, recebido, a receber, MRR de manutenções e projeção 12 meses."""
    return json.dumps(f_financeiro(), ensure_ascii=False)

@mcp.tool()
def regenerar_dashboard() -> str:
    """Regenera o dashboard.html (painel visual) com os dados atuais do banco. Use ao final de qualquer sequência de alterações."""
    return json.dumps(f_dashboard(), ensure_ascii=False)

@mcp.tool()
def exportar_csv(status: str = '') -> str:
    """Exporta os leads do CRM para um arquivo CSV na pasta do projeto (encoding UTF-8 com BOM para Excel).
    Opcional: filtrar por status (novo, redesenhado, publicado, proposta, respondeu, fechado, descartado).
    Retorna o caminho do arquivo gerado e o total de leads exportados."""
    return json.dumps(f_exportar_csv(status or None), ensure_ascii=False)

@mcp.tool()
def pontuar_site(url: str) -> str:
    """Pré-qualifica um site automaticamente SEM abrir o navegador (usa apenas urllib da stdlib).
    Verifica: HTTPS, tempo de resposta, meta viewport (responsividade), presença de WhatsApp,
    plataformas gratuitas (Wix, Google Sites...) e redirecionamento para redes sociais.
    Retorna score (0=site parece adequado, >=2=candidato forte para redesign) e lista de problemas.
    Use ANTES de abrir o navegador para acelerar a qualificação na prospecção."""
    return json.dumps(f_pontuar_site(url), ensure_ascii=False)

if __name__ == '__main__':
    mcp.run()
