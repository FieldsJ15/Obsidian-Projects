# 🔧 INSTALAR POPPLER (OBRIGATÓRIO)

## ❌ Problema

O erro "Unable to get page count. Is poppler installed and in PATH?" significa que o **Poppler não está instalado** ou não está no PATH do Windows.

---

## ✅ SOLUÇÃO: Instalar Poppler no Windows

### Passo 1: Descarregar Poppler

1. Vai a: **https://github.com/oschwartz10612/poppler-windows/releases**
2. Descarrega o ficheiro ZIP da **última release** (ex: `Release-XX.XX.X-X.zip`)
3. Extrai o ZIP para uma pasta (ex: `C:\Program Files\poppler`)

### Passo 2: Adicionar ao PATH

1. **Abre "Variáveis de Ambiente":**
   - Pressiona `Win + R`
   - Escreve: `sysdm.cpl`
   - Pressiona Enter
   - Vai ao separador **"Avançado"**
   - Clica em **"Variáveis de Ambiente"**

2. **Edita a variável PATH:**
   - Na secção **"Variáveis do sistema"**, procura **"Path"**
   - Seleciona e clica em **"Editar"**
   - Clica em **"Novo"**
   - Adiciona: `C:\Program Files\poppler\Library\bin`
     (ou o caminho onde extraíste o Poppler, seguido de `\Library\bin`)
   - Clica **OK** em todas as janelas

3. **Reinicia o terminal/PowerShell:**
   - Fecha todos os terminais
   - Abre um novo PowerShell
   - Testa: `pdftoppm -h`
   - Se mostrar ajuda, está instalado!

### Passo 3: Reiniciar o Cursor

1. **Fecha completamente o Cursor**
2. **Abre novamente**
3. **Testa novamente o comando**

---

## 🧪 Verificar Instalação

Abre um PowerShell e executa:

```powershell
pdftoppm -h
```

**Se funcionar:** Mostra ajuda do Poppler ✅  
**Se não funcionar:** O PATH não está correto ❌

---

## ⚠️ Nota Importante

Se não conseguires instalar o Poppler agora, podes:
1. Instalar mais tarde
2. Ou usar um método alternativo (mas o Poppler é o mais simples)

---

**Depois de instalar o Poppler, volta aqui e executa o comando novamente!** 🚀

