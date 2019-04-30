from yandex_translate import YandexTranslate

#API KEY FOR YNDX TRANSLATE
keylong = '4a360.907b12c1d0b00c3d0555378e945df82d09824dd2'
translate1 = YandexTranslate('trnsl.1.1.20181216T165708Z.256f0281500' + keylong)
#API KEY FOR YNDX TRANSLATE

def text_to_text(text, lang_to, lang_from):
    # Translator. First elemant - text
    # Second element - language from which to translate
    # Third - language to translate
    if lang_to == 'en':
        lang_to_y = 'en'
    elif lang_to == 'ru':
        lang_to_y = 'ru'
    if lang_from == 'en':
        lang_fy = 'en'
    elif lang_from == 'ru':
        lang_fy = 'ru'
    return(str((translate1.translate(text, lang_fy + '-' + lang_to_y).get('text')[0])))
