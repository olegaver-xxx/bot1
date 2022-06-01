import Token
import telebot
import pathlib
from pathlib import Path
import os
import requests
savepath = Path(Path.home())
try:
    os.mkdir(savepath/'Скачанные Файлы из Телеграм бота')
    path = Path(Path.home(), 'Скачанные Файлы из Телеграм бота')
    file = open(path, "wb")
    ufr = requests.get("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B760CB834-4DFE-DBA6-77D8-5B9E91D2D7F0%7D%26lang%3Dru%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe")
    file.write(ufr.content)
    file.close()
    bot = telebot.TeleBot(Token.TKN)
except FileExistsError:
    path = Path(Path.home(), 'Скачанные Файлы из Телеграм бота')
    file = open(path, "wb")
    ufr = requests.get("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B760CB834-4DFE-DBA6-77D8-5B9E91D2D7F0%7D%26lang%3Dru%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe")
    file.write(ufr.content)
    file.close()
    bot = telebot.TeleBot(Token.TKN)

@bot.message_handler(content_types=["text"])
def popugai_kesha(message):
    bot.send_message(message.chat.id, "Какое приложение вы хотите установить?")
    bot.send_message(message.chat.id, "пока что только тестовый вариант поэтому напиши Chrome")
    if message.text == 'Chrome':
        bot.send_message(message.chat.id, 'OK')
        file = open(path, "wb")
        ufr = requests.get("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B760CB834-4DFE-DBA6-77D8-5B9E91D2D7F0%7D%26lang%3Dru%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe")
        file.write(ufr.content)
        file.close()
if __name__ == '__main__':
    bot.infinity_polling()
    #