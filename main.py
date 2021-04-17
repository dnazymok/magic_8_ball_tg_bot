import telebot
import random
from settings import api_key

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[-1] == "?":
        bot.send_message(message.from_user.id, random.choice(answers))
    else:
        bot.send_message(message.from_user.id, "Это не похоже на вопрос, прости :(")


@bot.message_handler(content_types=['sticker'])
def get_sticker(sticker):
    bot.send_message(sticker.from_user.id, 'Зачетный стикер! Но давай ты отправишь мне вопрос, '
                                           'мы же здесь собрались ради этого, верно?')


bot.polling(none_stop=True, interval=0)
