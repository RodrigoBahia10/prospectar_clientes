---
name: deploy-hospedagem
description: Esta skill deve ser usada ao publicar páginas em qualquer hospedagem web ou VPS (FTP, cPanel, SFTP, Hostinger, HostGator, Locaweb, VPS Linux, etc.) — upload via script local automático, FTP/SFTP ou cPanel, criação de pastas por cliente, verificação da URL pública e HTTPS. Acione quando o usuário disser "publicar", "subir o site", "colocar no ar", "deploy", "hospedagem", "subir na vps" ou pedir para publicar (skill deploy-hospedagem).
---

# Deploy em Hospedagem Web / VPS

Publicar páginas em `public_html/[pastaBase]/[slug]/` (ou pasta configurada) e garantir a URL pública `https://[dominio]/[pastaBase]/[slug]/` funcionando perfeitamente com HTTPS.

Compatível com qualquer provedor de hospedagem (Hostinger, HostGator, Locaweb, cPanel padrão) e VPS (via FTP/SFTP/SSH).

## Credenciais

Tudo vem de `prospector-config.json` (bloco `hospedagem` ou retrocompatível `hostgator`):
- `servidor`: endereço FTP/SFTP (ex.: `ftp.seudominio.com.br` ou IP da VPS)
- `usuario`: usuário do FTP/cPanel/SSH
- `senha`: senha da hospedagem (**vive SÓ no arquivo local, NUNCA no chat**)
- `dominio`: domínio principal (ex.: `seudominio.com.br`)
- `pastaBase`: subpasta dos clientes (padrão `clientes`)

> Se a senha estiver vazia, oriente o usuário: dashboard → aba Configurações → Conexão de Hospedagem → colar a senha e salvar.

## Método 1 — Publicador automático local (RECOMENDADO: instala uma vez, nunca mais clica)

A publicação roda na máquina do usuário via um publicador local: a cada minuto ele verifica a fila e sobe o que houver, lendo as credenciais do config de forma segura.

1. **Garanta os arquivos do publicador na pasta do projeto** (copiados de `references/`):
   - **Windows**: `publicar-agora.ps1`, `publicar-agora.bat`, `publicador-oculto.vbs`, `instalar-publicador.bat`.
   - **Mac / Linux**: `publicar-agora.command` e `instalar-publicador.command`.
2. **Primeira vez**: peça UM duplo clique no instalador (cria a rotina em segundo plano).
3. **Monte a fila**: escreva `fila-publicacao.txt` na raiz da pasta do projeto, uma linha por arquivo: `caminho/local/arquivo.html|public_html/[pastaBase]/[slug]/index.html`.
4. **Em até 1 minuto**, o publicador sobe tudo sozinho e renomeia a fila para `fila-publicada-[data].txt` (o log fica em `publicador-log.txt`).

## Método 2 — FTP/SFTP direto via comando

Tente publicar diretamente:
```bash
curl -sS --connect-timeout 15 -T [arquivo] "ftp://[servidor]/public_html/[pastaBase]/[slug]/index.html" --user "[usuario]:[senha]" --ftp-create-dirs
```
Se a rede local ou sandbox bloquear conexões externas, use o **Método 1**.

## Método 3 — Navegador (cPanel / Painel Web)

Se os métodos via linha de comando falharem: abrir o Gerenciador de Arquivos do cPanel / painel da hospedagem via MCP de navegador (Playwright). O usuário faz o login dele e o agente navega para criar as pastas e realizar o upload.

## Verificação (obrigatória, após qualquer método)

1. Abra `https://[dominio]/[pastaBase]/[slug]/` e a capa `.../proposta.html` — confirme que carregam com conteúdo certo e responsivo.
2. **HTTPS obrigatório**: precisa carregar com cadeado SSL válido.
3. Atualize o status no CRM via `atualizar_status(slug, "publicado")` com a URL final.

