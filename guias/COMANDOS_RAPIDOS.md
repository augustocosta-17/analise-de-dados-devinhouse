# ⚡ Comandos Rápidos - Cheat Sheet

## 🔧 Git & GitHub

### **Ativar Git Portátil**
```powershell
$env:Path = "D:\PortableGit\bin;D:\PortableGit\cmd;" + $env:Path
```

### **Workflow Completo**
```powershell
# 1. Ver status
git status

# 2. Adicionar tudo
git add .

# 3. Commit
git commit -m "sua mensagem aqui"

# 4. Push
git push origin main

# 5. Ver histórico
git log --oneline
```

### **Mensagens de Commit Profissionais**
```bash
# Documentação
git commit -m "docs: Adiciona README da semana 06"
git commit -m "docs: Atualiza badges no README principal"

# Novos recursos
git commit -m "feat: Adiciona exercício de análise de vendas"
git commit -m "feat: Implementa sistema de login"

# Correções
git commit -m "fix: Corrige cálculo de média no exercício 3"
git commit -m "fix: Resolve bug no conversor de temperatura"

# Melhorias
git commit -m "refactor: Melhora organização do código"
git commit -m "style: Formata código seguindo PEP8"

# Recursos visuais
git commit -m "docs: Adiciona screenshots do projeto"
git commit -m "docs: Cria diagramas de fluxo"
```

---

## 📸 Screenshots

### **Capturar Tela (Windows)**
```
Windows + Shift + S
```

### **Organizar Screenshots**
```powershell
# Criar pasta
New-Item -ItemType Directory -Path "modulo_01_programacao_e_modelagem_de_dados\semana_0X\screenshots"

# Mover arquivo
Move-Item "C:\Users\...\Downloads\screenshot.png" "modulo_01_programacao_e_modelagem_de_dados\semana_0X\screenshots\nome_descritivo.png"
```

### **Adicionar no README**
```markdown
# Imagem simples
![Descrição](./screenshots/imagem.png)

# Imagem centralizada
<div align="center">
  <img src="./screenshots/imagem.png" alt="Descrição" width="600">
</div>

# Imagem clicável
[![Demo](./screenshots/thumb.png)](./codigo.py)
```

---

## 🎨 Badges

### **Gerar Badge Personalizado**
```markdown
![Texto](https://img.shields.io/badge/TEXTO-VALOR-COR?style=ESTILO&logo=LOGO)
```

**Exemplos:**
```markdown
![Status](https://img.shields.io/badge/Status-Completo-success?style=flat-square)
![Progresso](https://img.shields.io/badge/Progresso-75%25-yellow?style=flat-square)
![Semana](https://img.shields.io/badge/Semana-06-blue?style=flat-square)
```

### **Cores Disponíveis**
- `brightgreen`, `green`, `yellowgreen`
- `yellow`, `orange`, `red`
- `blue`, `lightblue`, `success`, `important`

### **Estilos**
- `flat` (padrão)
- `flat-square` (quadrado)
- `for-the-badge` (grande)
- `plastic` (3D)
- `social` (estilo GitHub)

---

## 📁 Estrutura de Pastas

### **Criar Estrutura Completa**
```powershell
# Criar múltiplas pastas de uma vez
New-Item -ItemType Directory -Path @(
    "modulo_01_programacao_e_modelagem_de_dados\semana_06",
    "modulo_01_programacao_e_modelagem_de_dados\semana_06\screenshots",
    "modulo_01_programacao_e_modelagem_de_dados\semana_07",
    "modulo_01_programacao_e_modelagem_de_dados\semana_07\screenshots"
)
```

---

## 📝 Templates Markdown

### **Seção Expansível**
```markdown
<details>
<summary><b>📖 Clique para expandir</b></summary>

Conteúdo oculto aqui...

</details>
```

### **Tabela**
```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Dado 1   | Dado 2   | Dado 3   |
| Dado 4   | Dado 5   | Dado 6   |
```

### **Lista de Tarefas**
```markdown
- [ ] Tarefa pendente
- [x] Tarefa completa
```

### **Código com Syntax Highlight**
````markdown
```python
def exemplo():
    return "Python"
```

```bash
echo "Bash"
```

```sql
SELECT * FROM tabela;
```
````

### **Citação/Alerta**
```markdown
> 💡 **Dica:** Informação importante

> ⚠️ **Atenção:** Cuidado aqui

> ✅ **Sucesso:** Funcionou!
```

### **Linha Horizontal**
```markdown
---
```

### **Link**
```markdown
[Texto do Link](URL)
[Ver código](./arquivo.py)
[Documentação](https://docs.python.org)
```

---

## 🎯 Workflow de Nova Semana

### **Passo a Passo Completo**
```powershell
# 1. Criar estrutura
$semana = "semana_07"
New-Item -ItemType Directory -Path "modulo_01_programacao_e_modelagem_de_dados\$semana\screenshots"

# 2. Desenvolver exercícios
# ... (codificar)

# 3. Tirar screenshots
# Windows + Shift + S (capturar)
# Salvar em screenshots/

# 4. Criar README (copiar template)
Copy-Item "TEMPLATE_SEMANA_MELHORADO.md" "modulo_01_programacao_e_modelagem_de_dados\$semana\README.md"

# 5. Editar README com informações da semana

# 6. Git workflow
$env:Path = "D:\PortableGit\bin;D:\PortableGit\cmd;" + $env:Path
cd D:\analise-de-dados-devinhouse
git add .
git commit -m "feat: Adiciona exercícios e documentação da $semana"
git push origin main

# 7. Atualizar README do módulo
# Adicionar link para nova semana

# 8. Commit final
git add .
git commit -m "docs: Atualiza índice do módulo com $semana"
git push origin main
```

---

## 🔍 Verificar Antes de Commitar

### **Checklist Rápido**
```powershell
# Ver o que vai ser commitado
git status

# Ver diferenças
git diff

# Ver arquivos que serão adicionados
git add --dry-run .

# Último commit
git log -1
```

---

## 📊 Estatísticas do Projeto

### **Contar Arquivos**
```powershell
# Arquivos Python
(Get-ChildItem -Recurse -Filter "*.py").Count

# Arquivos CSV
(Get-ChildItem -Recurse -Filter "*.csv").Count

# Todos os arquivos
(Get-ChildItem -Recurse -File).Count
```

### **Linhas de Código**
```powershell
# Contar linhas em arquivos Python
Get-ChildItem -Recurse -Filter "*.py" | Get-Content | Measure-Object -Line

# Ver tamanho total
Get-ChildItem -Recurse -File | Measure-Object -Property Length -Sum
```

---

## 🌐 URLs Úteis

### **Ferramentas**
- Shields.io: https://shields.io/
- Carbon (código bonito): https://carbon.now.sh/
- Mermaid Live Editor: https://mermaid.live/
- Emoji Cheat Sheet: https://github.com/ikatyang/emoji-cheat-sheet
- GitHub Stats: https://github.com/anuraghazra/github-readme-stats

### **Referências**
- Markdown Guide: https://www.markdownguide.org/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Python PEP 8: https://pep8.org/

---

## 🚀 Atalhos do VS Code

```
Ctrl + ` - Abrir terminal
Ctrl + B - Toggle sidebar
Ctrl + P - Quick open file
Ctrl + Shift + P - Command palette
Ctrl + K, V - Preview Markdown
```

---

## 💡 Dicas Rápidas

### **Git**
```bash
# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Ver diferença do último commit
git diff HEAD~1

# Criar branch
git checkout -b nome-branch
```

### **README**
```markdown
# Use emojis estrategicamente
✅ ❌ 🎯 📊 💡 🚀 📝 🔧 📚 💻 🎨 🔥

# Alinhe elementos
<div align="center">
  Conteúdo centralizado
</div>

# Crie hierarquia visual
## Título 2
### Título 3
#### Título 4
```

### **Screenshots**
```markdown
# Nome de arquivos descritivos
✅ conversor_temperatura_exemplo1.png
✅ jogo_adivinhacao_vitoria.png
❌ Screenshot1.png
❌ img001.png
```

---

## 🎯 Meta Semanal

```markdown
Segunda a Sexta:
- [ ] Desenvolver exercícios
- [ ] Tirar 2-3 screenshots
- [ ] Documentar no README
- [ ] 3-5 commits ao longo da semana

Sábado:
- [ ] Revisar documentação
- [ ] Adicionar insights aprendidos
- [ ] Commit final da semana

Domingo:
- [ ] Descansar! 😎
```

---

**Salve este arquivo como referência rápida! 📌**

