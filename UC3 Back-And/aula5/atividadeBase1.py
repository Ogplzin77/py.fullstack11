# Atividade Prática: Sistema de uma Biblioteca
'''
Contexto:
Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

Requisitos:
- O sistema deve permitir o cadastro de livros, usuários e empréstimos.
- O sistema deve permitir a consulta de livros cadastrados.
- O sistema deve permitir a consulta de usuários cadastrados.
'''

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.

class Livro:
    def __init__(self, titulo, autor, ano,): #Método construtor __init__ para inicializar o livro com título, autor e ano.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self): #Método especial __str__ para representação legível para humanos. 
        return f"{self.titulo} por {self.autor} ({self.ano})" #Retorna uma string formatada com o título, autor e ano do livro.


class Usuario:
    def __init__(self, nome, identificador): #Método construtor __init__ para inicializar o usuário com nome e identificador.
        self.nome = nome #Atributo da classe Usuario que representa o nome do usuário. 
        self.identificador = identificador

    def __str__(self):
        return f"{self.nome} (ID: {self.identificador})"


class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao=None): 
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def __str__(self):
        status = f"Empréstimo ativo" if not self.data_devolucao else f"Devolvido em {self.data_devolucao}"
        return f"{self.livro} emprestado para {self.usuario} em {self.data_emprestimo}. {status}"


# Classe LivroDigital, herdando de Livro
class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, formato, download):
        super().__init__(titulo, autor, ano)
        self.formato = formato
        self.link_download = download

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano}) - Formato: {self.formato} - Download: {self.link_download}"


# Testando o sistema
livro1 = Livro("1984", "flamengo", 1949)
usuario1 = Usuario("Pabllo", 101)
emprestimo1 = Emprestimo(livro1, usuario1, "07/05/2025")

livro_digital = LivroDigital("Python", "Autor Desconhecido", 2024, "PDF", "http://download_link.com")

print(livro1)
print(usuario1)
print(emprestimo1)
print(livro_digital)
