# 🛠️ Resolução de Problemas - Agents-Tribunal

## ❌ Erro: "pip: The term 'pip' is not recognized"

### Causa
O ambiente virtual não está ativado ou o `pip` não está disponível no PATH.

### Solução

**Opção 1: Usar `python -m pip` (Recomendado)**
```powershell
# Sempre funciona, mesmo sem ambiente virtual ativado
python -m pip install -r requirements.txt
```

**Opção 2: Ativar o ambiente virtual corretamente**
```powershell
# Navegar para o diretório do projeto
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"

# Criar ambiente virtual (se ainda não existir)
python -m venv .venv

# Ativar o ambiente virtual
.venv\Scripts\Activate.ps1

# Se der erro de política de execução, executar primeiro:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Agora o pip deve funcionar
pip install -r requirements.txt
```

**Opção 3: Usar o caminho completo do pip**
```powershell
.venv\Scripts\pip.exe install -r requirements.txt
```

---

## ❌ Erro: "Poppler not found" ou "Failed to read PDF"

### Causa
O Poppler não está instalado ou não está no PATH do sistema.

### Solução

1. **Descarregar Poppler:**
   - Vai a: https://github.com/oschwartz10612/poppler-windows/releases
   - Descarrega o ZIP da última release
   - Extrai para `C:\Program Files\poppler`

2. **Adicionar ao PATH:**
   - Abre "Variáveis de Ambiente" no Windows
   - Edita a variável "Path" do sistema
   - Adiciona: `C:\Program Files\poppler\bin`
   - Clica OK e reinicia o terminal

3. **Verificar instalação:**
   ```powershell
   pdftoppm -h
   ```
   Se mostrar ajuda, está instalado corretamente.

---

## ❌ Erro: "Module not found: mcp" ou outras dependências

### Causa
As dependências não foram instaladas ou o ambiente virtual não está ativado.

### Solução

```powershell
# 1. Ativar ambiente virtual
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
.venv\Scripts\Activate.ps1

# 2. Instalar dependências
python -m pip install -r requirements.txt

# 3. Verificar instalação
python -c "import mcp; print('MCP instalado!')"
```

---

## ❌ Erro: "MCP não aparece no Cursor"

### Causa
Configuração incorreta no Cursor ou caminhos errados.

### Solução

1. **Verificar configuração no Cursor:**
   - Abre Settings (`Ctrl + ,`)
   - Vai a **Features → MCP**
   - Verifica se o servidor está listado

2. **Verificar caminhos:**
   - **Command**: `python` (ou `.venv\Scripts\python.exe` se usar venv)
   - **Args**: `server.py`
   - **Working directory**: `C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal`

3. **Reiniciar o Cursor:**
   - Fecha completamente o Cursor
   - Abre novamente
   - Verifica se o MCP aparece

4. **Verificar logs:**
   - Vai a **View → Output**
   - Seleciona "MCP" no dropdown
   - Procura por erros

---

## ❌ Erro: "Execution Policy" no PowerShell

### Causa
O PowerShell bloqueia scripts por questões de segurança.

### Solução

```powershell
# Permitir execução de scripts locais (apenas para o utilizador atual)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois tenta ativar o ambiente virtual novamente
.venv\Scripts\Activate.ps1
```

---

## ❌ Erro: "PDF não pode ser renderizado"

### Causa
PDF corrompido ou Poppler não consegue processar.

### Solução

1. **Verificar se o PDF abre normalmente:**
   - Tenta abrir o PDF num visualizador normal
   - Se não abrir, o PDF pode estar corrompido

2. **Verificar Poppler:**
   ```powershell
   pdftoppm -h
   ```

3. **Testar com outro PDF:**
   - Tenta com um PDF simples primeiro
   - Se funcionar, o problema é com o PDF específico

---

## ✅ Verificação Rápida do Sistema

Execute estes comandos para verificar se tudo está correto:

```powershell
# 1. Verificar Python
python --version
# Deve mostrar: Python 3.10 ou superior

# 2. Verificar Poppler
pdftoppm -h
# Deve mostrar ajuda do Poppler

# 3. Verificar ambiente virtual
cd "C:\Users\joaop\Desktop\Cursor Projects\Agents-Tribunal"
.venv\Scripts\Activate.ps1
# Deve mostrar (.venv) no início da linha

# 4. Verificar dependências
python -c "import mcp, pdf2image, nbformat; print('Tudo OK!')"
# Deve mostrar: Tudo OK!

# 5. Verificar servidor
python -c "import server; print('Servidor OK!')"
# Deve mostrar: Servidor OK!
```

---

## 📞 Ainda com problemas?

1. **Verifica os logs do Cursor:**
   - View → Output → MCP

2. **Verifica o terminal:**
   - Procura por mensagens de erro específicas

3. **Verifica os ficheiros:**
   - Confirma que `server.py` existe
   - Confirma que `requirements.txt` existe
   - Confirma que `.venv` foi criado

4. **Reinstala tudo:**
   ```powershell
   # Remove ambiente virtual antigo
   Remove-Item -Recurse -Force .venv

   # Cria novo
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

---

**Última atualização:** 2025-01-XX

