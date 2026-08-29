---
name: qualificacao-automacao
description: Qualificar leads para venda de automações (n8n, Make, Zapier, Python) usando ferramentas automatizadas — Playwright para analisar o site do lead e o perfil LinkedIn, gerando um score 0-10 e diagnóstico de ROI. Acione quando o usuário disser "qualifica para automação", "analisa o processo de [empresa]", "vê se vale automação" ou após a prospecção de um lead com oferta=automacao.
---

# Qualificação automatizada — Automações

Detectar processos manuais no negócio do lead e calcular o potencial de ROI de uma automação. O objetivo é sair desta skill com: score 0–10, diagnóstico objetivo e uma estimativa de ROI que vai direto para a proposta.

## Fontes de análise (Playwright + pontuar_site)

A qualificação usa duas fontes automatizadas, na ordem:

1. **`pontuar_site(url)`** — verificação técnica rápida (já checa responsividade, HTTPS, WhatsApp). Gratuito, sem navegador.
2. **Playwright no site do lead** — análise profunda do site para sinais de processo.
3. **Playwright no LinkedIn** — leitura de posts e resumo do perfil (se o URL estiver em `obs`).

## Critérios de qualificação (Playwright no site)

Abrir o site do lead com o MCP de navegador e verificar os seguintes sinais:

### Sinais de processo manual (cada sinal = +1 ponto no score)

| Sinal | Como detectar no site |
|-------|-----------------------|
| Agendamento por WhatsApp | Texto "agende pelo WhatsApp", "entre em contato para agendar" sem botão de agenda online |
| Controle de estoque manual | E-commerce sem integração visível (apenas catálogo estático) |
| Orçamento manual | "Solicite um orçamento" → formulário simples sem automação |
| Sem área do cliente | Nenhum login, portal ou área restrita visível |
| Nota no Google alta + site simples | `pontuar_site().score >= 2` (sem WhatsApp, sem viewport) |
| Sem integração de pagamento | Sem Stripe, PagSeguro, Mercado Pago, PIX automatizado |
| Processo de onboarding manual | "Ligue para", "venha até nós", sem autoatendimento |

### Análise do LinkedIn (se URL disponível)

Abrir perfil/página da empresa no LinkedIn via Playwright e verificar:
- Posts com palavras-chave: "planilha", "WhatsApp", "manual", "volume", "equipe cresceu"
- Reclamações de repetição: "fazemos isso todo dia manualmente"
- Cargo de quem posta: dono/gestor posta sobre operação = dor real

### Score final (0–10)

| Score | Classificação | Ação |
|-------|---------------|------|
| 0–2 | Não qualificado | Descartar |
| 3–5 | Potencial baixo | Marcar como novo, retornar se abrir espaço |
| 6–8 | Candidato | Gerar proposta |
| 9–10 | Hot lead | Proposta + contato prioritário |

## Diagnóstico de ROI

Gerar um diagnóstico objetivo com base nos sinais encontrados:

```
Diagnóstico de automação — [Nome do negócio]
Score: [X]/10

Processos manuais identificados:
1. [Processo 1] — ex.: "Agendamento feito por WhatsApp sem sistema. Estimativa: 2h/dia."
2. [Processo 2] — ex.: "Envio manual de confirmações. ~50 mensagens/dia."
3. [Processo 3] — ...

Estimativa de ganho com automação:
- Tempo economizado: ~[X]h/semana
- Custo de mão de obra evitada: ~R$[Y]/mês (baseado em salário mínimo regional)
- ROI em [Z] meses com projeto de R$[valor_estimado]

Automações mais impactantes:
1. [Automação mais óbvia e rápida de implementar]
2. [Segunda mais impactante]
```

**Regras do diagnóstico:**
- Nunca inventar números. Estimativas marcadas como "~" (aproximado).
- Usar salário mínimo + custo de encargos do estado como referência para custo de mão de obra.
- Só incluir processos com evidência encontrada no site/LinkedIn.

## Registrar no CRM

Chamar `salvar_qualificacao(slug, score, diagnostico)` com o diagnóstico completo.

O diagnóstico fica no campo `diagnostico` do lead e é usado diretamente pela skill `proposta-automacao` para compor o e-mail — não precisa ser resumido, pode ter até 500 palavras.

## Encerrar

Apresentar o score e o diagnóstico para o usuário. Perguntar:
- Se score >= 6: "Quer enviar a proposta de automação para [Nome]?"
- Se score < 6: "Lead abaixo do limiar. Guardar no CRM para revisar depois?"
