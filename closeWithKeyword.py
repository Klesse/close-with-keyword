import speech_recognition as sr
import os

def ouvir_microfone():

    microphone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = microphone.listen(source)
        
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        phrase = microphone.recognize_google(audio,language='pt-BR')
        print("You said: " + phrase)
        
    except sr.UnkownValueError:
        print("Não entendi")
        
    return phrase

name = input("The name of the process that will be terminated:")
keyword  = input("The keyword to close the process:")

while 1:
    if keyword.lower() in ouvir_microfone().lower():
        os.system("taskkill /f /im " + name)
        break
        
