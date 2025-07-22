# Importa a função Word e o conjunto 'nums' da biblioteca pyparsing
# Usado para identificar números em uma string
from pyparsing import Word, nums

# Função que interpreta uma frase com operação matemática e retorna o resultado
def Calculadora(frase):
    try:
        # Substitui o caractere 'x' por '*' para permitir multiplicação
        frase = frase.replace("x", "*")

        # Define um padrão para detectar números inteiros na frase
        numeros = Word(nums)

        # Busca todos os números na frase e retorna como uma lista de tokens
        numeros_encontrados = numeros.searchString(frase)

        # Extrai os valores inteiros dos tokens encontrados
        numbers = [int(token[0]) for token in numeros_encontrados]

        # Verifica se a frase contém uma operação de soma
        if "somar" in frase or "+" in frase:
            result = numbers[0] + numbers[1]
            return f"{numbers[0]} mais {numbers[1]} é igual a {result}"
        
        # Verifica se a frase contém uma operação de subtração
        if "menos" in frase or "-" in frase:
            result = numbers[0] - numbers[1]
            return f"{numbers[0]} menos {numbers[1]} é igual a {result}"
        
        # Verifica se a frase contém uma operação de multiplicação
        if "vezes" in frase or "*" in frase:
            result = numbers[0] * numbers[1]
            return f"{numbers[0]} vezes {numbers[1]} é igual a {result}"
        
        # Verifica se a frase contém uma operação de divisão
        if "dividido" in frase or "/" in frase:
            result = numbers[0] / numbers[1]
            return f"{numbers[0]} dividido para {numbers[1]} é igual a {result}"
        
        # Verifica se a frase contém um cálculo de porcentagem
        if "%" in frase:
            result = ((numbers[0] / 100) * numbers[1])
            return f"{numbers[0]} % de {numbers[1]} é igual a {result}"

    # Caso ocorra algum erro (como ausência de números ou operação inválida)
    except:
        return "Não foi possível fazer esta operação"
