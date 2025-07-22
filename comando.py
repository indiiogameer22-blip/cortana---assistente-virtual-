# Importa bibliotecas necessárias
import json                         # Usada para ler o arquivo de comandos (formato JSON)
import webbrowser                   # Permite abrir páginas da web
import subprocess                   # Permite abrir programas instalados no sistema

# Importa funções auxiliares do projeto
from utils import speak, time_hour  # 'speak' transforma texto em fala, 'time_hour' retorna a hora atual

# Importa módulos personalizados para ações específicas
from modulos.calcula import Calculadora              # Função para realizar cálculos
from modulos.pesquisa import realizar_pesquisa       # Função para pesquisar no Google
from modulos.criaçao import Create                   # Função para criar arquivos ou pastas

# Armazena a hora atual (utilizada nos comandos de hora e data)
agora = time_hour()

# Função que carrega os comandos do arquivo comandos.json
def carregar_comandos():
    with open("comandos.json", "r") as arquivo:  # Abre o arquivo JSON com os comandos
        dados = json.load(arquivo)               # Carrega os dados como dicionário Python
        comandos = dados["comandos"]             # Acessa a lista de comandos dentro do dicionário
    return comandos                              # Retorna a lista de comandos

# Função que executa os comandos com base na frase falada pelo usuário
def Comandos(frase, comandos):
    for comando in comandos:  # Passa por cada comando carregado
        # Verifica se algum dos identificadores está presente na frase falada
        if any(identificador in frase for identificador in comando["identificador"]):
            name = comando["name"]  # Pega o nome do comando (ex: "abrir", "data", etc.)

            # Comando para abrir sites ou programas
            if name == "abrir":
                for item in comando["itens"]:  # Passa por cada item configurado dentro do comando
                    for palavra_chave in item["palavra_chave"]:  # Verifica se uma palavra-chave do item está na frase
                        if palavra_chave in frase:
                            if item.get("url"):  # Se o item possui uma URL
                                webbrowser.open(item["url"])  # Abre a página no navegador
                                speak(item["speak"])           # Fala a mensagem associada
                            elif item.get("name_program"):     # Se o item possui um programa
                                subprocess.Popen(item["name_program"])  # Abre o programa
                                speak(item["speak"])           # Fala a mensagem associada

            # Comando para informar o horário atual
            elif name == "horario":
                speak(f"São {agora.hour}, horas e {agora.minute} minutos")  # Fala as horas e minutos

            # Comando para informar a data atual
            elif name == "data":
                speak(f"Hoje é dia {agora.day} do {agora.month} de {agora.year}")  # Fala a data completa

            # Comando para realizar cálculos com base na frase
            elif name == "calculadora":
                speak(Calculadora(frase))  # Chama a função de cálculo e fala o resultado

            # Comando para realizar uma pesquisa na internet
            elif name == "pesquisa":
                speak(realizar_pesquisa(frase))  # Faz a pesquisa e fala o resultado (resumo)

            # Comando para criar algum objeto (como arquivos, pastas, etc.)
            elif name == "criar":
                for item in comando["itens"]:  # Passa por cada item que pode ser criado
                    for palavra_chave in item["palavra_chave"]:  # Verifica se a palavra-chave está na frase
                        if palavra_chave in frase:
                            name = item["objeto"]         # Define o que deve ser criado
                            speak(Create(name))           # Cria o item e fala a confirmação
