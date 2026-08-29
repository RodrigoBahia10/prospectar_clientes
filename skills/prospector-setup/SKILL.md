---
name: prospector-setup
description: Configuração inicial do Prospector Pro no Antigravity — coleta ofertas ativas, canais, assinatura e conexão HostGator. Use quando o usuário disser "configurar prospector", "setup", "começar", "meus dados", ou na primeira vez que rodar qualquer skill do Prospector Pro sem um prospector-config.json.
---

# Prospector Pro — configuração inicial

Rode UMA vez por instalação. Salva tudo em `prospector-config.json` na pasta de trabalho.

## 1. Verificar config existente

Procure `prospector-config.json`. Se existir, mostre um resumo (SEM senhas) e pergunte o que atualizar. Se não existir, colete os dados abaixo em blocos curtos.

## 2. Dados do usuário

- **Assinatura**: nome completo, como se apresenta (ex.: "Especialista em automação de processos") e WhatsApp `55DDDNUMERO`.
- **Ofertas ativas**: quais tipos de serviço vende? (marque todos que se aplicam)
  - `redesign` — redesign de sites para negócios locais
  - `automacao` — automações com n8n, Make, Zapier ou Python
  - `saas` — produto digital com recorrência mensal
  - `app` — aplicativo mobile ou web customizado
  - `consultoria` — diagnóstico e consultoria de processos
  - `presenca` — gestão de redes sociais, GMB, tráfego pago, SEO (negócios e autônomos)
- **Oferta padrão**: qual é a principal?
- **Canais ativos**: Maps (negócios locais), LinkedIn (empresas/profissionais), manual (indicação/inbound)?
- **Nichos alvo** por oferta (ex.: redesign → nutricionistas; automação → clínicas; consultoria → e-commerce).
- **Cidade/região padrão**.
- **Leads por busca**: padrão 10.
- **Modo de envio da proposta**: padrão "rascunho no Gmail para revisão".

## 3. Conexão HostGator (só se oferta "redesign" estiver ativa)

Se já contratou a hospedagem: **não colete a senha pelo chat**. Oriente a preencher no arquivo ou no dashboard os campos `usuario`, `dominio`, `servidor` e `senha`. A senha vive SÓ no arquivo local.

## 4. Salvar

```json
{
  "assinatura": { "nome": "", "apresentacao": "", "whatsapp": "" },
  "ofertas": ["redesign", "automacao"],
  "ofertaPadrao": "redesign",
  "prospeccao": {
    "nichos": { "redesign": ["nutricionistas","psicologos"], "automacao": ["clinicas","escritorios"] },
    "cidade": "",
    "leadsPorBusca": 10,
    "canais": ["maps", "linkedin"]
  },
  "envio": { "modo": "rascunho" },
  "hostgator": { "usuario": "", "dominio": "", "servidor": "", "senha": "", "pastaBase": "clientes" }
}
```

## 5. Painel local

Siga a skill `dashboard-leads` para instalar o servidor e criar o banco `prospector.db`. O banco agora inclui os campos `oferta`, `canal`, `score_qualificacao` e `diagnostico` — o servidor migra automaticamente bancos antigos.

## 6. Pré-requisitos do Antigravity

1. **Plugin Google Maps Platform** — Customizations → Build with Google (API key; necessário para canal "maps").
2. **MCP de navegador (Playwright)** — já declarado no `mcp_config.json` (canal "linkedin" e qualificação automatizada).
3. **MCP Prospector CRM** (`prospector-mcp.py`) — declarado no `mcp_config.json`.
4. (Opcional) **MCP/plugin Gmail** — para criar rascunhos de proposta direto.

## 7. Encerrar

Confirme o que foi salvo. Explique o ciclo por oferta:

- **Redesign**: `prospeccao-maps` → `qualificacao-automacao` (pontuar_site) → `redesign-premium` → `deploy-hostgator` → `proposta-gmail`
- **Automação**: `prospeccao-maps` ou `prospeccao-linkedin` → `qualificacao-automacao` → `proposta-automacao`
- **SaaS/App**: `prospeccao-linkedin` → `qualificacao-saas`/`qualificacao-app` → `proposta-saas`/`proposta-app`
- **Consultoria**: `prospeccao-linkedin` → `qualificacao-consultoria` → `proposta-consultoria`
- **Presença digital**: `prospeccao-maps` (negócios locais) ou `prospeccao-linkedin` (autônomos) → `qualificacao-presenca` → `proposta-presenca`

Em todos os casos: `follow-up-proposta` → `contrato-servico` → `dashboard-leads` como painel central.
