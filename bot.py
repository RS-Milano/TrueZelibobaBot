import telebot

from my_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(regexp="Andrew")
def ask_weight(message):
	bot.reply_to(message, "What is ypur weight today?\nPlease send in '74.55' format")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Andrew loves you")
	markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = telebot.types.KeyboardButton('Andrew')
	itembtn2 = telebot.types.KeyboardButton('Ksenia')
	markup.add(itembtn1, itembtn2)
	bot.send_message("512920324", "Choose one letter:", reply_markup=markup)

bot.infinity_polling()