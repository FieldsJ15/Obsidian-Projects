## Agents-Tribunal – Pipeline Biomédico com MCP em Cursor

Este projeto implementa um servidor MCP em Python para:
- Ler slides em PDF de aulas de medicina/engenharia biomédica.
- Converter cada slide em imagem.
- Gerar um Jupyter Notebook com explicações detalhadas suportadas por um “Tribunal” de perspetivas (Observer, Clínico, Engenheiro).

Tudo foi pensado para funcionar de forma integrada com o Cursor (MCP via `stdio`), de forma rápida e simples.

---

### 1. Pré‑requisitos (Windows – máquina do utilizador)

- **Python 3.10+** instalado.
- **PyMuPDF** (`pip install PyMuPDF`) – já está listado em `requirements.txt` e elimina a dependência obrigatória do Poppler.
- (Opcional) **Poppler** – apenas necessário se quiseres manter o fallback `pdf2image`.
- **Conta no Google AI Studio** para obter a API key do Gemini (mesmo que uses Cursor Pro).
- **Cursor Pro** com acesso aos modelos multimodais.

Opcional mas recomendado:
- **uv** (gestor de ambientes Python ultrarrápido):

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Se não quiseres usar `uv`, podes usar `pip` normalmente.

---

### 2. Instalar dependências do projeto

No diretório do projeto (`C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal`):

#### Com `uv` (recomendado)

```powershell
uv venv
uv pip install -r requirements.txt
```

#### Com `pip` normal

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Servidor MCP: `server.py`

O ficheiro `server.py` implementa o servidor MCP **Biomedical-Slide-Processor** com três tools:

- **`inspect_pdf_metadata(pdf_path: str)`**
  - Abre o PDF com **PyMuPDF** e retorna o número de páginas (sem precisar de Poppler).
  - Se PyMuPDF não estiver disponível, recorre ao `pdf2image` como fallback.

- **`process_slide_for_vision(pdf_path: str, page_number: int)`**
  - Renderiza a página (1‑based) em alta resolução (2×) com PyMuPDF e guarda `notebook_images/slide_{page}.png`.
  - Cria uma versão JPEG reduzida para enviar ao modelo multimodal (Gemini/GPT‑4o) com consumo de tokens otimizado.

- **`append_to_notebook(notebook_path: str, slide_number: int, analysis_text: str, biomedical_context: str, relevant_links: str, external_images: str = "", python_code: str = "")`**
  - Cria (ou atualiza) um ficheiro `.ipynb`.
  - Cada secção inclui:
    - Imagem do slide.
    - Análise visual (Observer).
    - Contexto biomédico (Clínico + Engenheiro).
    - Referências (PubMed, guidelines, etc.).
    - Imagens externas (documentos oficiais, PubMed, etc.).
    - Código Python executável (simulações/exercícios).

O diretório `notebook_images` é criado automaticamente ao correr o servidor.

Para testar isoladamente (fora do Cursor), pode correr:

```powershell
python server.py
```

(irá ficar à espera de mensagens MCP no `stdin`, portanto normalmente só se usa através do Cursor).

---

### 4. Configurar o MCP no Cursor

1. Abrir **Settings** do Cursor.
2. Ir a **Features → MCP**.
3. Clicar em **Add New MCP Server**.

Servidor 1 – Processador de Slides:
- **Name**: `Biomed-Slide-Agent`
- **Type**: `command (stdio)`
- **Command**: `python`
- **Args**: `server.py`
- **Working directory**: apontar para o diretório do projeto `Agents-Tribunal`.

Opcional – Servidor PubMed:
- Pode adicionar um servidor MCP de PubMed disponível na comunidade (via `uvx` ou `npx`), por exemplo:
  - **Command**: `uvx`
  - **Args**: `pubmed-search-mcp-server`

---

### 5. Regras do Tribunal: `.cursorrules`

O ficheiro `.cursorrules` já foi criado neste projeto e:
- Define três papéis internos: **Observer**, **Clínico**, **Engenheiro**.
- Instrui o modelo do Cursor a:
  - Usar `inspect_pdf_metadata` para validar o PDF.
  - Usar `process_slide_for_vision` para cada slide.
  - (Opcional) Consultar PubMed ou outras tools biomédicas para validar factos.
  - Agregar o resultado com `append_to_notebook`.
- Obriga a escrita em **português** e recomenda estrutura clara (Resumo, Fisiologia/Patologia, Engenharia, Referências).

Pode ajustar o texto em `.cursorrules` conforme preferir (mais clínico, mais engenharia, etc.).

---

### 6. Fluxo de utilização dentro do Cursor

1. Certificar-se de que:
   - As dependências Python estão instaladas.
   - O servidor MCP `Biomed-Slide-Agent` está configurado.
   - O PDF de interesse (ex.: `Lecture_01.pdf`) está acessível a partir da pasta do projeto (ou indicar o caminho absoluto).

2. Abrir o **Composer** do Cursor (atalho tipo "chat" com o agente).

3. Escrever um pedido em linguagem natural, por exemplo:

> Processa os primeiros 5 slides do ficheiro `Lecture_01.pdf`, usa o Tribunal para explicar cada slide em detalhe (fisiologia + engenharia biomédica), valida conceitos importantes com PubMed, e guarda tudo num notebook chamado `Estudo_cardiologia.ipynb`.

4. O Cursor deve:
   - Chamar `inspect_pdf_metadata`.
   - Loop de páginas 1..5, chamando:
     - `process_slide_for_vision`.
     - (Opcional) tools de PubMed.
     - `append_to_notebook`.
   - No fim, informar que o notebook foi criado/atualizado.

5. Abrir o `Estudo_cardiologia.ipynb` (ou o nome que escolheu) no próprio Cursor ou noutro ambiente Jupyter para rever os apontamentos gerados.

---

### 7. Extensões futuras (ideias)

- Integrar um servidor MCP real de **multi‑agentes** (ex.: CrewAI via MCP) e usá‑lo como “segundo Tribunal” que revê o trabalho.
- Adicionar tools para:
  - Pesquisa em guidelines (ESC, ACC, etc.).
  - Base de dados de fármacos (interações, farmacocinética).
  - Dados de dispositivos médicos (marcapassos, próteses, stents).
- Gerar automaticamente **células de código Python** no notebook para:
  - Simular modelos fisiológicos.
  - Visualizar sinais (ECG, EMG, EEG) com bibliotecas como `mne`, `matplotlib`, `scipy`.

Tudo o que é necessário para o fluxo básico de PDFs → Notebook biomédico com Tribunal já está preparado neste repositório.

---

### 8. Integração com o Google Gemini (GCP + AI Studio)

1. **Obter a API key**
   - Vai a https://aistudio.google.com/app/apikey e cria a tua chave (funciona com o programa *Google Cloud for Students*).
   - Guarda a key como variável de ambiente `GEMINI_API_KEY` ou adiciona-a em `Cursor → Settings → Accounts → Google AI`.

2. **Configurar o modelo no Cursor**
   - Abre o Composer (`Ctrl + I`) e, no seletor de modelos, escolhe:
     - `gemini-1.5-pro-latest` (Juiz: síntese profunda, janela 2M tokens).
     - `gemini-1.5-flash-latest` ou `gemini-2.0-flash-exp` (Analista/Crítico: rápido, barato, com visão).
   - Se precisares de usar o endpoint OpenAI-compatível, adiciona em `Settings → Models`:
     ```
     Name: Gemini-Flash
     Base URL: https://generativelanguage.googleapis.com/v1beta/openai/
     API Key: <GEMINI_API_KEY>
     Model: gemini-1.5-flash-latest
     ```

3. **Context caching / economia de tokens**
   - Mantém o mesmo chat aberto para todo o processo do PDF (não abras uma nova thread).
   - Sobe o PDF/slide uma única vez por sessão; nas mensagens seguintes refere-te a “este documento em cache”.
   - Para grandes corpora, usa `gemini-1.5-pro` como “Juiz” final e `gemini-1.5-flash` para os rascunhos (estratégia tribunal).

4. **MCPs extra sugeridos**
   ```json
   {
     "mcpServers": {
       "pdf-analyst": {
         "command": "npx",
         "args": ["-y", "@fabriqa.ai/pdf-reader-mcp"]
       },
       "pubmed-researcher": {
         "command": "npx",
         "args": ["-y", "@cyanheads/pubmed-mcp-server"]
       },
       "filesystem-notes": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:/Users/joaop/Documentos/Notas"]
       }
     }
   }
   ```
   - **pdf-analyst**: extração de texto + imagens (com `read_pdf_images`).
   - **pubmed-researcher**: validação científica via NCBI E-utilities.
   - **filesystem-notes**: gravação segura das notas em disco.

5. **Fluxo sugerido (Tribunal)**
   1. **Analista** (Gemini Flash): extrai tópicos, chama `process_slide_for_vision`, guarda imagens.
   2. **Crítico** (Gemini Flash): usa `pubmed-researcher` para confirmar cada afirmação.
   3. **Juiz** (Gemini Pro): gera a versão final, chama `append_to_notebook` e escreve o `.ipynb`.

Com esta arquitetura, tens um *stack* completo: extração local (PyMuPDF), validação científica (PubMed), armazenamento organizado e raciocínio multimodal de alto nível com o Gemini.


