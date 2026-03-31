# 🎯 Exemplo Prático: Processar PDFs de Radioterapia

Este guia mostra exatamente como processar os PDFs da pasta de Radioterapia.

---

## 📁 PDFs Disponíveis

Na pasta `C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6`:

1. **`FMDT_6_RT_COMPLETA2526 (1).pdf`** - Aulas completas de Radioterapia
2. **`Serie5 - RT.pdf`** - Série de exercícios de Radioterapia
3. **`Radioterapia_Notebook.ipynb`** - Notebook existente (pode ser atualizado)

---

## 🚀 Comando Completo para o Cursor

Copia e cola isto no **Composer do Cursor** (`Ctrl + I`):

```
Processa TODOS os PDFs da pasta 'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6':

PDFs a processar:
1. 'FMDT_6_RT_COMPLETA2526 (1).pdf'
2. 'Serie5 - RT.pdf'

Para cada PDF, faz o seguinte:

1. VALIDAÇÃO:
   - Usa inspect_pdf_metadata para verificar se cada PDF é válido
   - Confirma o número total de páginas

2. PROCESSAMENTO DE CADA PÁGINA:
   - Usa process_slide_for_vision para converter cada página em imagem
   - Analisa a imagem com o Tribunal Multi-Passagem:
     * OBSERVER: Descreve tudo o que vê (texto, gráficos, tabelas, equações, diagramas)
     * CLÍNICO: Interpreta em contexto de radioterapia clínica (aplicações, guidelines, implicações)
     * ENGENHEIRO: Explica física, matemática, instrumentação, cálculos passo a passo
   - Extrai e explica TODAS as equações de física
   - Identifica e explica gráficos, tabelas e diagramas
   - Se houver exercícios, resolve-os passo a passo com explicações detalhadas

3. INFORMAÇÕES ADICIONAIS:
   - Para cada conceito importante, busca informações adicionais relevantes
   - Adiciona referências bibliográficas (PubMed, guidelines de radioterapia)
   - Correlaciona conceitos entre diferentes slides e PDFs
   - Explica aplicações práticas e clínicas

4. ORGANIZAÇÃO DO NOTEBOOK:
   - Cria o notebook 'Radioterapia_Completo_FMDT6_S5.ipynb'
   - Organiza por:
     * PDF de origem (FMDT_6 primeiro, depois Serie5)
     * Tema/conceito dentro de cada PDF
     * Sequência lógica de aprendizagem
   - Para cada slide, inclui:
     * Imagem em alta resolução
     * Análise visual completa (Observer)
     * Contexto biomédico detalhado (Clínico + Engenheiro)
     * Explicações de física e cálculos
     * Comentários inline explicando cada elemento visual
     * Referências e links relevantes
     * Imagens de documentos oficiais quando aplicável

5. ESPECIALMENTE IMPORTANTE:
   - Explica TODAS as equações de física em detalhe
   - Resolve TODOS os exercícios passo a passo
   - Correlaciona conceitos entre os dois PDFs
   - Adiciona informações sobre aplicações clínicas
   - Inclui comentários perto de gráficos, tabelas e diagramas explicando o que mostram

Começa a processar agora!
```

---

## 📋 Versão Simplificada (Para Testar)

Se quiseres testar primeiro com poucas páginas:

```
Processa apenas as primeiras 5 páginas do PDF 
'FMDT_6_RT_COMPLETA2526 (1).pdf' da pasta 
'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6'.

Para cada página:
- Converte em imagem usando process_slide_for_vision
- Analisa com o Tribunal (Observer, Clínico, Engenheiro)
- Explica física e cálculos em detalhe
- Adiciona comentários explicativos

Cria o notebook 'Teste_Radioterapia.ipynb' com os resultados.
```

---

## 🔍 O Que Esperar

### Durante o Processamento

O Cursor vai:
1. ✅ Validar cada PDF
2. ✅ Converter cada página em imagem
3. ✅ Analisar cada imagem com o Tribunal
4. ✅ Buscar informações adicionais quando necessário
5. ✅ Criar/atualizar o notebook

**Podes acompanhar o progresso** vendo:
- As imagens a serem criadas em `notebook_images/`
- O notebook a ser atualizado em tempo real

### Resultado Final

Terás um notebook `.ipynb` com:
- ✅ Todas as imagens dos slides em alta resolução
- ✅ Análises detalhadas do Tribunal
- ✅ Explicações de física e cálculos
- ✅ Exercícios resolvidos passo a passo
- ✅ Comentários inline explicando cada elemento
- ✅ Referências bibliográficas
- ✅ Correlações entre conceitos

---

## 🎓 Exemplo de Estrutura do Notebook Final

O notebook terá uma estrutura como esta:

```markdown
# Radioterapia Completo - FMDT_6 e Série 5

## PDF 1: FMDT_6_RT_COMPLETA2526

### Slide 1: Introdução à Radioterapia
![Slide 1](notebook_images/slide_1.png)

#### Análise Visual (Observer)
[Descrição detalhada do que está visível]

#### Contexto Biomédico (Tribunal)
[Interpretação clínica + física + engenharia]

#### Equações e Cálculos
[Explicação detalhada de cada equação]

#### Informações Adicionais
[Referências, guidelines, etc.]

### Slide 2: Dosimetria
[...]

## PDF 2: Serie5 - RT

### Exercício 1: Cálculo de Dose
![Exercício 1](notebook_images/slide_X.png)

#### Enunciado
[Texto do exercício]

#### Resolução Passo a Passo
[Resolução detalhada com explicações]

#### Explicação da Física
[Porquê cada passo funciona]

[...]
```

---

## ⚠️ Notas Importantes

1. **Tempo de Processamento:**
   - Cada página demora alguns segundos
   - Um PDF com 50 páginas pode demorar 5-10 minutos
   - Podes processar em lotes se preferires

2. **Espaço em Disco:**
   - Cada imagem ocupa ~500KB-2MB
   - 100 slides = ~50-200MB
   - Certifica-te que tens espaço suficiente

3. **Qualidade das Imagens:**
   - As imagens são guardadas em alta resolução
   - Adequadas para impressão e visualização

4. **Revisão Manual:**
   - Sempre revê o notebook final
   - O Tribunal é muito bom, mas não é perfeito
   - Verifica especialmente cálculos complexos

---

## 🎉 Pronto!

Copia o comando acima, cola no Cursor Composer, e deixa o Tribunal trabalhar!

**Bons estudos!** 📚✨

