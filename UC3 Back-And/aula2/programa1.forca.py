import random
def jogo_da_forca(): # Função do jogo da forca
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"] # Lista de palavras para o jogo
    palavra_secreta = random.choice(palavras) # Escolhe uma palavra aleatória
    letras_corretas = set() # Conjunto para armazenar as letras corretas
    tentativas = 6 # Número de tentativas
    
    while tentativas > 0: # Loop principal do jogo
        # Mostra a palavra com letras adivinhadas
        palavra_exibida = "" # Variável para armazenar a palavra exibida
        for letra in palavra_secreta: # Loop para criar a palavra exibida
            if letra in letras_corretas: # Verifica se a letra foi adivinhada
                palavra_exibida += letra # Adiciona a letra a palavra exibida
            else: # Caso contrário
                palavra_exibida += "_" # Adiciona um tracinho na palavra exibida
        print(palavra_exibida) # Imprime a palavra exibida
        
        if palavra_exibida == palavra_secreta: # Verifica se todas as letras foram adivinhadas
            print("Parabéns! Você venceu!") # Imprime a mensagem de vitoria
            return # Encerra o jogo
        
        # Pede uma letra
        letra = input("Digite uma letra: ").lower() # Entrada de dados em minúsculo para evitar erros 
         
        if letra in letras_corretas: # Verifica se a letra foi adivinhada
            print("Você já tentou essa letra.") # Imprime a mensagem de erro
        elif letra in palavra_secreta: # Verifica se a letra esta na palavra
            letras_corretas.add(letra) # Adiciona a letra ao conjunto
            print("Letra correta!") # Imprime a mensagem de acerto
        else: # Caso contrário (letra incorreta) 
            tentativas -= 1 # Decrementa o número de tentativas 
            print(f"Letra incorreta! Tentativas restantes: {tentativas}") # Imprime a mensagem de erro
    
    print(f"Game over! A palavra era: {palavra_secreta}") # Imprime a mensagem de derrota e mostra a palavra secreta
 
jogo_da_forca() # Chama a função do jogo da forca 