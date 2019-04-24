# ����������� ����������� ������.
from telegram.ext import Updater, MessageHandler, Filters
from MainClass import TranslatorClass as tcs

# ���������� �������-���������� ���������.
# � �� ��� ���������, ��� ��� � ����� updater, ��������� ���������.
def echo(bot, update):
    # � ������� ������ Updater ���� ���� message, ����������
    # �������� ���������.
    # � message ���� ���� text, ���������� ����� ����������� ���������,
    # � ����� ����� reply_text(str), ���������� ����� ������������,
    # �� �������� �������� ���������.
    update.message.reply_text(tcs.text_to_text(update.message.text))


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
    text_handler = MessageHandler(Filters.text, echo)

    # ������������ ���������� � ����������.
    dp.add_handler(text_handler)

    # ��������� ���� ������ � ��������� ���������.
    updater.start_polling()

    # ��� ���������� ����������.
    # (��������, ��������� ������� SIG_TERM ��� ������� ������ Ctrl+C)
    updater.idle()


# ��������� ������� main() � ������ ������� �������.
if __name__ == '__main__':
    main()