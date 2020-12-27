import telebot
import config
import keyboard
import random
import stickers

bot = telebot.TeleBot(config.TOKEN)
# bot = telebot.TeleBot('1448780946:AAHZj31LiknjQS1lAcq5gsh8tZ8ZWg8PY0Q')
from telebot import types

find = False
TYPE1 = "Unknown"
TYPE2 = "Unknown"
name = "Unknown"
isRunning = False
subcategoryRun = False
changeRun = False

rightKeyboard = keyboard.rightKeyboard
videoCategoryKeyboard = keyboard.videoCategoryKeyboard
articleCategoryKeyboard = keyboard.videoCategoryKeyboard
documentCategoryKeyboard = keyboard.documentCategoryKeyboard
spreadsheetsCategoryKeyboard = keyboard.documentCategoryKeyboard
cloudDriveCategoryKeyboard = keyboard.cloudDriveCategoryKeyboard
githubCategoryKeyboard = keyboard.githubCategoryKeyboard
websiteCategoryKeyboard = keyboard.websiteCategoryKeyboard
ChangeTYPE2Keyboard = keyboard.ChangeTYPE2Keyboard
rightKeyboard_without_subcategory = keyboard.rightKeyboard_without_subcategory


@bot.message_handler(content_types=['text'])
def send_text(message):
    global find
    global TYPE1
    global TYPE2
    global isRunning
    if isRunning == True:  # если выбор был прерван, просто сохранить ссылку по дефолту
        bot.send_message(message.chat.id, 'Мы еще с прошлым сообщением не разобрались, а ты с новым лезешь')
        return
    text = message.text.lower()
    chat_id = message.chat.id
    if text in keyboard.jiveList:
        msg = random.choice(stickers.jiveBelarus)
        bot.send_sticker(message.chat.id, msg)
    elif "https" in text or "http" in text:
        TYPE1 = "Link"
        isRunning = True
        find = False
        bot.send_message(message.chat.id, 'это ссылка, нафиг')
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
                    bot.send_message(message.chat.id, 'Данная ссылка определена как облачное хранилище',
                                     reply_markup=rightKeyboard)
                    find = True
                    isRunning = True
        if not find:
            bot.send_message(message.chat.id, 'Данная ссылка определена как сайт',
                             reply_markup=rightKeyboard)
            TYPE2 = "Website"
            find = True
            isRunning = True
    
    else:
        bot.send_message(message.chat.id, 'что-то другое, нафиг')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global isRunning, TYPE1, TYPE2, name, subcategoryRun, changeRun
    try:
        if call.message:
            if TYPE1 == "Link":
                if TYPE2 in keyboard.TYPE2List:
                    name = keyboard.changeType2Dict.get(TYPE2)
                    if call.data == 'OK':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text='Данная ссылка сохранена как ' + name, reply_markup=None)
                        isRunning = False
                        # здесь происходит сейв по дефолту
                    elif call.data == 'Change':
                        changeRun = True
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text="Меняем категорию " + name + " на категорию...",
                                              reply_markup=ChangeTYPE2Keyboard)

# call.data сохраняем во временные переменные, ибо когда они обрабатываются (edit or send message),
# они по сути считаются отработаными, и исчезают

                    if changeRun:
                        if call.data in keyboard.changeType2Dict.keys():  # если call_data встречается в ключах
                            changeRun = False
                            temp_call_data = call.data                    # словаря то
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
                            # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                            subcategoryRun = False
                            isRunning = False


            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
    except Exception as e:
        print(repr(e))


def get_surname(message):
    bot.send_message(message.chat.id, 'Переход состоялся')


bot.polling(none_stop=True)
