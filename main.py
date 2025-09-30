# <!-- main.py(logica do codigo e menu) -->
import sqlite3 
# Conectar ao banco biblioteca.db.
# import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()
# • Criar a tabela livros com os campos:
# Criar a tabela livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel TEXT NOT NULL CHECK(disponivel IN ('Sim', 'Não'))
)
''')

# Commit e fechamento da conexão
conn.commit()
conn.close()

print("Banco de dados e tabela 'livros' criados com sucesso.")

# o id → chave primária (INTEGER, autoincremento).
# o título → texto obrigatório.
# o autor → texto obrigatório.
# o ano → número inteiro.
# o disponível → texto (valores "Sim" ou "Não").
# segundo commit
# Etapa 2 – Função de Cadastro
def cadastrar_livro(titulo, autor, ano):
    conn = conectar()
    cursor = conn.cursor()
# função cadastrar_livro(titulo, autor, ano) que insere um
# livro na tabela.
    cursor.execute("""
     INSERT INTO LIVROS(titulo, autor, ano, disponível)
     VALUES  (?, ?, ?, ?)
     """, titulo, autor, ano, "Sim")
# • Todo livro novo deve ser cadastrado com
# disponivel = "Sim".

# Etapa 3 – Listagem de Livros
# <!-- • Criar uma função listar_livros() que mostre todos os -->
# <!-- livros cadastrados. -->
def listar_livro():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, titulo, autor, ano, disponível FROM livros")
    livros = cursor.fetchall() 
    # para recuperar todas as linhas restantes 
    print("Lista de livros cadastrados")

    print("{:<5} {:<30} {:<20} {:<6} {:<12}".format("ID", "Titulo", "Autor", "Ano", "Disponível"))
    print("-" * 50)
    
    for livro in livros:
        print("{:<5} {:<30} {:<20} {:<6} {:<12}".format(livro[0], livro[1], livro[2], livro[3], livro[4]))
        # • Exibir colunas: ID, Título, Autor, Ano, Disponibilidade.
        if __name__ == "__main__":
            criar_tabela()
            listar_livros()
# Etapa 4 – Atualização de Disponibilidade
def atualizar_disponibilidade(id_livro):
    try:
    
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        
        # Verificar a disponibilidade atual do livro
        cursor.execute("SELECT disponível FROM livros WHERE id = ?", (id_livro,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("Livro não encontrado.")
            return
        
        disponivel_atual = resultado[0]
        novo_status = "Não" if disponivel_atual == "Sim" else "Sim"
        
        # Atualizar o status de disponibilidade
        cursor.execute("UPDATE livros SET disponível = ? WHERE id = ?", (novo_status, id_livro))
        conn.commit()
        
        print(f"Disponibilidade do livro com ID {id_livro} atualizada para '{novo_status}'.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar disponibilidade: {e}")        
    finally:
        if conn:
            conn.close()
# terminado
# Etapa 5 – Remoção de Livros
def remover_livro (id_livro):
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        
        # Verificar se o livro existe
        cursor.execute("SELECT * FROM livros WHERE id = ?", (id_livro,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("Livro não encontrado.")
            return
        
        # Remover o livro
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conn.commit()
        
        print(f"Livro com ID {id_livro} removido com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao remover livro: {e}")
    finally:
        if conn:
            conn.close()
# Commit esperado: "Etapa 5 - Função de remoção de livros implementada"
# Etapa 6 – Menu Interativo
def menu():
    while True:
        print("\nMenu da Biblioteca")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Disponibilidade")
        print("4. Remover Livro")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            cadastrar_livro(titulo, autor, ano)
        elif escolha == '2':
            listar_livro()
        elif escolha == '3':
            id_livro = int(input("ID do livro para atualizar disponibilidade: "))
            atualizar_disponibilidade(id_livro)
        elif escolha == '4':
            id_livro = int(input("ID do livro para remover: "))
            remover_livro(id_livro)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
           
        menu()
        criar_tabela()
        listar_livros()
    
    