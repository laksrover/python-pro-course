import telebot
from u1l2 import gen_pass
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7770954749:AAFWEkcjpNpRfQTKizCQmqwbNwpxJQeb6Go")
   
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
   
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, ":)")
   
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['pass'])
def pass_cre(message):
    bot.reply_to(message, gen_pass(10))
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
