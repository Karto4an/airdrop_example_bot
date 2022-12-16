import telebot
import os
import dotenv

import text
import reply_markups

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text.start(message.from_user.first_name), reply_markup=reply_markups.start)

@bot.message_handler(commands=['tasks'])
def tasks(message):
    bot.send_message(message.chat.id, text.tasks())

@bot.message_handler(commands=['referral'])
def referral(message):
    bot.send_message(message.chat.id, text.referral())

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, text.about())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text == "🤖 Tasks":
        tasks(message)
    elif message.text == "👥 Referral program":
        referral(message)
    elif message.text == "🌎 About":
        about(message)

    else:
        print(f"Unknown text command: {message.text}")

bot.polling()
