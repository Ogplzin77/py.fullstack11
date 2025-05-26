def calcular_imc(): # Função para calcular o IMC
    peso = float(input("Digite seu peso (kg): ")) # Entrada de dados
    altura = float(input("Digite sua altura (m): ")) # Entrada de dados 
    
    imc = peso / (altura ** 2) # Fórmula do IMC
    
    print(f"Seu IMC é {imc:.2f}") # 2f para duas casas decimais 
    
    if imc < 18.5:
        print("Classificação: Magreza")
    elif imc < 25:
        print("Classificação: Normal")
    elif imc < 30:
        print("Classificação: gordinha")
    elif imc < 40:
        print("Classificação: gordona")
    else:
        print("Classificação: sobre gorda") 

calcular_imc() # Chamada da função