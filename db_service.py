import logging, psycopg2, os

DATABASE_URL = os.environ['DATABASE_URL']

class DbService:
    __instance = None
    __cursor = None
    __conn = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DbService, cls).__new__(cls)

        return cls.__instance

    def get_conn(self):
        return self.__conn

    def get_cursor(self):
        return self.__cursor

    def close(self):
        self.__cursor.close()
        self.__conn.close()

    def commit(self):
        self.__conn.commit()

    def db_connect(self):
        try:
            self.__conn = psycopg2.connect(DATABASE_URL)
            self.__cursor = self.__conn.cursor()

        except psycopg2.Error as e:
            logging.error(e)