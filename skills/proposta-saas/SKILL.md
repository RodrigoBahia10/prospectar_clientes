---
name: proposta-saas
description: Escrever proposta comercial para leads de SaaS — e-mail que apresenta o problema de mercado identificado e convida para demo ou reunião de apresentação do produto. Acione quando o usuário disser "manda proposta de SaaS", "envia proposta de produto", "proposta para [empresa] sobre o sistema".
---

# Proposta por e-mail — SaaS

A proposta de SaaS diferencia-se das demais: o produto já existe (ou está sendo construído), então o e-mail apresenta a solução, não o diagnóstico. O foco é despertar curiosidade sobre como o produto resolve especificamente a dor do nicho deste lead.

## Pré-requisito

Lead com `oferta: saas` e `diagnostico` do `qualificacao-saas`. Carregar via `obter_lead(slug)`.

## Princípios

1. **Problema do nicho antes do produto.** Abrir com a dor específica do segmento, não com "temos um software".
2. **Especificidade como credibilidade.** Mostrar que você conhece o nicho: citar o processo específico que o produto resolve.
3. **CTA = demo ou trial.** Não fecha por e-mail — abre uma demonstração.
4. **Diferencial concreto.** Por que não uma planilha? Por que não um sistema genérico? Responder isso em 1 frase.
5. **Curto.** 120–180 palavras.

## Estrutura

- **Assunto**: `[Nome], [empresas do nicho] estão trocando [ferramenta genérica] por isso` ou `Como [nicho] eliminou o [processo manual] com 1 sistema`
- **Parágrafo 1**: problema de mercado do nicho (do diagnóstico) — específico e verificável.
- **Parágrafo 2**: como o produto resolve, em termos de resultado, não de funcionalidade.
- **Parágrafo 3**: diferencial de 1 linha (o que não existe em alternativas genéricas).
- **CTA**: demo de 20 minutos ou link para trial.
- **Assinatura**.

## Checklist anti-spam

- [ ] Assunto sem "Software", "Sistema", "SaaS", "Solução" — termos vendem menos
- [ ] Sem lista de funcionalidades
- [ ] Sem preço no primeiro e-mail
- [ ] Máx 1 link (demo/trial/calendário)
- [ ] Tom de par, não de vendedor

## Envio e registro

Criar rascunho no Gmail. Chamar `atualizar_status(slug, "proposta")` após criar o rascunho.
