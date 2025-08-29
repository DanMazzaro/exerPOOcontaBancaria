class Conta:
    def __init__(self, titular, numero, ):
        self.titular = titular
        self.numero = numero
        self.saldo = 0.0
        
    
    def get_titular(self):
        return self.titular
    
    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    def set_titular(self, titular):
        self.titular = titular

    def set_numero(self, numero):
        self.titular = numero
    
    def set_saldo(self, saldo):
        self.nome = saldo
    
    def set_numero(self, numero):
        self.nome = numero

    def depositar(self, saldo):
        if (saldo <0):
            print('saldo não suficiente')
        else:
            self.saldo = self.saldo + saldo
    
    def sacar(self, saldo):
        if (saldo > 0 and saldo <= self.saldo):
            self.saldo = self.saldo - saldo
        else:
            print('saque negado')
