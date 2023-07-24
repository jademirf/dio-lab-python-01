menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def validate_saque(valor):
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES

    if valor > saldo:
            print("Você não possui saldo suficiente para o valor solicitado.")
    elif valor > limite: 
        print("Valor do saque ultrapassa o valor limite diário.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você já utilizou o limite diário de saques.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou, valor inválido")

while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: \n"))

        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Não foi possível concluir a operação, valor informado não é válido.")
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        print("\n---------------------------------------------")

        validate_saque(valor)

    elif opcao == "e":
        print("\n=================== EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("---------------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor escolha uma das opções disponíveis no menu.")