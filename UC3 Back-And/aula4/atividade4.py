## crie um programa que :
''''''
# armazene uruarios (nome, e-mail,) em um arquivo.
# liste todos os usuarios.
#permita excluir um usuario.

def armazenar_users():
 with open('usuarios.txt', 'w') as arquivo:
    arquivo.write ("\n nome:Pabllo\nE-mail:pabllonunes010@gmail.com\nSenha:27112001")

def listar_users():
    with open('usuarios.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


with open('usuarios.txt', 'a') as arquivo:
    arquivo.write("\nNome: Pabllo\nE-mail: pabllonunes010@gmail.com\nSenha: 27112001")


import os 
if os.path.exists('usuarios.txt'):
    os.remove('usuarios.txt')

    print("Arquivo removido!")  
else:
    print("Arquivo não encontrado.")








# Criando e escrevendo em um arquivo
with open('usuarios.txt', 'w') as dados:
    dados.write("Nome: Joao\nEmail: joao@email\n")
    dados.write("Nome: Maria\nEmail: maria@email\n")
    dados.write("Nome: Pedro\nEmail: pedro@email\n")
    dados.write("Nome: Ana\nEmail: ana@email\n")

# Lendo o arquivo dados
with open('usuarios.txt' ,'r') as dados:
    conteudo = dados.read()
    print(conteudo)

# Adicionando mais dados (append)
with open('usuarios.txt', 'a') as dados:
    dados.write ("/nome:pabllo\nE-mail:pabllonunes010@gmail.com\nSenha:27112001")

# Excluindo o arquivo (importar o módulo 'os') #Sitema Operacional
import os 
if os.path.exists('usuarios.txt'):
    os.remove('usuarios.txt')
    print("Arquivo removido!")
else:
    print("Arquivo não encontrado.")

#Listar usuários
def listarUsuarios(nome_arquivo):
    '''Retorna o número de linhas de um arquivo.'''
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())








