
# Criando e escrevendo em um arquivo
with open('usuarios.txt', 'w') as dados: #w = write escrita r = read leitura a = append adicionar 
    dados.write("Nome: Pabllo\nEmail: pabllo@email\n")  # \n = quebra de linha 
    dados.write("Nome: Maria\nEmail: maria@email\n") 
    dados.write("Nome: Pedro\nEmail: pedro@email\n")
    dados.write("Nome: Ana\nEmail: ana@email\n")

# Lendo o arquivo dados
with open('usuarios.txt' ,'r') as dados:
    conteudo = dados.read()
    print(conteudo)

# Adicionando mais dados (append)
with open('usuarios.txt', 'a') as dados:
    dados.write ("/nome:pabllo\nE-mail:pabllo@email.com\nSenha:27112001")

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








