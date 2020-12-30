import sqlite3


class SQLite:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # def add_data(self):
    # db = sqlite3.connect("data.db")
    # sql = db.cursor()

    def data_exists(self, text):
        """Проверяем, есть ли уже text в базе"""
        with self.connection:
            result = self.cursor.execute(
                "SELECT links_and_text FROM data_table WHERE links_and_text == ? ", (text,)).fetchall()
            return bool(len(result))

    def link_exists(self, text, intTYPE1):
        """Проверяем, есть ли уже text в базе"""
        with self.connection:
            result = self.cursor.execute(
                "SELECT links_and_text FROM data_table WHERE links_and_text == ? AND TYPE1== ?",
                (text, intTYPE1,)).fetchall()
            return bool(len(result))

    def get_data(self, intTYPE1):
        """Получаем все записи"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM data_table WHERE TYPE1== ?", (intTYPE1,)).fetchall()

    def get_data1(self, intTYPE1, intTYPE2):
        """Получаем все записи с категорией"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM data_table WHERE TYPE1== ? AND TYPE2== ?",
                                       (intTYPE1, intTYPE2,)).fetchall()

    def add_data(self, text, user_id, TYPE1, TYPE2, subcategory):
        """Добавляем данные"""
        with self.connection:
            self.cursor.execute("INSERT INTO data_table VALUES(?,?,?,?,?)",
                                (text, user_id, TYPE1, TYPE2, subcategory))
            # self.connection.commit()

    def clear(self, user_id,):
        """Удаляем данные"""
        with self.connection:
            self.cursor.execute("DELETE FROM data_table WHERE user_id = ?", (user_id,))

    def clear1(self, user_id, intTYPE1):
        """Удаляем данные"""
        with self.connection:
            self.cursor.execute("DELETE FROM data_table WHERE user_id = ? AND TYPE1 = ?", (user_id, intTYPE1,))







    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
