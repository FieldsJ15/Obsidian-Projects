# 📚 Instruções Completas: Agents-Tribunal

## Sistema de Tribunal Multi-Agente para Análise Biomédica

Este projeto implementa um sistema avançado de análise de slides PDF biomédicos usando um **Tribunal de Agentes** que trabalha em múltiplas passagens para garantir a melhor resposta possível.

---

## 🎯 O que este sistema faz

1. **Converte PDFs de slides em imagens** de alta resolução
2. **Analisa cada slide** usando três agentes especializados (Observer, Clínico, Engenheiro)
3. **Itera múltiplas vezes** sobre cada resposta para melhorar qualidade
4. **Busca informações adicionais** de fontes oficiais (PubMed, guidelines, etc.)
5. **Gera notebooks Jupyter** completos com imagens, análises e referências

---

## 📋 Pré-requisitos

### 1. Python 3.10 ou superior

Verifica se tens Python instalado:

```powershell
python --version
```

Se não tiveres, descarrega de [python.org](https://www.python.org/downloads/).

### 2. Poppler (para conversão de PDF)

**Windows:**
1. Vai a: https://github.com/oschwartz10612/poppler-windows/releases
2. Descarrega o ZIP da última release
3. Extrai para `C:\Program Files\poppler`
4. Adiciona `C:\Program Files\poppler\bin` à variável de ambiente **PATH**
   - Abre "Variáveis de Ambiente" no Windows
   - Edita a variável "Path" do sistema
   - Adiciona `C:\Program Files\poppler\bin`
   - Reinicia o terminal

**Verifica se funciona:**
```powershell
pdftoppm -h
```

### 3. Node.js (opcional, para alguns MCPs)

Se quiseres usar MCPs baseados em Node.js (ex: Context7, Sequential Thinking):

1. Descarrega de [nodejs.org](https://nodejs.org/)
2. Instala e verifica:
```powershell
node --version
npm --version
```

---

## 🚀 Instalação do Projeto

### Passo 1: Navegar para o diretório do projeto

```powershell
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
```

### Passo 2: Criar ambiente virtual (recomendado)

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Passo 3: Instalar dependências

```powershell
pip install -r requirements.txt
```

**Dependências instaladas:**
- `mcp[cli]` - SDK do Model Context Protocol
- `pdf2image` - Conversão de PDF para imagens
- `Pillow` - Processamento de imagens
- `nbformat` - Criação de notebooks Jupyter
- `requests` - Para futuras integrações de APIs

---

## ⚙️ Configuração no Cursor

### Passo 1: Abrir Settings do Cursor

1. Pressiona `Ctrl + ,` (ou `Cmd + ,` no Mac)
2. Vai a **Features → MCP**
3. Clica em **Add New MCP Server**

### Passo 2: Adicionar o servidor de processamento de slides

**Servidor 1: Biomedical-Slide-Processor**

- **Name**: `Biomed-Slide-Agent`
- **Type**: `command (stdio)`
- **Command**: `python`
- **Args**: `server.py`
- **Working directory**: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal`

**Nota:** Se usares um ambiente virtual, o comando pode ser:
- **Command**: `.venv\Scripts\python.exe`
- **Args**: `server.py`

### Passo 3: Adicionar MCPs opcionais (recomendados)

#### A) PubMed MCP (para busca de literatura médica)

- **Name**: `PubMed-Search`
- **Type**: `command (stdio)`
- **Command**: `uvx`
- **Args**: `pubmed-search-mcp-server`

**Nota:** Requer `uv` instalado. Se não tiveres:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### B) Sequential Thinking (raciocínio passo a passo)

- **Name**: `Sequential-Thinking`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-sequential-thinking`

#### C) Context7 (documentação atualizada de bibliotecas)

- **Name**: `Context7`
- **Type**: `command (stdio)`
- **Command**: `npx`

- **Args**: `-y context7`

#### D) Perplexity (busca web com referências)

- **Name**: `Perplexity`
- **Type**: `command (stdio)`
- **Command**: `npx`
- **Args**: `-y @modelcontextprotocol/server-perplexity`

**Nota:** Pode requerer API key do Perplexity (configurar nas variáveis de ambiente).

---

##  Como Usar

### Exemplo 1: Processar slides de uma aula

1. **Coloca o PDF na pasta do projeto** (ex: `Lecture_01.pdf`)

2. **Abre o Composer do Cursor** (`Ctrl + I` ou `Cmd + I`)

3. **Escreve:**
```
Processa os primeiros 5 slides do ficheiro 'Lecture_01.pdf'. 
Usa o Tribunal para analisar cada slide em detalhe, valida os conceitos 
importantes com PubMed e guarda tudo num notebook chamado 
'Estudo_cardiologia.ipynb'.
```

4. **O sistema vai:**
   - Validar o PDF
   - Converter cada slide em imagem
   - Analisar com Observer → Clínico → Engenheiro (múltiplas passagens)
   - Buscar referências no PubMed quando necessário
   - Criar o notebook com tudo organizado

### Exemplo 2: Análise de um slide específico

```
Analisa o slide 3 do ficheiro 'Aula_Neuro.pdf'. 
Inclui imagens de documentos oficiais (PubMed, guidelines) 
relacionados com o tema e cria um resumo detalhado.
```

### Exemplo 3: Criar caderno completo de uma aula

```
Processa todos os slides do ficheiro 'Aula_01.pdf' e cria um 
notebook completo chamado 'Aula_01_Completo.ipynb' com:
- Imagens de cada slide
- Explicações detalhadas
- Referências bibliográficas
- Imagens de documentos oficiais quando relevante
```

---

##                                   Como Funciona o Tribunal Multi-Passagem

Quando fazes uma pergunta, o sistema:

1. **Cria uma resposta inicial simples**

2. **Observer (Passagem 1):**
   - Descreve o que vê no slide
   - Identifica elementos visuais
   - Reescreve a resposta melhorada

3. **Clínico (Passagem 1):**
   - Interpreta em contexto médico
   - Valida factos com PubMed (se necessário)
   - Reescreve a resposta melhorada

4. **Engenheiro (Passagem 1):**
   - Adiciona perspetiva de engenharia biomédica
   - Explica modelos e instrumentação
   - Reescreve a resposta melhorada

5. **Clínico (Passagem 2):**
   - Revalida a resposta final
   - Garante precisão clínica
   - Reescreve se necessário

6. **Observer (Passagem 2):**
   - Verifica coerência visual
   - Simplifica linguagem complexa
   - Produz versão final

7. **Meta-Tribunal:**
   - Síntese final
   - Garante clareza e correção
   - Produz resposta única para o utilizador

**Tu só vês a versão final**, mas todas as iterações ficam guardadas internamente.

---

## 📁 Estrutura de Ficheiros

```
Agents-Tribunal/
├── server.py                    # Servidor MCP principal
├── .cursorrules                 # Regras do Tribunal
├── requirements.txt             # Dependências Python
├── README.md                    # Documentação geral
├── INSTRUCOES_COMPLETAS.md      # Este ficheiro
├── MCPs_RECOMENDADOS.md         # Lista de MCPs opcionais
├── notebook_images/             # Imagens dos slides (criado automaticamente)
└── *.ipynb                      # Notebooks gerados
```

---

## 🛠️ Resolução de Problemas

### Erro: "Poppler not found"

**Solução:**
1. Verifica se o Poppler está no PATH
2. Reinicia o terminal após adicionar ao PATH
3. Testa: `pdftoppm -h`

### Erro: "Module not found: mcp"

**Solução:**
```powershell
pip install -r requirements.txt
```

### Erro: "PDF não pode ser renderizado"

**Solução:**
1. Verifica se o PDF não está corrompido
2. Tenta abrir o PDF num visualizador normal
3. Confirma que o Poppler está instalado corretamente

### MCP não aparece no Cursor

**Solução:**
1. Verifica os caminhos no Settings → MCP
2. Reinicia o Cursor
3. Verifica os logs do Cursor (View → Output → MCP)

---

## 📚 Recursos Adicionais

### MCPs Recomendados

Ver ficheiro `MCPs_RECOMENDADOS.md` para lista completa de MCPs úteis.

### Documentação Oficial

- **MCP**: https://modelcontextprotocol.io
- **FastMCP**: https://github.com/jlowin/fastmcp
- **Cursor MCP**: https://cursor.directory

---

## 💡 Dicas

1. **Começa com poucos slides** (ex: 3-5) para testar
2. **Usa nomes descritivos** para os notebooks (ex: `Aula_01_Cardiologia.ipynb`)
3. **Mantém os PDFs na pasta do projeto** para facilitar referências
4. **Revisa as referências** geradas - o sistema busca automaticamente, mas sempre verifica

---

## 🎉 Pronto!

Agora tens um sistema completo de análise biomédica com Tribunal Multi-Agente. 

**Faz uma pergunta ao Cursor e vê a magia acontecer!** ✨

---

**Última atualização:** 2025-01-XX
**Versão:** 1.0

