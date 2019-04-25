# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
from MainClass import TranslatorClass as tcs


reply_keyboard = [['/help', '/stop'],
                  ['/startranslate']]
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

def help(bot, update):
    #команда показывающая все возможные команды
    update.message.reply_text("Вот все мои команды:\n"
        "/help - все команды\n"
        "/stop - прекратить выполнение команды\n"
        "/startranslate - начать перевод", reply_markup=markup)
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
        CommandHandler('start', start_bot)
        ],
        states={
            1:[MessageHandler(Filters.text, translate)],
            },
        fallbacks=[CommandHandler('stop', stop)])

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()