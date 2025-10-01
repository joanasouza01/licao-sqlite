import sqlite3

#criar conexao com biblioteca.db
conexao = sqlite3.connect("biblioteca.db")

#serve p executar os comandos no sql
cursor = conexao.cursor()

#criando a tabela 
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,         
    titulo TEXT, 
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel CHAR(3)       
)

""")

print("Tabela criada com sucesso")