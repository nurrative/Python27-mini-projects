import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message('892891195', "Вы лучшая")
# bot.polling()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEIBRJkBXYK07kB_oVdgDN7qbWo1_RiHAACHw8AAofNWUt7QB9HavILXS4E')
    bot.send_photo(message.chat.id,'https://avatars.mds.yandex.net/get-mpic/4262452/img_id5635830207981014623.jpeg/orig')

@bot.message_handler(content_types=['text'])
def aaa(message):
    if message.text =="привет":
        bot.send_message(message.chat.id,'Ты дурак')
    else:
        bot.send_message(message.chat.id,'Пиши нормально')

@bot.message_handler(content_types=['sticker'])
def sticker_return(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()