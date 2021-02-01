import telebot

TOKEN = '1659513627:AAEmZ-0qk1xrP3E1OYqxIM4-Lqcrt9Pv5OU'

bot = telebot.TeleBot(TOKEN)



# Обработчик сообщений 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Привет! Сенпай!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.from_user.id, 'Нья :3')
	else:
		bot.send_message(message.from_user.id, 'Ди нах')


bot.polling(none_stop=True)