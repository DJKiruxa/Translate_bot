from translator_init import translate1
from speechToText import *
from textToSpeech import *
from string import ascii_letters
from gtts import gTTS
from yandex_translate import YandexTranslate
import speech_recognition as sr  # Импортируем распознавание голоса
# Модуль для удобного использования

# API KEY FOR YNDX TRANSLATE
keylong = '4a360.907b12c1d0b00c3d0555378e945df82d09824dd2'
translate1 = YandexTranslate('trnsl.1.1.20181216T165708Z.256f0281500' + keylong)
# API KEY FOR YNDX TRANSLATE


class TranslatorClass:
    def text_to_text(text, lang_from='ru', lang_to='en'):
        # Translator. First elemant - text
        # Second element - language from which to translate
        # Third - language to translate
        if all(map(lambda c: c in ascii_letters, text)) is True:
            lang_from = 'en'
            lang_to = 'ru'
        else:
            lang_from = 'ru'
            lang_to = 'en'
        return(str((translate1.translate(text, lang_from + '-' + lang_to).get('text')[0])))

    def stt(flag, path='', lang='ru'):
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

    def tts(text1, fl, lang_to='en'):
        # Первый элемент текст, второй - язык для считывания
        if lang_to == 'ru':
            tts = gTTS(text=text1, lang='ru')
            tts.save(fl)
        if lang_to == 'en':
            tts = gTTS(text=text1, lang='en')
            tts.save(fl)


class GameClass:
    def __init__(self):
        self.score = 0

    def start_game(self):
        import random
        self.line = random.choice(open('words_alpha.txt').readlines())[:-1]
        while all(map(lambda c: c in ascii_letters, \
                      TranslatorClass.text_to_text(\
                                                   self.line, \
                                                   'en', 'ru'))) is True:
            self.line = random.choice(open('words_alpha.txt').readlines())[:-1]

        return(self.line)

    def checker(self, inp):
        if TranslatorClass.text_to_text(self.line, 'en', \
                                        'ru').lower()[:-1] == inp.lower()[:-1]:
            self.score += 1
            return('Правильно. Ваш счёт: {}.'.format(self.score))
        else:
            return('Неверно, правильный ответ: {}. Ваш счёт: {}.'.format(TranslatorClass.text_to_text(self.line, \
                                                                                                      'en', 'ru'), self.score))
