---
name: qualificacao-saas
description: Qualificar leads para venda de SaaS (produto digital com recorrência) usando Playwright para analisar o site e LinkedIn da empresa, gerando score 0-10 e diagnóstico de fit de mercado. Acione quando o usuário disser "qualifica para SaaS", "analisa o fit de [empresa]", "vê se tem mercado" ou após prospecção com oferta=saas.
---

# Qualificação automatizada — SaaS

Avaliar se o lead representa um mercado viável para um produto digital recorrente. Diferente da automação (que tem ROI calculável), o SaaS exige fit de mercado: dor recorrente, disposição a pagar mensalmente e ausência de solução dominante no nicho.

## Fontes de análise

1. **`pontuar_site(url)`** — verificação inicial.
2. **Playwright no site** — análise da operação e ferramentas usadas.
3. **Playwright no LinkedIn** — tamanho da empresa, cargo, linguagem dos posts.
4. **Pesquisa Google** — verificar se existe concorrente direto para este nicho específico.

## Critérios de qualificação (Playwright)

### Dimensão 1 — Tamanho do mercado endereçável (peso: 30%)

Verificar no LinkedIn: quantas empresas similares existem na cidade/estado?
- > 500 empresas similares no Brasil → mercado grande (3 pts)
- 100–500 → mercado médio (2 pts)
- < 100 → nicho pequeno, risco alto (0–1 pt)

### Dimensão 2 — Intensidade da dor (peso: 40%)

Abrir o site da empresa e verificar:
- Usa planilha/WhatsApp/e-mail para o processo central do negócio? (2 pts cada)
- O processo se repete diariamente com volume? (2 pts)
- Custo de erro é alto (saúde, financeiro, jurídico)? (2 pts)
- Sinais no LinkedIn de frustração com processo atual? (2 pts)

### Dimensão 3 — Ausência de concorrente dominante (peso: 30%)

Busca Google: `"[ferramenta para] [nicho específico]" site:br` ou `"software para [nicho]"`:
- Resultado: sem ferramenta específica dominante → 3 pts
- Resultado: 1–2 ferramentas genéricas não especializadas → 2 pts
- Resultado: ferramenta dominante consolidada → 0 pts (desqualificar)

### Score final (0–10)

Somar os pontos (máximo 10) e classificar:

| Score | Classificação | Ação |
|-------|---------------|------|
| 0–3 | Mercado desfavorável | Descartar |
| 4–6 | Mercado possível | Validar com mais pesquisa antes de propor |
| 7–9 | Fit alto | Proposta de MVP ou parceria piloto |
| 10 | Fit perfeito | Proposta prioritária + apresentação executiva |

## Diagnóstico de fit

```
Diagnóstico de SaaS — [Nicho/segmento]
Score: [X]/10

Mercado endereçável: [tamanho estimado]
Dor central identificada: [descrição objetiva]
Ferramentas atuais do mercado: [o que as empresas usam hoje]
Concorrência: [existe? qual? como se diferencia?]

Proposta de produto mínimo viável:
- Core: [funcionalidade central que resolve a dor]
- Diferencial: [o que nenhum concorrente faz bem]
- Modelo de preço sugerido: R$[X]/mês por empresa (baseado em economia gerada)
- TAM estimado: [nº empresas] × R$[preço] = R$[mercado] MRR potencial regional
```

## Registrar no CRM

Chamar `salvar_qualificacao(slug, score, diagnostico)`.

## Encerrar

Se score >= 7: sugerir proposta de reunião/demo.
Se score < 7: apresentar o que falta para qualificar e perguntar se quer pesquisar mais.
