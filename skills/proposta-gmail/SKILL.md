---
name: proposta-gmail
description: Roteador de propostas comerciais — detecta o tipo de oferta do lead no CRM e direciona para a skill de proposta correta. Acione quando o usuário disser "envia proposta", "manda o e-mail", "proposta para [empresa]" sem especificar o tipo. Para tipos específicos, o Antigravity chama diretamente proposta-automacao, proposta-saas, proposta-app ou proposta-consultoria.
---

# Proposta por e-mail — Roteador

## 1. Detectar o tipo de oferta

Carregar o lead via `obter_lead(slug)` e ler o campo `oferta`:

| `oferta` | Skill a acionar |
|----------|-----------------|
| `redesign` | Continuar nesta skill (fluxo abaixo) |
| `automacao` | Delegar para `proposta-automacao` |
| `saas` | Delegar para `proposta-saas` |
| `app` | Delegar para `proposta-app` |
| `consultoria` | Delegar para `proposta-consultoria` |
| `presenca` | Delegar para `proposta-presenca` |

Se `oferta` estiver vazio ou for `redesign`, seguir o fluxo desta skill.
Se for outro tipo, avisar o usuário que está seguindo o fluxo correto para aquela oferta e usar a skill correspondente.

---

# Proposta de redesign de site (oferta: redesign)

O e-mail NÃO vende — ele desperta curiosidade e prova trabalho feito. O fechamento (preço, escopo, reunião) acontece na resposta. Um e-mail que parece de vendedor morre no spam; um e-mail que parece de uma pessoa que já trabalhou de graça pro destinatário é aberto e respondido.

## Princípios

1. **Rapport primeiro.** Abrir com elogio ESPECÍFICO e verificável: a nota no Google, uma avaliação real citada, uma credencial do site. Nunca elogio genérico.
2. **A dor sem ofensa.** Apontar 1-2 defeitos objetivos do site atual como oportunidade ("notei que no celular o site fica difícil de ler"), nunca como crítica ao profissional.
3. **A prova antes do pedido.** O trabalho JÁ está feito e no ar. O link é a proposta.
4. **Zero preço.** Preço só na conversa que a resposta abre.
5. **Zero pressão.** Sem urgência falsa, sem "últimas vagas". Um único CTA: dar uma olhada e responder o que achou.
6. **Curto.** 120-180 palavras. Profissional ocupado não lê e-mail longo de desconhecido.

## Estrutura

- **Assunto**: pergunta pessoal e específica, ≤ 60 caracteres, sem cara de marketing. Ex.: `Dra. [Nome], posso te mostrar uma coisa sobre seu site?` ou `Preparei algo para a [Clínica X]`.
- **Parágrafo 1**: quem encontrou + elogio específico (avaliações/credencial).
- **Parágrafo 2**: observação sobre o site atual (1-2 pontos objetivos).
- **Parágrafo 3**: "preparei uma nova versão, já no ar" + O ÚNICO LINK do e-mail: a página-capa (`.../proposta.html`), que mostra antes e depois lado a lado. Se a capa não existir, linkar a página nova direto.
- **Parágrafo 4**: CTA — abrir no celular também, responder com a impressão.
- **Assinatura**: nome, apresentação e WhatsApp do config (assinatura completa humaniza e reduz suspeita).

## Checklist anti-spam (BLOQUEANTE — rodar antes de criar o rascunho)

Revise o e-mail pronto contra CADA item; se falhar em qualquer um, reescreva antes de criar o rascunho:

- [ ] **1 link só** (a página-capa). Dois links no máximo se incluir o site antigo — nunca mais que isso.
- [ ] **Sem encurtador de URL** (bit.ly e afins = spam na certa). O link é o domínio real, com `https://`.
- [ ] **Link como âncora HTML com texto visível limpo.** O Gmail embrulha TODO link em um redirect próprio (`google.com/url?q=...`) ao salvar — não dá pra impedir, e em corpo de texto puro o embrulho fica VISÍVEL, o que parece golpe. Por isso o rascunho é criado com corpo HTML e o link como âncora: `<a href="https://[dominio]/[pastaBase]/[slug]/proposta.html">https://[dominio]/[pastaBase]/[slug]/proposta.html</a>` — texto visível = a URL limpa montada a partir do config (nunca copiada de outro e-mail). O redirect do Google fica só no href invisível, como em qualquer e-mail do Gmail. Depois de criar, confira o rascunho: o texto visível deve começar em `https://[dominio do config]`.
- [ ] **Domínio limpo e humano.** Se o domínio do config for um subdomínio técnico/temporário (cheio de números, tipo `nome1783367206076.meuprovedor.com`), PARE antes de enviar qualquer proposta: link assim parece golpe e mata a confiança que a capa constrói. Oriente o usuário a ativar o domínio próprio (registro em registro.br ou no provedor de hospedagem) e atualizar o campo `dominio` nas Configurações do dashboard. Proposta só sai com domínio apresentável.
- [ ] **Sem palavras-gatilho**: grátis, promoção, imperdível, oferta, desconto, clique aqui, 100%, garantido, urgente.
- [ ] **Sem CAIXA ALTA no assunto, sem "!!", sem emoji** no assunto.
- [ ] **Texto simples** — corpo HTML minimalista (só parágrafos e a âncora do link; zero cores, botões, imagens ou anexos) (anexo de desconhecido aumenta score de spam E medo de abrir; a capa no link substitui o preview).
- [ ] **Assunto ≤ 60 caracteres**, formulado como pergunta ou frase pessoal com o nome do negócio.
- [ ] **Primeira linha 100% personalizada** (nome + fato real das avaliações) — filtros de spam e humanos reconhecem template genérico.
- [ ] **Remetente = conta Gmail pessoal ativa do usuário** (já tem SPF/DKIM do Google). Nunca sugerir disparo em massa: os envios são 1 a 1, poucos por dia — padrão humano.

## Envio

- Modo **rascunho** (padrão): criar via MCP do Gmail do Antigravity (ferramenta de criar rascunho) ou pelo link de compose do Gmail (`https://mail.google.com/mail/?view=cm&fs=1&to=...&su=...&body=...`) com destinatário, assunto e corpo prontos. Avisar o usuário para revisar antes de enviar.
- Modo **enviar direto**: se o conector não suportar envio, abrir o Gmail web via o MCP de navegador (Playwright), ou criar o rascunho e avisar.
- Nunca enviar para lead sem e-mail confirmado; nesses casos, sugerir contato via WhatsApp com a mesma mensagem adaptada.

## Página-capa (o que o cliente vê ao clicar)

O link do e-mail leva à página-capa gerada no `a skill deploy-hostgator` (template em `references/capa-proposta-template.html`): nome do cliente no topo, antes/depois lado a lado e a assinatura do usuário. Ela existe para dar credibilidade ao clique — o cliente vê o próprio negócio, não um link estranho. Exigências: servida em `https://`, personalizada com dados reais, sem pedido de dado pessoal nenhum.

## Depois do envio

Registrar no banco/`leads.md` (status + data) e no dashboard. As respostas são verificadas pelo comando `a checagem de respostas no Gmail` (Gmail via conector) — sugira ao usuário agendar a verificação diária. Follow-up pelo `o follow-up de propostas` após 3+ dias úteis sem resposta (1 único follow-up por lead: curto, gentil, "conseguiu ver a página?").
