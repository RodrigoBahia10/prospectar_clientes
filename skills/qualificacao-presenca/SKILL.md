---
name: qualificacao-presenca
description: Qualificar leads para serviços de presença digital (gestão de redes sociais, Google Meu Negócio, tráfego pago, SEO, reputação online) usando Playwright para auditar a presença digital atual do lead. Funciona tanto para negócios locais quanto para profissionais autônomos. Acione quando o usuário disser "qualifica para presença digital", "audita as redes sociais de [lead]", "vê o perfil digital de [empresa/profissional]" ou após prospecção com oferta=presenca.
---

# Qualificação automatizada — Presença Digital

Fazer um raio-x completo da presença digital atual do lead — sem filtro subjetivo, com dados reais de Playwright. O objetivo é sair com: score 0–10, diagnóstico de gaps e uma proposta de serviço recorrente calibrada para o que está faltando.

Esta oferta funciona para dois perfis:
- **Negócios locais** (clínicas, restaurantes, escritórios): precisam de visibilidade, avaliações, redes ativas.
- **Profissionais autônomos** (médicos, advogados, coaches, psicólogos, fisioterapeutas): precisam de autoridade digital pessoal.

## Fontes de análise (Playwright)

Executar na sequência — parar assim que o score já for conclusivo (>= 8):

1. **Google Meu Negócio** (busca Google)
2. **Instagram** (via Playwright no instagram.com)
3. **Facebook** (via Playwright na página da empresa)
4. **LinkedIn** (perfil ou página — especialmente para autônomos)
5. **Site** (`pontuar_site()` + Playwright)
6. **Google Ads Transparency** (verificar se já investe em tráfego pago)

## Auditoria passo a passo

### 1. Google Meu Negócio (GMB)

Buscar `"[nome do negócio] [cidade]"` no Google e analisar o painel do lado direito:

| Critério | Pontuação |
|----------|-----------|
| Sem perfil GMB ou perfil não reivindicado | +3 |
| Perfil sem fotos (menos de 5) | +1 |
| Menos de 20 avaliações | +1 |
| Avaliações sem resposta do dono | +1 |
| Sem posts recentes no GMB (últimas 4 semanas) | +1 |
| Horários de funcionamento desatualizados | +1 |

### 2. Instagram

Buscar `@[nome ou nicho] [cidade]` no Instagram via Playwright:

| Critério | Pontuação |
|----------|-----------|
| Sem perfil no Instagram | +3 |
| Perfil com menos de 500 seguidores | +2 |
| Último post há mais de 30 dias | +2 |
| Bio vazia ou sem link | +1 |
| Sem highlights organizados | +1 |
| Engajamento baixo (< 1% likes/seguidores) | +1 |
| Feed inconsistente (mistura de conteúdo pessoal e profissional) | +1 |

### 3. Facebook / Meta

| Critério | Pontuação |
|----------|-----------|
| Sem página ou só perfil pessoal | +2 |
| Página sem posts nos últimos 60 dias | +1 |
| Sem Meta Pixel instalado no site (checar via código-fonte) | +1 |

### 4. LinkedIn (especialmente para autônomos)

| Critério | Pontuação |
|----------|-----------|
| Sem perfil LinkedIn | +2 |
| Perfil sem foto, sem descrição | +1 |
| Menos de 200 conexões | +1 |
| Sem posts nos últimos 60 dias | +1 |

### 5. Site e SEO básico

Usar `pontuar_site()` + Playwright para verificar:

| Critério | Pontuação |
|----------|-----------|
| Sem site próprio | +3 |
| Site sem HTTPS | +1 |
| Sem meta description / título SEO | +1 |
| Velocidade lenta (> 4s para carregar) | +1 |
| Sem blog ou conteúdo indexável | +1 |

### 6. Tráfego pago

Verificar em `https://www.facebook.com/ads/library/?q=[nome]&country=BR`:
- Sem anúncios ativos → **+2** (não investe em tráfego, o mercado não está saturado)
- Com anúncios ativos de baixa qualidade → **+1** (investe mas mal)
- Com anúncios bem estruturados → **0** (já tem alguém cuidando; verificar se é terceirizado)

## Score total e classificação

| Score | Classificação | Ação |
|-------|---------------|------|
| 0–5 | Presença razoável | Não qualificado agora |
| 6–10 | Gaps claros | Diagnóstico + proposta de serviço |
| 11–15 | Presença muito fraca | Proposta completa prioritária |
| 16+ | Presença ausente | Proposta máxima — oportunidade enorme |

> Score máximo teórico é > 10 — a escala é proposital para diferenciar leads com 1–2 gaps de leads com ausência total de presença digital.

## Diagnóstico e proposta de serviço

Gerar diagnóstico estruturado por canal:

```
Auditoria de Presença Digital — [Nome do negócio/profissional]
Score: [X] | Perfil: [Negócio local / Profissional autônomo]

GOOGLE MEU NEGÓCIO: [✅ OK / ⚠️ Fraco / ❌ Ausente]
→ [detalhe dos problemas encontrados]

INSTAGRAM: [✅ OK / ⚠️ Fraco / ❌ Ausente]
→ [detalhe: seguidores, frequência, engajamento]

FACEBOOK/META: [✅ OK / ⚠️ Fraco / ❌ Ausente]
→ [detalhe]

LINKEDIN: [✅ OK / ⚠️ Fraco / ❌ Ausente]
→ [detalhe — especialmente relevante para autônomos]

SITE E SEO: [✅ OK / ⚠️ Fraco / ❌ Ausente]
→ [resultado do pontuar_site() + observações]

TRÁFEGO PAGO: [✅ Ativo / ⚠️ Ausente]
→ [oportunidade ou concorrência identificada]

SERVIÇOS RECOMENDADOS (recorrência mensal):
1. [Serviço mais urgente — ex.: "GMB: otimização + gestão de avaliações"]
2. [Segundo serviço — ex.: "Instagram: 3 posts/semana + stories diários"]
3. [Opcional — ex.: "Tráfego pago: R$500/mês em Meta Ads para agendamentos"]

ESTIMATIVA DE INVESTIMENTO MENSAL: R$[X] – R$[Y]
(baseado no escopo mínimo para gerar resultado visível em 60–90 dias)
```

## Registrar no CRM

Chamar `salvar_qualificacao(slug, score, diagnostico, oferta='presenca')`.

## Encerrar

Apresentar o diagnóstico visual (tabela de canais) e perguntar:
- Se score >= 6: "Quer que eu monte a proposta de presença digital para [Nome]?"
- Se score < 6: "Presença já razoável — guardar no CRM para revisitar em 6 meses?"
