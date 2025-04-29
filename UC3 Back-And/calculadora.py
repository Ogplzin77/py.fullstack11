import math

def calculadora(): # Função principal
    operacoes = { # Dicionário de operações
        '+': lambda x, y: x + y, # Adição
        '-': lambda x, y: x - y, # Subtração 
        '*': lambda x, y: x * y, # Multiplicação 
        '/': lambda x, y: x / y, # Divisão
        '^': lambda x, y: x ** y, # Potência
        '√': lambda x: math.sqrt(x), # Raiz quadrada
        'sen': lambda x: math.sin(math.radians(x)), # Seno em radianos
        'cos': lambda x: math.cos(math.radians(x)), # Cosseno em radianos
        'tan': lambda x: math.tan(math.radians(x)) # Tangente em radianos
    }
    
    while True: # Loop infinito
        print("\nOperações disponíveis:") # Imprime as operações disponíveis
        print("+, -, *, /, ^ (potência), √ (raiz), sen, cos, tan") # Imprime as operações disponíveis
        print("Digite 'sair' para encerrar") # Imprime a opção de sair
        
        op = input("Operação: ") # Entrada de dados
        
        if op.lower() == 'sair': # Verifica se a opção de sair foi escolhida
            break # Encerra o loop
        
        if op in ['√', 'sen', 'cos', 'tan']: # Verifica se a opção de raiz, seno, cosseno ou tangente foi escolhida
            num = float(input("Número: ")) # Entrada de dados
            try: # Tenta executar o cálculo
                resultado = operacoes[op](num) # Executa o cálculo
                print(f"Resultado: {resultado:.4f}") # Imprime o resultado com quatro casas decimais
            except ValueError as e: # Trata o erro de entrada inválida
                print(f"Erro: {e}") # Imprime o erro
        elif op in operacoes: # Verifica se a opção de operação foi escolhida
            num1 = float(input("Primeiro número: ")) # Entrada de dados
            num2 = float(input("Segundo número: ")) # Entrada de dados
            try: # Tenta executar o cálculo
                resultado = operacoes[op](num1, num2) # Executa o cálculo
                print(f"Resultado: {resultado:.4f}") # Imprime o resultado com quatro casas decimais
            except ZeroDivisionError: # Trata o erro de divisão por zero
                print("Erro: Divisão por zero!") # Imprime o erro
            except Exception as e: # Trata outros erros
                print(f"Erro: {e}") # Imprime o erro
        else: # Caso contrário
            print("Operação inválida!") # Imprime a mensagem de erro

calculadora() # Chama a função principal