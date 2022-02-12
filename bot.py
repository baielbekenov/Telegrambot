import telebot
from decouple import config
from telebot import types
bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)

@bot.message_handler(commands=['start', 'Привет', 'Hi'])
def answer_start(message):
    print(message.from_user.username)
    text = f"Добро пожаловать в бота {message.from_user.username} !!!" \
            f"Выберите тот курс на который хотите пойти"
    keyboard_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Python', callback_data='python')
    btn_2 = types.InlineKeyboardButton(text='Java', callback_data='java')
    btn_3 = types.InlineKeyboardButton(text='C++', callback_data='c++')
    keyboard_in.add(btn_1, btn_2, btn_3)
    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)

@bot.callback_query_handler(func=lambda call:True)
def send_course(call):
    if call.data == 'python':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('python morning')
        btn_2 = types.KeyboardButton('python evening')
        btn_3 = types.KeyboardButton('python bootcamp')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать группу!!!'
        bot.send_message(call.message.chat.id, text, reply_markup=murkup_reply)
    elif call.data == 'java':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('java morning')
        btn_2 = types.KeyboardButton('java evening')
        btn_3 = types.KeyboardButton('java bootcamp')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать группу!!!'
        bot.send_message(call.message.chat.id, text, reply_markup=murkup_reply)
    elif call.data == 'c++':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('c++ morning')
        btn_2 = types.KeyboardButton('c++ evening')
        btn_3 = types.KeyboardButton('c++ bootcamp')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали {call.data}! теперь необходимо выбрать группу!!!'
        bot.send_message(call.message.chat.id, text, reply_markup=murkup_reply)


@bot.message_handler(content_types=['text'])
def send_good_message(message):
    if message.text == 'python morning':
        bot.send_message(message.chat.id, f'вас записали на курс python morning менеджер свами свяжется!')
    elif message.text == 'python evening':
        bot.send_message(message.chat.id, f'вас записали на курс python evening менеджер свами свяжется!')
    elif message.text == 'python bootcamp':
        bot.send_message(message.chat.id, f'вас записали на курс python bootcamp менеджер свами свяжется!')
    elif message.text == 'java morning':
        bot.send_message(message.chat.id, f'вас записали на курс java morning менеджер свами свяжется!')
    elif message.text == 'java evening':
        bot.send_message(message.chat.id, f'вас записали на курс java evening менеджер свами свяжется!')
    elif message.text == 'java bootcamp':
        bot.send_message(message.chat.id, f'вас записали на курс java bootcamp менеджер свами свяжется!')
    elif message.text == 'c++ morning':
        bot.send_message(message.chat.id, f'вас записали на курс c++ morning менеджер свами свяжется!')
    elif message.text == 'c++ evening':
        bot.send_message(message.chat.id, f'вас записали на курс c++ evening менеджер свами свяжется!')
    elif message.text == 'c++ bootcamp':
        bot.send_message(message.chat.id, f'вас записали на курс c++ bootcamp менеджер свами свяжется!')


bot.polling()