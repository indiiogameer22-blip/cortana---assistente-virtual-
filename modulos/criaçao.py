# Importa o módulo 'os' para interações com o sistema operacional (como criar pastas e arquivos)
import os 

# Função responsável por criar pastas ou arquivos no Desktop do usuário
def Create(name):
    
    # Obtém o caminho da área de trabalho (Desktop) do usuário, independentemente do sistema
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Se o comando for para criar uma pasta
    if name == "pasta":
        x = 0  # Contador para evitar nomes duplicados
        nome_base = os.path.join(desktop_path, "Nova Pasta")  # Nome base da pasta
        nome_pasta = nome_base  # Inicialmente, o nome da pasta é o nome base

        # Verifica se a pasta já existe e, se sim, incrementa o contador até achar um nome livre
        while os.path.exists(nome_pasta):
            x += 1
            nome_pasta = f"{nome_base} ({x})"

        # Cria a nova pasta com o nome disponível
        os.makedirs(nome_pasta)
        return "Pasta criada"

    # Se o comando for para criar um arquivo do bloco de notas
    elif name == "bloco de notas":
        x = 0  # Contador para evitar nomes duplicados
        nome_base = os.path.join(desktop_path, "Novo Documento")  # Nome base do arquivo
        nome_documento = f"{nome_base}.txt"  # Nome do arquivo com extensão .txt

        # Verifica se o arquivo já existe e incrementa até achar um nome disponível
        while os.path.exists(nome_documento):
            x += 1
            nome_documento = f"{nome_base} ({x}).txt"

        # Cria o novo arquivo em branco no desktop
        with open(nome_documento, "x") as arquivo:
            return "arquivo criado"
