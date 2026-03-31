# 🔧 MCPs Recomendados para Agents-Tribunal

Lista de servidores MCP (Model Context Protocol) úteis para enriquecer o sistema de análise biomédica.

---

## 📚 Categoria: Literatura e Pesquisa

### 1. PubMed MCP
**Função:** Busca de artigos científicos na base de dados PubMed

**Configuração no Cursor:**
- **Name**: `PubMed-Search`
- **Type**: `command (stdio)`
- **Command**: `uvx`
- **Args**: `pubmed-search-mcp-server`

**Instalação:**
```powershell
# Requer uv instalado
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Repositório:** `gradusnikov/pubmed-search-mcp-server` ou `masa061580/enhanced-pubmed-mcp-server`

**Ferramentas expostas:**
- `search_publications(query: str)` - Busca artigos
- `get_publication_details(pubmed_id: str)` - Detalhes de um artigo

---

### 2. Perplexity MCP
**Função:** Busca web com referências e citações

**Configuração no Cursor:**
- **Name**: `Perplexity`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-perplexity`

**Nota:** Pode requerer API key do Perplexity (configurar em variáveis de ambiente).

**Repositório:** `modelcontextprotocol/servers`

---

## 🧠 Categoria: Raciocínio e Análise

### 3. Sequential Thinking
**Função:** Força o modelo a pensar passo a passo sobre problemas complexos

**Configuração no Cursor:**
- **Name**: `Sequential-Thinking`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-sequential-thinking`

**Repositório:** `modelcontextprotocol/servers`

**Uso:** Melhora a qualidade de explicações complexas, especialmente em fisiologia e patologia.

---

### 4. DeepWiki
**Função:** Busca em documentações e repositórios de código

**Configuração no Cursor:**
- **Name**: `DeepWiki`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-deepwiki`

**Repositório:** `modelcontextprotocol/servers`

**Uso:** Útil para buscar documentação de bibliotecas Python (ex: scikit-learn, mne) usadas em análise biomédica.

---

## 💻 Categoria: Código e Documentação

### 5. Context7
**Função:** Busca documentação atualizada de bibliotecas de software

**Configuração no Cursor:**
- **Name**: `Context7`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y context7`

**Repositório:** `upstash/context7`

**Uso:** Garante que o código Python gerado nos notebooks usa funções atualizadas e não deprecadas.

---

### 6. GitHub MCP
**Função:** Acesso a repositórios GitHub (código, issues, PRs)

**Configuração no Cursor:**
- **Name**: `GitHub`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-github`

**Nota:** Requer token GitHub (configurar em variáveis de ambiente).

**Repositório:** `modelcontextprotocol/servers`

---

## 🏥 Categoria: Dados Biomédicos Específicos

### 7. Healthcare MCP
**Função:** Acesso a bases de dados de fármacos, FDA, RxNorm, guidelines clínicas

**Configuração no Cursor:**
- **Name**: `Healthcare`
- **Type**: `command (stdio)`
- **Command**: `uvx`
- **Args**: `healthcare-mcp-public`

**Repositório:** `Cicatriiz/healthcare-mcp-public` ou `JamesANZ/medical-mcp`

**Uso:** Informações sobre fármacos, interações, vias metabólicas (ex: CYP2C9 para Warfarin).

---

### 8. BioContext MCP
**Função:** Acesso a bases de dados genómicas e proteómicas (UniProt, etc.)

**Configuração no Cursor:**
- **Name**: `BioContext`
- **Type**: `command (stdio)`
- **Command**: `uvx`
- **Args**: `biomcp`

**Repositório:** `genomoncology/biomcp`

**Uso:** Essencial para slides sobre proteínas, sequências genéticas, folding.

---

## 🔍 Categoria: Busca e Extração

### 9. Markitdown (Microsoft)
**Função:** Converte PDFs, Word, imagens em Markdown

**Configuração no Cursor:**
- **Name**: `Markitdown`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @microsoft/markitdown-mcp`

**Repositório:** `microsoft/markitdown`

**Uso:** Alternativa/complemento ao `pdf2image` para extrair texto de PDFs.

---

### 10. Playwright MCP
**Função:** Controla navegador para extrair dados de páginas web

**Configuração no Cursor:**
- **Name**: `Playwright`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-playwright`

**Repositório:** `modelcontextprotocol/servers`

**Uso:** Útil para buscar imagens/documentos de sites oficiais (ex: guidelines ESC/ACC).

---

## 🤖 Categoria: Multi-Agente e Feedback

### 11. Zen MCP
**Função:** Orquestra múltiplos modelos (Claude, GPT-4, Gemini) para consenso

**Configuração no Cursor:**
- **Name**: `Zen`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-zen`

**Nota:** Requer configuração de APIs dos modelos (Claude, OpenAI, Google).

**Repositório:** `modelcontextprotocol/servers`

**Uso:** Permite que vários modelos "discutam" antes de dar resposta final (tribunal real).

---

### 12. MCP Feedback Enhanced
**Função:** Sistema de feedback melhorado com Gemini

**Configuração no Cursor:**
- **Name**: `Feedback-Enhanced`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @minidoracat/mcp-feedback-enhanced`

**Repositório:** `Minidoracat/mcp-feedback-enhanced`

**Uso:** Avalia e melhora respostas geradas.

---

## 📊 Categoria: Visualização e Dados

### 13. Memory (Knowledge Graph)
**Função:** Memória persistente para guardar factos importantes

**Configuração no Cursor:**
- **Name**: `Memory`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-memory`

**Repositório:** `modelcontextprotocol/servers`

**Uso:** Guarda informações de slides anteriores para manter contexto em conversas longas.

---

## 🎯 Configuração Mínima Recomendada

Para começar, configura pelo menos:

1. **Biomed-Slide-Agent** (já implementado)
2. **PubMed-Search** (literatura médica)
3. **Sequential-Thinking** (raciocínio passo a passo)

Depois, adiciona conforme necessidade:
- **Context7** (se gerar código Python)
- **Perplexity** (busca web com referências)
- **Healthcare** (se trabalhar com fármacos)

---

## 📝 Notas Importantes

- **Variáveis de Ambiente:** Alguns MCPs requerem API keys. Configura-as no sistema ou via scripts wrapper.
- **Node.js:** Muitos MCPs requerem Node.js. Instala de [nodejs.org](https://nodejs.org/).
- **uv:** Para MCPs Python via `uvx`, instala: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

---

## 🔗 Recursos

- **MCP Registry:** https://github.com/modelcontextprotocol/servers
- **Awesome MCP Servers:** https://github.com/awesome-mcp/awesome-mcp-servers
- **Documentação MCP:** https://modelcontextprotocol.io

---

**Última atualização:** 2025-01-XX

