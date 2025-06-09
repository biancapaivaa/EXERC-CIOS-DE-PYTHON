def criar_conta(nome, conta_numero, saldo, limite):
    conta = {"nome": nome, "c/c": conta_numero, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta,valor):
    conta['saldo'] += valor
    print(f"Você depositou R${valor},00 e agora obtem R${conta['saldo']},00")
    return conta

def sacar(conta, valor):
    conta['saldo'] -= valor
    print(f"Você sacou R${valor},00 e ainda possui em saldo: R${conta['saldo']},00")
    return conta

def extrato(conta):
    print(f"Saldo atual: R${conta['saldo']},00")
    return conta

nome = input("Digite seu nome: ")
conta_numero = input("Digite sua conta: ")
saldo = int(input("Digite seu saldo: "))
limite = 1000

conta = criar_conta(nome, conta_numero, saldo, limite)

opcao = input("\nEscolha uma operação: \n1) Depositar\n2) Sacar\n3) Extrato\n:")

if opcao == "1":
    valor = int(input("Digite o valor d depósito: "))
    conta = depositar(conta,valor)
    
elif opcao == "2":
    valor = int(input("Digite o valor do saque: "))
    conta = sacar(conta, valor)
    
elif opcao == "3":
    conta = extrato(conta)
    
else:
    print("Opção inválida. Tente novamente.")
