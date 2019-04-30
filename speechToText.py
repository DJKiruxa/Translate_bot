import speech_recognition as sr  # Импортируем распознавание голоса


def speech_to_text(flag, lang, path=''):
    r = sr.Recognizer()  # Инициализируем распознаватель голоса
    if flag is False:  # Проверка флага
        with sr.Microphone() as source:
            audio = r.listen(source)  # Прослушиваем микрофон
    else:
        open_file = sr.AudioFile(path)  # Открываем файл
        audio = r.record(open_file)
    try:
        lng = ''  # Параметр языка для google
        if lang == 'ru':
            lng = 'ru-RU'  # Русский язык
        elif lang == 'en':
            lng = 'en-EN'  # Английский язык
        return(r.recognize_google(audio, language=lng))
        # Возвращаем распознанный текст
    except sr.UnknownValueError:  # Ошибка распознавания
        pass
    except sr.RequestError as e:  # Ошибка запроса к сервису
        pass
