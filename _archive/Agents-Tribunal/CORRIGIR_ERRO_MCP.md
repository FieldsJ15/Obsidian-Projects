# 🔧 Corrigir Erro: "can't open file 'server.py'"

## ❌ Problema

O Cursor está a tentar executar `python server.py` mas procura o ficheiro em `C:\Users\joaop\` em vez do diretório do projeto.

**Erro nos logs:**
```
[error] C:\Users\joaop\AppData\Local\Python\pythoncore-3.14-64\python.exe: can't open file 'C:\\Users\\joaop\\server.py': [Errno 2] No such file or directory
```

---

## ✅ Solução

### Opção 1: Configurar via Interface do Cursor (Recomendado)

1. **Abre Settings** (`Ctrl + ,`)
2. **Vai a Features → MCP**
3. **Remove o servidor existente** (se houver)
4. **Clica em "Add Custom MCP"**
5. **Preenche:**
   - **Name**: `Biomed-Slide-Agent`
   - **Type**: `command (stdio)`
   - **Command**: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\.venv\Scripts\python.exe`
   - **Args**: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\server.py`
   - **Working directory**: (deixa vazio ou remove)

6. **Salva e reinicia o Cursor**

### Opção 2: Editar mcp.json Manualmente

O ficheiro `mcp.json` já foi corrigido com caminhos absolutos. Mas o Cursor pode procurá-lo em locais diferentes:

#### Localização A: Configuração Global do Cursor

O ficheiro pode estar em:
- `C:\Users\joaop\.cursor\mcp.json` (Windows)
- Ou na configuração do Cursor (Settings → Open Settings JSON)

**Conteúdo correto:**
```json
{
  "mcpServers": {
    "Biomed-Slide-Agent": {
      "command": "C:\\Users\\joaop\\Desktop\\Cursor Projects\\Agents-Tribunal\\.venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\joaop\\Desktop\\Cursor Projects\\Agents-Tribunal\\server.py"]
    }
  }
}
```

#### Localização B: No Projeto (`.cursor/mcp.json`)

Cria a pasta `.cursor` no projeto (se não existir) e coloca o `mcp.json` lá:

```powershell
# Criar pasta .cursor
New-Item -ItemType Directory -Force -Path ".cursor"

# Copiar mcp.json para lá
Copy-Item "mcp.json" ".cursor\mcp.json"
```

---

## 🔍 Verificar se Está a Funcionar

1. **Reinicia o Cursor completamente**
2. **Vai a Settings → Features → MCP**
3. **Verifica se `Biomed-Slide-Agent` aparece sem erro** (sem ponto vermelho)
4. **Vê os logs:**
   - View → Output
   - Seleciona "MCP" no dropdown
   - Deve mostrar mensagens de sucesso, não erros

---

## 🧪 Testar o Servidor Manualmente

Antes de configurar no Cursor, testa se o servidor funciona:

```powershell
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
.venv\Scripts\Activate.ps1
python server.py
```

Se funcionar, o servidor vai ficar à espera de mensagens MCP (podes cancelar com `Ctrl+C`).

---

## ⚠️ Notas Importantes

1. **Caminhos Absolutos:** Usei caminhos absolutos porque o `cwd` não estava a funcionar
2. **Python do Venv:** Usei o Python do ambiente virtual (`.venv\Scripts\python.exe`)
3. **Reiniciar Cursor:** Sempre reinicia o Cursor após alterar configurações MCP

---

## 🎯 Se Ainda Não Funcionar

1. **Verifica se o `server.py` existe:**
   ```powershell
   Test-Path "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\server.py"
   ```

2. **Verifica se o Python do venv existe:**
   ```powershell
   Test-Path "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal\.venv\Scripts\python.exe"
   ```

3. **Testa o servidor diretamente:**
   ```powershell
   cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
   .venv\Scripts\python.exe server.py
   ```

4. **Verifica os logs do Cursor:**
   - View → Output → MCP
   - Procura por mensagens de erro específicas

---

**Última atualização:** 2025-11-26

