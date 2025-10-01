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

#inserir um livro o banco de dados 
def cadastrar_livro(nomelivro, autor, ano):
    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano, disponivel) 
    VALUES (?, ?, ?, 'sim')
    """, (nomelivro, autor, ano) )
    conexao.commit()

    print("livro cadastrado com sucesso!")
    

#listagem de livros
def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    #exibir colunas
    for linha in livros:
        print(f"id: {linha[0]} | titulo: {linha[1]} | autor: {linha[2]} | ano: {linha[3]} | disponivel: {linha[4]}")
    conexao.close()


#atualização de disponibilidade
def atualizar_livros():
    id = int(input("digite o id do livro que deseja pegar: "))
    while True: 
        disponivel = input("Deixar disponivel ou não (sim ou não): ").lower()
        if disponivel == "sim" or disponivel == "não":
            break
        else:
            print("Digite apenas sim ou não para deixar disponivel.")
    cursor.execute("""
    UPDATE livros
    SET disponivel = ? 
    WHERE id = ?
    """, (disponivel,id)
    )
    conexao.commit()

#remoção de livros 
def remover_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id = int(input("digite o id do livro que queira remover: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        conexao.commit()
        print("livro removido com sucesso!")

    except Exception as ex:
        print("erro ao tentar remover!: ", ex)

    finally:
        conexao.close()

#menu

while True:
    print("1 - cadastrar livro")
    print("2 - listar livro")
    print("3 - atualizar disponibilidade")
    print("4 - remover livro")
    print("5 - sair")

    opcao = input("escolha uma opcão: ")
    
    if opcao == "1":
        nomelivro = input("digite o nome do livro que deseja inserir: ")
        autor = input("digite o nome do autor: ")
        ano = int(input("digite o ano em que o livro foi postado: "))
        cadastrar_livro(nomelivro, autor, ano)

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        atualizar_livros()

    elif opcao == "4":
        remover_livro()

    else:
        print("saindo")
        break



