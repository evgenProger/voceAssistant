import webbrowser

import pyttsx3
import requests
import speech_recognition

engine = pyttsx3.init()


def command_bot():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language="ru")
        print(speech)
        return speech
    except speech_recognition.UnknownValueError:
        return "Ошибка распознования"
    except speech_recognition.RequestError:
        return "Ошибка"


def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if "joke" in data:
        return data["joke"]
    else:
        return "Не удалось получить анекдот."


def get_cat_fact():
    url = "https://meowfacts.herokuapp.com/"
    response = requests.get(url)
    data = response.json()

    if "data" in data:
        return data["data"]
    else:
        return "Не удалось получить факт о кошках."


def say(message):
    engine.say(message)
    engine.runAndWait()
    print(message)


def go(message):
    message = message.lower()

    if "привет" in message:
        say("О Здарово! Где пропадал?")

    elif "прикол" in message:
        joke = get_joke()
        say(joke)

    elif "кошка" in message:
        cat_fact = get_cat_fact()
        say(cat_fact)

    elif "анекдот" in message:
        webbrowser.open("https://www.youtube.com/watch?v=UlAbMlyqHZo&ab_channel=%D0%98%D0%BB%D1%8C%D1%8F%D0%A1%D1%8B"
                        "%D1%87%D0%B5%D0%B2", new=2)


while True:
    command = command_bot()
    go(command)
