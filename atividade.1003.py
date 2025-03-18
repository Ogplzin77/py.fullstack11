##################################
#Cálculo de Desconto em uma Loja Declare duas variáveis, preco e desconto, com valores 150.0 e 20, respectivamente. 
#Calcule o preço final após aplicar o desconto e imprima o resultado
preco=150.0 
desconto= 20
preco_final= preco - desconto
print(preco_final)
##################################

#Cálculo de IMC (Índice de Massa Corporal) Declare duas variáveis, peso e altura, com valores 70 e 1.75, respectivamente.
#Calcule o IMC usando a fórmula: IMC = peso / (altura ** 2). Imprima o resultado.
peso= 70
altura=1.75
imc_final= peso / (altura **2)
print(imc_final) 
###################################

#verificação de Elegibilidade para um Concurso Declare duas variáveis, idade e tem_experiencia, com valores 22 e True, respectivamente.
#Verifique se a pessoa é elegível para o concurso (idade maior ou igual a 18 e tem experiência) e imprima o resultado.

idade=22
tem_experiencia= True
if idade >=18 and tem_experiencia:
    print ('elegível para o concurso')
else:
    print('não elegível para o concurso')

    ####################################################
    #Classificação de Níveis de Acesso Declare uma variável nivel_acesso com um valor entre 1 e 3.
    # Use estruturas condicionais para imprimir:

nivel_acesso=1
if nivel_acesso == 3:
    print ('acesso total')
elif nivel_acesso == 2:
    print('acesso restrito')
else:
    print('acesso parcial')

#########################################################
    #Conversão de Temperatura Declare uma variável celsius com um valor de temperatura em graus Celsius.
    #Converta a temperatura para Fahrenheit usando a fórmula: F = (C * 9/5) + 32. Imprima o resultado
    
    celsius= int(input('digite a temperatura: '))
    F = (celsius*9/5) +32
    print ('temperatura de', + F)

##########################################################
#Verificação de Números Pares e Ímpares Declare uma variável numero com um valor inteiro.
#Use estruturas condicionais para verificar se o número é par ou ímpar e imprima o resultado.
    numero= -463654232
    if numero % 3 == 0:
        print(f" o numero {numero} é par.")
    else:
     print(f"o numero){numero} é ímpar.:")

    ######################################################
     #Cálculo de Frete com Base no Peso Declare uma variável peso com o peso de um pacote em kg.
     #alcule o frete com base nas seguintes regras:
     peso=10 
     if peso <= 15:
         frete = 10
     elif peso<= 40:
         frete = 20
     else:
         frete =30
     print (f"valor do frete:')R$ {frete:2f}")