######################################################
     #Cálculo de Frete com Base no Peso Declare uma variável peso com o peso de um pacote em kg.
     #alcule o frete com base nas seguintes regras:
def calcular_frete(peso):
    """Calcula o valor do frete com base no peso informado."""
    if peso <= 15:
        return 10
    elif peso <= 40:
        return 20
    else:
        return 30

def solicitar_peso():
    """Solicita um peso válido ao usuário."""
    while True:
        try:
            peso = float(input("Informe o peso da encomenda (em kg): "))
            if peso >= 0:
                return peso
            else:
                print(" O peso não pode ser negativo. Tente novamente.")
        except ValueError:
            print(" Entrada inválida! Digite um número válido para o peso.")

def main():
    print("=== CÁLCULO DE FRETE ===")
    peso = solicitar_peso()
    frete = calcular_frete(peso)
    print(f"\nPeso informado: {peso:.2f} kg")
    print(f" Valor do frete: R$ {frete:.2f}")

# Executa o programa
if __name__ == "__main__":
    main()
