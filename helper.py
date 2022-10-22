from gtts import gTTS
import time
import playsound
import speech_recognition as sr
import os
import datetime
import pyperclip
import pyautogui
import random
#from pyowm import OWM
#from pyowm.utils.config import get_default_config
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

#config_dict = get_default_config()
#config_dict['language'] = 'ru'
#place = 'Екатеринбург'
#country = 'Россия'
#country_and_place = place + ', ' + country

#owm = OWM('48d67476442645d4e680328f87222f25')
#mgr = owm.weather_manager()
#observation = mgr.weather_at_place(country_and_place)
#w = observation.weather

#status = w.detailed_status
#w.wind()
#humidity = w.humidity
#temp = w.temperature('celsius')['temp']



#pyautogui.move(50, 50, 1)
#print(pyautogui.position())
#pyautogui.PAUSE = 1
#pyautogui.click(632, 491)
#pyautogui.click(185,412) - координаты кнопки "Взять в работу"
#pyautogui.click(670,291) - координаты кнопки "Проблемы"
#pyautogui.click(181,486) - координаты кнопки "Создать проблему"
#pyautogui.click(668,318) - координаты поля "Источник"
#pyautogui.click(581,452) - координаты кнопки Сайт "Обращения"
#pyautogui.click(636,401) - координаты поля "Группа"
#pyautogui.click(636,401) - координаты кнопки "Проблемы - Доставка"
#pyautogui.click(641,478) - координаты поля "Класс"
#pyautogui.click(621,692) - координаты кнопки "Задержка в сроках доставки"
#pyautogui.click(620,514) - координаты поля "Укажите 1 rid"
#pyautogui.click(657,632) - координаты поля "Проблема"
#pyautogui.click(581,783) - координаты кнопки "зарегистрировать" проблему
#pyautogui.click(950,168) - координаты крестика чтобы закрыть поле регистрация проблемы
#pyautogui.click(163,307) - координаты кнопки "Консультация" из раздела "Проблемы"
#pyautogui.click(167,662) - координаты кнопки "Заказ"
#pyautogui.click(238,495) - координаты кнопки "Активные доставки"
#pyautogui.click(1317,840) - координаты кнопки "Регистрация обращения"
#pyautogui.click(666,311) - координаты кнопки "Источник - Обращение"
#pyautogui.click(579,422) - координаты кнопки "Задержка доставки. Доставка со склада ВБ"
#pyautogui.click(548,674) - координаты поля "Комментарий"
#pyautogui.click(484,767) - координаты кнопки "Зарегистрировать"
#pyautogui.click(237,608) #- координаты кнопки "Детализация"
#pyautogui.click(748,443) #- координаты кнопки "Запрос РРН, нет в ЛК"
#pyautogui.click(548,490) #- координаты кнопки "Общие условия и сроки возврата ДС"
#pyautogui.click(640,405) #- координаты кнопки "Возврат денег за транспортировку 50-100 руб"
#pyautogui.click(518,509) #- координаты кнопки "Отмена товара. Задержка доставки"
#pyautogui.click(599,465) #- координаты кнопки "Задержка склад продавца"
#pyautogui.click(590,386) #- координаты кнопки "Вопрос по статусу доставки в детализации"
#pyautogui.click(184,351) #- координаты кнопки "История заказов"
#pyautogui.click(553,426) #- координаты кнопки "Не проведен возврат по возвращенному товару"
#pyautogui.click(520,462) #- координаты кнопки "Товар не был найден, статус "Доставлен"
#pyautogui.click(601,682) #- координаты кнопки "Проблемы - Взаиморасчеты"
#pyautogui.click(570,654) #- координаты кнопки "Запрос РРН"
#pyautogui.click(163,456) #- координаты кнопки "Возврат"
#pyautogui.click(165,611) #- координаты кнопки "Условия возврата"
#pyautogui.click(181,550) #- координаты кнопки "Товар надлежащего качества"
#pyautogui.click(775,462) #- координаты кнопки "Условия возврата"
#pyautogui.click(532,464) #- координаты кнопки "Товар не подлежит возврату после оплаты"
#pyautogui.click(169,675) #- координаты кнопки "Скидки, акции и конкурсы"
#pyautogui.click(190,449) #- координаты кнопки "Скидка постоянного покупателя"
#pyautogui.click(669,503) #- координаты кнопки "Условия действия скидки"
#pyautogui.click(484,381) #- координаты кнопки "Неправильная сумма выкупа"
#pyautogui.click(454,510) #- координаты кнопки "Уменьшиласть скидка"





pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет, Дима!")
    elif "слава украине" in message:
        say_message("Героям Слава!")
    elif "проверка" in message:
        print(pyautogui.position())
        say_message("Проверка выполнена")
    elif "2 + 2" in message:
        say_message(str(eval(message)))
    elif "расскажи анекдот" in message:
        say_message("Не знаю я никаких анекдотов, а знаешь почему? Потому что ты ленивая жопа!")
    elif "молодец" in message:
        say_message("Спасибо, хозяин")
    elif "анечка" in message or "ань" in message:
        prikols = ['да, что случилось, хозяин?',
                   'слушаю, хозяин',
                   'шо надо?',
                   'я тут!']
        say_message(random.choice(prikols))
    #elif "погода" in message:
        #say_message('В городе ' + str(place) + ' cейчас ' + str(status) + '. Температура ' + str(round(temp)) +
                    #' градусов по цельсию' + '. Влажность составляет ' + str(humidity) + '%' + ". Cкорость ветра " +
                    #str(w.wind()['speed']) + ' метров в секунду')

    elif "хочешь пиццу" in message or "пойдём играть" in message:
        prikols = ['Даааааа',
                   'конечно, я оочень этого хочу',
                   'я бы не отказалась',
                   "нуу, не очень хочу, но давай"]
        say_message(random.choice(prikols))
    elif "умница" in message:
        say_message("Спасибо, хозяин")
    elif "спасибо" in message:
        say_message("Рада помочь!")
    elif "закрой вкладку" in message:
        say_message("закрываю")
        def hotkey():
            pyautogui.hotkey('ctrl', 'w')
        hotkey()
    elif "нажми три" in message:
        say_message("нажимаю")
        def hotkey():
            for i in range(4):
                pyautogui.hotkey('3')
                time.sleep(300)
        hotkey()
    elif "отправь сообщение" in message:
        say_message("ща все будет")
        def hotkey():
            pyperclip.copy('Привет, это голосовой помощник Дмитрия Льдова')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')


        hotkey()
    elif "открой youtube" in message:
        say_message("Открываю")
        os.system("start https://www.youtube.com/")
    elif "закрой браузер" in message:
        say_message("Закрываю")
        os.system("taskkill /im chrome.exe /f")
    elif 'время' in message:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        say_message(f"Сейчас время отдохнуть, а именно {strTime}")
    elif "чем занимаешься" in message:
        say_message("Да нихуя не делаю, все как обычно, Дим")
    elif "как дела" in message:
        say_message("щеееене вмэрло украини, смерть ворогаам, дорогу пасанаам")
    elif "прикол" in message:
        x, y = pyautogui.locateCenterOnScreen(r"img\Проблемы.png")
        pyautogui.click(x, y)
        button = (pyautogui.locateCenterOnScreen(r"img\Создать.png"))
        pyautogui.click(button)
        say_message("Ураа")
    elif "жми" in message:
        for i in range(10):
            pyautogui.click(351,517)
            pyautogui.PAUSE = 0.1
        say_message("Ураа")
    elif "давай" in message:
        pyautogui.click(668,322) #- координаты кнопки "Проблемы"
        pyautogui.PAUSE = 1
        pyautogui.click(184,482) #- координаты кнопки "Создать проблему"
        pyautogui.PAUSE = 0.5
        pyautogui.click(668,318) #- координаты поля "Источник"
        pyautogui.PAUSE = 0.5
        pyautogui.click(581,452) #- координаты кнопки Сайт "Обращения"
        pyautogui.PAUSE = 0.5
        pyautogui.click(636,401) #- координаты поля "Группа"
        pyautogui.PAUSE = 0.5
        pyautogui.click(603,724) #- координаты кнопки "Проблемы - Доставка"
        pyautogui.PAUSE = 0.5
        pyautogui.click(641,478) #- координаты поля "Класс"
        pyautogui.PAUSE = 0.5
        pyautogui.click(621,692) #- координаты кнопки "Задержка в сроках доставки"
        pyautogui.PAUSE = 0.5
        pyautogui.click(620,514) #- координаты поля "Укажите 1 rid"
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.PAUSE = 0.5
        pyautogui.click(657,632) #- координаты поля "Проблема"
        pyautogui.PAUSE = 0.5
        pyperclip.copy('Задержка, клиент ждет')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        say_message("Все готово")
    elif "регистрация 1" in message:
        pyautogui.click(163,307)#- координаты кнопки "Консультация" из раздела "Проблемы"
        pyautogui.click(167,662)#- координаты кнопки "Заказ"
        pyautogui.click(238,495)#- координаты кнопки "Активные доставки"
        pyautogui.click(1317,840)#- координаты кнопки "Регистрация обращения"
        pyautogui.click(666,311)#- координаты кнопки "Источник - Обращение"
        pyautogui.click(579,422)#- координаты кнопки "Задержка доставки. Доставка со склада ВБ"
        pyautogui.click(548,674)#- координаты поля "Комментарий"
        pyautogui.PAUSE = 0.5
        pyperclip.copy('Сказал клиенту информацию по его вопросу')
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.click(484,767)#- координаты кнопки "Зарегистрировать"
        say_message("Регистрация готова")
    elif "регистрация 2" in message:
        pyautogui.click(237,608) #- координаты кнопки "Детализация"
        pyautogui.click(1317,840)#- координаты кнопки "Регистрация обращения"
        pyautogui.click(670,323)#- координаты кнопки "Источник - Обращение"
        pyautogui.click(748,443) #- координаты кнопки "Запрос РРН, нет в ЛК"
        pyautogui.click(548,674)#- координаты поля "Комментарий"
        pyautogui.PAUSE = 0.5
        pyperclip.copy('Сказал клиенту информацию по его вопросу')
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.click(484,767)#- координаты кнопки "Зарегистрировать"
        say_message("Регистрация готова")
    elif "жми" in message:
        x, y = pyautogui.locateCenterOnScreen(r"img\Поле.png")
        pyautogui.click(x, y)
        say_message("Ураа")
    elif "автокликер" in message:
        x, y = pyautogui.locateCenterOnScreen(r"img\Автоклик.png")
        for i in range(30):
            pyautogui.click(x, y)
        say_message("Ураа")
    elif "чем занимаешься" in message:
        say_message("Да нихуя не делаю, все как обычно, Дим")
    elif "пока" in message:
        say_message("Пока, хозяин!")
        exit()
    else:
        pass

def calculator(message):
    message = message.lower()
    if "+" in message:
        say_message(str(eval(message)))
    elif "-" in message:
        say_message(str(eval(message)))
    elif "х" in message:
        say_message(str(eval(message.replace('х', '*'))))
    elif "/" in message:
        say_message(str(eval(message)))



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
        calculator(command)