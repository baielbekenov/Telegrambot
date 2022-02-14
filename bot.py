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

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    audio1 = types.KeyboardButton("Music1")
    audio2 = types.KeyboardButton("Music2")
    audio3 = types.KeyboardButton("Music3")
    markup.add(audio1, audio2, audio3)



    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Добро пожаловать {message.from_user.username}"
                                      f" я бот созданный чтобы отвечать на ваши вопросы! \U0001F604", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text.lower() == 'Рандомное число'.lower():
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text.lower() == 'Как дела?'.lower():

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично сам как?', reply_markup=markup)
        elif message.text.lower() == 'Какие планы на выходные?'.lower():
            bot.send_message(message.chat.id, "Я не знаю! Что предложишь? \U0001F64B")
        elif message.text.lower() == 'Может в горы?'.lower():
            bot.send_message(message.chat.id, "Нее, я уже сходил!")
            bot.send_message(message.chat.id, "Давай в клуб!")
        elif message.text.lower() == 'Расскажи анекдот'.lower():
            bot.send_message(message.chat.id, "Возвращается домой пьяный мужик. Дверь открывает жена. Тут мужик берет и захлопывает дверь:"
                                                "— Откуда пришла — там и ночуй! \U0001F602")
        elif message.text.lower() == 'Music3'.lower():
            audio = open('music/the-weeknd-blinding-lights.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
        elif message.text.lower() == 'Music2'.lower():
            audio = open('music/The Weeknd — Devil May Cry.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
        elif message.text.lower() == 'Music1'.lower():
            audio = open('music/The Weeknd — Faith.mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
        else:
            bot.send_message(message.chat.id, 'Я не понимаю тебя! Пожалуйста \U0001F64F пиши разборчиво! \U0001F609')



@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Правда? завидую!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ну удачи! справляйся!')

            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)


