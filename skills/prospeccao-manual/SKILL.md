---
name: prospeccao-manual
description: Esta skill deve ser usada para cadastrar leads manualmente no CRM — vindos de indicação, evento, inbound, networking ou qualquer fonte não automatizável. Acione quando o usuário disser "adicionar lead", "cadastrar cliente", "recebi uma indicação", "tenho um contato" ou pedir para adicionar alguém no CRM.
---

# Prospecção manual (entrada livre)

Qualquer lead que o usuário já tem em mãos — indicação, cartão de visita, formulário de contato, evento, LinkedIn copiado manualmente — entra aqui.

## Fluxo conversacional

### 1. Coletar dados em blocos

Perguntar em no máximo 3 rodadas (não fazer 1 pergunta por vez para cada campo):

**Rodada 1 — Identificação:**
- Nome completo / nome do negócio
- E-mail
- Telefone / WhatsApp (formato `55DDDNUMERO` para wa.me)
- Cidade

**Rodada 2 — Contexto:**
- Tipo de oferta que se aplica a este lead: redesign / automacao / saas / app / consultoria
- Canal de origem: indicação / evento / inbound / networking / outro
- O que o usuário já sabe sobre a dor ou necessidade deste lead (campo livre — vira o `motivo`)

**Rodada 3 — Opcional:**
- URL do site (se tiver)
- URL do LinkedIn (guardar em `obs`)
- Nicho/segmento da empresa
- Alguma observação importante

### 2. Registrar no CRM

Chamar `salvar_lead()` com todos os dados coletados:
- `canal: "manual"` (ou "indicacao"/"inbound" conforme origem)
- `oferta: [tipo escolhido]`
- `status: "novo"`
- `obs: "LinkedIn: [url] | [observações do usuário]"`

Se o usuário já tem informações suficientes para uma pré-qualificação:
- Chamar `salvar_qualificacao(slug, score, diagnostico)` com o que foi dito.
- Score baseado no que o usuário relatou: 1–3 = interesse vago; 4–6 = dor clara; 7–10 = urgência declarada.

### 3. Sugerir próximo passo

Com base na oferta e no que foi coletado, sugerir:
- `score >= 7` → qualificar agora com a skill correspondente (`qualificacao-automacao`, etc.)
- `score 4–6` → enviar proposta diretamente (`proposta-gmail`)
- `score < 4` → marcar como `novo` e retomar quando tiver mais contexto

### 4. Confirmação

Mostrar um resumo do que foi salvo (sem senha) e perguntar se está correto.

## Múltiplos leads de uma vez

Se o usuário quiser cadastrar vários leads (ex.: trouxe 5 cartões de um evento), processar um por vez mas sem interromper com confirmações a cada campo — perguntar todos os dados de cada lead em bloco e só confirmar ao final de todos.
