# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''

class Conta:
    def __init__(self, saldo = 0): # saldo privado
        self._saldo =saldo  # usa o setter para validar

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Erro: saldo não pode ser negativo.")
        self._saldo = valor
            

conta1=Conta(1000)
print(conta1._saldo)

conta2=Conta(-100)
print(conta2._saldo)







