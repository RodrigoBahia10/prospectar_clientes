---
name: prospeccao-linkedin
description: Esta skill deve ser usada para prospectar leads no LinkedIn via Playwright — ideal para ofertas de automação, SaaS, app e consultoria. Acione quando o usuário disser "prospecta no LinkedIn", "busca empresas no LinkedIn", "acha leads no LinkedIn" ou qualquer variação.
---

# Prospecção no LinkedIn (via Playwright)

Encontrar profissionais e empresas com dor identificável para automação, SaaS, app ou consultoria. O LinkedIn revela cargo, empresa, setor e, acima de tudo, sinais de dor nos próprios posts e perfis.

## Pré-requisito

O MCP de navegador (Playwright) deve estar ativo. O LinkedIn exige login — o usuário já deve estar logado no navegador que o Playwright controla. **Nunca peça a senha do LinkedIn no chat.**

Se o LinkedIn detectar automação e bloquear: pausar, avisar o usuário, aguardar instrução. Não insistir.

## Fluxo

### 1. Definir alvo

Coletar do usuário (ou do config):
- **Oferta**: automacao / saas / app / consultoria
- **Nicho-alvo**: ex. "clínicas de estética", "escritórios de advocacia", "lojas de e-commerce"
- **Cargo-alvo**: ex. "proprietário", "gerente de operações", "CEO", "diretor"
- **Cidade/região** (opcional, refina a busca)
- **Quantidade**: padrão do config (leadsPorBusca)

### 2. Buscar no LinkedIn

Abrir o navegador e executar a busca via Playwright:

**Opção A — Busca de pessoas** (para consultoria e automação):
- URL: `https://www.linkedin.com/search/results/people/?keywords=[cargo]+[nicho]&geoUrn=[cidade]`
- Filtros: conexões de 2º grau preferencialmente; verificar se tem empresa vinculada.

**Opção B — Busca de empresas** (para SaaS e app):
- URL: `https://www.linkedin.com/search/results/companies/?keywords=[nicho]`
- Filtros: tamanho de empresa (10–200 funcionários para automação/app; 1–50 para consultoria inicial).

**Ritmo seguro**: navegar devagar (2–4s entre ações), sem scroll veloz, sem cliques em massa. LinkedIn penaliza automação agressiva.

### 3. Coletar dados por lead

Para cada perfil encontrado, extrair via Playwright:

| Campo | Fonte |
|-------|-------|
| Nome | Título do perfil |
| Cargo | Subtítulo |
| Empresa | Experiência atual |
| Cidade | Localização |
| URL do perfil | `window.location.href` |
| Resumo/About | Seção "Sobre" (primeiros 500 chars) |
| Posts recentes | Atividade (últimos 3–5 posts, título + data) |
| Site da empresa | Página da empresa → Website |
| E-mail | Seção "Informações de contato" (nem sempre visível) |

**E-mail**: se não estiver no LinkedIn, buscar no site da empresa (rodapé, página "Contato") ou via pesquisa Google: `"[nome completo]" "[empresa]" email contact`. Se não encontrar: registrar como `email_pendente=true` e marcar no obs.

**WhatsApp**: raramente no LinkedIn. Buscar no site da empresa ou mencionar no obs para abordar via LinkedIn InMail como fallback.

### 4. Identificar sinais de dor (ainda no Playwright)

Antes de registrar o lead, ler os posts recentes e o resumo em busca de sinais por oferta:

**Para automação:**
- Menciona planilhas, WhatsApp para pedidos/agendamentos, controle manual
- Reclamações de volume de trabalho repetitivo
- Posts sobre "estamos crescendo mas..." (sinal de gargalo operacional)

**Para SaaS:**
- Usa ferramentas genéricas para algo muito específico do nicho
- Não cita nenhuma ferramenta dedicada ao core do negócio
- Setor com processo repetível em escala

**Para app:**
- Equipe em campo sem ferramenta mobile
- Menciona delivery, visita técnica, vendedor externo
- Usa grupos de WhatsApp para coordenar operação

**Para consultoria:**
- C-level/gestor com posts sobre desafios de escala, contratação, processos
- Empresa em crescimento rápido sem estrutura visível
- Posts de busca de parceiros, fornecedores, soluções

### 5. Pré-qualificar

Atribuir um `score_pre` (0–3) com base nos sinais encontrados:
- 0 sinais → pular, não registrar
- 1 sinal → registrar como `status: novo` com `score_qualificacao: 3`
- 2+ sinais → registrar como candidato forte com `score_qualificacao: 7`

A qualificação profunda (score 0–10 com diagnóstico detalhado) é feita pela skill correspondente (`qualificacao-automacao`, `qualificacao-saas`, etc.) depois.

### 6. Registrar no CRM

Para cada lead qualificado, chamar `salvar_lead()` com:
- `canal: "linkedin"`
- `oferta: [tipo]`
- `motivo: [sinais encontrados nos posts/resumo]`
- `score_qualificacao: [score_pre × 3.33]` (escala 0–10)

Chamar `salvar_qualificacao(slug, score, diagnostico_inicial)` com o resumo dos sinais coletados.

### 7. Encerrar

Apresentar tabela com os leads coletados (nome, empresa, cargo, sinal principal, score) e perguntar se quer rodar a qualificação profunda nos candidatos fortes.

## Boas práticas

- **Nunca mais de 20 perfis por sessão** — LinkedIn detecta e pode banir.
- **Pausar 10–30s entre perfis** se a sessão for longa.
- **Priorizar 2ª conexão** — a abordagem é mais fácil com contexto de conexão em comum.
- **Registrar o URL do perfil** em `obs` — facilita retomar a conversa depois.
