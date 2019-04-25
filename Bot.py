# ����������� ����������� ������.
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
from MainClass import TranslatorClass as tcs

# ���������� �������-���������� ���������.
# � �� ��� ���������, ��� ��� � ����� updater, ��������� ���������.
def start_bot(bot, update):
    update.message.reply_text("� ���������� ��� ����������, ����� ��� ��������� ���� ��������� ������� /help")
    return ConversationHandler.END

def start_translate(bot, update):
    update.message.reply_text("� ����� ���������� �� � �������� �� ���������� � �������� :D")
    return 1

def translate(bot, update):
    # � ������� ������ Updater ���� ���� message, ����������
    # �������� ���������.
    # � message ���� ���� text, ���������� ����� ����������� ���������,
    # � ����� ����� reply_text(str), ���������� ����� ������������,
    # �� �������� �������� ���������.
    update.message.reply_text(tcs.text_to_text(update.message.text))

def help(bot, update):
    update.message.reply_text("��� ��� ��� �������:\n"
        "/help - ��� �������\n"
        "/stop - ���������� ���������� �������\n"
        "/startranslate - ������ �������")
    return ConversationHandler.END

def stop(bot, update):
    update.message.reply_text(
        "� ��������� ���������� ��������� �������!")
    return ConversationHandler.END

def main():
    # ������ ������ updater. ������ ����� "TOKEN" ���� ����������
    # ���������� �� @BotFather �����
    updater = Updater("801307540:AAFiDRxsXzWrMACdKODd697laNDVx6Rk004")

    # �������� �� ���� ��������� ���������.
    dp = updater.dispatcher

    # ������ ���������� ��������� ���� Filters.text
    # �� ��������� ���� ������� echo()
    # ����� ����������� ����������� � ���������� ��� �������
    # ����� ���������� ��� ��������� ��������� � ����� "�����",
    # �.�. ��������� ���������.
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

# ��������� ������� main() � ������ ������� �������.
if __name__ == '__main__':
    main()