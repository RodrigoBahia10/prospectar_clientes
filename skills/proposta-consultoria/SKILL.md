---
name: proposta-consultoria
description: Escrever proposta de diagnóstico pago para leads de consultoria — e-mail que apresenta o pré-diagnóstico e convida para uma reunião exploratória, com posterior proposta de projeto. Acione quando o usuário disser "manda proposta de consultoria", "proposta de diagnóstico", "envia proposta para [empresa]" com oferta=consultoria.
---

# Proposta por e-mail — Consultoria

A proposta de consultoria tem uma diferença importante: o CTA não é fechar o projeto — é a reunião de diagnóstico inicial (que pode ser paga). O e-mail é a porta de entrada para essa conversa.

## Pré-requisito

Lead com `oferta: consultoria` e `diagnostico` do `qualificacao-consultoria`. Carregar via `obter_lead(slug)`.

## Princípios

1. **Pré-diagnóstico como âncora.** "Já analisei o que encontrei publicamente sobre vocês" é a abertura mais forte.
2. **Específico ao sinal encontrado.** Referenciar o post, vaga aberta ou página do site que revelou a dor.
3. **Consultoria como investimento, não custo.** O e-mail não menciona preço — mas framing de ROI/resultado está presente.
4. **CTA = conversa de 30 min.** A reunião é exploratória — não um pitch de venda.
5. **Tom de par.** Você não vende consultoria — você quer entender se faz sentido trabalhar juntos.

## Estrutura

- **Assunto**: `[Nome], sobre os desafios de [área detectada] na [Empresa]` ou `[Nome], uma observação sobre [sinal específico encontrado]`
- **Parágrafo 1**: como encontrou + observação específica sobre o desafio detectado (post, vaga, site).
- **Parágrafo 2**: o que esse tipo de desafio costuma custar em tempo de gestão / decisões erradas / oportunidades perdidas.
- **Parágrafo 3**: quem você é e como costuma ajudar empresas em momento similar — sem listar serviços.
- **CTA**: "Faz sentido conversar 30 minutos para eu entender melhor o contexto de vocês?"
- **Assinatura**.

## Exemplo

```
Assunto: Carlos, sobre a expansão da equipe da Distribuidora Ágil

Olá, Carlos! Vi no LinkedIn que a Distribuidora Ágil está contratando para mais 3 posições na operação — sinal claro de que o negócio está crescendo. Parabéns.

Pelo que vi na publicação e no site, imagino que esse crescimento traz um desafio comum: processos que funcionavam bem com equipe menor começam a criar ruído, retrabalho e dependência da memória das pessoas.

Trabalho com gestores nesse momento de transição — quando escalar começa a exigir estrutura, não só pessoas. Já ajudei distribuídoras regionais a reduzir tempo de onboarding de novos funcionários e centralizar decisões operacionais sem desacelerar o crescimento.

Faz sentido conversar 30 minutos para entender melhor o contexto de vocês?

[assinatura]
```

## Checklist anti-spam

- [ ] Assunto fala do desafio específico, não de "consultoria" ou "gestão"
- [ ] Sem lista de serviços
- [ ] Sem preço
- [ ] Máx 1 link
- [ ] Tom de igual para igual, não de vendedor

## Envio e registro

Criar rascunho no Gmail. Chamar `atualizar_status(slug, "proposta")` após criar o rascunho.
