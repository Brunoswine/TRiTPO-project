from typing import List

import telebot

from telebot import types

# Тут написано, что это лист, но на деле кортежи(просто менять не хочется), ибо быстрее

videoList = ("youtube.com/watch", "vk.com/video", "youtu.be")

articleList = ("habr.com", "reddit.com", "dev.by", "naked-science.ru", "stopgame.ru", "wikipedia.org", "popmech.ru",
               "cyberleninka.ru", "meduza.io", "onliner.by", "tut.by", "lifehacker.ru")

documentList = ("docs.google.com/document/", "docs.google.com/presentation/", ".ppt", ".pptx", ".doc", ".docx", ".pdf",
                ".txt", ".htm")
spreadsheetList = (".exel", "docs.google.com/spreadsheets/")

cloudDriveList = ("drive.google.com", "www.dropbox.com", "mega.nz", "cloud.mail.ru", "disk.yandex.ru", "onedrive")

githubList = ("github.com", "gitlab.com")

jiveList = ('живе беларусь', 'жыве беларусь', 'живе беларусь!', 'жыве беларусь!')

mainTYPE2List = ("Video", "Article", "Document", "Spreadsheet", "CloudDrive", "Github", "Website")

TYPE2List = ["Video", "Article", "Document", "Spreadsheet", "CloudDrive", "Github", "Website", "Product",
             "Other"]

mainKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
item1 = types.KeyboardButton("🌐Ссылки")
item2 = types.KeyboardButton("📝Заметки")
item3 = types.KeyboardButton("🎲 Рандомное число")
# item4 = types.KeyboardButton("🗒Задачи")
mainKeyboard.add(item1, item2, item3)

noteKeyboard = types.InlineKeyboardMarkup(row_width=2)
noteKey1 = types.InlineKeyboardButton('Да', callback_data="Yes")
noteKey2 = types.InlineKeyboardButton('Нет', callback_data="No")
noteKeyboard.add(noteKey1, noteKey2)

existsKeyboard = types.InlineKeyboardMarkup(row_width=2)
existsKey1 = types.InlineKeyboardButton('Окей', callback_data="Ok_exists")
existsKey2 = types.InlineKeyboardButton('Редактивровать', callback_data="Redact")
existsKeyboard.add(existsKey1, existsKey2)

noteAskKeyboard = types.InlineKeyboardMarkup(row_width=2)
noteAskKey1 = types.InlineKeyboardButton('Все', callback_data="N_Look_all")
noteAskKey2 = types.InlineKeyboardButton('Выбрать категорию', callback_data="N_Look_Category")
noteAskKey3 = types.InlineKeyboardButton('Редактировать', callback_data="N_Redact")
noteAskKey4 = types.InlineKeyboardButton('Удалить', callback_data="N_Delete")
noteAskKeyboard.add(noteAskKey1, noteAskKey2, noteAskKey3, noteAskKey4)

linkAskKeyboard = types.InlineKeyboardMarkup(row_width=2)
linkAskKey1 = types.InlineKeyboardButton('Все', callback_data="L_Look_all")
linkAskKey2 = types.InlineKeyboardButton('Выбрать категорию', callback_data="L_Look_Category")
linkAskKey3 = types.InlineKeyboardButton('Редактировать', callback_data="L_Redact")
linkAskKey4 = types.InlineKeyboardButton('Удалить', callback_data="L_Delete")
linkAskKeyboard.add(linkAskKey1, linkAskKey2, linkAskKey3, linkAskKey4)

link2AskKeyboard = types.InlineKeyboardMarkup(row_width=2)
link2AskKey1 = types.InlineKeyboardButton('Все', callback_data="L_all")
link2AskKey2 = types.InlineKeyboardButton('Выбрать подкатегорию', callback_data="L_Look_subcategory")
link2AskKeyboard.add(link2AskKey1, link2AskKey2)

rightKeyboard = types.InlineKeyboardMarkup(row_width=2)
rightKey1 = types.InlineKeyboardButton('Окей', callback_data="OK")
rightKey2 = types.InlineKeyboardButton('Нет, изменить', callback_data="Change")
rightKey3 = types.InlineKeyboardButton('Добавить подкатегорию', callback_data="subcategory")
rightKeyboard.add(rightKey1, rightKey2, rightKey3)

rightKeyboard_without_subcategory = types.InlineKeyboardMarkup(row_width=2)
rightKeyboard_without_subcategory.add(rightKey1, rightKey2)

ChangeTYPE2Keyboard = types.InlineKeyboardMarkup(row_width=2)
ChangeTYPE2Key1 = types.InlineKeyboardButton('Видео', callback_data="Video")
ChangeTYPE2Key2 = types.InlineKeyboardButton('Статья', callback_data="Article")
ChangeTYPE2Key3 = types.InlineKeyboardButton('Документ', callback_data="Document")
ChangeTYPE2Key4 = types.InlineKeyboardButton('Таблица', callback_data="Spreadsheet")
ChangeTYPE2Key5 = types.InlineKeyboardButton('Облако', callback_data="CloudDrive")
ChangeTYPE2Key6 = types.InlineKeyboardButton('Github', callback_data="Github")
ChangeTYPE2Key7 = types.InlineKeyboardButton('Сайт', callback_data="Website")
ChangeTYPE2Key8 = types.InlineKeyboardButton('Товар', callback_data="Product")
ChangeTYPE2Key9 = types.InlineKeyboardButton('Другое', callback_data="Other")
ChangeTYPE2Keyboard.add(ChangeTYPE2Key1, ChangeTYPE2Key2, ChangeTYPE2Key3, ChangeTYPE2Key4, ChangeTYPE2Key5,
                        ChangeTYPE2Key6, ChangeTYPE2Key7, ChangeTYPE2Key8, ChangeTYPE2Key9)

videoCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
videoCategoryKey1 = types.InlineKeyboardButton('Развлекательное', callback_data="V_Entertainment")
videoCategoryKey2 = types.InlineKeyboardButton('Интересное', callback_data="V_Interesting")
videoCategoryKey3 = types.InlineKeyboardButton('Избранное', callback_data="V_Favorite")
videoCategoryKey4 = types.InlineKeyboardButton('Познавательное', callback_data="V_Informative")
videoCategoryKey5 = types.InlineKeyboardButton('Обучение', callback_data="V_Training")
videoCategoryKey6 = types.InlineKeyboardButton('Университет', callback_data="V_University")
videoCategoryKey7 = types.InlineKeyboardButton('Програмирование', callback_data="V_Programming")
videoCategoryKey8 = types.InlineKeyboardButton('Игры', callback_data="V_Games")
videoCategoryKey9 = types.InlineKeyboardButton('Здоровье', callback_data="V_Health")
videoCategoryKey10 = types.InlineKeyboardButton('Английский язык', callback_data="V_English")
videoCategoryKey11 = types.InlineKeyboardButton('Новости', callback_data="V_News")
videoCategoryKey12 = types.InlineKeyboardButton('Другое', callback_data="V_Other")
videoCategoryKey13 = types.InlineKeyboardButton('Несортированное', callback_data="V_Unsorted")
videoCategoryKeyboard.add(videoCategoryKey1, videoCategoryKey2, videoCategoryKey3, videoCategoryKey4, videoCategoryKey5,
                          videoCategoryKey6, videoCategoryKey7, videoCategoryKey8, videoCategoryKey9,
                          videoCategoryKey10, videoCategoryKey11, videoCategoryKey12, videoCategoryKey13)

noteCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
noteCategoryKey1 = types.InlineKeyboardButton('Фильмы', callback_data="N_Films")
noteCategoryKey2 = types.InlineKeyboardButton('Музыка', callback_data="N_Music")
noteCategoryKey3 = types.InlineKeyboardButton('Игры', callback_data="N_Games")
noteCategoryKey4 = types.InlineKeyboardButton('Идеи для подарков', callback_data="N_Presents")
noteCategoryKey5 = types.InlineKeyboardButton('Пароли', callback_data="N_Passwords")
noteCategoryKey6 = types.InlineKeyboardButton('Важная информация', callback_data="N_Important")
noteCategoryKey7 = types.InlineKeyboardButton('Не забыть', callback_data="N_Remember")
noteCategoryKey8 = types.InlineKeyboardButton('Другое', callback_data="N_Other")
noteCategoryKeyboard.add(noteCategoryKey1, noteCategoryKey2, noteCategoryKey3, noteCategoryKey4, noteCategoryKey5,
                         noteCategoryKey6, noteCategoryKey7, noteCategoryKey8)

noteCategory1Keyboard = types.InlineKeyboardMarkup(row_width=2)
noteCategory1Key1 = types.InlineKeyboardButton('Фильмы', callback_data="N_Films1")
noteCategory1Key2 = types.InlineKeyboardButton('Музыка', callback_data="N_Music1")
noteCategory1Key3 = types.InlineKeyboardButton('Игры', callback_data="N_Games1")
noteCategory1Key4 = types.InlineKeyboardButton('Идеи для подарков', callback_data="N_Presents1")
noteCategory1Key5 = types.InlineKeyboardButton('Пароли', callback_data="N_Passwords1")
noteCategory1Key6 = types.InlineKeyboardButton('Важная информация', callback_data="N_Important1")
noteCategory1Key7 = types.InlineKeyboardButton('Не забыть', callback_data="N_Remember1")
noteCategory1Key8 = types.InlineKeyboardButton('Другое', callback_data="N_Other1")
noteCategory1Keyboard.add(noteCategory1Key1, noteCategory1Key2, noteCategory1Key3, noteCategory1Key4, noteCategory1Key5,
                          noteCategory1Key6, noteCategory1Key7, noteCategory1Key8)

# подкатегории статьи и видео совпадают, в принципе

"""         
articleCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
articleCategoryKey1 = types.InlineKeyboardButton('Развлекательное', callback_data="V_Entertainment")
articleCategoryKey2 = types.InlineKeyboardButton('Интересное', callback_data="V_Interesting")
articleCategoryKey3 = types.InlineKeyboardButton('Избранное', callback_data="V_Favorite")
articleCategoryKey4 = types.InlineKeyboardButton('Обучение', callback_data="V_Training")
articleCategoryKey5 = types.InlineKeyboardButton('Университет', callback_data="V_University")
articleCategoryKey6 = types.InlineKeyboardButton('Програмирование', callback_data="V_Programming")
articleCategoryKey7 = types.InlineKeyboardButton('Здоровье', callback_data="V_Health")
articleCategoryKey8 = types.InlineKeyboardButton('Английский язык', callback_data="V_English")
articleCategoryKey9 = types.InlineKeyboardButton('Другое', callback_data="V_Other")
articleCategoryKey10 = types.InlineKeyboardButton('Несортированное', callback_data="V_Unsorted")
articleCategoryKeyboard.add(articleCategoryKey1, articleCategoryKey2, articleCategoryKey3, articleCategoryKey4,
                            articleCategoryKey5, articleCategoryKey6, articleCategoryKey7, articleCategoryKey8)
"""
documentCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
documentCategoryKey1 = types.InlineKeyboardButton('Университет', callback_data="D_University")
documentCategoryKey2 = types.InlineKeyboardButton('Лабораторные', callback_data="D_Labs")
documentCategoryKey3 = types.InlineKeyboardButton('Лекции', callback_data="D_Lectures")
documentCategoryKey4 = types.InlineKeyboardButton('Книги', callback_data="D_Books")
documentCategoryKey5 = types.InlineKeyboardButton('Даташит', callback_data="D_Datasheets")
documentCategoryKey6 = types.InlineKeyboardButton('Интересное', callback_data="D_Interesting")
documentCategoryKey7 = types.InlineKeyboardButton('Другое', callback_data="D_Other")
documentCategoryKey8 = types.InlineKeyboardButton('Несортированное', callback_data="D_Unsorted")
documentCategoryKeyboard.add(documentCategoryKey1, documentCategoryKey2, documentCategoryKey3, documentCategoryKey4,
                             documentCategoryKey5, documentCategoryKey6, documentCategoryKey7, documentCategoryKey8)

spreadsheetsCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
spreadsheetsCategoryKey1 = types.InlineKeyboardButton('Университет', callback_data="S_University")
spreadsheetsCategoryKey2 = types.InlineKeyboardButton('Лабораторные', callback_data="S_Labs")
spreadsheetsCategoryKey3 = types.InlineKeyboardButton('Списки', callback_data="S_Lists")
spreadsheetsCategoryKey4 = types.InlineKeyboardButton('Другое', callback_data="S_Other")
spreadsheetsCategoryKey5 = types.InlineKeyboardButton('Несортированное', callback_data="S_Unsorted")
spreadsheetsCategoryKeyboard.add(spreadsheetsCategoryKey1, spreadsheetsCategoryKey2, spreadsheetsCategoryKey3,
                                 spreadsheetsCategoryKey4, spreadsheetsCategoryKey5)

cloudDriveCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
cloudDriveCategoryKey1 = types.InlineKeyboardButton('Университет', callback_data="CD_University")
cloudDriveCategoryKey2 = types.InlineKeyboardButton('Проекты', callback_data="CD_Project_RED(xe-xe)")
cloudDriveCategoryKey3 = types.InlineKeyboardButton('Документы', callback_data="CD_Documents")
cloudDriveCategoryKey4 = types.InlineKeyboardButton('Файлы', callback_data="CD_Files")
cloudDriveCategoryKey5 = types.InlineKeyboardButton('Фотографии', callback_data="CD_Photo")
cloudDriveCategoryKey6 = types.InlineKeyboardButton('Другое', callback_data="CD_Other")
cloudDriveCategoryKey7 = types.InlineKeyboardButton('Несортированное', callback_data="CD_Unsorted")
cloudDriveCategoryKeyboard.add(cloudDriveCategoryKey1, cloudDriveCategoryKey2, cloudDriveCategoryKey3,
                               cloudDriveCategoryKey4, cloudDriveCategoryKey5, cloudDriveCategoryKey6,
                               cloudDriveCategoryKey7)

githubCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
githubCategoryKey1 = types.InlineKeyboardButton('Репозиторий', callback_data="GH_Repository")
githubCategoryKey2 = types.InlineKeyboardButton('Проект', callback_data="GH_Project")
githubCategoryKey3 = types.InlineKeyboardButton('Документация', callback_data="GH_Documentation")
githubCategoryKey4 = types.InlineKeyboardButton('Интересное', callback_data="GH_Interesting")
githubCategoryKey5 = types.InlineKeyboardButton('Другое', callback_data="GH_Other")
githubCategoryKey6 = types.InlineKeyboardButton('Несортированное', callback_data="GH_Unsorted")
githubCategoryKeyboard.add(githubCategoryKey1, githubCategoryKey2, githubCategoryKey3, githubCategoryKey4,
                           githubCategoryKey5, githubCategoryKey6)

websiteCategoryKeyboard = types.InlineKeyboardMarkup(row_width=2)
websiteCategoryKey1 = types.InlineKeyboardButton('Обучение', callback_data="WS_Training")
websiteCategoryKey2 = types.InlineKeyboardButton('Интересное', callback_data="WS_Interesting")
websiteCategoryKey3 = types.InlineKeyboardButton('Избранное', callback_data="WS_Favorite")
websiteCategoryKey4 = types.InlineKeyboardButton('Программирование', callback_data="WS_Programming")
websiteCategoryKey5 = types.InlineKeyboardButton('Игры', callback_data="WS_Games")
websiteCategoryKey6 = types.InlineKeyboardButton('Блог', callback_data="WS_Blog")
websiteCategoryKey7 = types.InlineKeyboardButton('Другое', callback_data="WS_Other")
websiteCategoryKey8 = types.InlineKeyboardButton('Несортированное', callback_data="WS_Unsorted")
websiteCategoryKeyboard.add(websiteCategoryKey1, websiteCategoryKey2, websiteCategoryKey3, websiteCategoryKey4,
                            websiteCategoryKey5, websiteCategoryKey6, websiteCategoryKey7, websiteCategoryKey8)

videoDict = {"V_Entertainment": 'Развлекательное', "V_Interesting": 'Интересное', "V_Favorite": 'Избранное',
             "V_Informative": 'Познавательное', "V_Training": 'Обучение', "V_University": 'Университет',
             "V_Programming": "Програмирование", "V_Games": 'Игры', "V_Health": 'Здоровье',
             "V_English": 'Английский язык', "V_News": 'Новости', "V_Other": 'Другое', "V_Unsorted": 'Несортированное'}

changeType2Dict = {"Video": 'Видео', "Article": 'Статья', "Document": 'Документ', "Spreadsheet": 'Таблица',
                   "CloudDrive": 'Облако', "Github": 'Github', "Website": 'Сайт', "Product": 'Товар',
                   "Other": 'Другое'}

documentDict = {"D_University": 'Университет', "D_Labs": 'Лабораторные', "D_Lectures": 'Лекции',
                "D_Books": 'Книги', "D_Datasheets": 'Даташит', "D_Interesting": 'Интересное',
                "D_Other": 'Другое', "D_Unsorted": 'Несортированное'}

spreadsheetDict = {"S_University": 'Университет', "S_Labs": 'Лабораторные', "S_Lists": 'Списки',
                   "S_Other": 'Другое', "S_Unsorted": 'Несортированное'}

cloudDriveDict = {"CD_University": 'Университет', "CD_Project_RED(xe-xe)": 'Проекты', "CD_Documents": 'Документы',
                  "CD_Files": 'Файлы', "CD_Photo": 'Фотографии', "CD_Other": 'Другое',
                  "CD_Unsorted": "Несортированное"}

githubDict = {"GH_Repository": 'Репозиторий', "GH_Project": 'Проект', "GH_Documentation": 'Документация',
              "GH_Interesting": 'Интересное', "GH_Other": 'Другое', "GH_Unsorted": 'Несортированное'}

noteDict = {"N_Films": 'Фильмы', "N_Music": 'Музыка', "N_Games": 'Игры', "N_Presents": 'Идеи для подарков',
            "N_Passwords": 'Пароли', "N_Important": 'Важная информация', "N_Remember": 'Не забыть', "N_Other": 'Другое'}

websiteDict = {"WS_Training": 'Обучение', "WS_Interesting": 'Интересное', "WS_Favorite": 'Избранное',
               "WS_Programming": 'Программирование', "WS_Games": 'Игры', "WS_Blog": 'Блог',
               "WS_Other": "Другое", "WS_Unsorted": 'Несортированное'}

associativeDict = {"Video": '1', "Article": '2', "Document": '3', "Spreadsheet": '4',
                   "CloudDrive": '5', "Github": '6', "Website": '7', "Product": '8',
                   "Other": '9'}

associativeDictnum = {"Video": 1, "Article": 2, "Document": 3, "Spreadsheet": 4,
                      "CloudDrive": 5, "Github": 6, "Website": 7, "Product": 8,
                      "Other": 9}

mirroredRAssociativeDict = {"1": 'Видео', "2": 'Статья', "3": 'Документ', "4": 'Таблица',
                            "5": 'Облако', "6": 'Github', "7": 'Сайт', "8": 'Товар',
                            "9": 'Другое'}

mirroredAssociativeDict = {"1": videoDict, "2": videoDict, "3": documentDict, "4": spreadsheetDict,
                           "5": cloudDriveDict, "6": githubDict, "7": websiteDict, "8": 'Product',
                           "9": 'Other'}

noteAssociativeDict = {"N_Films": '1', "N_Music": '2', "N_Games": '3', "N_Presents": '4',
                       "N_Passwords": '5', "N_Important": '6', "N_Remember": '7', "N_Other": '8'}

noteAssociativeDict1 = {"N_Films1": '1', "N_Music1": '2', "N_Games1": '3', "N_Presents1": '4',
                       "N_Passwords1": '5', "N_Important1": '6', "N_Remember1": '7', "N_Other1": '8'}

mirroredNoteAssociativeDict = {"1": 'Фильмы', "2": 'Музыка', "3": 'Игры', "4": 'Идеи для подарков',
                               "5": 'Пароли', "6": 'Важная информация', "7": 'Не забыть', "8": 'Другое'}

changeKeyboardsDict = {"Video": videoCategoryKeyboard, "Article": videoCategoryKeyboard,
                       "Document": documentCategoryKeyboard, "Spreadsheet": spreadsheetsCategoryKeyboard,
                       "CloudDrive": cloudDriveCategoryKeyboard, "Github": githubCategoryKeyboard,
                       "Website": websiteCategoryKeyboard}

unsortedDict = {"Video": 'V_Unsorted', "Article": 'V_Unsorted', "Document": 'D_Unsorted', "Spreadsheet": 'S_Unsorted',
                "CloudDrive": 'CD_Unsorted', "Github": 'GH_Unsorted', "Website": 'WS_Unsorted', "Product": 'V_Unsorted',
                "Other": 'V_Unsorted'}

# О да, это словарь со словарями вы меня правильно поняли, все для того, чтобы сделать легко расширяемый код,
# без дублирований, но блина, Я пока все это наладил, столько времени прошло, похер на эти 200+лишних строк кода в мэйне

dictionaryDict = {"Video": videoDict, "Article": videoDict, "Document": documentDict, "Spreadsheet": spreadsheetDict,
                  "CloudDrive": cloudDriveDict, "Github": githubDict, "Website": websiteDict}
