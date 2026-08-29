---
name: qualificacao-consultoria
description: Qualificar leads para consultoria e diagnóstico de processos, gerando um roteiro de entrevista personalizado e um pré-diagnóstico baseado em análise automatizada de site e LinkedIn via Playwright. Acione quando o usuário disser "qualifica para consultoria", "prepara diagnóstico de [empresa]", "gera roteiro de entrevista" ou após prospecção com oferta=consultoria.
---

# Qualificação automatizada — Consultoria

A consultoria começa com um diagnóstico pago — não é serviço gratuito. A qualificação tem duas etapas: análise automatizada (Playwright) para decidir se vale entrar em contato, e geração de roteiro de entrevista personalizado para a reunião inicial.

## Fontes de análise

1. **`pontuar_site(url)`** — verificação técnica básica.
2. **Playwright no site** — maturidade digital, complexidade da operação, indícios de crescimento.
3. **Playwright no LinkedIn** — cargo do contato, posts sobre desafios de gestão, tamanho da equipe, crescimento recente.
4. **Google** — buscar notícias ou menções sobre crescimento, expansão, contratações.

## Análise automatizada (Playwright)

### Sinais de empresa que precisa de consultoria

**No site** (via Playwright):
- Muitos serviços/produtos listados sem organização clara (crescimento desordenado)
- Página "sobre" menciona "crescimento rápido", "equipe em expansão", "atendemos mais de X cidades"
- Site com múltiplos estilos inconsistentes (reformas sem planejamento)
- Formulários de contato genéricos sem especialização de fluxo
- Múltiplos números de telefone sem centralização

**No LinkedIn** (via Playwright):
- Empresa com 10–200 funcionários (tamanho que sente dor de crescimento mas tem budget)
- Posts do gestor/dono sobre: "estamos crescendo mas...", "buscamos profissionais", "precisamos de soluções"
- Vagas abertas para áreas administrativas ou de processos
- Perfil do dono: muitas responsabilidades listadas (sinal de centralização/gargalo)
- Mudanças de ferramenta recentes (ex.: "migramos para X" nos posts)

### Score (0–10)

| Critério | Pontos |
|----------|--------|
| Empresa 10–200 funcionários | 2 |
| Posts de desafio de escala no LinkedIn | 2 |
| Site com desorganização visível | 1 |
| Vagas abertas para operação/admin | 2 |
| Dono acumula muitos cargos | 1 |
| Setor com alta regulação ou complexidade | 1 |
| Crescimento recente detectado (news/LinkedIn) | 1 |

| Score | Ação |
|-------|------|
| 0–3 | Não qualificado agora |
| 4–6 | Contato exploratório (InMail ou e-mail) |
| 7–10 | Proposta de diagnóstico pago |

## Gerar roteiro de entrevista personalizado

Esta é a entrega principal desta skill: um roteiro de perguntas para a reunião de diagnóstico inicial, personalizado para o que foi encontrado na análise.

```
Roteiro de Entrevista — [Nome da empresa]
Score: [X]/10

OBJETIVO DA REUNIÃO: Diagnóstico inicial (30-45 min) para propor projeto de consultoria.

ABERTURA (5 min):
- Contextualizar: "Vi no LinkedIn que [menção específica ao post/perfil]. Queria entender melhor..."
- Validar o tempo disponível.

PERGUNTAS POR ÁREA DE DOR IDENTIFICADA:

[Se detectou crescimento rápido:]
- "Você mencionou que a equipe cresceu. Quais processos ficaram mais difíceis de controlar com esse crescimento?"
- "O que você faz hoje manualmente que antes era simples mas virou gargalo?"

[Se detectou site desorganizado:]
- "Como os clientes chegam até vocês hoje? O site ajuda nisso?"
- "Qual é o fluxo desde o primeiro contato até a venda? Quantas pessoas tocam nesse processo?"

[Se detectou vagas abertas:]
- "Vi que estão contratando para [área]. Isso resolve o problema ou é um sintoma de algo maior?"

PERGUNTAS UNIVERSAIS (sempre fazer):
- "Se você pudesse resolver 1 problema operacional hoje, qual seria?"
- "O que você tentou antes que não funcionou?"
- "Qual seria o impacto no negócio se esse problema fosse resolvido?"
- "Quem mais na empresa é afetado por esse problema?"
- "Você tem budget definido para projetos de melhoria de processos?"

ENCERRAMENTO (5 min):
- Resumir os 2–3 pontos principais levantados.
- Apresentar a proposta de diagnóstico: "Com base no que você me contou, faz sentido fazer um diagnóstico estruturado. Posso preparar uma proposta de como isso funcionaria?"
```

## Registrar no CRM

Chamar `salvar_qualificacao(slug, score, diagnostico)` onde o `diagnostico` inclui tanto o pré-diagnóstico quanto o roteiro de entrevista.

## Encerrar

Apresentar o score e o roteiro. Perguntar:
- Se score >= 7: "Quer que eu prepare a proposta de diagnóstico pago para [Nome]?"
- Se score 4–6: "Sugiro um contato exploratório primeiro. Quer que eu prepare o e-mail?"
