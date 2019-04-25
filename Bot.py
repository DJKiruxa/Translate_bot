# ����������� ����������� ������.
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
from MainClass import TranslatorClass as tcs
from MainClass import GameClass

Gc = GameClass()
#�������� ����������
reply_keyboard = [['/help', '/stop'],
                  ['/startranslate', '/letsplay']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# ���������� �������-���������� ���������.
# � �� ��� ���������, ��� ��� � ����� updater, ��������� ���������.

def start_bot(bot, update):
    #������ ����������
    update.message.reply_text("� ���������� ��� ����������, ����� ��� ��������� ���� ��������� ������� /help", reply_markup = markup)
    return ConversationHandler.END

def start_translate(bot, update):
    #������� ����������� ����������
    update.message.reply_text("� ����� ���������� �� � �������� �� ���������� � �������� :D", reply_markup = markup)
    return 1

def translate(bot, update):
    #���������� ������������ ���������
    update.message.reply_text(tcs.text_to_text(update.message.text), reply_markup = markup)

def letsplay(bot, update):
    #������ ����
    update.message.reply_text("���� ��������! ���������� ������� ������� ����� �� �������!\n"
        "������ � ��� ��������� (� Yandex(a) �������� ������� :0)\n"
        "����� ������ ������, �������� '�����'  ")
    return 2

def game1(bot, update):
    global Gc
    #���� ����
    update.message.reply_text(Gc.start_game())
    return 3

def game2(bot,update):
    global Gc
    update.message.reply_text(Gc.checker(update.message.text))
    return 2
def help(bot, update):
    #������� ������������ ��� ��������� �������
    update.message.reply_text("��� ��� ��� �������:\n"
        "/help - ��� �������\n"
        "/stop - ���������� ���������� �������\n"
        "/startranslate - ������ �������\n"
        "/letsplay - ������ ����", reply_markup=markup)
    return ConversationHandler.END

def stop(bot, update):
    update.message.reply_text(
        "� ��������� ���������� ��������� �������!", reply_markup = markup)
    return ConversationHandler.END

def main():
    # ������ ������ updater.
    updater = Updater("801307540:AAFiDRxsXzWrMACdKODd697laNDVx6Rk004")

    # �������� �� ���� ��������� ���������.
    dp = updater.dispatcher

    #������������ �������
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

# ��������� ������� main() � ������ ������� �������.
if __name__ == '__main__':
    main()