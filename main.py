import telebot
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_zodiac_signs = telebot.types.KeyboardButton('Знак Зодиака')
    key_guess_number = telebot.types.KeyboardButton('Угадай число')
    key_stickers = telebot.types.KeyboardButton('Узнать ID стикера')
    markup.add(key_zodiac_signs, key_guess_number, key_stickers)
    bot.send_message(msg.chat.id, 'Выбирай', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(msg):
    if msg.text == 'Знак Зодиака':
        markup = telebot.types.InlineKeyboardMarkup()
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='1')
        item_2 = telebot.types.InlineKeyboardButton('Телец', callback_data='2')
        item_3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='3')
        item_4 = telebot.types.InlineKeyboardButton('Рак', callback_data='4')
        item_5 = telebot.types.InlineKeyboardButton('Лев', callback_data='5')
        item_6 = telebot.types.InlineKeyboardButton('Дева', callback_data='6')
        item_7 = telebot.types.InlineKeyboardButton('Весы', callback_data='7')
        item_8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='8')
        item_9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='9')
        item_10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='10')
        item_11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='11')
        item_12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='12')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(msg.chat.id, 'Выбери знак о котором хочешь узнать.', reply_markup=markup)
    elif msg.text == 'Угадай число':
        num = bot.send_message(msg.chat.id, 'Я загадал число от 1-3, отгадай его')
        bot.register_next_step_handler(num, num_random)
    elif msg.text == 'Узнать ID стикера':
        msg = bot.send_message(msg.chat.id, 'Отправь сюда стикер ID которого хочешь узнать')
        bot.register_next_step_handler(msg, sticker_find_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    zodiac = find_zodiac()
    stick_zodiac = find_stickers_zodiac()
    if call.data == '1':
        bot.send_sticker(call.message.chat.id, stick_zodiac[
            '1'].rstrip())  # str.rstrip() обрезает все ненужные знаки типа \n и символы chars -->
        bot.send_message(call.message.chat.id, zodiac['1'])  # без этого метода выдаёт ошибку о длинне строки

    elif call.data == '2':
        bot.send_sticker(call.message.chat.id, stick_zodiac['2'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['2'])

    elif call.data == '3':
        bot.send_sticker(call.message.chat.id, stick_zodiac['3'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['3'])

    elif call.data == '4':
        bot.send_sticker(call.message.chat.id, stick_zodiac['4'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['4'])

    elif call.data == '5':
        bot.send_sticker(call.message.chat.id, stick_zodiac['5'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['5'])

    elif call.data == '6':
        bot.send_sticker(call.message.chat.id, stick_zodiac['6'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['6'])

    elif call.data == '7':
        bot.send_sticker(call.message.chat.id, stick_zodiac['7'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['7'])

    elif call.data == '8':
        bot.send_sticker(call.message.chat.id, stick_zodiac['8'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['8'])

    elif call.data == '9':
        bot.send_sticker(call.message.chat.id, stick_zodiac['9'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['9'])

    elif call.data == '10':
        bot.send_sticker(call.message.chat.id, stick_zodiac['10'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['10'])

    elif call.data == '11':
        bot.send_sticker(call.message.chat.id, stick_zodiac['11'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['11'])

    elif call.data == '12':
        bot.send_sticker(call.message.chat.id, stick_zodiac['12'].rstrip())
        bot.send_message(call.message.chat.id, zodiac['12'])


@bot.message_handler(content_types=["sticker"])
def sticker_find_id(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, f'Вот ID твоего стикера: \n {sticker_id}')


def find_zodiac():
    with open('zodiac.txt', 'r', encoding='utf-8') as file:
        dict = {}
        for i in range(1, 13):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
        return dict


def find_stickers_zodiac():
    with open('zodiac_stickers.txt', 'r', encoding='utf-8') as file:
        dict = {}
        for i in range(1, 13):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
        return dict


def num_random(message):
    x = random.randint(0, 3)
    if message.text == str(x):
        bot.send_message(message.chat.id, f'Угадал, моё число было {x}, Ура!')
    else:
        bot.send_message(message.chat.id, f'Ты не угадал, мой число было {x}...\n Попробуй ещё раз!')


bot.polling(none_stop=True)
