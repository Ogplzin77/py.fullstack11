#POO em Python:

#Conceitos Teóricos:

#Classes vs. Objetos:
''' 
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular  # Atributo
        self.saldo = saldo      # Atributo

conta1 = ContaBancaria("João")  # Objeto
'''
#Métodos:
'''
def depositar(self, valor):
    self.saldo += valor
    '''
#Herança:
'''
class ContaPoupanca(ContaBancaria):  # Herda de ContaBancaria
    def render_juros(self, taxa):
        self.saldo *= (1 + taxa)
        '''


class ContaBancaria: 
    """Classe que representa uma conta bancária genérica.
    
    Atributos:
        numero_conta (str): Número identificador da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo atual da conta (inicia em 0 por padrão).
    """
    
    def __init__(self, numero_conta, titular, saldo=0): #Método construtor __init__ para inicializar a conta com número, titular e saldo. 
        """Inicializa a conta com número, titular e saldo opcional."""
        self.numero_conta = numero_conta # Atributo da classe ContaBancaria que representa o número da conta. self representa a instância da classe ContaBancaria. 
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): # Método para depositar dinheiro na conta. 
        """Adiciona um valor ao saldo da conta.
        
        Args:
            valor (float): Valor a ser depositado (deve ser positivo).
        
        Returns:
            str: Mensagem de confirmação com novo saldo.
        """
        if valor > 0: # Verifica se o valor é maior que zero. 
            self.saldo += valor # Se for maior que zero, adiciona o valor ao saldo. 
            return f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}" # Retorna uma mensagem de confirmação com o novo saldo. 
        return "Valor inválido para depósito!" # Se o valor for menor ou igual a zero, retorna uma mensagem de erro. 
    
    def sacar(self, valor): # Método para sacar dinheiro da conta. 
        """Subtrai um valor do saldo, se houver fundos suficientes.
        
        Args:
            valor (float): Valor a ser sacado.
        
        Returns:
            str: Mensagem de confirmação ou erro.
        """
        if valor > 0 and self.saldo >= valor: # Verifica se o valor é maior que zero e se houver saldo suficiente. 
            self.saldo -= valor # Se for maior que zero e houver saldo suficiente, subtrai o valor do saldo.
            return f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}" # Retorna uma mensagem de confirmação com o novo saldo. 
        return "Saldo insuficiente ou valor inválido!" # Se o valor for menor ou igual a zero ou houver saldo insuficiente, retorna uma mensagem de erro. 

    def transferir(self, outra_conta, valor): # Método para transferir dinheiro de uma conta para outra. 
        """Transfere valor para outra conta, se houver saldo.
        
        Args:
            outra_conta (ContaBancaria): Objeto da conta destino.
            valor (float): Valor a transferir.
        
        Returns:
            str: Mensagem de confirmação ou erro.
        """
        if self.sacar(valor) != "Saldo insuficiente ou valor inválido!": # Chama o método sacar para verificar se houver saldo suficiente. 
            outra_conta.depositar(valor) # Se houver saldo suficiente, chama o método depositar na outra conta para transferir o dinheiro. 
            return f"Transferência de R${valor} para {outra_conta.titular} realizada." # Retorna uma mensagem de confirmação. 
        return "Transferência falhou!"
    
class ContaPoupanca(ContaBancaria): # Herda da classe ContaBancaria. 
    """Classe que representa uma conta poupança, herdando de ContaBancaria.
    
    Adiciona funcionalidade de render juros.
    """
    
    def render_juros(self, taxa): # Método para aplicar juros na conta.
        """Aumenta o saldo com base em uma taxa de juros.
        
        Args:
            taxa (float): Taxa de juros (ex: 0.05 para 5%).
        
        Returns:
            str: Mensagem com novo saldo.
        """
        if 0 < taxa < 1: # Verifica se a taxa é maior que zero e menor que um. 
            self.saldo *= (1 + taxa) # Se for maior que zero e menor que um, multiplica o saldo pelo valor da taxa. 
            return f"Juros de {taxa*100}% aplicados. Novo saldo: R${self.saldo}" # Retorna uma mensagem com o novo saldo. 
        return "Taxa de juros inválida!" # Se a taxa for menor que zero ou maior que um, retorna uma mensagem de erro. 
    
conta_poup = ContaPoupanca("789", "Maria", 1000) # Cria uma instância da classe ContaPoupanca. 
print(conta_poup.render_juros(0.1))  # Saída: "Juros de 10.0% aplicados. Novo saldo: R$1100.0"