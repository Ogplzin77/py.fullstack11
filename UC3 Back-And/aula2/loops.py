# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja", "uva"] # lista de frutas
for fruta in frutas: # percorrendo a lista de frutas
    print(fruta.upper()) # imprimindo em maiúsculo

# Com enumerate para índice e valor
for indice, fruta in enumerate(frutas, start=1): # percorrendo a lista de frutas
    print(f"{indice}. {fruta}") # imprimindo em maiúsculo

# Range
for i in range(5):  # 0 a 4
    print(i) 

for i in range(1, 11, 2):  # 1, 3, 5, 7, 9
    print(i)

# "List comprehension"
quadrados = [x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]