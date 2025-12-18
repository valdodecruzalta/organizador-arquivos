# 🗂️ Organizador Automático de Arquivos

Este projeto é um **organizador automático de arquivos**, desenvolvido em **Python**, que identifica arquivos em uma pasta e os move automaticamente para subpastas organizadas por tipo (imagens, documentos, vídeos, PDFs, etc.).  
É uma solução simples e eficiente para manter diretórios limpos e organizados.

---

## 🚀 Objetivo do Projeto

Demonstrar habilidades iniciais em:

- Manipulação de arquivos e diretórios com Python  
- Uso de módulos padrão (`os`, `shutil`, `pathlib`)  
- Automação de tarefas repetitivas  
- Estruturação de código limpo e organizado  
- Criação de scripts úteis para o dia a dia  

Este é um dos meus primeiros projetos práticos na transição para a área de **Desenvolvimento Python**.

---

## 🧠 Como funciona

O script:

1. Lê todos os arquivos da pasta escolhida  
2. Identifica a extensão de cada arquivo  
3. Cria automaticamente pastas para cada tipo (se não existirem)  
4. Move os arquivos para suas respectivas categorias  

Exemplo de categorias:

- `Imagens/` → .jpg, .png, .gif  
- `Documentos/` → .pdf, .docx, .txt  
- `Vídeos/` → .mp4, .avi  
- `Planilhas/` → .xlsx, .csv  
- `Compactados/` → .zip, .rar  

---

## 📦 Tecnologias utilizadas

- **Python 3**  
- Módulos padrão:
  - `os`
  - `shutil`
  - `pathlib`

Nenhuma instalação adicional é necessária.

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/valdodecruzalta/organizador-arquivos
