import telebot
import config
import random
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp/Privet.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Добро пожаловать {message.from_user.username}"
                                      f"я бот созданный чтобы отвечать на ваши вопросы! \U0001F604", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично сам как?', reply_markup=markup)
        elif message.text == 'Какие планы на выходные?':
            bot.send_message(message.chat.id, "Я не знаю! Что предложишь? \U0001F64B")
        elif message.text == 'Может в горы?':
            bot.send_message(message.chat.id, "Нее, я уже сходил!")
            bot.send_message(message.chat.id, "Давай в клуб!")
        elif message.text == 'Расскажи анекдот!':
            bot.send_message(message.chat.id, "Возвращается домой пьяный мужик. Дверь открывает жена. Тут мужик берет и захлопывает дверь:"
                                                "— Откуда пришла — там и ночуй! \U0001F602")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить! \U0001F609')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Каааайф')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ну фигово! справляйся!')

            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)


