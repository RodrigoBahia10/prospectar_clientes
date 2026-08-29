---
name: proposta-presenca
description: Escrever proposta comercial de presença digital para negócios locais ou profissionais autônomos — e-mail que apresenta a auditoria de gaps e propõe um plano de serviço recorrente (gestão de redes, GMB, tráfego pago, SEO). Acione quando o usuário disser "manda proposta de presença digital", "proposta de redes sociais para [lead]", "proposta de tráfego pago", "manda o diagnóstico de presença".
---

# Proposta por e-mail — Presença Digital

O e-mail de presença digital tem uma vantagem única sobre as outras ofertas: **a auditoria é a prova**. Você já sabe exatamente o que está faltando — e mencionar isso no e-mail demonstra competência sem precisar explicar.

Existem dois modos de proposta, dependendo do perfil do lead:

- **Modo Negócio Local**: tom mais direto, foco em clientes/agendamentos/visibilidade no Maps.
- **Modo Autônomo/Profissional**: tom mais pessoal, foco em autoridade, referências e posicionamento de especialista.

## Pré-requisito

Lead com `oferta: presenca` e `diagnostico` do `qualificacao-presenca`. Carregar via `obter_lead(slug)`.

Identificar o perfil (negócio vs. autônomo) pelo nicho e pelo que foi encontrado na auditoria.

## Princípios universais

1. **Citar o gap mais óbvio primeiro.** "Vi que [negócio] não tem uma página no Instagram" é mais impactante que "identificamos oportunidades de melhoria na sua presença digital."
2. **Mostrar o que os concorrentes já fazem.** Breve menção ao benchmarking gera urgência sem pressão.
3. **Serviço recorrente, não projeto único.** Deixar claro que é uma parceria mensal — não um freela pontual.
4. **CTA = conversa, não fechamento.** O preço não vai no e-mail — vai na reunião/call.
5. **Curto.** 120–180 palavras. Longo demais soa como newsletter de agência.

## Modo Negócio Local

### Estrutura

- **Assunto**: `[Nome], olhei a presença digital da [Empresa] e encontrei algo importante` ou `[Empresa] — [X] clientes potenciais por mês que não te encontram`
- **Parágrafo 1**: nome + o maior gap encontrado na auditoria — específico, com dado real (ex.: "zero posts nos últimos 3 meses", "37 avaliações sem nenhuma resposta").
- **Parágrafo 2**: o que a concorrência direta está fazendo que [Empresa] não está — 1 exemplo concreto.
- **Parágrafo 3**: o que você faz e o que mudaria em 60–90 dias — em resultado, não em tarefas.
- **CTA**: "Posso te mostrar o diagnóstico completo e o plano em 20 minutos — tem disponibilidade essa semana?"
- **Assinatura**.

### Exemplo

```
Assunto: Dra. Paula, olhei a presença digital da Clínica Essência

Olá, Dra. Paula! Vi a Clínica Essência no Google Maps — 4.8 estrelas e mais de 120 avaliações é excelente. Mas percebo que o Instagram (@clinicaessencia) não tem post novo há 2 meses, e o perfil do Google Meu Negócio não tem nenhuma foto dos espaços.

Clínicas concorrentes na mesma região postam 3–4 vezes por semana no Instagram e respondem avaliações ativamente — o que gera mais agendamentos orgânicos e melhor posicionamento no Maps.

Cuidamos da presença digital de clínicas como a sua: publicação constante, gestão de avaliações e campanhas de captação no Meta. Em 60 dias a diferença é visível em agendamentos.

Posso te mostrar o diagnóstico completo em 20 minutos — tem disponibilidade essa semana?

[assinatura]
```

## Modo Autônomo / Profissional

### Diferenças-chave

- Tom mais pessoal: falar com a pessoa, não com o negócio.
- Foco em **autoridade e referências**, não em visibilidade de volume.
- Resultado: "clientes que já chegam sabendo quem você é", não "mais agendamentos".
- Para profissionais de saúde: citar SEMPRE compliance (CFM/CRM para médicos, OAB para advogados) — conteúdo dentro das normas éticas.

### Estrutura

- **Assunto**: `Dr(a). [Nome], sua presença digital não reflete a sua reputação` ou `[Nome], vi seu perfil no LinkedIn — deixa eu te mostrar algo`
- **Parágrafo 1**: elogio à especialidade/reputação + o gap de presença identificado (sem parecer crítica).
- **Parágrafo 2**: o que profissionais similares com boa presença digital conquistaram — em autoridade, não em seguidores.
- **Parágrafo 3**: o que você faz — conteúdo dentro do CFM/OAB/normas do conselho + posicionamento de especialista.
- **CTA**: "Posso preparar um mini-plano de presença para você — sem compromisso?"
- **Assinatura**.

### Exemplo (médico)

```
Assunto: Dr. Marcos, sua reputação merece mais visibilidade online

Olá, Dr. Marcos! Vi sua especialidade em medicina esportiva — área com demanda crescente mas pouquíssimos especialistas com presença digital estruturada na região.

Médicos com conteúdo regular no Instagram e no Google chegam a dobrar o volume de indicações orgânicas em 6 meses — sem depender de planos de saúde.

Produzimos conteúdo educativo dentro das normas do CFM: sem antes/depois, sem promessas, mas com autoridade técnica que faz pacientes chegarem já com confiança. Cuidamos de tudo: pauta, arte, legenda e publicação.

Posso preparar um mini-plano de conteúdo para você — sem compromisso. Tem interesse?

[assinatura]
```

## Checklist anti-spam

- [ ] Assunto sem "marketing", "social media", "tráfego pago", "Instagram" (palavras que geram spam)
- [ ] Primeiro parágrafo: dado específico da auditoria (não genérico)
- [ ] Sem lista de serviços ou pacotes
- [ ] Sem preço
- [ ] Máx 1 link

## Envio e registro

Criar rascunho no Gmail via MCP ou link de compose.
Após criar o rascunho: chamar `atualizar_status(slug, "proposta")`.

## Serviços incluídos (referência para o consultor — não vão no e-mail)

| Serviço | Modelo | Para quem |
|---------|--------|-----------|
| Gestão de Instagram/Facebook | Recorrente mensal | Negócios + Autônomos |
| Otimização e gestão do GMB | Setup + mensal | Negócios locais |
| Tráfego pago (Meta/Google Ads) | Mensal (gestor + verba) | Negócios com budget |
| Produção de conteúdo LinkedIn | Recorrente mensal | Autônomos/profissionais |
| SEO on-page | Setup pontual + revisão trimestral | Quem tem site |
| Monitoramento de reputação | Mensal | Todos |
| Bio link / link na bio page | Setup único | Autônomos sem site |
