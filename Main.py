from Cliente import Clientes
from Conta import Conta


nome = input('digite o nome do cliente: ')
telefone = input('digite o telefone do cliente: ') 
endereço =  input('digite o endereço do cliente: ')

numero = input('digite o numero da conta: ')

cliente = Clientes(nome, telefone, endereço)

titular = cliente

conta = Conta(titular, numero)


opcao = input('digite 1 para sacar, 2 para depositar, 3, para sair: ')

while opcao == '1' or '2':

    if opcao == '1':
        valor = input('quantos voce quer sacar?')
        conta.sacar(valor)
        print(f'o seu saldo agora é: {conta.get_saldo}')
        opcao = input('digite 1 para sacar, 2 para depositar, 3, para sair')
    
    elif opcao == '2':
        valor = input('quantos quer depositar? ')
        conta.depositar(valor)
        print(f'o seu saldo agora é: {conta.get_saldo}')
        opcao = input('digite 1 para sacar, 2 para depositar, 3, para sair')
    
    elif opcao == '3':
        print('voce saiu')
        break

    else:
        print('digite um valor valido')

