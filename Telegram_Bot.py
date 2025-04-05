import telebot
TOKEN = '7701018516:AAGxfpJpYlMaFXnBju1tv-M6u6qH4tLgeYo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def start_command(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)