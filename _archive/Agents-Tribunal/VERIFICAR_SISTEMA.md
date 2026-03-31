# ✅ Verificar que o Tribunal e MCPs Estão a Funcionar

## 🔍 Checklist de Verificação

### 1. Verificar MCP no Cursor

1. **Abre Settings** (`Ctrl + ,`)
2. **Vai a Features → MCP**
3. **Verifica:**
   - `Biomed-Slide-Agent` deve estar listado
   - Deve mostrar "3 tools enabled" (sem erro)
   - Não deve ter ponto vermelho ou mensagem de erro

### 2. Verificar Logs do MCP

1. **View → Output**
2. **Seleciona "MCP" no dropdown**
3. **Procura por:**
   - ✅ `[info] Found 3 tools` (sucesso)
   - ❌ `[error] can't open file` (erro - precisa corrigir)

### 3. Testar Servidor Manualmente

Abre um terminal PowerShell e executa:

```powershell
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
.venv\Scripts\python.exe server.py
```

**Se funcionar:** O servidor fica à espera (podes cancelar com `Ctrl+C`).  
**Se der erro:** Verifica as dependências instaladas.

### 4. Testar Ferramentas MCP

No **Composer do Cursor** (`Ctrl + I`), testa:

```
Testa o servidor MCP: verifica se o PDF 
'C:\Users\joaop\Desktop\Física Médica\Notebook RadioTerapia e Série 6\Serie5 - RT.pdf' 
é válido usando inspect_pdf_metadata.
```

**Se funcionar:** Deves ver uma resposta confirmando que o PDF é válido.  
**Se não funcionar:** O MCP não está configurado corretamente.

---

## 🛠️ Se Houver Problemas

### Erro: "can't open file 'server.py'"

**Solução:** Verifica o `mcp.json`:
- Deve usar caminhos absolutos
- Command: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\.venv\Scripts\python.exe`
- Args: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\server.py`

### Erro: "Module not found: mcp"

**Solução:**
```powershell
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### MCP não aparece no Cursor

**Solução:**
1. Reinicia o Cursor completamente
2. Verifica Settings → Features → MCP
3. Adiciona manualmente se necessário

---

## ✅ Quando Estiver Tudo a Funcionar

Quando verificares que:
- ✅ MCP aparece no Cursor sem erros
- ✅ Teste de `inspect_pdf_metadata` funciona
- ✅ Logs mostram "Found 3 tools"

**Então podes processar os PDFs!** 🎉

Vai ao ficheiro `PROCESSAR_RADIOTERAPIA.md` e copia o comando completo.

---

**Última atualização:** 2025-11-26

