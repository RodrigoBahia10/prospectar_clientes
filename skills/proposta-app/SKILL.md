---
name: proposta-app
description: Escrever proposta comercial para leads de aplicativo mobile ou web — e-mail que apresenta o caso de uso móvel identificado e convida para reunião de briefing. Acione quando o usuário disser "manda proposta de app", "proposta de aplicativo para [empresa]", "envia proposta mobile".
---

# Proposta por e-mail — Aplicativo

O e-mail de app apresenta um caso de uso específico de mobilidade que o lead não tem hoje. Não vende tecnologia — vende a operação funcionando em campo.

## Pré-requisito

Lead com `oferta: app` e `diagnostico` do `qualificacao-app`. Carregar via `obter_lead(slug)`.

## Princípios

1. **Citar a operação em campo.** A dor é concreta: "sua equipe de técnicos", "seus entregadores", "seus vendedores externos".
2. **Antes/depois em 2 frases.** Hoje: WhatsApp + planilha + ligo pro técnico. Com o app: [resultado concreto].
3. **Não falar de plataforma ou tecnologia.** Nunca mencionar React Native, Flutter, PWA — isso é detalhe de briefing.
4. **CTA = briefing de 30 minutos.** A reunião inicial é para entender a operação, não para fechar contrato.
5. **Curto.** 120–180 palavras.

## Estrutura

- **Assunto**: `[Nome], vi como funciona a operação de campo da [Empresa]` ou `[Nome], sobre a coordenação da equipe de [serviço]`
- **Parágrafo 1**: observação específica sobre a equipe externa detectada (do diagnóstico) + como parece funcionar hoje.
- **Parágrafo 2**: o que muda com um app — falar em resultado, não em funcionalidade.
- **Parágrafo 3**: proposta de reunião de briefing para entender a operação de perto.
- **CTA**: "Me conta como funciona hoje e eu preparo um escopo inicial — sem compromisso."
- **Assinatura**.

## Exemplo

```
Assunto: João, sobre a coordenação dos técnicos da Instalações Rápidas

Olá, João! Vi no site que a Instalações Rápidas atende toda a região com equipe própria de técnicos. Operação exigente — imagino que a coordenação de visitas seja bastante movimentada.

Trabalho com aplicativos para equipes em campo. Vejo que muitas empresas como a sua ainda coordenam via WhatsApp + ligação, o que cria bastante ruído e risco de encaixe errado.

Desenvolvemos apps que o técnico abre no celular, vê a rota do dia, registra o serviço com foto e assina no próprio aparelho — tudo integrado ao gestor em tempo real.

Posso entender melhor a operação de vocês em 30 minutos e preparar um escopo inicial, sem compromisso. Funciona para você essa semana?

[assinatura]
```

## Checklist anti-spam

- [ ] Assunto fala de operação/equipe, não de "app" ou "tecnologia"
- [ ] Sem menção a plataforma (React, Flutter, iOS, Android)
- [ ] Sem preço
- [ ] Máx 1 link
- [ ] Primeira linha com dado real da empresa

## Envio e registro

Criar rascunho no Gmail. Chamar `atualizar_status(slug, "proposta")` após criar o rascunho.
