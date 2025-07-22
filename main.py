# Importa a biblioteca de reconhecimento de voz
import speech_recognition as sr 

# Importa função para dividir frases em palavras
from nltk.tokenize import word_tokenize

# Importa a função principal de comandos e a função para carregar os comandos disponíveis
from comando import Comandos, carregar_comandos

# Importa a função de "falar" e a função para pegar o horário atual
from utils import speak, time_hour

# Define a função que retorna uma saudação com base na hora do dia
def Time_day():
    time = time_hour()  # Pega a hora atual do sistema
    hora = time.hour    # Separa só a hora (ex: 15 de 15:30)

    # Dependendo da hora, define a saudação apropriada
    if 5 <= hora < 11:
        info = "Bom dia"
    elif 11 <= hora < 17:
        info = "Boa tarde"
    elif 17 <= hora <= 23 or 0 <= hora < 5:
        info = "Boa Noite"

    return info  # Retorna a saudação

# Remove artigos desnecessários das frases (como "o", "a", etc.)
def Tratamento_frase(palavras):
    artigos = ["o", "a", "os", "as"]  # Palavras que não ajudam no entendimento do comando
    palavras_filtradas = [palavra for palavra in palavras if palavra not in artigos]  # Remove esses artigos
    return " ".join(palavras_filtradas)  # Junta as palavras novamente como uma frase

# Inicializa o reconhecedor de voz
microfone = sr.Recognizer()

# Função principal da assistente
def Assistente(comandos):
    while True:  # Loop que mantém a assistente ativa indefinidamente
        with sr.Microphone() as source:  # Usa o microfone como entrada de áudio
            microfone.adjust_for_ambient_noise(source)  # Ajusta para ruídos de fundo
            audio = microfone.listen(source, None, 5)  # Escuta por até 5 segundos

            try:
                # Converte o áudio em texto (em português)
                frase = microfone.recognize_google(audio, language='pt-br').lower()

                # Se o usuário disser "eva" ou "iniciar", a assistente começa a funcionar
                if any(palavra in frase for palavra in ["eva", "iniciar"]):
                    print("Ouvindo...")
                    boas_vindas = Time_day()  # Gera a saudação com base no horário
                    speak(f"{boas_vindas}")   # A assistente fala a saudação

                    assistente_ativa = True  # Liga a assistente

                    while assistente_ativa:  # Loop interno com a assistente ativa
                        with sr.Microphone() as source:
                            microfone.adjust_for_ambient_noise(source)  # Ajuste para ruído
                            audio = microfone.listen(source, None, 8)  # Escuta por até 8 segundos

                            try:
                                # Converte áudio em texto
                                frase = microfone.recognize_google(audio, language='pt-br').lower()

                                # Separa a frase em palavras
                                palavras = word_tokenize(frase)

                                # Remove palavras desnecessárias
                                frase = Tratamento_frase(palavras)

                                # Mostra no terminal o que foi entendido
                                print(f"Usuario>> {frase}")

                                # Executa o comando de acordo com a frase dita
                                Comandos(frase, comandos)

                                # Se o usuário disser "obrigado", "desligar" ou "brigado", a assistente desliga
                                if frase in ["obrigado", "desligar", "brigado"]:
                                    speak("De nada")  # A assistente responde
                                    assistente_ativa = False  # Sai do loop interno

                            # Caso o áudio não seja entendido (nenhuma palavra detectada)
                            except sr.UnknownValueError:
                                print("Não consigo escutá-lo!")

                            # Qualquer outro erro técnico é mostrado no terminal
                            except Exception as e:
                                print(f"Erro: {e}")

            # Se a frase não for reconhecida, apenas ignora
            except sr.UnknownValueError:
                print("")

            # Outros erros são exibidos no terminal
            except Exception as e:
                print(f"Erro: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    print('Diga "eva", "iniciar" para começar.')  # Mensagem inicial para o usuário
    comandos = carregar_comandos()  # Carrega os comandos disponíveis da assistente
    Assistente(comandos)  # Inicia a assistente passando os comandos carregados
