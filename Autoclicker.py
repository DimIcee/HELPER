from gtts import gTTS
import time
import playsound
import speech_recognition as sr
import os
import datetime
import pyperclip
import pyautogui
import random
from pyowm import OWM
from pyowm.utils.config import get_default_config
sr.pause_threshold = 0.5

def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language='ru')
        print('Вы сказали: '+our_speech)
        return our_speech

    except sr.UnknownValueError:
        return 'ошибка'
    except sr.RequestError as e:
        return 'ошибка'
    #return input("Скажите вашу команду: ")


pyautogui.FAILSAFE = True


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет!")
    elif "жми" in message:
        x, y = pyautogui.locateCenterOnScreen(r"img\Автоклик.png")
        for i in range(30):
            pyautogui.click(x, y)
        say_message("Ураа")
    elif "пока" in message:
        say_message("Пока, хозяин!")
        exit()
    else:
        pass




def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = '_audio_'+str(time.time())+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
