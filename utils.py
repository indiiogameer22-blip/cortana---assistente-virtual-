# Importa a biblioteca pyttsx3, usada para converter texto em fala (voz)
import pyttsx3

# Importa a biblioteca datetime, usada para trabalhar com data e hora
import datetime

# Inicializa o mecanismo de voz (Text-to-Speech)
voz = pyttsx3.init()

# Função que recebe uma frase e fala ela em voz alta
def speak(frase):
    voz.say(frase)        # Adiciona a frase à fila de reprodução de voz
    voz.runAndWait()      # Executa a fala (espera até terminar)

# Função que retorna a data e hora atual
def time_hour():
    agora = datetime.datetime.now()  # Pega o exato momento atual (com data e hora)
    return agora                     # Retorna o objeto datetime completo
