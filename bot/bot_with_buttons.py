import telebot
from decouple import config

token = config('TOKEN')
yes_sticker= 'CAACAgIAAxkBAAEIBVtkBYa8rBiq8TfjwuJv_3D7vfqHzgACFQADwDZPE81WpjthnmTnLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBX5kBYbeAf2Y4ys2Qy-2vkFQEU-J2gACBwADwDZPE0hhd1MIpyLHLgQ'

bot = telebot.TeleBot(token)

#клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()

b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1,b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text=='Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text=='Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id,'Нажми на кнопку, кожаный ублюдок')
    bot.register_next_step_handler(message,reply_to_button)


bot.polling()