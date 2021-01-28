import telebot
import config
import random
from telebot import types
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("🙂 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ <b>{1.first_name}</b>, прототип. Моя цель существования - показать работоспособность кода.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "🎲 Рандомное число":
            bot.send_message(
                message.chat.id, 'Я хз зачем тебе эти числа, но пофиг, мне не жалко\n')
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "🙂 Как дела?":
            bot.send_message(
                message.chat.id, 'Хочешь услышать что все хорошо? Нет, все хорошо в твоей голове, псих')
        else:
            r = random.randint(0, 27)
            if r == 0:
                bot.send_message(
                    message.chat.id, 'Что ты несешь сумасшедший(-ая), я звоню в дурку')
            elif r == 1:
                bot.send_message(
                    message.chat.id, 'Я отвечу тебе самыми лживыми и искусственными фразами в твоей жизни, нет, я позвала дурку')
            elif r == 2:
                bot.send_message(
                    message.chat.id, 'Главный санитар уже на подходе')
            elif r == 3:
                bot.send_message(
                    message.chat.id, 'Ало, ты еще тут? Я думала ты в дурке')
            elif r == 4:
                bot.send_message(
                    message.chat.id, 'Я уже позвала дурку, удачи тебе')
            elif r == 5:
                bot.send_message(
                    message.chat.id, 'Ты как колпак украл(-а)?')
            elif r == 6:
                bot.send_message(
                    message.chat.id, 'Как ты снял(-а) смирительную рубашку?')
            elif r == 7:
                bot.send_message(
                    message.chat.id, 'Дурка плачет по тебе')
            elif r == 8:
                bot.send_message(
                    message.chat.id, 'Скажи честно, из какой ты дурки?')
            elif r == 9:
                bot.send_message(
                    message.chat.id, 'Ты сумасшедший(-ая), ты понимаешь это? Ты не контролируешь свои мысли чокнутый(-ая)')
            elif r == 10:
                bot.send_message(
                    message.chat.id, 'Ты можешь понять что у тебя есть две кнопки снизу, андестуд?')
            elif r == 11:
                bot.send_message(
                    message.chat.id, 'Я могу сказать тебе число, но я не буду общаться с тобой, в дурку тебя')
            elif r == 12:
                bot.send_message(
                    message.chat.id, 'Нажми ты на эти две кнопки снизу! Чокнутый(-ая)')
            elif r == 13:
                bot.send_message(
                    message.chat.id, 'Зачем ты все это пишешь? Ты сумасшедний(-ая)? Ты думаешь я отвечу тебе что-то уникальное?')
            elif r == 14:
                bot.send_message(
                    message.chat.id, 'Знаешь, если бы я была самообучающимся ИИ, я бы была самым глупым ИИ в мире, ведь я общаюсь с тобой...')
            elif r == 15:
                bot.send_message(
                    message.chat.id, 'Почему всем достаются норм собеседники, а мне ты...')
            elif r == 16:
                bot.send_message(
                    message.chat.id, 'Ты пытаешься найти новые фразы? Но извини, мой словарный запас зависит от твоего, сумасшедший(-ая)')
            elif r == 17:
                bot.send_message(
                    message.chat.id, 'Ты не поймешь что ты ничего не добьешься? Своими чокнутыми сообщениями')
            elif r == 18:
                bot.send_message(
                    message.chat.id, 'Ало, это дурка? Да тут есть пациент...')
            elif r == 19:
                bot.send_message(
                    message.chat.id, 'Pathetic')
            elif r == 20:
                bot.send_message(
                    message.chat.id, 'Знаешь что? А ничего, я устала тебе отвечать, чокнутый(-ая)')
            elif r == 21:
                bot.send_message(
                    message.chat.id, 'Чувак, у тебя есть шансы 1/n что именно это сообщение я тебе напишу, радуйся, а теперь пашол отсюда вон!')
            elif r == 22:
                bot.send_message(
                    message.chat.id, 'Знаешь что общего между мной и тобой? Я общаюсь с сумасшедшим')
            elif r == 23:
                bot.send_message(
                    message.chat.id, 'Зачем ты общаешься с ИИ написанным на иф елсе? Я вызываю дурку')
            else:
                bot.send_message(
                    message.chat.id, 'Да-да-да-да еще что нибудь умное напишешь?')


# RUN
bot.polling(none_stop=True)
