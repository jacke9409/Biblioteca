<!-- projeto para gerenciar livros usando SQLite. -->
<!-- main.py(logica do codigo e menu) -->
<!-- app.py(interface com streamlit) -->
<!-- primeiro commit 

# o id → chave primária (INTEGER, autoincremento).
# o título → texto obrigatório.
# o autor → texto obrigatório.
# o ano → número inteiro.
# o disponível → texto (valores "Sim" ou "Não"). -->
<!-- segundo commit -->

<!-- Etapa 2 – Função de Cadastro -->

<!-- • Implementar no main.py uma função que permita
inserir livros no banco. -->
<!-- • função cadastrar_livro(titulo, autor, ano) que insere um
livro na tabela. -->
<!-- • Todo livro novo deve ser cadastrado com
disponivel = "Sim". -->

<!-- Etapa 3 – Listagem de Livros -->
<!-- • Criar uma função listar_livros() que mostre todos os -->
<!-- livros cadastrados. -->
<!-- • Exibir colunas: ID, Título, Autor, Ano, Disponibilidade. -->
<!-- Commit esperado: "Etapa 3 - Função Listagem de livros" -->

<!-- Etapa 4 – Atualização de Disponibilidade -->

<!-- • Criar função que altere o campo disponivel: -->
<!-- o Se estava "Sim", vira "Não". -->
<!-- o Se estava "Não", vira "Sim". -->
<!-- terminado -->

<!-- • Criar função remover_livro(id) que remova um livro -->
<!-- pelo ID. -->
<!-- Commit esperado: "Etapa 5 - Função de remoção de livros -->
<!-- implementada" -->

<!-- Etapa 6 – Menu Interativo no Console -->
<!-- • Implementar um menu de opções no main.py: -->
<!-- 1. Cadastrar livro -->
<!-- 2. Listar livros -->
<!-- 3. Atualizar disponibilidade -->
<!-- 4. Remover livro -->
<!-- 5. Sair -->

<!-- Cada opção deve chamar a função correspondente. -->
<!-- Commit esperado: "Etapa 6 - Menu interativo no console" -->

Este é um projeto simples em Python que utiliza SQLite para gerenciar um banco de dados de livros. O sistema permite cadastrar, listar, atualizar e remover livros, com um menu interativo para facilitar o uso.

Cadastrar novos livros

Listar todos os livros disponíveis

Atualizar o status de disponibilidade dos livros

Remover livros do sistema

A aplicação roda em modo console, com um menu interativo que facilita o uso. É ideal para fins didáticos e projetos iniciais de programação, especialmente para quem está aprendendo a trabalhar com bancos de dados relacionais em Python.
