---
name: proposta-automacao
description: Escrever e enviar proposta comercial para leads de automação (n8n, Make, Zapier, Python) — e-mail que apresenta o diagnóstico de ROI identificado na qualificação e convida para uma reunião. Acione quando o usuário disser "manda proposta de automação", "envia o diagnóstico", "proposta para [empresa] de automação".
---

# Proposta por e-mail — Automação

O e-mail de automação NÃO vende automação — ele demonstra que você já fez o trabalho de entender o problema do lead. A proposta é o diagnóstico, não o preço.

## Pré-requisito

O lead deve ter `oferta: automacao` e `diagnostico` preenchido no CRM (resultado da `qualificacao-automacao`). Se não tiver, rodar a qualificação primeiro.

Carregar via `obter_lead(slug)` para usar os dados reais: nome, nicho, diagnóstico, score.

## Princípios

1. **O diagnóstico como prova de competência.** Você JÁ mapeou o problema deles — isso diferencia de qualquer vendedor genérico.
2. **ROI antes do preço.** Mostrar o ganho potencial (tempo/custo) antes de mencionar qualquer valor.
3. **CTA é a reunião, não o fechamento.** 30 minutos para apresentar a automação concreta.
4. **Zero jargão técnico.** Nunca mencionar n8n, webhook, API, Make. Falar em processos e resultados.
5. **Curto.** 120–180 palavras. Profissional ocupado não lê mais que isso de desconhecido.

## Estrutura do e-mail

- **Assunto**: específico ao processo identificado. Ex.: `[Nome], analisei o agendamento da [Empresa]` ou `Encontrei algo sobre o fluxo de orçamentos da [Empresa]`
- **Parágrafo 1**: quem você é + como encontrou + 1 observação específica sobre o processo manual identificado (tirar do `diagnostico`).
- **Parágrafo 2**: o custo estimado do processo manual atual (em tempo ou dinheiro, do diagnóstico).
- **Parágrafo 3**: "Mapeei uma automação que resolve isso. Posso te mostrar em 30 minutos como funciona na prática."
- **CTA**: "Tem 30 minutos essa semana?" + link de calendário se o usuário tiver, ou instrução para responder com disponibilidade.
- **Assinatura**: nome + como se apresenta (da config) + WhatsApp.

## Exemplo (adaptar com dados reais)

```
Assunto: Ana, analisei o processo de agendamentos da Clínica Bem Estar

Olá, Ana! Vi a Clínica Bem Estar no Google — parabéns pelos mais de 4.9 no Maps e 200 avaliações. São poucos consultórios que chegam nesse nível.

Enquanto olhava o site, percebi que o agendamento acontece pelo WhatsApp — o que provavelmente significa muita conversa manual para confirmar horários, lembretes e encaixes de última hora.

Mapeei uma automação que tira esse processo do WhatsApp manual e transforma em agenda automática, com confirmações e lembretes sem nenhum clique da equipe. Estimativa de ganho: ~2h/dia da sua recepção.

Posso te mostrar como funciona em 30 minutos essa semana. Tem disponibilidade?

[assinatura]
```

## Checklist anti-spam

- [ ] Assunto ≤ 60 caracteres, sem maiúsculas, sem exclamações
- [ ] Sem palavras-gatilho: grátis, urgente, promoção, ROI garantido
- [ ] Sem links (apenas o de calendário se tiver — máx 1)
- [ ] Nenhum jargão técnico (n8n, API, webhook)
- [ ] Primeira linha 100% personalizada com nome + dado real

## Envio e registro

Criar rascunho no Gmail via MCP ou link de compose.
Após criar o rascunho: chamar `atualizar_status(slug, "proposta")`.
Avisar o usuário para revisar antes de enviar.
