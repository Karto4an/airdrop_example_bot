from telebot import types

start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
start.row("🤖 Tasks")
start.row("👥 Referral program")
start.row("🌎 About")
