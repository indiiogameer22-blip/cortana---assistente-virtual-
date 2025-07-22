# Importa o módulo 're' para trabalhar com expressões regulares
import re

# Importa o módulo webbrowser com um apelido 'web' para abrir URLs no navegador
import webbrowser as web

# Lista de palavras que podem indicar uma intenção de pesquisa
PALAVRAS_CHAVE = [
    'procurar sobre',
    'pesquisar sobre',
    'pesquisa sobre',
    'procurar',
    'pesquisar',
    'pesquisa',
    'acerca de',
    'a respeito de'
]

# Função responsável por realizar uma pesquisa no Google ou no YouTube
def realizar_pesquisa(frase):
    # Procura se o usuário mencionou 'google' ou 'youtube' na frase
    text = re.search(r'\b(google|youtube)\b', frase)

    # Se encontrou, pega qual plataforma foi mencionada
    plataforma = text.group(0)

    # Remove a expressão "no google" ou "no youtube" da frase
    frase = frase.replace(f"no {plataforma}", " ").strip()

    # Inicializa a variável 'pesquisa' com a frase inteira (por padrão)
    for palavra_chave in PALAVRAS_CHAVE:
        if palavra_chave in frase:
            # Se a frase contém uma das palavras-chave, separa a parte final da frase como o termo de busca
            pesquisa = re.split(rf"\b{re.escape(palavra_chave)}\b", frase)[-1].strip()
            break
        else:
            # Se nenhuma palavra-chave for encontrada, usa a frase inteira como termo de busca
            pesquisa = frase

    # Monta a URL de pesquisa com base na plataforma mencionada
    if plataforma == 'google':
        url = f'https://www.google.com.br/search?q={pesquisa}'
    elif plataforma == 'youtube':
        url = f'https://www.youtube.com/results?search_query={pesquisa}'

    # Abre a URL no navegador padrão
    web.open(url)

    # Retorna uma mensagem que será falada pela assistente
    return f"Pesquisando sobre {pesquisa} no {plataforma}"
