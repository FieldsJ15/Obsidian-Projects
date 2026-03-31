# 📖 Guia Completo: Como Usar os MCPs para Criar Notebooks Perfeitos

## 🎯 Objetivo

Criar notebooks Jupyter completos a partir de PDFs que:
- ✅ Extraem imagens de alta qualidade dos PDFs
- ✅ Analisam texto mesmo quando está em formato de imagem (OCR automático via visão do modelo)
- ✅ Incluem comentários explicativos perto de cada imagem
- ✅ Adicionam informações adicionais relevantes (PubMed, guidelines, etc.)
- ✅ Correlacionam conceitos entre slides e documentos
- ✅ Explicam física, cálculos e provas em detalhe
Para além disto o Notebook é para ter muito mais informações do que aquilo que se lê e vê. Para além das explicações de todos os conceitos visiveis vamos ainda falar destes em mais detalhes e complexidade. Sobre todos os seus componentes/Conceitos relacionados especialmente ao nível de Medicina Humana, Medicina Nuclear, Engenharia Biomédica e Biofísica, Biologia, Histologia, Fisiologia etc.... 
extrapolar ainda mais e falar sobre a versao avançada de todos os conceitos vistos de forma a sabermos mais do que o professor/doutor que escreveu este slide ou pelo mneos saber MUITO MAS MUITO MAIS que os colegas restantes que leam o PDF e estudem por ele 
---

## 🔧 MCPs Disponíveis e Como Funcionam

### 1. **Biomedical-Slide-Processor** (Já Configurado)

Este é o servidor MCP principal que criámos. Ele fornece 3 ferramentas:

#### A) `inspect_pdf_metadata(pdf_path: str)`
**O que faz:** Verifica se um PDF é legível antes de processar.

**Quando usar:** Sempre antes de processar um PDF pela primeira vez.

**Exemplo de uso no Cursor:**
```
Verifica se o PDF 'FMDT_6_RT_COMPLETA2526 (1).pdf' é válido.
```

#### B) `process_slide_for_vision(pdf_path: str, page_number: int)`
**O que faz:** 
- Converte uma página do PDF em imagem PNG de alta resolução
- Guarda em `notebook_images/slide_{page}.png`
- Devolve uma versão reduzida para análise visual pelo modelo

**Quando usar:** Para cada página/slide que quiseres analisar.

**Exemplo de uso no Cursor:**
```
Converte a página 1 do PDF 'FMDT_6_RT_COMPLETA2526 (1).pdf' em imagem.
```

#### C) `append_to_notebook(notebook_path: str, slide_number: int, analysis_text: str, biomedical_context: str, relevant_links: str, external_images: str = "")`
**O que faz:**
- Cria ou atualiza um notebook Jupyter
- Adiciona uma secção por slide com:
  - Imagem do slide
  - Análise visual (Observer)
  - Contexto biomédico (Clínico + Engenheiro)
  - Referências e links
  - Imagens externas opcionais (documentos oficiais, etc.)

**Quando usar:** No final da análise de cada slide.

---

## 🚀 Fluxo Completo: Como Processar PDFs

### Passo 1: Preparar o Pedido

No **Composer do Cursor** (`Ctrl + I`), escreve um pedido detalhado:

```
Processa os PDFs da pasta 'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6':

1. Para cada PDF:
   - Valida o PDF usando inspect_pdf_metadata
   - Processa TODAS as páginas usando process_slide_for_vision
   - Para cada página:
     * Analisa a imagem com o Tribunal (Observer → Clínico → Engenheiro)
     * Extrai texto mesmo que esteja em formato de imagem
     * Identifica equações, gráficos, tabelas e diagramas
     * Busca informações adicionais relevantes (PubMed, guidelines de radioterapia)
     * Correlaciona conceitos entre diferentes slides
     * Explica física, cálculos e provas em detalhe
     * Adiciona comentários explicativos perto de cada elemento visual

2. Cria um notebook completo chamado 'Radioterapia_Completo.ipynb' com:
   - Todas as imagens dos slides em alta resolução
   - Análises detalhadas do Tribunal
   - Explicações de física e cálculos
   - Referências bibliográficas
   - Imagens de documentos oficiais quando relevante
   - Comentários inline explicando cada elemento visual

3. Organiza o notebook por:
   - PDF de origem
   - Tema/conceito
   - Sequência lógica de aprendizagem
```

### Passo 2: O Que Acontece Automaticamente

O Cursor (seguindo as regras do `.cursorrules`) vai:

1. **Chamar `inspect_pdf_metadata`** para cada PDF
2. **Para cada página:**
   - Chamar `process_slide_for_vision` para obter a imagem
   - **Observer** analisa a imagem e descreve:
     - Texto visível (mesmo que seja imagem)
     - Gráficos, tabelas, esquemas
     - Equações e fórmulas
     - Diagramas e ilustrações
   - **Clínico** interpreta em contexto médico:
     - Aplicações clínicas
     - Guidelines relevantes
     - Implicações para pacientes
   - **Engenheiro** adiciona perspetiva técnica:
     - Física e matemática
     - Instrumentação
     - Modelos e cálculos
   - **Busca informações adicionais** (se tiveres PubMed MCP configurado)
   - **Chama `append_to_notebook`** com tudo organizado

3. **Repete o processo** para todas as páginas de todos os PDFs

### Passo 3: Resultado Final

Terás um notebook `.ipynb` com:
- ✅ Todas as imagens dos slides
- ✅ Análises detalhadas do Tribunal
- ✅ Explicações de física e cálculos
- ✅ Comentários inline
- ✅ Referências bibliográficas
- ✅ Correlações entre conceitos

---

## 📝 Exemplos Práticos de Pedidos

### Exemplo 1: Processar um PDF Específico

```
Processa o PDF 'FMDT_6_RT_COMPLETA2526 (1).pdf' da pasta 
'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6'.

Para cada página:
- Extrai a imagem em alta resolução
- Analisa com o Tribunal (Observer, Clínico, Engenheiro)
- Identifica e explica todas as equações de física
- Explica os cálculos passo a passo
- Adiciona informações adicionais sobre radioterapia
- Correlaciona com conceitos de física médica

Cria o notebook 'FMDT_6_Radioterapia.ipynb' com tudo organizado.
```

### Exemplo 2: Processar Múltiplos PDFs e Correlacionar

```
Processa TODOS os PDFs da pasta 
'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6':

1. 'FMDT_6_RT_COMPLETA2526 (1).pdf'
2. 'Serie5 - RT.pdf'

Para cada PDF:
- Processa todas as páginas
- Analisa com o Tribunal
- Identifica temas principais (ex: dosimetria, planeamento, física de partículas)

Cria um notebook 'Radioterapia_Completo.ipynb' que:
- Organiza por tema (não por PDF)
- Correlaciona conceitos entre os diferentes PDFs
- Explica física e cálculos em detalhe
- Inclui exercícios resolvidos se houver
- Adiciona referências e informações adicionais
```

### Exemplo 3: Foco em Exercícios e Cálculos

```
Processa o PDF 'Serie5 - RT.pdf' focando especialmente em:

1. Exercícios e problemas propostos
2. Resoluções passo a passo
3. Explicações de física por trás de cada cálculo
4. Aplicações clínicas dos conceitos

Cria o notebook 'Serie5_Exercicios_Resolvidos.ipynb' com:
- Cada exercício como uma secção
- Resolução detalhada com explicações
- Comentários sobre a física envolvida
- Referências a guidelines quando aplicável
```

---

## 🎓 Como o Tribunal Analisa Texto em Imagem

O modelo do Cursor tem capacidade de **visão** (Vision Language Model). Isto significa que:

1. **Quando `process_slide_for_vision` é chamado:**
   - O PDF é convertido em imagem
   - A imagem é enviada ao modelo
   - O modelo "lê" o texto mesmo que esteja em formato de imagem

2. **O Observer analisa:**
   - Texto visível (OCR automático via visão)
   - Estrutura do documento
   - Elementos visuais

3. **O Clínico e Engenheiro interpretam:**
   - O texto extraído
   - Contexto médico/técnico
   - Correlações com outros conceitos

**Não precisas de OCR separado!** O modelo faz isso automaticamente.

---

## 🔍 Adicionar MCPs Opcionais para Melhorar Análise

### PubMed MCP (Recomendado)

**O que faz:** Busca artigos científicos na base PubMed.

**Como adicionar:**
1. Settings → Features → MCP
2. Add Custom MCP
3. **Name**: `PubMed-Search`
4. **Type**: `command (stdio)`
5. **Command**: `uvx`
6. **Args**: `pubmed-search-mcp-server`

**Quando é usado automaticamente:**
- Quando o Tribunal encontra termos médicos
- Quando precisa validar factos clínicos
- Quando quer adicionar referências bibliográficas

### Sequential Thinking MCP

**O que faz:** Força raciocínio passo a passo.

**Como adicionar:**
1. Settings → Features → MCP
2. Add Custom MCP
3. **Name**: `Sequential-Thinking`
4. **Type**: `command (stdio)`
5. **Command**: `npx`
6. **Args**: `-y @modelcontextprotocol/server-sequential-thinking`

**Quando é usado:**
- Para explicar cálculos complexos passo a passo
- Para estruturar explicações de física
- Para resolver exercícios de forma organizada

---

## 💡 Dicas Avançadas

### 1. Processar PDFs Grandes

Se o PDF tiver muitas páginas, processa em lotes:

```
Processa as páginas 1-10 do PDF 'FMDT_6_RT_COMPLETA2526 (1).pdf'.
Depois processa as páginas 11-20, etc.
```

### 2. Focar em Tópicos Específicos

```
Processa o PDF 'FMDT_6_RT_COMPLETA2526 (1).pdf' mas foca especialmente em:
- Dosimetria
- Planeamento de tratamento
- Física de partículas

Ignora páginas que não sejam relevantes para estes tópicos.
```

### 3. Correlacionar com Notebook Existente

```
Processa o PDF 'Serie5 - RT.pdf' e adiciona ao notebook existente 
'Radioterapia_Notebook.ipynb', correlacionando com o conteúdo já presente.
```

### 4. Criar Múltiplos Notebooks por Tema

```
Processa todos os PDFs e cria notebooks separados:
- 'Radioterapia_Dosimetria.ipynb' (apenas sobre dosimetria)
- 'Radioterapia_Planeamento.ipynb' (apenas sobre planeamento)
- 'Radioterapia_Fisica.ipynb' (apenas sobre física)
```

---

## ✅ Checklist: Antes de Processar

- [ ] MCP `Biomed-Slide-Agent` configurado no Cursor
- [ ] Poppler instalado e no PATH
- [ ] Dependências Python instaladas (`.venv` ativado)
- [ ] PDFs na pasta correta
- [ ] Sabes o nome exato dos PDFs a processar

---

## 🎉 Pronto para Começar!

Agora tens tudo o que precisas para criar notebooks perfeitos a partir de PDFs.

**Faz um pedido ao Cursor e vê a magia acontecer!** ✨

---

**Última atualização:** 2025-01-XX

