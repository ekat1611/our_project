import telebot
bot = telebot.TeleBot('1482586619:AAH11_5FnmgBjrkMf6zbJLp24ro33dXvnRM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Здесь можно найти учебные материалы для изучения языка программирования "
                                               "Python. Выберите пункт меню, который вас интересует:\n"
                                               "/courses - бесплатные онлайн-курсы\n"
                                               "/books - книги для изучения языка\n"
                                               "/articles - полезные статьи\n")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")


bot.polling(none_stop=True, interval=0)
