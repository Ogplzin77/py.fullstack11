#Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10). 
# Calcule a média das notas e exiba o resultado. 
# Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".

notas = []
for i in range(4): # O programa solicita quatro notas ao usuário, que devem estar no intervalo de 0 a 10.
    nota = float(input(f"Digite a {i+1}ª nota (0 a 10): ")) 
    while nota < 0 or nota > 10: 
        print("Nota inválida! Digite uma nota entre 0 e 10.") 
        nota = float(input(f"Digite a {i+1}ª nota novamente: "))
    notas.append(nota) #As notas inseridas são convertidas para float, em seguida somadas e divididas por 4 para obter a média.

media = sum(notas) / (notas)

print(f"\nMédia: {media:.2f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


#Soma dos Números Pares em um Intervalo: Peça ao usuário dois números, representando o início e o fim de um intervalo. 
# Use um loop (for ou while) para calcular a soma de todos os números pares nesse intervalo e exiba o resultado.

# adicione dois números ao usuário
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))  # o programa solicita dois números inteiros ao usuário, que representam o início e o fim do intervalo.

# Garante que o início seja menor que o fim
if inicio > fim:
    inicio, fim = fim, inicio #Se o primeiro número (inicio) for maior que o segundo (fim), os valores são trocados.

# Ajuste o início para o próximo número par
if inicio % 2 != 0:
    inicio += 1

# Calcula a soma dos números pares usando while
soma_pares = 0 # variável soma_pares e inicio com 0, onde será armazenada a soma dos números pares.
while inicio <= fim: # while percorre os números dentro do intervalo, mas somente os pares.
    soma_pares += inicio 
    inicio += 2  #Como inicio já é um número par, somamos ele a soma_pares e depois incrementamos 2 a inicio, para garantir que o próximo número a ser somado também seja par.

 # resultado
print(f"A soma dos números pares é: {soma_pares}")


# verificação de Palíndromo: Peça ao usuário uma palavra ou frase. 
# Verifique se a entrada é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente, ignorando espaços e maiúsculas/minúsculas).
#  Exiba "É palíndromo" ou "Não é palíndromo".

# solicite ao usuário que digite uma palavra ou frase.
texto= input("Digite uma palavra ou frase: ")

# Remove espaços e converte para minúsculas
texto_limpo = '.join(texto.lower().split())' #lower() converte todos os caracteres para minúsculas, garantindo que a verificação não seja sensível a maiúsculas e minúsculas.

# Verifica se é um palíndromo
if texto_limpo == texto_limpo[::-1]: # verifica se a string formatada é igual à sua versão invertida. O fatiamento [::-1] inverte a string.
    print("É palíndromo") #Se a string formatada for igual à sua versão invertida, significa que a entrada é um palíndromo, e o programa imprime "É palíndromo".

else:
    print("Não é palíndromo") #Caso contrário, o programa imprime "Não é palíndromo".


#Cálcule juros Simples: Peça ao usuário o valor principal (P), a taxa de juros anual (r) e o tempo em anos (t).
#  Calcule o montante final usando a fórmula de juros simples M=P×(1+r×t) e exiba o resultado.

# Solicita os valores ao usuário
#A fórmula de juros simples é:
#A fórmula de juros simples é:

P= float(input("Digite o valor principal (P): ")) #Valor principal (P): valor inicial do qual os juros serão calculados.
R= float(input("Digite a taxa de juros anual (r) em porcentagem: ")) / 100  # taxa de juros expressa em porcentagem. É importante dividir o valor da taxa por 100 para convertê-lo em um valor decimal.
T= float(input("Digite o tempo em anos (t): ")) # período de tempo (em anos) durante o qual os juros serão aplicados.

# Calcula o montante final
M = P * (1 + r * t) # (M) é o montante final (capital inicial + juros).  (P) é o valor principal. (R) é a taxa de juros anual, convertida para decimal. (T) é o tempo em anos.

# Exibe o resultado
print(f"O montante final após {t} anos será: R$ {M:.2f}") # O programa imprime o montante final (M) com duas casas decimais, usando a formatação {M:.2f}.


#Contagem de Dígitos: Peça ao usuário um número inteiro positivo.
#  Conte quantos dígitos esse número possui e exiba o resultado.

# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# O programa verifica se o número digitado é positivo. Se o número for menor ou igual a zero, ele exibe uma mensagem pedindo para digitar um número positivo.
if numero <= 0:
    print("Por favor, digite um número positivo.")
else:
    # O número é convertido para uma string usando str(numero). Isso permite que possamos contar o número de caracteres (dígitos) da string.
    num_digitos = len(str(numero))

    # Exibe o número de dígitos
    print(f"O número {numero} possui {num_digitos} dígitos.")
