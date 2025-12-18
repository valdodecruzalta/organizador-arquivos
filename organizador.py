import os
import shutil
from pathlib import Path

# Dicionário com categorias e extensões
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".odt"],
    "Planilhas": [".xlsx", ".csv"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Compactados": [".zip", ".rar", ".tar", ".gz"]
}

def organizar_pasta(caminho):
    caminho = Path(caminho)

    if not caminho.exists():
        print("❌ Caminho não encontrado.")
        return

    for arquivo in caminho.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()

            # Encontrar categoria correspondente
            categoria = None
            for nome_categoria, extensoes in CATEGORIAS.items():
                if extensao in extensoes:
                    categoria = nome_categoria
                    break

            # Se não encontrou categoria, pula
            if not categoria:
                continue

            # Criar pasta da categoria
            pasta_destino = caminho / categoria
            pasta_destino.mkdir(exist_ok=True)

            # Mover arquivo
            shutil.move(str(arquivo), str(pasta_destino / arquivo.name))
            print(f"📁 Movido: {arquivo.name} → {categoria}/")

    print("\n✅ Organização concluída!")

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta que deseja organizar: ")
    organizar_pasta(pasta)
