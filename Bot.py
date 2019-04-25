# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
from MainClass import TranslatorClass as tcs

# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def start_bot(bot, update):
    update.message.reply_text("О здравствуй мой повелитель, узнай как управлять мною используя команду /help")
    return ConversationHandler.END

def start_translate(bot, update):
    update.message.reply_text("Я готов переводить всё с русского на английский и наоборот :D")
    return 1

def translate(bot, update):
    # У объекта класса Updater есть поле message, являющееся
    # объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str), отсылающий ответ пользователю,
    # от которого получено сообщение.
    update.message.reply_text(tcs.text_to_text(update.message.text))

def help(bot, update):
    update.message.reply_text("Вот все мои команды:\n"
        "/help - все команды\n"
        "/stop - прекратить выполнение команды\n"
        "/startranslate - начать перевод")
    return ConversationHandler.END

def stop(bot, update):
    update.message.reply_text(
        "Я прекратил выполнение последней команды!")
    return ConversationHandler.END

def main():
    # Создаём объект updater. Вместо слова "TOKEN" надо разместить
    # полученный от @BotFather токен
    updater = Updater("801307540:AAFiDRxsXzWrMACdKODd697laNDVx6Rk004")

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере эта функция
    # будет вызываться при получении сообщения с типом "текст",
    # т.е. текстовых сообщений.
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