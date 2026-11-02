
import os
from time import sleep
from shutil import move


def list_dir(path: str) -> list:
    files = list()
    for file in os.listdir(path):
        way = os.path.join(path, file)
        if os.path.isfile(way):
            files.append({"path": path, "file": file})
    return files

def get_extension(file: dict) -> str:
    path, file = file["path"], file["file"]
    file = os.path.join(path, file)
    end = file.rfind(".")
    return file[end+1:].upper()

def create_folder(path: str, ext: str) -> bool:
    try:
        os.mkdir(os.path.join(path, ext.upper()))
        return True
    except FileExistsError:
        return False

def mv_file(file: dict, folder) -> bool:
    path, file = file["path"], file["file"]
    new_path = os.path.join(path, folder)
    old_path = os.path.join(path, file)
    return move(old_path, new_path)

def log(message: str, level: str = "INFO"):
    icons = {
        "INFO": "🔵",
        "SUCCESS": "🟢",
        "WARNING": "🟡",
        "ERROR": "🔴",
        "PROCESS": "⚙️"
    }

    icon = icons.get(level, "📌")
    print(f"{icon} [{level}] {message}")

def main(path: str):
    print("\n" + "═" * 55)
    print(f"{'🚀 PY ORGANIZER'.center(55)}")
    print(f"{'Organizador automático de ficheiros'.center(55)}")
    print("═" * 55)

    # 1 - Criar pastas
    log("INICIANDO ORGANIZAÇÃO", "PROCESS")
    log(f"Diretório: {path}")

    folders = []

    for file in list_dir(path):
        ext = get_extension(file)

        if create_folder(path, ext):
            folders.append(ext)
            log(f"Pasta {ext} criada com sucesso.", "SUCCESS")

    log(f"{len(folders)} novas pastas criadas.", "INFO")

    # 2 - Mover ficheiros
    print("\n" + "─" * 55)
    log("INICIANDO MOVIMENTAÇÃO DE FICHEIROS", "PROCESS")
    print("─" * 55)

    moved = 0

    for file in list_dir(path):
        ext = get_extension(file)

        if mv_file(file, ext):
            moved += 1
            log(f"{file['file']} → {ext}/", "SUCCESS")
            sleep(0.2)

    # 3 - Relatório final
    print("\n" + "═" * 55)
    log("ORGANIZAÇÃO CONCLUÍDA!", "SUCCESS")
    print("─" * 55)

    log(f"Novas pastas: {len(folders)}")
    log(f"Ficheiros movimentados: {moved}")
    log(f"Diretório processado: {path}")

    print("═" * 55)
    print(f"{'Até à próxima! 👋'.center(55)}")
    print("═" * 55)


    
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    path = input("Digite o caminho do diretório a organizar: ")
    main(path)
