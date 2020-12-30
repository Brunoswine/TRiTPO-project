import telebot
import config
import keyboard
import random
import stickers
# import sqlite3

from sqlite import SQLite

bot = telebot.TeleBot(config.TOKEN)
# bot = telebot.TeleBot('1448780946:AAHZj31LiknjQS1lAcq5gsh8tZ8ZWg8PY0Q')
from telebot import types

# инициализируем соединение с БД
# db = SQLite('data.db')
# db = sqlite3.connect("data.db")
# sql = db.cursor()


# def add_data(text, user_id, TYPE1, TYPE2, subcategory): # Добавляем данные
#  global sql, db
#  sql.execute(f"INSERT INTO data_table VALUES(?,?,?,?,?)", (text, user_id, TYPE1, TYPE2, subcategory))
#  db.commit()

N_allRun = False
L_allRun = False
Note = False
find = False
TYPE1 = "Unknown"
TYPE2 = "Unknown"
text = "Unknown"
name = "Unknown"
isRunning = False
subcategoryRun = False
changeRun = False

mainKeyboard = keyboard.mainKeyboard
rightKeyboard = keyboard.rightKeyboard
noteCategoryKeyboard = keyboard.noteCategoryKeyboard
noteKeyboard = keyboard.noteKeyboard
"""
videoCategoryKeyboard = keyboard.videoCategoryKeyboard
articleCategoryKeyboard = keyboard.videoCategoryKeyboard
documentCategoryKeyboard = keyboard.documentCategoryKeyboard
spreadsheetsCategoryKeyboard = keyboard.documentCategoryKeyboard
cloudDriveCategoryKeyboard = keyboard.cloudDriveCategoryKeyboard
githubCategoryKeyboard = keyboard.githubCategoryKeyboard
websiteCategoryKeyboard = keyboard.websiteCategoryKeyboard
"""
ChangeTYPE2Keyboard = keyboard.ChangeTYPE2Keyboard
rightKeyboard_without_subcategory = keyboard.rightKeyboard_without_subcategory


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    texxxt = 'https://www.youtube.com/watch?v=YvZqIoAwUh8&ab_channel=thebootlegboy2'
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для организации ссылок и заметок. "
                     "Чтобы получить помощь, отправьте /help".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=mainKeyboard)
    bot.send_message(message.chat.id, f"<a href='{texxxt}'>Доров</a>", parse_mode='html')


@bot.message_handler(commands=['help'])
def help_mes(message):
    bot.send_message(message.chat.id, "Список команд: \n"
                                      "/help - Собственно список команд\n"
                                      "/start - Приветствие и вызов клавиатуры, если она по какой-то причине потерялась\n"
                                      "/reset - Если по какой-то причине бот завис, сброс флагов\n"
                                      "/hard_clear - Удаление всех ваших данных из БД\n"
                                      "/clear_links - Удаление всех ваших ссылок из БД\n"
                                      "/clear_notes - Удаление всех ваших заметок из БД\n"
                                      "Чтобы начать работу с ботом, ему нужно отправить ссылку или текстовое сообщение,"
                                      "он определит категорию сообщения, предложит добавить подкатегории, "
                                      "а также изменить категорию, если она была определена неправильно. При выборе "
                                      "ответа 'окей', сообщение будет сохранено как несортированное.")


@bot.message_handler(commands=['reset'])
def help_mes(message):
    global N_allRun
    global L_allRun
    global Note
    global find
    global isRunning
    global subcategoryRun
    global changeRun
    N_allRun = False
    L_allRun = False
    Note = False
    find = False
    isRunning = False
    subcategoryRun = False
    changeRun = False

@bot.message_handler(commands=['hard_clear'])
def clear(message):
    db = SQLite('data.db')
    db.clear(message.chat.id)

    bot.send_message(message.chat.id, "От вас в БД не осталось ни следа")
    db.close()

@bot.message_handler(commands=['clear_links'])
def clear1(message):
    db = SQLite('data.db')
    db.clear1(message.chat.id, 1)
    bot.send_message(message.chat.id, "Ссылки удалены")
    db.close()


@bot.message_handler(commands=['clear_notes'])
def clear2(message):
    db = SQLite('data.db')
    db.clear1(message.chat.id, 2)
    bot.send_message(message.chat.id, "Заметки удалены")
    db.close()


@bot.message_handler(commands=['help'])
def welcome(message):
    # keyboard
    bot.send_message(message.chat.id, "")


@bot.message_handler(content_types=['text'])
def send_text(message):
    global find
    global TYPE1
    global TYPE2
    global isRunning
    global text

    if isRunning == True:  # если выбор был прерван, просто сохранить ссылку по дефолту
        bot.send_message(message.chat.id, 'Мы еще с прошлым сообщением не разобрались, а ты с новым лезешь')
        return
    db = SQLite('data.db')
    text = message.text.lower()
    chat_id = message.chat.id
    # if db.data_exists(text):
    # bot.send_message(message.chat.id, 'Уже существует')

    if "https" in text or "http" in text or "www" in text:
        bot.send_message(message.chat.id, 'это ссылка, нафиг')
        if db.link_exists(text, 1):
            bot.send_message(message.chat.id, "Такая ссылка уже есть, текущая обновит предыдущую")
        TYPE1 = "Link"
        isRunning = True
        find = False
        # Если не найдено соответствие, продолжаем поиск
        if not find:
            if "youtube.com" in text and not "watch" in text:
                bot.send_message(message.chat.id, 'Это ссылка на youtube, зачем вам ее сохранять? Автор?')
            for key in keyboard.videoList:
                if find:
                    break  # чтобы дальше не искать совпадение делаем break
                if key in text:
                    TYPE2 = "Video"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как видео', reply_markup=rightKeyboard)
                    find = True
                    isRunning = True

        if not find:
            for key in keyboard.articleList:
                if find:
                    break
                if key in text:
                    TYPE2 = "Article"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как статья', reply_markup=rightKeyboard)
                    find = True
                    isRunning = True

        if not find:
            for key in keyboard.documentList:
                if find:
                    break
                if key in text:
                    TYPE2 = "Document"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как документ',
                                     reply_markup=rightKeyboard)
                    find = True
                    isRunning = True

        if not find:
            for key in keyboard.spreadsheetList:
                if find:
                    break
                if key in text:
                    TYPE2 = "Spreadsheet"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как таблица',
                                     reply_markup=rightKeyboard)
                    find = True
                    isRunning = True

        if not find:
            for key in keyboard.cloudDriveList:
                if find:
                    break
                if key in text:
                    TYPE2 = "CloudDrive"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как облачное хранилище',
                                     reply_markup=rightKeyboard)
                    find = True
                    isRunning = True

        if not find:
            for key in keyboard.githubList:
                if find:
                    break
                if key in text:
                    TYPE2 = "github"
                    bot.send_message(message.chat.id, 'Данная ссылка определена как github',
                                     reply_markup=rightKeyboard)
                    find = True
                    isRunning = True
        # Если ни с чем не совпало - то это сайт
        if not find:
            bot.send_message(message.chat.id, 'Данная ссылка определена как сайт',
                             reply_markup=rightKeyboard)
            TYPE2 = "Website"
            find = True
            isRunning = True
    elif message.text == '🎲 Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == "🌐Ссылки":
        bot.send_message(message.chat.id, '🌐Ссылки', reply_markup=keyboard.linkAskKeyboard)
    elif message.text == "📝Заметки":
        bot.send_message(message.chat.id, '📝Заметки', reply_markup=keyboard.noteAskKeyboard)

        # elif message.text == "🗒Задачи":
        # bot.send_message(message.chat.id, 'Типо задачи')
        # bot.register_next_step_handler(message, ToDo)  # следующий шаг – функция get_name
    elif text in keyboard.jiveList:
        msg = random.choice(stickers.jiveBelarus)
        bot.send_sticker(message.chat.id, msg)
    elif text:
        isRunning = True
        if db.link_exists(text, 2):
            bot.send_message(message.chat.id, "Такая заметка уже есть, текущая обновит предыдущую")
        # db.add_subscriber(message.from_user.id, False)
        # db.close()
        bot.send_message(message.chat.id, 'Это заметка?', reply_markup=noteKeyboard)


    else:
        bot.send_message(message.chat.id, "Эмм, не знаю что и сказать")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    db = SQLite('data.db')
    # db = sqlite3.connect("data.db")
    # sql = db.cursor()
    user_id = call.from_user.id
    global isRunning, TYPE1, TYPE2, name, subcategoryRun, changeRun, Note, text, L_allRun, N_allRun
    try:
        if call.message:
            if call.data == 'Yes':
                TYPE1 = "Note"
                isRunning = True

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Заметка с категорией...', reply_markup=noteCategoryKeyboard)
            elif call.data == 'No':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Не заметка', reply_markup=None)
                bot.send_message(chat_id=call.message.chat.id,
                                 text="Эмм, не знаю что и сказать, видимо, я не знаком с данной командой")
                isRunning = False

            if TYPE1 == "Link":
                if TYPE2 in keyboard.TYPE2List:
                    name = keyboard.changeType2Dict.get(TYPE2)
                    if call.data == 'OK':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text='Данная ссылка сохранена как ' + name, reply_markup=None)
                        isRunning = False

                        db.add_data(text, user_id, 1, keyboard.associativeDict.get(TYPE2),
                                    keyboard.unsortedDict.get(TYPE2))
                        # TYPE Link = 1, Note = 2. Сделано Для скорости поиска по БД
                    # sql.execute("INSERT INTO data_table VALUES(?,?,?,?,?)",
                    #             (text, call.from_user.id, 1, 7, "Unsorted"))
                    # db.commit()

                    # add_data("sdsddsd",call.from_user.id, 1, 7, "Unsorted")
                    # здесь происходит сейв по дефолту
                    elif call.data == 'Change':
                        changeRun = True
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text="Меняем категорию " + name + " на категорию...",
                                              reply_markup=ChangeTYPE2Keyboard)


                    # call.data сохраняем во временные переменные, ибо когда они обрабатываются (edit or send message),
                    # они по сути считаются отработаными, и исчезают

                  #  if call.data in keyboard.changeType2Dict.keys():
                     #   changeRun = True
                    if changeRun == True:
                        if call.data in keyboard.changeType2Dict.keys():  # если call_data встречается в ключах
                            changeRun = False
                            temp_call_data = call.data  # словаря то
                            temp_item = keyboard.changeType2Dict.get(temp_call_data)
                            TYPE2 = temp_call_data
                            if TYPE2 in keyboard.mainTYPE2List:
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Категория изменена на " + temp_item,
                                                      reply_markup=rightKeyboard)
                            else:
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Категория изменена на " + temp_item,
                                                      reply_markup=rightKeyboard_without_subcategory)

                    if call.data == 'subcategory':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text="Данная ссылка определена как " + name + " с категорией...",
                                              reply_markup=keyboard.changeKeyboardsDict.get(TYPE2))
                        subcategoryRun = True

                    # Создал словари чтобы не писать много однотипного кода
                    # call_data Это то, на какую кнопку мы нажиаем, в данном случае это подкатегория

                    if subcategoryRun:
                        # первый if для скорости, чтобы не проверять весь список
                        # второй, чтобы не сработала команда раньше запроса
                        needed_dict = keyboard.dictionaryDict.get(TYPE2)  # нужный нам словарь находим от имени TYPE2
                        # например videoDict                                                                  #Video
                        if call.data in needed_dict.keys():
                            temp_call_data = call.data
                            temp_item = needed_dict.get(temp_call_data)
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text="Данная ссылка сохранена как " + name + " c категорией " +
                                                       temp_item, reply_markup=None)
                            db.add_data(text, user_id, 1, keyboard.associativeDict.get(TYPE2),
                                        temp_call_data)
                            # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                            subcategoryRun = False
                            isRunning = False

            if TYPE1 == "Note":
                if call.data in keyboard.noteDict.keys():
                    temp_call_data = call.data
                    temp_item = keyboard.noteDict.get(temp_call_data)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Данная заметка сохранена в категорию " + temp_item, reply_markup=None)
                    db.add_data(text, user_id, 2, keyboard.noteAssociativeDict.get(temp_call_data),
                                "Note")
                    # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_   Description?
                    isRunning = False
            if call.data == "L_Look_all":
                result = db.get_data(1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🌐Ссылки", reply_markup=None)
                bot.send_message(chat_id=call.message.chat.id,
                                 text="Список")
                i = 1
                for tuple_ in result:
                    t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
                    if not t_type2 == 8 and not t_type2 == 9:
                        needed__dict = keyboard.mirroredAssociativeDict.get(
                            str(t_type2))  # В кортеже хранится int для скорости, поэтому преобразовываем
                        # videoDict                                         # 1=Video
                        number = str(i)
                        category = keyboard.mirroredRAssociativeDict.get(str(t_type2))
                        t_subcategory_done = needed__dict.get(t_subcategory)
                        texxxt = str(t_text)
                        bot.send_message(chat_id=call.message.chat.id,
                                         text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
                                              f"Категория: {category}\nПодкатегория: {t_subcategory_done}",
                                         parse_mode='html')
                        i = i + 1
                    else:
                        bot.send_message(chat_id=call.message.chat.id,
                                         text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
                                              f"Категория: {category}",
                                         parse_mode='html')
                        i = i + 1
            elif call.data == "L_Look_Category":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="🌐Выбрерите категорию...", reply_markup=keyboard.ChangeTYPE2Keyboard)
                L_allRun = True

           # if call.data in keyboard.changeType2Dict.keys():
           #     L_allRun = True

            if L_allRun and call.data in keyboard.changeType2Dict.keys():
                if L_allRun:
                    temp_call_data = call.data
                    number = keyboard.associativeDictnum.get(temp_call_data)
                    L_allRun = False
                    result = db.get_data1(1, number)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="🌐Категории", reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text="Список")
                    i = 1
                    for tuple_ in result:
                        t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
                        if not t_type2 == 8 and not t_type2 == 9:
                            needed__dict = keyboard.mirroredAssociativeDict.get(
                                str(t_type2))  # В кортеже хранится int для скорости, поэтому преобразовываем
                            # videoDict                                         # 1=Video
                            number = str(i)
                            category = keyboard.mirroredRAssociativeDict.get(str(t_type2))
                            t_subcategory_done = needed__dict.get(t_subcategory)
                            texxxt = str(t_text)
                            bot.send_message(chat_id=call.message.chat.id,
                                             text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
                                                  f"Категория: {category}\nПодкатегория: {t_subcategory_done}",
                                             parse_mode='html')
                            i = i + 1

                        else:
                            bot.send_message(chat_id=call.message.chat.id,
                                             text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
                                                  f"Категория: {category}",
                                             parse_mode='html')
                            i = i + 1

            # if call.data == "L_Redact":
            #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
            #     result = db.get_data(1)
            #     bot.send_message(chat_id=call.message.chat.id,
            #                      text="result")
            #     i = 1
            #     number = str(i)
            #     for tuple_ in result:
            #         markup.add(number)
            #
            #         i = i + 1
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                       text="Чтобы редактировать, отправьте номер записи сообщения", reply_markup=markup)
            #
            # if call.data == "L_Delete":
            #     pass

            if call.data == "N_Look_all":
                result = db.get_data(2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="📝Заметки", reply_markup=None)
                bot.send_message(chat_id=call.message.chat.id,
                                 text="Список")
                i = 1
                for tuple_ in result:
                    t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
                    number = str(i)
                    category = keyboard.mirroredNoteAssociativeDict.get(str(t_type2))
                    bot.send_message(chat_id=call.message.chat.id,
                                     text=f"{number}. Заметка. Категория: {category}\n"
                                          f"{t_text}\n",
                                     parse_mode='html')
                    i = i + 1

            elif call.data == "N_Look_Category":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="📝Выбрерите категорию...", reply_markup=keyboard.noteCategory1Keyboard)
                N_allRun = True

            #if call.data in keyboard.noteAssociativeDict1.keys():


            if N_allRun and call.data in keyboard.noteAssociativeDict1.keys():
                if N_allRun:
                    temp_call_data = call.data
                    number = int(keyboard.noteAssociativeDict1.get(temp_call_data))
                    N_allRun = False
                    result = db.get_data1(2, number)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="📝Категории", reply_markup=None)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text="Список:")
                    i = 1
                    for tuple_ in result:
                        t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
                       # needed__dict = keyboard.mirroredAssociativeDict.get(
                      #      str(t_type2))  # В кортеже хранится int для скорости, поэтому преобразовываем
                        # videoDict                                         # 1=Video
                        number = str(i)
                        category = keyboard.mirroredNoteAssociativeDict.get(str(t_type2))
                        #t_subcategory_done = needed__dict.get(t_subcategory)
                        texxxt = str(t_text)
                        bot.send_message(chat_id=call.message.chat.id,
                                         text=f"{number}. Заметка. Категория: {category}\n"
                                              f"{t_text}\n",
                                         parse_mode='html')
                        i = i + 1

            # if call.data == "N_Redact":
            #    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
            #     result = db.get_data(1)
            #     bot.send_message(chat_id=call.message.chat.id,
            #                      text="result")
            #     i = 1
            #     number = str(i)
            #     for tuple_ in result:
            #        # markup.add(number)
            #
            #         i = i + 1
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                       text="Чтобы редактировать, отправьте номер записи сообщения", reply_markup=markup)
            #
            # if call.data == "N_Delete":
            #     pass

        # if call.data == "L_Look_Category":

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
    except Exception as e:
        print(repr(e))
    db.close()


def ToDo(message):
    bot.send_message(message.chat.id, 'Переход состоялся')


bot.polling(none_stop=True)
