## Arquitetura de Agentes Cognitivos em Nuvem

Guia completo para integrar Google Cloud Platform (GCP), API Gemini e Model Context Protocol (MCP) dentro do Cursor IDE, replicando o fluxo em “tribunal” descrito no relatório original.

---

### 1. Google Cloud Platform (GCP)

1. **Hierarquia**
   - Projeto dedicado (ex.: `cursor-research`) para isolar créditos do programa *Google Cloud for Students*.
   - Usa IAM com *Service Accounts* de permissões mínimas (evita utilizar a conta *Owner* em scripts).

2. **Serviços recomendados**
   - **AI Studio**: gera a API key do Gemini (free tier).
   - **Cloud Run**: hospeda MCPs pesados (ex.: `pubmed-mcp-server`) pagando apenas pelo tempo de execução.
   - **Cloud Storage**: armazena PDFs/figuras em buckets (o Gemini consegue ler diretamente de GCS).
   - **BigQuery**: cruza dados públicos (datasets clínicos, genómicos) com o conteúdo dos slides.

3. **Custos & créditos**
   - Mantém o consumo do Gemini no AI Studio (não gasta os $300 de Vertex AI).
   - Reservar o Vertex AI/Compute Engine apenas para workloads específicos (ex.: pipelines de OCR massivo).

---

### 2. API Gemini & Economia de Tokens

| Modelo              | Função no Tribunal | Notas                                  |
|---------------------|--------------------|----------------------------------------|
| **Gemini 1.5 Pro**  | Juiz               | 2M tokens de contexto, síntese final.  |
| **Gemini 1.5 Flash**| Analista/Crítico   | Mais barato, ideal para rascunhos.     |
| **Gemini 2.0 Flash exp** | Analista multimodal | Versão experimental com visão melhorada.|

**Context caching**
- Faz upload do PDF apenas uma vez por thread.
- Referencia “o documento em cache” nas perguntas seguintes (latência + custo mínimos).

---

### 3. Cursor + MCP

1. **Configurar o Gemini**
   ```text
   Base URL: https://generativelanguage.googleapis.com/v1beta/openai/
   Model: gemini-1.5-pro-latest (ou flash-latest)
   API Key: <GEMINI_API_KEY>
   ```
   *Mesmo com Cursor Pro, a chave própria permite usar todos os modelos públicos do AI Studio.*

2. **mcp.json de referência**
   ```json
   {
     "mcpServers": {
       "biomed-slide-agent": {
         "command": "python",
         "args": ["server.py"],
         "cwd": "C:/Users/joaop/Desktop/Cursor Projects/Agents-Tribunal"
       },
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
         "args": [
           "-y",
           "@modelcontextprotocol/server-filesystem",
           "C:/Users/joaop/Documentos/Notas"
         ]
       }
     }
   }
   ```

3. **Fluxo multimodal**
   - `process_slide_for_vision` cria `notebook_images/slide_X.png`.
   - O modelo multimodal (Gemini ou GPT‑4o) “vê” a imagem e gera:
     - `analysis_text`
     - `biomedical_context`
     - `relevant_links`
     - `python_code`
   - `append_to_notebook` grava tudo no `.ipynb`.

---

### 4. Tribunal Multi-Agente

1. **Analista (Gemini Flash)**
   - Extrai tópicos, figuras e prepara rascunhos em JSON (economia de tokens).
   - Guarda imagens via `filesystem-notes`.

2. **Crítico (Gemini Flash)**
   - Valida cada afirmação com `pubmed-researcher`.
   - Marca “Aprovado / Necessita contexto / Rejeitado”.

3. **Juiz (Gemini Pro)**
   - Integra o feedback e produz a nota final em português académico.
   - Chama `append_to_notebook`.

*Todas as instruções estão formalizadas no `.cursorrules`, garantindo disciplina no ciclo de revisões.*

---

### 5. Estratégias avançadas

- **Batch automation**: criar um MCP `process_batch.py` que iterate slides → análise → notebook automaticamente.
- **Caching local**: guardar análises em `cache/slide_X.json` para reaproveitar resultados.
- **Tokens**: usar bullet points/JSON entre Analista e Crítico, prosa apenas na resposta final do Juiz.

---

### 6. Próximos passos sugeridos

1. Selecionar `gemini-1.5-pro-latest` no Composer e manter uma única thread por PDF (cache quente).
2. Automatizar lotes de 5 páginas (renderização → análise multimodal → `append_to_notebook`).
3. Adicionar `filesystem-notes` no MCP para guardar notas finais (`./Notas/Radioterapia/`).
4. Usar Cloud Run para MCPs que devam ficar sempre acessíveis (PubMed, Brave Search, etc.).

Com esta arquitetura, o Cursor deixa de ser apenas um IDE e passa a ser uma estação de investigação multimodal, com validação científica e produção de notas ricas em imagens, equações e código executável.

