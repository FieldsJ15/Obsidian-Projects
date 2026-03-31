# 🚀 COMEÇA AQUI: Guia Rápido para Processar os Teus PDFs

## ✅ O Que Já Está Pronto

1. ✅ **Servidor MCP configurado** (`Biomed-Slide-Agent`)
2. ✅ **Dependências instaladas** (Python, MCP, pdf2image, etc.)
3. ✅ **Tribunal Multi-Agente** configurado (Observer, Clínico, Engenheiro)
4. ✅ **Sistema pronto para processar PDFs**

---

## 🎯 O Que Fazer AGORA

### Passo 1: Verificar Configuração MCP no Cursor

1. Abre **Settings** no Cursor (`Ctrl + ,`)
2. Vai a **Features → MCP**
3. Verifica se `Biomed-Slide-Agent` está listado
4. Se não estiver, adiciona:
   - **Name**: `Biomed-Slide-Agent`
   - **Type**: `command (stdio)`
   - **Command**: `python` (ou `.venv\Scripts\python.exe`)
   - **Args**: `server.py`
   - **Working directory**: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal`

### Passo 2: Processar os PDFs de Radioterapia

Abre o **Composer do Cursor** (`Ctrl + I`) e cola isto:

```
Processa TODOS os PDFs da pasta 'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6':

1. 'FMDT_6_RT_COMPLETA2526 (1).pdf'
2. 'Serie5 - RT.pdf'

Para cada PDF:
- Valida usando inspect_pdf_metadata
- Processa TODAS as páginas usando process_slide_for_vision
- Para cada página, analisa com o Tribunal (Observer → Clínico → Engenheiro)
- Extrai e explica TODAS as equações de física
- Resolve TODOS os exercícios passo a passo
- Adiciona informações adicionais relevantes
- Correlaciona conceitos entre slides

Cria o notebook 'Radioterapia_Completo.ipynb' com:
- Todas as imagens em alta resolução
- Análises detalhadas do Tribunal
- Explicações de física e cálculos
- Comentários inline explicando cada elemento
- Referências bibliográficas
- Organização por tema e sequência lógica
```

### Passo 3: Aguardar e Revisar

- O Cursor vai processar automaticamente
- Podes acompanhar o progresso
- No final, terás um notebook completo!

---

## 📚 Documentação Completa

Se precisares de mais detalhes, consulta:

1. **`GUIA_USO_MCPs.md`** - Como usar todos os MCPs
2. **`EXEMPLO_PRATICO_RADIOTERAPIA.md`** - Exemplo específico para os teus PDFs
3. **`INSTRUCOES_COMPLETAS.md`** - Instalação e configuração completa
4. **`MCPs_RECOMENDADOS.md`** - MCPs opcionais para melhorar análise
5. **`RESOLUCAO_PROBLEMAS.md`** - Resolver problemas comuns

---

## 🎓 Como Funciona

### O Que Acontece Quando Pedes para Processar:

1. **Validação:** `inspect_pdf_metadata` verifica o PDF
2. **Conversão:** `process_slide_for_vision` converte cada página em imagem
3. **Análise:** O Tribunal analisa cada imagem:
   - **Observer** descreve o que vê (texto, gráficos, equações)
   - **Clínico** interpreta em contexto médico
   - **Engenheiro** explica física e cálculos
4. **Melhoria:** Cada agente revisa e melhora a resposta (múltiplas passagens)
5. **Síntese:** Meta-Tribunal produz resposta final
6. **Notebook:** `append_to_notebook` cria/atualiza o notebook

### Texto em Formato de Imagem?

**Não precisas de OCR separado!** O modelo do Cursor tem visão e "lê" texto mesmo quando está em formato de imagem.

---

## 💡 Dicas

1. **Começa com poucas páginas** para testar (ex: primeiras 5)
2. **Processa em lotes** se os PDFs forem muito grandes
3. **Revisa o notebook final** - o Tribunal é muito bom, mas sempre verifica cálculos complexos
4. **Adiciona MCPs opcionais** (PubMed, Sequential Thinking) para melhorar ainda mais

---

## 🎉 Pronto!

**Agora é só fazer o pedido ao Cursor e ver a magia acontecer!** ✨

**Bons estudos!** 📚

