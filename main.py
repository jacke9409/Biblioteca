# <!-- main.py(logica do codigo e menu) -->
import sqlite3 
# Conectar ao banco biblioteca.db.
import sqlite3

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
     