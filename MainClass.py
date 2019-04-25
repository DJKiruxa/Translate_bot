from string import ascii_letters
from gtts import gTTS
from yandex_translate import YandexTranslate
import speech_recognition as sr  # ����������� ������������� ������
import random
# ������ ��� �������� �������������

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
        r = sr.Recognizer()  # �������������� �������������� ������
        if flag is False:  # �������� �����
            with sr.Microphone() as source:
                audio = r.listen(source)  # ������������ ��������
        else:
            open_file = sr.AudioFile(path)  # ��������� ����
            audio = r.record(open_file)
        try:
            lng = ''  # �������� ����� ��� google
            if lang == 'ru':
                lng = 'ru-RU'  # ������� ����
            elif lang == 'en':
                lng = 'en-EN'  # ���������� ����
            return(r.recognize_google(audio, language=lng))
            # ���������� ������������ �����
        except sr.UnknownValueError:  # ������ �������������
            pass
        except sr.RequestError as e:  # ������ ������� � �������
            pass

    def tts(text1, fl, lang_to='en'):
        # ������ ������� �����, ������ - ���� ��� ����������
        if lang_to == 'ru':
            tts = gTTS(text=text1, lang='ru')
            tts.save(fl)
        if lang_to == 'en':
            tts = gTTS(text=text1, lang='en')
            return tts

line = None
class GameClass:
    def __init__(self):
        self.score = 0

    def start_game(self):
        global line
        line = random.choice(open('words_alpha.txt').readlines())[:-1]
        while all(map(lambda c: c in ascii_letters, \
                      TranslatorClass.text_to_text(\
                                                   line, \
                                                   'en', 'ru'))) is True:
            line = random.choice(open('words_alpha.txt').readlines())[:-1]

        return(line)

    def checker(self, inp):
        global line
        if TranslatorClass.text_to_text(line, 'en', \
                                        'ru').lower()[:-1] == inp.lower()[:-1]:
            self.score += 1
            return('���������. ��� ����: {}.'.format(self.score))
        else:
            return('�������, ���������� �����: {}. ��� ����: {}.'.format(TranslatorClass.text_to_text(line, \
                                                                                                      'en', 'ru'), self.score))
