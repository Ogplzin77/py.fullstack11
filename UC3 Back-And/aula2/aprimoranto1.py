                ###### aulas dia 25 de março de 2015 #####


###### calculo média de notas
#Cálculo de Média de Notas: Peça ao usuário que insira 8 notas (de 0 a 10). 
# Calcule a média das notas e exiba o resultado. 
# Se a média for maior ou igual a 6, exiba "Aprovado". Caso contrário, exiba "Reprovado".
notas = []

for i in range(8): # O programa solicita oito notas ao usuário, que devem estar no intervalo de 0 a 10.
    nota = float(input(f"Digite a {i+1}ª nota (0 a 10): ")) # O programa solicita oito notas ao usuário, que devem estar no intervalo de 0 a 10.
    while nota < 0 or nota > 10: # O programa verifica se a nota inserida pelo usuário está dentro do intervalo de 0 a 10.
        print("Nota inválida! Digite uma nota entre 0 e 10.") # O programa informa ao usuário que a nota inserida é inválida.
        nota = float(input(f"Digite a {i+1}ª nota novamente: ")) # O programa solicita uma nova nota ao usuário.
    notas.append(nota) #As notas inseridas são convertidas para float, em seguida somadas e divididas por 8 para obter a média.
    
media = sum(notas) / len(notas) #A soma das notas é feita usando a função sum() e a divisão pela quantidade de notas usando a função len().
print(f"\nMédia: {media:.2f}") # O programa imprime a média com duas casas decimais, usando a formatação {media:.2f}.

if media >= 6:
    print("Aprovado")   
else:
    print("Reprovado")
