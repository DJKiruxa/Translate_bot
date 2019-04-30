from gtts import gTTS


def text_to_text(text1, lang_to, fl):
    # Первый элемент текст, второй - язык для считывания
    if lang_to == 'ru':
        tts = gTTS(text=text1, lang='ru')
        tts.save(fl)
    if lang_to == 'en':
        tts = gTTS(text=text1, lang='en')
        tts.save(fl)
