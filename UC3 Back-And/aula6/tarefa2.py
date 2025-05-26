# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''

from abc import ABC, abstractmethod # Importa as classes ABC e abstractmethod do módulo abc para trabalhar com classes abstratas. 

# Classe abstrata
class Animal(ABC): # Define a classe Animal como uma classe abstrata. 
    def __init__(self, nome):
        self.nome = nome

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    @abstractmethod # Define o método emitir_som como abstrato. 
    def emitir_som(self): 
        pass # Define o corpo do método emitir_som como vazio. 


# Classe Cachorro
class Cachorro(Animal): 
    def emitir_som(self):
        print(f"{self.nome} diz: Au au!")


    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabinho.")


# Classe Gato
class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

    def subir_em_moveis(self):
        print(f"{self.nome} subiu no móvel.")


dog = Cachorro("Taz Mania")
dog.dormir()
dog.emitir_som()
dog.abanar_rabo()

cat = Gato("Sophia")
cat.dormir()
cat.emitir_som()
cat.subir_em_moveis()

        
        
        
        
