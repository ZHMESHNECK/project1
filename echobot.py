import telebot
from Token import token

bot = telebot.TeleBot(token)

@bot.message_handler()
def func(message):
    bot.send_message(message.from_user.id,message.text)

bot.infinity_polling()