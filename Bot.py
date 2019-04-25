# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
from MainClass import TranslatorClass as tcs
from MainClass import GameClass

Gc = GameClass()
#создание клавиатуры
reply_keyboard = [['/help', '/stop'],
                  ['/startranslate', '/letsplay']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.

def start_bot(bot, update):
    #функия привествия
    update.message.reply_text("О здравствуй мой повелитель, узнай как управлять мною используя команду /help", reply_markup = markup)
    return ConversationHandler.END

def start_translate(bot, update):
    #функция запускающая переводчик
    update.message.reply_text("Я готов переводить всё с русского на английский и наоборот :D", reply_markup = markup)
    return 1

def translate(bot, update):
    #отсылается переведенное сообщение
    update.message.reply_text(tcs.text_to_text(update.message.text), reply_markup = markup)

def letsplay(bot, update):
    #начало игры
    update.message.reply_text("Игра началась! Попробуйте угадать перевод слова от яндекса!\n"
        "Врядли у вас получится (У Yandex(a) косячный перевод :0)\n"
        "Когда будете готовы, напишите 'Готов'  ")
    return 2

def game1(bot, update):
    global Gc
    #сама игра
    update.message.reply_text(Gc.start_game())
    return 3

def game2(bot,update):
    global Gc
    update.message.reply_text(Gc.checker(update.message.text))
    return 2
def help(bot, update):
    #функция показывающая все возможные команды
    update.message.reply_text("Вот все мои команды:\n"
        "/help - все команды\n"
        "/stop - прекратить выполнение команды\n"
        "/startranslate - начать перевод\n"
        "/letsplay - начало игры", reply_markup=markup)
    return ConversationHandler.END

def stop(bot, update):
    update.message.reply_text(
        "Я прекратил выполнение последней команды!", reply_markup = markup)
    return ConversationHandler.END

def main():
    # Создаём объект updater.
    updater = Updater("801307540:AAFiDRxsXzWrMACdKODd697laNDVx6Rk004")

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    #регистрируем команды
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('startranslate', start_translate),
        CommandHandler('help', help),
        CommandHandler('start', start_bot),
        CommandHandler('letsplay', letsplay)
        ],
        states={
            1:[MessageHandler(Filters.text, translate)],
            2:[MessageHandler(Filters.text, game1)],
            3:[MessageHandler(Filters.text, game2)]
            },
        fallbacks=[CommandHandler('stop', stop)])

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()