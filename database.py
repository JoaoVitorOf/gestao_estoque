import sqlite3 # Importando o módulo sqlite3, que permite ao Python trabalhar com bancos de dados SQLite.

def get_connection(): # def = função no python que conecta ao banco.
    return sqlite3.connect("estoque.db") # Dentro dessa função ela cria e retorna uma conexão com o banco de dados chamado "estoque.db" 

def initialize_db(): # É uma função que cria a tabela no banco de dados se ela não existir.
    conn = get_connection()
    cursor = conn.cursor() # cria um cursor, que é um objeto usado para executar comandos SQL no banco.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit() #salva as alterações feitas no banco.
    conn.close() #fecha a conexão com o banco, liberando recursos.