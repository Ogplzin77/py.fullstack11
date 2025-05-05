import json # O módulo json que é usado para converter o dicionário de tarefas para uma representação em JSON (formato de texto estruturado, legível e usado em APIs/web).

# Dicionário de tarefas
tarefas = {
    1: {"titulo": "Estudar Python", "status": "pendente"}, # Dicionário de tarefas com duas tarefas
    2: {"titulo": "Fazer relatório", "status": "concluído"} 
}

# Conjunto de status válidos
status_validos = {"pendente", "em andamento", "concluído"} # Conjunto de status válidos para as tarefas (no exemplo, "pendente", "em andamento" e "concluído"). 

# Função para listar todas as tarefas em formato JSON
def listar_tarefas(): # Função para listar todas as tarefas em formato JSON 
    return json.dumps(tarefas, indent=4, ensure_ascii=False) #json.dumps: converte o dicionário Python em uma string JSON. indent=4: define o nível de indentação da string JSON. ensure_ascii=False: desativa a conversão de caracteres especiais para Unicode. 

# Função para adicionar uma nova tarefa
def adicionar_tarefa(id, titulo, status): # Função para adicionar uma nova tarefa com o ID, o título e o status da tarefa 
    if id in tarefas: # Verifica se o ID da tarefa ja existe no dicionário de tarefas 
        return f"Erro: Tarefa com ID {id} já existe." # Se o ID da tarefa ja existir, retorna uma mensagem de erro informando que a tarefa ja existe. 
    if status not in status_validos: # Verifica se o status da tarefa é valido 
        return f"Erro: Status inválido." # Se o status da tarefa nao for valido, retorna uma mensagem de erro informando que o status nao eh valido.
    tarefas[id] = {"titulo": titulo, "status": status} # Adiciona a nova tarefa ao dicionário de tarefas
    return f"{id} adicionada com sucesso." # Retorna uma mensagem de sucesso informando que a tarefa foi adicionada com sucesso

# Função para atualizar o status de uma tarefa
def atualizar_status(id, novo_status): # Função para atualizar o status de uma tarefa pelo ID da tarefa 
    if id not in tarefas: # Verifica se o ID da tarefa existe no dicionário de tarefas 
        return f"Erro: Tarefa com ID {id} não encontrada." # Se o ID da tarefa nao existir, retorna uma mensagem de erro informando que a tarefa nao foi encontrada.
    if novo_status not in status_validos: # Verifica se o novo status da tarefa é valido 
        return f"Erro: Status inválido." # Se o novo status da tarefa nao for valido, retorna uma mensagem de erro informando que o status não é válido.
    tarefas[id]["status"] = novo_status # Atualiza o status da tarefa no dicionário de tarefas 
    return f"Status da tarefa {id} atualizado para '{novo_status}'." # Retorna uma mensagem de sucesso informando que o status da tarefa foi atualizado

# Função para remover uma tarefa
def remover_tarefa(id): # Função para remover uma tarefa pelo ID da tarefa 
    if id not in tarefas: # if id not in tarefas verifica se o ID da tarefa nao existe no dicionário de tarefas
        return f"Erro: {id} não encontrada." # Se o ID da tarefa nao existir, retorna uma mensagem de erro informando que a tarefa nao foi encontrada
    del tarefas[id] # Remove a tarefa do dicionário de tarefas 
    return f" {id} removida com sucesso." # Retorna uma mensagem de sucesso informando que a tarefa foi removida 