import telebot
bot = telebot.TeleBot('1482586619:AAH11_5FnmgBjrkMf6zbJLp24ro33dXvnRM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напиши привет!")


bot.polling(none_stop=True, interval=0)
