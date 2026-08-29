---
name: follow-up-proposta
description: Esta skill deve ser usada para fazer o follow-up de propostas enviadas que ainda não receberam resposta. Acione quando o usuário disser "follow-up", "quem não respondeu", "reforçar a proposta", "checar respostas", "lembrar o cliente" ou pedir para verificar/enviar follow-ups.
---

# Follow-up de propostas

O follow-up é a segunda chance de converter um lead que abriu o e-mail mas não respondeu. Ele é curto, gentil e diferente da proposta — não é reenviar a proposta, é uma pergunta humana.

## Regras invioláveis

1. **Máximo 1 follow-up por lead, nunca repetir.** Se `obs` do lead já contém "Follow-up enviado", pule — não há segundo follow-up.
2. **Mínimo 3 dias úteis desde a proposta.** Checar `dataProposta` do lead.
3. **Nunca enviar em fim de semana.** Se for sábado ou domingo, avisar o usuário e agendar para segunda.
4. **Nunca reenviar a proposta ou o link.** O follow-up NÃO anexa nada, NÃO repete o link da capa.
5. **Tom humano, não de vendedor.** Sem urgência, sem pressão, sem gatilhos de marketing.

## Fluxo

### 1. Verificar quem precisa de follow-up

Chamar `followups_pendentes(dias=3)` do MCP `prospector-crm`. Retorna apenas leads:
- Com `status='proposta'`
- Com `dataProposta` há 3+ dias
- Sem "follow-up" já registrado em `obs`

Se a lista estiver vazia: informar ("Nenhum lead aguardando follow-up no momento.") e encerrar.

Se houver leads: apresentar a lista (nome, e-mail, data da proposta, dias aguardando) e perguntar se quer enviar para todos ou para um específico.

### 2. Compor o e-mail de follow-up

Para cada lead selecionado:

**Obrigatório:**
- **Comprimento**: 60–90 palavras no corpo (sem assinatura).
- **Assunto**: curto, pessoal, sem "Follow-up:" no início. Ex.: `Dra. [Nome], conseguiu ver a página?`
- **Parágrafo único**: pergunta gentil se conseguiu ver a proposta, reconhecendo que a agenda é corrida.
- **Sem o link**: o cliente já tem o e-mail anterior. Repetir o link sinalizaria spam.
- **Assinatura completa**: nome + apresentação + WhatsApp do config.

**Estrutura sugerida:**
> Olá [Nome]! Enviei uma página nova para [nome do negócio] há alguns dias — queria saber se teve uma chance de dar uma olhada. Se não, sem problema — a página continua no ar quando quiser. Só me diga o que achou quando puder. [assinatura]

**Proibido:**
- Reenviar link da capa ou da página nova
- Mencionar preço
- Palavras de pressão: "última chance", "urgente", "imperdível"
- Emojis no assunto
- CAIXA ALTA

### 3. Checklist anti-spam

- [ ] Assunto ≤ 60 caracteres, formulado como pergunta pessoal
- [ ] Sem link no corpo
- [ ] Sem palavras-gatilho de spam
- [ ] Corpo HTML minimalista (só parágrafos, sem cores, botões ou imagens)
- [ ] Primeira linha 100% personalizada com o nome do lead

### 4. Criar rascunho no Gmail

Usar o MCP/conector do Gmail do Antigravity para criar o rascunho. Se não disponível, gerar link de compose:

```
https://mail.google.com/mail/?view=cm&fs=1&to=[email]&su=[assunto em URL]&body=[corpo em URL]
```

Avisar: **"Revise o rascunho antes de enviar — nunca enviar em massa, apenas 1 por 1."**

### 5. Registrar o follow-up no CRM

Após criar o rascunho (não após enviar):

```
registrar_followup(slug="[slug do lead]")
```

Isso marca "Follow-up enviado em [data]" nas observações, impedindo duplicatas.

### 6. Encerrar

Confirmar quantos rascunhos foram criados. Sugerir verificar respostas em 2–3 dias.

## Variações de assunto (referência)

- `[Nome], conseguiu ver a página que preparei?`
- `Passando para saber sua impressão, [Nome]`
- `[Nome do negócio] — só um acompanhamento rápido`
- `Dra./Dr. [Nome], sua opinião sobre a página`

## Boas práticas de timing

- Dias ideais: terça, quarta ou quinta-feira.
- Horários: 8h–11h ou 14h–17h (horário do lead).
- Segunda e sexta: aceitável mas não ideal.
- Fim de semana: nunca.
