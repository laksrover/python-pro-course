import telebot
import random
from telebot.types import ReactionTypeEmoji
from u1l2 import gen_pass
import os
import datetime
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("token")
   
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['memday'])
def send_memd(message):
    daymo = datetime.datetime.now()
    daymn = int((daymo.strftime("%d")))%4

    img_name = os.listdir('images')[daymn]
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
          
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, ":)")
@bot.message_handler(commands=['calc'])
def send_calc(message):
    try:
        eval("bot.reply_to(message,{eval(message.text.split()[1])})")
    except NameError:
        bot.reply_to(message, "couldn't calculate")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['pass'])
def pass_cre(message):
    bot.reply_to(message, gen_pass(10))
@bot.message_handler(commands=["emoji"])
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
