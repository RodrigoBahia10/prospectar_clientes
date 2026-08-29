# Prospector Pro — Plugin para Google Antigravity

Plataforma de prospecção semiautomática multi-oferta empacotada como **Plugin do Antigravity** (Agy 2.0 / IDE / CLI compartilham a mesma config).

Suporta **5 tipos de oferta** × **3 canais de prospecção** com um CRM unificado, dashboard local, propostas anti-spam por e-mail e geração de contratos.

---

## Tipos de oferta suportados

| Oferta | O que vende | Canal principal |
|--------|-------------|-----------------|
| `redesign` | Redesign premium de sites | Google Maps |
| `automacao` | Automações (n8n, Make, Zapier, Python) | Maps + LinkedIn |
| `saas` | Produto digital com recorrência | LinkedIn |
| `app` | Aplicativo mobile ou web customizado | LinkedIn + Maps |
| `consultoria` | Diagnóstico e consultoria de processos | LinkedIn + indicação |
| `presenca` | Gestão de redes sociais, GMB, tráfego pago, SEO | Maps + LinkedIn + Manual |

---

## Estrutura do plugin

```
prospector-pro/
├── plugin.json               marcador do plugin (nome: prospector-pro)
├── mcp_config.json           MCP servers: CRM (SQLite) + navegador Playwright
├── prospector-mcp.py         servidor MCP do CRM
├── dashboard/                painel local (Python + SQLite)
│   ├── dashboard-server.py   servidor HTTP local (porta 8765)
│   ├── dashboard-template.html
│   └── iniciar-dashboard.*   iniciadores Windows/Mac
└── skills/
    ├── prospector-setup/         configuração inicial (multi-oferta)
    │
    ├── [CANAIS DE PROSPECÇÃO]
    ├── prospeccao-maps/          Google Maps Platform + Playwright
    ├── prospeccao-linkedin/      LinkedIn via Playwright
    ├── prospeccao-manual/        entrada manual de leads
    │
    ├── [QUALIFICAÇÃO POR OFERTA — usa ferramentas automáticas]
    ├── qualificacao-automacao/   detecta processos manuais + gera ROI
    ├── qualificacao-saas/        analisa fit de mercado + sinais de produto
    ├── qualificacao-app/         detecta operações mobile não digitalizadas
    ├── qualificacao-consultoria/ gera roteiro de entrevista de diagnóstico
    │
    ├── [ENTREGÁVEIS]
    ├── redesign-premium/         redesign HTML premium (oferta redesign)
    ├── deploy-hostgator/         publicação FTP/cPanel (oferta redesign)
    │
    ├── [PROPOSTAS POR OFERTA]
    ├── proposta-gmail/           roteador anti-spam (detecta oferta → direciona)
    ├── proposta-automacao/       proposta + diagnóstico de ROI
    ├── proposta-saas/            proposta + demo/trial
    ├── proposta-app/             proposta + escopo básico
    ├── proposta-consultoria/     proposta de diagnóstico pago
    │
    ├── [PÓS-VENDA]
    ├── follow-up-proposta/       follow-up único por lead (regras anti-spam)
    ├── contrato-servico/         contrato parametrizável por tipo de serviço
    └── dashboard-leads/          CRM, kanban, financeiro, exportação
```

---

## Instalação

### 1. Instalar o plugin

Copie a pasta inteira para um dos locais que o Antigravity varre:

- **Global (todos os projetos):** `~/.gemini/config/plugins/prospector-pro/`
- **Só no projeto atual:** `.agents/plugins/prospector-pro/` na raiz do workspace.

> Se a pasta `plugins/` não existir, crie-a. O Antigravity espera essa estrutura.

### 2. Ajustar o `mcp_config.json`

Abra `mcp_config.json` e corrija os caminhos do `prospector-crm`:
- Caminho do `prospector-mcp.py`
- `--pasta` = pasta do seu projeto (onde ficam `prospector.db` e os sites)

### 3. Plugin Google Maps Platform (para prospecção via Maps)

Em **Settings → Customizations → Build with Google**, instale o plugin **Google Maps Platform**. Precisa de uma API key do Maps Platform (cota grátis mensal).

### 4. Configurar o Prospector Pro

No chat: **"configurar o prospector"** → a skill `prospector-setup` coleta suas ofertas, canais, dados de assinatura e instala o painel local.

---

## Como usar (linguagem natural)

### Redesign de sites
1. `"prospecta nutricionistas em São Paulo"` → Maps → qualificação de site → dashboard
2. `"redesenha os 5 melhores"` → redesign premium + editor + comparador
3. `"publica na HostGator"` → FTP/cPanel + verificação HTTPS
4. `"manda a proposta"` → e-mail anti-spam com capa antes/depois

### Automações
1. `"prospecta clínicas no LinkedIn para automação"` → Playwright → qualificação de processo
2. `"qualifica a Clínica X para automação"` → detecta processos manuais + gera diagnóstico de ROI
3. `"manda proposta de automação para a Clínica X"` → e-mail com diagnóstico + CTA de reunião

### SaaS / App / Consultoria
- `"prospecta empresas de logística para SaaS no LinkedIn"` → qualificação de fit
- `"qualifica a Empresa Y para consultoria"` → gera roteiro de entrevista
- `"manda proposta de consultoria para a Empresa Y"` → proposta de diagnóstico pago

### CRM e pipeline
- `"quem está aguardando proposta há mais de 3 dias?"` → follow-up automático
- `"mostra o financeiro"` → total fechado, MRR, projeção 12 meses
- `"exporta os leads de automação para CSV"` → arquivo pronto para Excel

---

## Tools MCP disponíveis (prospector-crm)

| Tool | Descrição |
|------|-----------|
| `listar_leads(status)` | Lista todos ou por status |
| `listar_por_oferta(oferta)` | Lista por tipo de oferta |
| `obter_lead(slug)` | Dados completos de um lead |
| `salvar_lead(...)` | Cria ou atualiza lead |
| `salvar_qualificacao(slug, score, diagnostico)` | Salva resultado da qualificação |
| `atualizar_status(slug, status)` | Move no funil |
| `registrar_fechamento(slug, valor)` | Fecha negócio |
| `followups_pendentes(dias)` | Leads aguardando follow-up |
| `registrar_followup(slug)` | Marca follow-up enviado |
| `resumo_financeiro()` | Painel financeiro |
| `regenerar_dashboard()` | Atualiza dashboard.html |
| `exportar_csv(status, oferta)` | Exporta para CSV |
| `pontuar_site(url)` | Pré-qualifica site automaticamente |

---

## Campos do CRM

Além dos campos básicos (nome, e-mail, telefone, WhatsApp, etc.), o banco inclui:

| Campo | Descrição |
|-------|-----------|
| `oferta` | redesign / automacao / saas / app / consultoria |
| `canal` | maps / linkedin / manual / indicacao / inbound |
| `score_qualificacao` | 0–10 (gerado pela skill de qualificação) |
| `diagnostico` | Diagnóstico textual da qualificação automatizada |

---

## Diferenças em relação à versão original

| | Prospector de Sites (v1) | Prospector Pro (v2) |
|---|---|---|
| Ofertas | Redesign de sites | 5 ofertas |
| Canais | Google Maps | Maps + LinkedIn + Manual |
| Qualificação | Visual (site ruim) | Automatizada por oferta |
| Propostas | 1 template | 1 por tipo de oferta |
| CRM | 22 campos | 26 campos (+oferta, canal, score, diagnóstico) |
| Distribuição | Uso próprio | Produto para freelancers e agências |

---


