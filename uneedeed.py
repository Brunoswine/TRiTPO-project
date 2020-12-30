"""
"youtube.com/watch" in text or "vk.com/video" in text or "youtu.be" in text:
            TYPE2 = "Video"
            bot.send_message(message.chat.id, 'Данная ссылка определена как видео', reply_markup=rightKeyboard)
            isRunning = True

 if "youtube.com" in text and not "watch" in text:
            bot.send_message(message.chat.id, 'Это ссылка на youtube, зачем вам ее сохранять? Автор?')
        else:

                    elif call.data == "V_Entertainment":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Развлекательное",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Interesting":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Интересное",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Favorite":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Избранное",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Training":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Обучение",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Programming":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+"' c категорией Программирование",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_University":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Университет",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Unsorted":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Несортированное",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Other":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Другое",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_Health":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Здоровье",
                      reply_markup=None)
                      isRunning = False

                    elif call.data == "V_English":
                      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Данная ссылка определена как "+name+" c категорией Английский язык",
                      reply_markup=None)
                      isRunning = False
"""

"""
                        if TYPE2 == "Video" or TYPE2 == "Article":
                            if call.data in keyboard.videoDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.videoDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " +
                                                           temp_item, reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False

                        elif TYPE2 == "Document":
                            if call.data in keyboard.documentDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.documentDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " +
                                                           temp_item, reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False

                        elif TYPE2 == "Spreadsheet":
                            if call.data in keyboard.spreadsheetDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.spreadsheetDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " +
                                                           temp_item, reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False

                        elif TYPE2 == "CloudDrive":
                            if call.data in keyboard.cloudDriveDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.cloudDriveDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " +
                                                           temp_item, reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False

                        elif TYPE2 == "Github":
                            if call.data in keyboard.githubDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.githubDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " + temp_item,
                                                      reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False

                        elif TYPE2 == "Website":
                            if call.data in keyboard.websiteDict.keys():
                                temp_call_data = call.data
                                temp_item = keyboard.websiteDict.get(temp_call_data)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                      text="Данная ссылка сохранена как " + name + " c категорией " + temp_item,
                                                      reply_markup=None)
                                # save user_id_TEXT_TYPE1_TYPE2_temp_call_data_Description?
                                subcategoryRun = False
                                isRunning = False
                        """

# if call.data == "Ok_exists":
            #     exists = True
            #     ok = True
            #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                           text='Окей', reply_markup=None)
            # if call.data == "Redact":
            #     ok = True
            #     exists = False
            #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                           text='Редактировать ссылку...', reply_markup=None)
            #     bot.send_message(call.message.chat.id, text)

# bot.send_message(chat_id=call.message.chat.id,
#                  text=str(i) + '. Ссылка.\n Категория: ' + keyboard.mirroredRAssociativeDict.get(
#                      str(t_type2)) +
#                       "\nПодкатегория: " + needed__dict.get(t_subcategory) + "\n" + t_text)
# print(result)
# print(t_type2)
# print(needed__dict)
# print(t_subcategory)
# print(keyboard.mirroredRAssociativeDict.get(str(t_type2)))
# print(needed__dict.get(t_subcategory))


# if call.data == "N_Look_all":
            #     result = db.get_data(2)
            #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                           text="📝Заметки", reply_markup=None)
            #     bot.send_message(chat_id=call.message.chat.id,
            #                      text="result")
            #     i = 1
            #     for tuple_ in result:
            #         t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
            #         needed__dict = keyboard.mirroredAssociativeDict.get(
            #             str(t_type2))  # В кортеже хранится int для скорости, поэтому преобразовываем
            #         # videoDict                                         # 1=Video
            #         number = str(i)
            #         category = keyboard.mirroredRAssociativeDict.get(str(t_type2))
            #         t_subcategory_done = needed__dict.get(t_subcategory)
            #         texxxt = str(t_text)
            #         bot.send_message(chat_id=call.message.chat.id,
            #                          text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
            #                               f"Категория: {category}\nПодкатегория: {t_subcategory_done}",
            #                          parse_mode='html')
            #         i = i + 1
            #
            # elif call.data == "N_Look_Category":
            #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                           text="🌐Выбрерите категорию...", reply_markup=keyboard.ChangeTYPE2Keyboard)
            #
            # if call.data in keyboard.changeType2Dict.keys():
            #     L_allRun = True
            #
            # if L_allRun:
            #     if call.data in keyboard.changeType2Dict.keys():
            #         temp_call_data = call.data
            #         number = keyboard.associativeDictnum.get(temp_call_data)
            #         L_allRun = False
            #         result = db.get_data1(1, number)
            #         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                               text="🌐Категории", reply_markup=None)
            #         bot.send_message(chat_id=call.message.chat.id,
            #                          text="result")
            #         i = 1
            #         for tuple_ in result:
            #             t_text, t_user_id, t_type1, t_type2, t_subcategory = tuple_
            #             if not t_type2 == 8 and not t_type2 == 9:
            #                 needed__dict = keyboard.mirroredAssociativeDict.get(
            #                     str(t_type2))  # В кортеже хранится int для скорости, поэтому преобразовываем
            #                 # videoDict                                         # 1=Video
            #                 number = str(i)
            #                 category = keyboard.mirroredRAssociativeDict.get(str(t_type2))
            #                 t_subcategory_done = needed__dict.get(t_subcategory)
            #                 texxxt = str(t_text)
            #                 bot.send_message(chat_id=call.message.chat.id,
            #                                  text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
            #                                       f"Категория: {category}\nПодкатегория: {t_subcategory_done}",
            #                                  parse_mode='html')
            #                 i = i + 1
            #
            #             else:
            #                 bot.send_message(chat_id=call.message.chat.id,
            #                                  text=f"{number}. <a href='{t_text}'>{t_text}</a>\n"
            #                                       f"Категория: {category}",
            #                                  parse_mode='html')
            #                 i = i + 1
            #
            # if call.data == "N_Redact":
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