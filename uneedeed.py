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