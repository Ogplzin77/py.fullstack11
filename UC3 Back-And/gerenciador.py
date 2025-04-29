from datetime import datetime # Importa a biblioteca datetime para trabalhar com datas e horas

def gerenciador_tarefas(): # Função para gerenciar tarefas
    tarefas = []  # Lista para armazenar as tarefas
    
    while True: # Loop infinito
        print("\nGerenciador de Tarefas") # Imprime o cabeçalho 
        print("1. Adicionar tarefa") # Imprime a opção de adicionar tarefa
        print("2. Listar tarefas") # Imprime a opção de listar tarefas
        print("3. Marcar como concluída") # Imprime a opção de marcar como concluída
        print("4. Editar tarefa") # Imprime a opção de editar tarefa
        print("5. Remover tarefa") # Imprime a opção de remover tarefa
        print("6. Encerrar sessão")  # Imprime a opção de encerrar sessão
        
        opcao = input("Escolha uma opção: ") # Entrada de dados
        
        if opcao == '1': # Verifica se a opção de adicionar tarefa foi escolhida
            tarefa = input("Digite a nova tarefa: ") # Entrada de dados
            prioridade = input("Prioridade (Alta, Média, Baixa): ").capitalize() # Entrada de dados
            data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M") # Formata a data e hora atual
            tarefas.append({ # Adiciona a nova tarefa na lista 
                "tarefa": tarefa, # Nome da tarefa
                "concluida": False, # Indica se a tarefa foi concluida
                "data": data_criacao, # Data de crianção
                "prioridade": prioridade # Prioridade da tarefa
            }) 
            print("Tarefa adicionada!")  # Imprime a mensagem de tarefa adicionada
        
        elif opcao == '2':  # Verifica se a opção de listar tarefas foi escolhida
            if not tarefas: # Verifica se a lista de tarefas esta vazia
                print("Nenhuma tarefa cadastrada.") # Imprime a mensagem de nenhuma tarefa cadastrada
            else: # Se a lista de tarefas nao estiver vazia 
                print("\nLista de Tarefas:")  # Imprime o cabeçalho da lista de tarefas 
                for i, item in enumerate(tarefas, 1): # Percorre a lista de tarefas e imprime cada tarefa com seus respectivos status, prioridade e data de crianção 
                    status = "✓" if item["concluida"] else " " # Define o status da tarefa como "✓" se ela foi concluida ou " " se nao
                    prioridade = item.get("prioridade", "Não definida") # Define a prioridade da tarefa como "Não definida" se ela nao tiver uma prioridade definida
                    print(f"{i}. [{status}] {item['tarefa']} (Criada em: {item['data']}, Prioridade: {prioridade})")  # Imprime a tarefa com seus respectivos status, prioridade e data de crianção
        
        elif opcao == '3':  # Verifica se a opção de marcar como concluida foi escolhida
            if not tarefas: # Verifica se a lista de tarefas esta vazia
                print("Nenhuma tarefa para marcar.") # Imprime a mensagem de nenhuma tarefa para marcar 
            else: # Se a lista de tarefas nao estiver vazia 
                try: # Verifica se a opção de marcar como concluida foi escolhida 
                    num = int(input("Número da tarefa concluída: ")) - 1 # Solicita ao usuario o número da tarefa que deseja marcar como concluida
                    if 0 <= num < len(tarefas): # Verifica se o número da tarefa eh valido (entre 0 e o tamanho da lista de tarefas) 
                        tarefas[num]["concluida"] = True # Marca a tarefa como concluida 
                        print("Tarefa marcada como concluída!") # Imprime a mensagem de tarefa marcada como concluida 
                    else:# Se o número da tarefa nao for valido 
                        print("Número inválido.") # Imprime a mensagem de numero invalido
                except ValueError: # Se a opção de marcar como concluida nao for escolhida 
                    print("Digite um número válido.") # Imprime a mensagem de digite um numero valido 

        elif opcao == '4': # Verifica se a opção de editar tarefa foi escolhida 
            if not tarefas: # Verifica se a lista de tarefas esta vazia 
                print("Nenhuma tarefa para editar.") # Imprime a mensagem de nenhuma tarefa para editar 
            else: # Se a lista de tarefas nao estiver vazia 
                try: # Verifica se a opção de editar tarefa foi escolhida 
                    num = int(input("Número da tarefa a editar: ")) - 1 # Solicita ao usuario o número da tarefa que deseja editar 
                    if 0 <= num < len(tarefas): # Verifica se o número da tarefa eh valido (entre 0 e o tamanho da lista de tarefas) 
                        nova_tarefa = input("Novo nome da tarefa (deixe vazio para manter): ") # Solicita ao usuario o novo nome da tarefa
                        nova_prioridade = input("Nova prioridade (Alta, Média, Baixa - deixe vazio para manter): ").capitalize() # Solicita ao usuario a nova prioridade da tarefa
                        if nova_tarefa: # Se o novo nome da tarefa for diferente de vazio 
                            tarefas[num]["tarefa"] = nova_tarefa # Atualiza o nome da tarefa na lista de tarefas 
                        if nova_prioridade: # Se a nova prioridade da tarefa for diferente de vazio 
                            tarefas[num]["prioridade"] = nova_prioridade # Atualiza a prioridade da tarefa na lista de tarefas
                        print("Tarefa atualizada!") # Imprime a mensagem de tarefa atualizada 
                    else: # Se o número da tarefa nao for valido
                        print("Número inválido.") # Imprime a mensagem de numero invalido 
                except ValueError: # Se a opção de editar tarefa nao for escolhida
                    print("Digite um número válido.") # Imprime a mensagem de digite um numero valido

        elif opcao == '5': # Verifica se a opção de remover tarefa foi escolhida
            if not tarefas: # Verifica se a lista de tarefas esta vazia
                print("Nenhuma tarefa para remover.") # Imprime a mensagem de nenhuma tarefa para remover
            else:  # Se a lista de tarefas nao estiver vazia 
                try:  # Verifica se a opção de remover tarefa foi escolhida 
                    num = int(input("Número da tarefa a remover: ")) - 1 # Solicita ao usuario o número da tarefa que deseja remover
                    if 0 <= num < len(tarefas): # Verifica se o número da tarefa eh valido (entre 0 e o tamanho da lista de tarefas) 
                        confirmacao = input(f"Tem certeza que deseja remover '{tarefas[num]['tarefa']}'? (sim/não): ").lower() # Solicita ao usuario a confirmação de remoção da tarefa
                        if confirmacao == 's': # Verifica se a confirmação de remoção da tarefa foi positiva
                            removida = tarefas.pop(num) # Remove a tarefa da lista de tarefas
                            print(f"Tarefa '{removida['tarefa']}' removida.") # Imprime a mensagem de tarefa removida
                        else: # Se a confirmação de remoção da tarefa nao for positiva 
                            print("Remoção cancelada.") # Imprime a mensagem de remoção cancelada 
                    else: # Se o número da tarefa nao for valido 
                        print("Número inválido.")  # Imprime a mensagem de numero invalido 
                except ValueError:  # Se a opção de remover tarefa nao for escolhida 
                    print("Digite um número válido.")  # Imprime a mensagem de digite um numero valido
        
        elif opcao == '6': # Verifica se a opção de sair do gerenciador foi escolhida 
            print("Saindo do gerenciador...") # Imprime a mensagem de saindo do gerenciador
            break # Encerra o loop do gerenciador
        
        else: # Se a opção nao for valida 
            print("Opção inválida!")  # Imprime a mensagem de opcao invalida
 
gerenciador_tarefas() # Chama a funcao de gerenciador de tarefas 
