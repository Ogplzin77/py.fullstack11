#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:
'''
Adicionar novos colaboradores.
Buscar colaborador por ID.
Listar colaboradores com salário acima de X.
'''
#Implemente utilizando funções.

# Lista para armazenar os colaboradores
colaboradores = []  # Lista para armazenar os colaboradores em memória (antes de migrar para um banco de dados) e retornados no formato JSON 

# Função para adicionar um novo colaborador
def ad_colaborador(id, nome, salario): #def = definição da função 
    colaborador = {"id": id, "nome": nome, "salario": salario} #criando um dicionário para armazenar os colaboradores 
    colaboradores.append(colaborador) #adicionando o colaborador na lista 
    print(f"Colaborador {nome} adicionado com sucesso.")  #print para informar que o colaborador foi adicionado com sucesso 

# Função para buscar colaborador por ID
def buscar_por_id(id): # Função para buscar um colaborador pelo ID 
    for colaborador in colaboradores: # Para cada colaborador na lista de colaboradores for 
        if colaborador["id"] == id: # Se o ID do colaborador for igual ao ID procurado 
            return colaborador # Retorna o colaborador encontrado 
    return None # Se nenhum colaborador for encontrado, retorna None 

# Função para listar colaboradores com salário acima de um valor X
def listar_acima_salario(x): # Função para listar colaboradores com salário acima de um valor X 
    return [c for c in colaboradores if c["salario"] > x] # Retorna uma lista com os colaboradores com salário acima de X 

# Exemplo de uso
adicionar_colaborador(1, "Pabllo", 3500) # Adiciona um colaborador com ID 1, nome "Pabllo" e salário de 3500
adicionar_colaborador(2, "Renan", 4500)
adicionar_colaborador(3, "Lucas", 3000)

print("\nBuscar colaborador com ID 2:") # Busca um colaborador com ID 2 
print(buscar_por_id(2)) # Retorna o colaborador encontrado ou None se nenhum for encontrado 

print("\nColaboradores com salário acima de 3200:") 
print(listar_acima_salario(3200))
