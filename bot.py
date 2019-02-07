from telegram.ext import Updater
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

import pandas as pd


updater = Updater(token='772138286:AAGttzXuuZ-c3atQeHdng2QONjtS2Smy1gg')
inputfile = 'Reviews.txt'
inputfilexe = 'museum.csv'



dispatcher = updater.dispatcher

from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Я готов тебе помогать в выборе музея! "
                          "Не понимаешь о чем я? Жми /help, а если понимаешь, то /go!")


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Я Бот-помощник по музеям. Очень хочу, чтобы твой выходной прошел на УРА, "
                          "поэтому задам тебе несколько вопросов и на основе ответов подберу прекрасные варианты "
                          "для похода в музей! Если хочешь начать, пиши /go!")


def feedback(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Здесь ты можешь оставить отзыв о моей работе."
                          "Если хочешь это сделать, напиши /yes, иначе /no.")


def yes(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Спасибо за отклик. Напиши свой отзыв ниже!")
    return 0


def no(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=":(")


def go(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Выбери категорию музея (напиши цифру нужного варианта)" + '\n' +
                     "1. Исторические музеи" + '\n' +
                     "2. Литературные музеи" + '\n' +
                     "3. Художественные музеи" + '\n' +
                     "4. Театральные и музыкальные музеи, музеи кино" + '\n' +
                     "5. Музеи науки и техники" + '\n' +
                     "6. Музеи транспорта" + '\n' +
                     "7. Спортивные музеи" + '\n')
    return 0

def cancel(bot, update):
    return ConversationHandler.END

def answer(bot, update):
    user = update.message.from_user
    f = open(inputfile, 'a', encoding='utf-8')
    f.write(update.message.from_user.first_name + ' ' + update.message.from_user.last_name + ', id пользователя: ')
    f.write(str(update.message.from_user.id) + '\n' + update.message.text + '\n')
    f.close()
    update.message.reply_text(text="Спасибо большое! Твой отзыв поможет мне узнать свои ошибки и работать еще лучше!")
    return ConversationHandler.END

def main(bot, update):
    global category
    user = update.message.from_user
    category = int(update.message.text)
    update.message.reply_text(text="Выбери ценовую катеорию" + '\n' +
                             '1. Бесплатно' + '\n' +
                             '2. 1 - 300 рублей' + '\n' +
                             '3. 301 - 500 рублей' + '\n' +
                             '4. 501 - 800 рублей' + '\n' +
                             '5. 801 - 1000 рублей' + '\n')
    return 1

def main2(bot, update):
    global price
    user = update.message.from_user
    price = int(update.message.text)
    update.message.reply_text(text="Выбери удобные для посещения дни" + '\n' +
                             '1. Понедельник' + '\n' +
                             '2. Вторник' + '\n' +
                             '3. Среда' + '\n' +
                             '4. Четверг' + '\n' +
                             '5. Пятница' + '\n' +
                             '6. Суббота' + '\n' +
                             '7. Воскресенье' + '\n')
    return 2

def main3(bot, update):
    global days, category, price
    user = update.message.from_user
    days = int(update.message.text)
    df = pd.read_csv('museum')
    if category == 1:
        cat = df[df['category'] == 'Исторические музеи']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    elif category == 2:
        cat = df[df['category'] == 'Литературные музеи']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    elif category == 3:
        cat = df[df['category'] == 'Художественные музеи']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    elif category == 4:
        cat = df[df['category'] == 'Театральные и музыкальные музеи, музеи кино']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    elif category == 5:
        cat = df[df['category'] == 'Музеи науки и техники']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    elif category == 6:
        cat = df[df['category'] == 'Музеи транспорта']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
    if category == 7:
        cat = df[df['category'] == 'Спортивные музеи']
        if price == 1:
            pr = cat[cat['price'] == 'бесплатно']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 2:
            pr = cat[cat['price'] == '300']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 3:
            pr = cat[cat['price'] == '500']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 4:
            pr = cat[cat['price'] == '800']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']
        elif price == 5:
            pr = cat[cat['price'] == '1000']
            if days == 1:
                d = pr[pr['monday'] == '+']
            elif days == 2:
                d = pr[pr['tuesday'] == '+']
            elif days == 3:
                d = pr[pr['wednesday'] == '+']
            elif days == 4:
                d = pr[pr['thursday'] == '+']
            elif days == 5:
                d = pr[pr['friday'] == '+']
            elif days == 6:
                d = pr[pr['saturday'] == '+']
            elif days == 7:
                d = pr[pr['sunday'] == '+']

    if d['name'].tolist() == []:
        bot.send_message(chat_id=update.message.chat_id, text= 'Извини, но по твоим критериям отсутствуют музеи. Не расстраивайся и попробуй еще рай! /go')
    else:
        L1 = d['name'].tolist()
        L2 = d['link_main'].tolist()
        for i in range(len(L1)):
            bot.send_message(chat_id=update.message.chat_id, text = L1[i] + ' ' +L2[i])
        bot.send_message(chat_id=update.message.chat_id, text = 'Если хочешь подобрать что-то другое, то тебе сюда /go!')


    return ConversationHandler.END



start_handler = CommandHandler('start', start)
go_handler = CommandHandler('go', go)
help_handler = CommandHandler('help', help)
feedback_handler = CommandHandler('feedback', feedback)
no_handler = CommandHandler('no', no)
yes_handler = CommandHandler('yes', yes)
conv_handler = ConversationHandler(
                                    entry_points = [CommandHandler('yes', yes)],
                                    states = {
                                        0: [MessageHandler(Filters.text, answer)]
                                    },
                                    fallbacks = [CommandHandler('cancel', cancel)]
                                  )

conv_handler2 = ConversationHandler(
                                    entry_points = [CommandHandler('go', go)],
                                    states = {
                                        0: [MessageHandler(Filters.text, main)],
                                        1: [MessageHandler(Filters.text, main2)],
                                        2: [MessageHandler(Filters.text, main3)]
                                    },
                                    fallbacks = [CommandHandler('cancel', cancel)]
                                  )


dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(feedback_handler)
dispatcher.add_handler(no_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(conv_handler2)

updater.start_polling()


