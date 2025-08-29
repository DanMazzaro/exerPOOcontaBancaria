class Clientes:
    def __init__(self, nome, fone, endereco):
        self.__nome = nome
        self.__telefone = fone
        self.__endereço = endereco

    
    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone
    
    def get_endereço(self):
        return self.__endereço
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_telefone(self, telefone):
        self.__nome = telefone
    
    def set_endereço(self, endereço):
        self.__nome = endereço
