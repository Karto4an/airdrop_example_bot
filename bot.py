import telebot
import os
import dotenv

import text

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text.start(message.from_user.first_name))

bot.polling()
