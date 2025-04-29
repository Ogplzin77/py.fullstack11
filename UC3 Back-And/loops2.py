# Exemplo básico
contador = 0 # Variável de controle
while contador < 5: # Condição de parada
    print(contador) # Bloco de instruções
    contador += 1 # Incremento

# Loop com break e continue
while True: # Loop infinito
    resposta = input("Digite 'sair' para terminar: ") # Entrada de dados
    if resposta.lower() == 'sair': # Condição de parada lower() converte para minúsculo
        break # Encerra o loop
    elif resposta == '': # Condição de parada vazia
        continue # Continua o loop
    print(f"Você digitou: {resposta}") # Bloco de instruções f para formatar strings

# Exemplo: Adivinhe o número
import random # Importa a biblioteca random
numero_secreto = random.randint(1, 100) # Gera um número aleatório
tentativas = 0 # Variável de controle

while True: # Loop infinito
    tentativa = int(input("Adivinhe o número (1-100): ")) # Entrada de dados
    tentativas += 1 # Incremento
    
    if tentativa < numero_secreto: # Condição de parada < menor que 
        print("Muito baixo!") # Bloco de instruções 
    elif tentativa > numero_secreto: # Condição de parada > maior que
        print("Muito alto!") # Bloco de instruções
    else: # Condição de parada
        print(f"Parabéns! Você acertou em {tentativas} tentativas.") # Bloco de instruções
        break # Encerra o loop