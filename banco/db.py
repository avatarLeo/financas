import sqlite3

class Banco:

    def __init__(self) -> None:
            
        self.sql_drop_table = """DROP TABLE IF EXISTS usuario;
                            DROP TABLE IF EXISTS despesas;"""

        self.sql_create_usuario = """CREATE TABLE usuario (
                                    cpf text PRIMARY KEY,
                                    TEXT UNIQUE NOT NULL,
                                    senha TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    id_despesas INTEGER,
                                    FOREIGN KEY (id_despesas) REFERENCES despesas (id_despesas)
                                );"""


        self.sql_create_despesas = """CREATE TABLE despesas (
                                    id_despesas INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    data_dadespesa TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    valor INTEGER NOT NULL
                                );"""


        self.con = sqlite3.connect('./banco.db')
        self.cursor = self.con.cursor()


    def create_schema(self):
            self.cursor.executescript(self.sql_drop_table)
            self.con.commit()
            self.cursor.execute(self.sql_create_usuario)
            self.con.commit()
            self.cursor.execute(self.sql_create_despesas)

    def insert(self):
         sql = """INSERT INTO usuario()"""

         self.cursor()



