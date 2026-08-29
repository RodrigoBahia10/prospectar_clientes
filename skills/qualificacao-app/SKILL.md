---
name: qualificacao-app
description: Qualificar leads para desenvolvimento de aplicativo mobile ou web customizado, usando Playwright para detectar operações não digitalizadas. Acione quando o usuário disser "qualifica para app", "vê se precisa de app", "analisa a operação de [empresa]" ou após prospecção com oferta=app.
---

# Qualificação automatizada — Aplicativo

Identificar empresas com operação que se beneficiaria de um app mobile/web. O sinal principal é mobilidade não digitalizada: equipe em campo, entrega, atendimento externo, vendedor fora do escritório.

## Fontes de análise

1. **`pontuar_site(url)`** — site sem viewport = operação não pensa em mobile.
2. **Playwright no site** — detectar menção a equipes externas, delivery, serviço em campo.
3. **Playwright no LinkedIn** — cargo dos funcionários, descrição da empresa, posts sobre equipe.

## Critérios de qualificação

### Sinais de necessidade de app (Playwright no site + LinkedIn)

| Sinal | Pontuação |
|-------|-----------|
| Menciona delivery, motoboy, entregador | +2 |
| Menciona técnico externo, vistoria, visita | +2 |
| Menciona vendedor externo, representante | +2 |
| Usa WhatsApp para coordenar equipe | +2 |
| Site sem viewport (não pensa em mobile) | +1 |
| Nenhum app mencionado no site/LinkedIn | +1 |
| Mais de 5 funcionários em campo (LinkedIn) | +1 |
| Processo de agendamento manual para equipe externa | +1 |

### Score (0–10, máximo somável = 12, capped em 10)

| Score | Classificação | Ação |
|-------|---------------|------|
| 0–3 | App não necessário agora | Descartar |
| 4–6 | Potencial moderado | Proposta exploratória |
| 7–10 | Alta necessidade | Proposta de MVP prioritária |

## Diagnóstico

```
Diagnóstico de App — [Nome do negócio]
Score: [X]/10

Operação em campo detectada:
- [Tipo de equipe externa encontrada]
- [Como coordenam hoje: WhatsApp / planilha / outro]

Casos de uso identificados para o app:
1. [Funcionalidade principal — ex.: "Agendamento de visitas para técnicos"]
2. [Funcionalidade secundária — ex.: "Registro de serviço com foto"]
3. [Funcionalidade de gestão — ex.: "Painel do gestor com localização em tempo real"]

Plataforma sugerida: [iOS + Android / PWA / Web responsivo]
Justificativa: [breve razão técnica e de custo]

Estimativa de impacto:
- Tempo economizado na coordenação: ~[X]h/semana
- Redução de erros de agendamento: ~[Y]%
```

## Registrar no CRM

Chamar `salvar_qualificacao(slug, score, diagnostico)`.

## Encerrar

Se score >= 7: proposta de MVP com foco no caso de uso principal.
Se score 4–6: reunião exploratória para entender melhor a operação.
Se score < 4: não é o momento certo para app.
