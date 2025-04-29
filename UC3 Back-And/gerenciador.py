def gerenciador_tarefas(): # Função do gerenciador de tarefas que permite adicionar, listar, marcar como concluída, remover e sair 
    tarefas = [] # Lista para armazenar as tarefas e seus status (concluídas ou não) 
    
    while True: # Loop principal do gerenciador de tarefas 
        print("\nGerenciador de Tarefas") # Imprime o cabeçalho do gerenciador de tarefas  
        print("1. Adicionar tarefa") # Imprime as opções do gerenciador de tarefas
        print("2. Listar tarefas") # Imprime as opções do gerenciador de tarefas
        print("3. Marcar como concluída") # Imprime as opções do gerenciador de tarefas
        print("4. Remover tarefa") # Imprime as opções do gerenciador de tarefas
        print("5. Sair") # Imprime as opções do gerenciador de tarefas
        
        opcao = input("Escolha uma opção: ") # Entrada de dados para a opção escolhida 
        
        if opcao == '1': # Verifica se a opção de adicionar tarefa foi escolhida 
            tarefa = input("Digite a nova tarefa: ") # Entrada de dados para a nova tarefa 
            tarefas.append({"tarefa": tarefa, "concluida": False}) # Adiciona a nova tarefa ao conjunto de tarefas 
            print("Tarefa adicionada!") # Imprime a mensagem de sucesso na adição da tarefa 
        
        elif opcao == '2': # Verifica se a opção de listar tarefas foi escolhida 
            if not tarefas: # Verifica se houve tarefas cadastradas 
                print("Nenhuma tarefa cadastrada.") # Imprime a mensagem de erro quando nenhuma tarefa foi cadastrada 
            else: # Caso contrário 
                print("\nLista de Tarefas:") # Imprime a lista de tarefas 
                for i, item in enumerate(tarefas, 1): # Loop para listar as tarefas com seus status (concluídas ou não) 
                    status = "✓" if item["concluida"] else " " # Verifica se a tarefa foi concluida ou nao 
                    print(f"{i}. [{status}] {item['tarefa']}") # Imprime a tarefa com seu status 
        
        elif opcao == '3': # Verifica se a opção de marcar tarefa como concluida foi escolhida 
            if not tarefas: # Verifica se houve tarefas cadastradas 
                print("Nenhuma tarefa para marcar.") # Imprime a mensagem de erro quando nenhuma tarefa foi cadastrada 
            else: # Caso contrário 
                try: # Try para lidar com erros de entrada de dados 
                    num = int(input("Número da tarefa concluída: ")) - 1 # Entrada de dados para o número da tarefa concluida 
                    if 0 <= num < len(tarefas): # Verifica se o número da tarefa concluida é valido 
                        tarefas[num]["concluida"] = True # Marca a tarefa como concluida 
                        print("Tarefa marcada como concluída!") # Imprime a mensagem de sucesso na marcar a tarefa como concluida
                    else: # Caso contrário 
                        print("Número inválido.") # Imprime a mensagem de erro quando o número da tarefa concluida é invalido 
                except ValueError: # Caso o número da tarefa concluida seja invalido 
                    print("Digite um número válido.") # Imprime a mensagem de erro quando o número da tarefa concluida é invalido
        
        elif opcao == '4': # Verifica se a opção de remover tarefa foi escolhida
            if not tarefas: # Verifica se houve tarefas cadastradas
                print("Nenhuma tarefa para remover.") # Imprime a mensagem de erro quando nenhuma tarefa foi cadastrada
            else: # Caso contrário
                try: # Try para lidar com erros de entrada de dados
                    num = int(input("Número da tarefa a remover: ")) - 1 # Entrada de dados para o número da tarefa a remover 
                    if 0 <= num < len(tarefas): # Verifica se o número da tarefa a remover é valido 
                        removida = tarefas.pop(num) # Remove a tarefa do conjunto de tarefas 
                        print(f"Tarefa '{removida['tarefa']}' removida.") # Imprime a mensagem de sucesso na remoção da tarefa
                    else: # Caso contrário
                        print("Número inválido.") # Imprime a mensagem de erro quando o número da tarefa a remover é invalido
                except ValueError: # Caso o número da tarefa a remover seja invalido
                    print("Digite um número válido.") # Imprime a mensagem de erro quando o número da tarefa a remover é invalido
        
        elif opcao == '5': # Verifica se a opção de sair foi escolhida
            print("Saindo do gerenciador...") # Imprime a mensagem de saída do gerenciador 
            break # Encerra o loop 
        
        else: # Caso contrário
            print("Opção inválida!") # Imprime a mensagem de erro quando a opção escolhida é invalida
 
gerenciador_tarefas() # Chama a função do gerenciador de tarefas