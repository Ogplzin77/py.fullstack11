def verificar_palindromo(): #função para verificar palíndromo
    texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "") #remove espaços e converte para minúsculas
    if texto == texto[::-1]: # verifica se a string formatada é igual à sua versão invertida
        print("É um palíndromo!") #Se a string formatada for igual à sua versão invertida, significa que a entrada é um palíndromo
    else:
        print("Não é um palíndromo.") #Caso contrário, o programa imprime "Não é palíndromo."

verificar_palindromo() #chama a função