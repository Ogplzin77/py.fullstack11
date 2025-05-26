import random
def jogo_da_forca():
    Frutas = ["banana", "abacaxi", "morango", "uva", "laranja", "melancia", "manga", "pera", "kiwi", "coco"]
    Animais=["elefante", "cachorro", "gato", "tigre", "jacaré", "leão", "pato", "papagaio", "coelho", "rinoceronte"]
    Países=["brasil", "argentina", "portugal", "japão", "canadá", "frança", "itália", "alemanha", "espanha", "méxico"]
    Objetos=["cadeira", "mesa", "relógio", "telefone", "lápis", "caneta", "carro", "bicicleta", "fogão", "espelho"]
    Profissões=["engenheiro", "médico", "professor", "advogado", "artista", "cozinheiro", "piloto", "jornalista", "bombeiro", "cientista"]

    listas=[Frutas, Animais, Países, Objetos, Profissões]
    lista_escolhida=random.choice(listas)
    palavra_secreta=random.choice(lista_escolhida)
    letras_corretas=set()
    tentativas=6
    while tentativas > 0:
        #exibe dica pra palavra secreta
        #categorias = ["Frutas", "Animais", "Países", "Objetos", "Profissões"]
        indice_lista = listas.index(lista_escolhida)
        print(f"A dica é: {lista_escolhida}")

        
        #exibe a palavra com os caracteres descobertos.
        palavra_exibida = " ".join(letra if letra in letras_corretas else "_" for letra in palavra_secreta)
      
        if palavra_exibida == palavra_secreta:
            print("parabéns! você venceu!")
            return
        #tentativa pra palavra ser completada
        resposta = input("Digite a palavra inteira ou pressione Enter para tentar adivinhar uma letra: ").strip().lower()
        if resposta:
            if resposta == palavra_secreta:
                print("Parabéns! Você acertou a palavra!")
                return
            else:
                print("Que pena! você errou a palavra!")
                return
        #entrada de usuário, garantinho que ele só possa digitar uma unica letra
        letra = input("digite uma letra:").strip().lower()
        if not letra.isalpha() or len(letra) !=1:
            print("por favor, digite apenas uma letra válida.")
            continue
        #verifica se a letra estar correta
        if letra in palavra_secreta:
            letras_corretas.add(letra)
            print("letra correta!")
        else:
            tentativas -= 1
            print(f"letra incorreta! tentativas restantes: {tentativas}")
    print(f"GAME OVER! A palavra era:{palavra_secreta}")
            
    jogo_da_forca()

    #print("lista sorteada:",palavra_secreta)
