                                         #######atividade 14 / 03 / 2025 ##########

# 1. Contagem Regressiva com FOR:
# Peça ao usuário um número e faça uma contagem regressiva a partir dele até 0.
numero = int (input) ("digite um número")
for i in range ( numero, -1, -1): 
  print (i)

# 2. Soma de Números com WHILE:
# Peça ao usuário um número e some 
#todos os números de 1 até ele.
  
numero = int (input ("digite o número")) #transformar o int em numero inteiro 
soma = 0  # 0= valor neutro
i = i #(i) indicador 1 inicio da soma
while i <= numero: # (while= enquanto) <maior =igual (inicio do looping)
        
        soma += 1 #(soma + soma = ele mesmo)
        i +=i 
print ("soma", soma)

# 3. Tabuada com FOR:
# Peça ao usuário um número e mostre a tabuada dele de 1 a 10.
  
numero = int (input ("digite o número da tabuada")) 
for i in range ( 1,11):
 print (f"{numero} x {i} = {numero * i}")
