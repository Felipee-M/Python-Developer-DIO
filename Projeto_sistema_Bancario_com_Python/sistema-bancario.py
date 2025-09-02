def depositar(saldo, lista_depositos):
    valor_deposito = int(input("Informe o valor a ser depositado: "))
    if valor_deposito < 0:
        print("Valor de deposito inválido, por gentileza verificar o valor depositado.")
        reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
        while reescolha != "s" and reescolha != "n":
            print("Opção inválida, por favor digitar novamente a opção.")
            reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
            if reescolha == "n" or reescolha == "s":
                while reescolha == "s":
                    valor_deposito = int(input("Informe o valor a ser depositado: "))
                    if valor_deposito < 0:
                        print("Valor de deposito inválido, por gentileza verificar o valor depositado.")
                        reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
                        while reescolha != "s" and reescolha != "n":
                            print("Opção inválida, por favor digitar novamente a opção.")
                            reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
                    else:
                        print(f"Depósito de R$ {valor_deposito} realizado com sucesso.")
                        saldo += valor_deposito
                        lista_depositos.append(valor_deposito)
                        reescolha = "n"
    else:
        print(f"Depósito de R$ {valor_deposito} realizado com sucesso.")
        saldo += valor_deposito
        lista_depositos.append(valor_deposito)
    return saldo, lista_depositos

def sacar(saldo, limite, numero_saques, lista_saques, LIMITE_SAQUES):
    valor_saque = int(input("Informe o valor a ser sacado: "))
    if valor_saque <= saldo:
        if valor_saque > 0 and valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            print(f"Saque de R$ {valor_saque} realizado com sucesso.")
            lista_saques.append(valor_saque)
            saldo -= valor_saque
            numero_saques += 1
        elif valor_saque >= 0 and valor_saque <= limite and numero_saques >= LIMITE_SAQUES:
            print(f"O limite dos {LIMITE_SAQUES} saques diários foi atingidos.")
            print(saldo)
        elif valor_saque >= 0 and valor_saque > limite and numero_saques < LIMITE_SAQUES:
            print(f"Valor de saque excedeu o limite de R${limite} por saque, por gentileza verificar o valor sacado.")
        else:
            print("Valor de saque inválido, por gentileza verificar o valor sacado.")
            reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
            while reescolha != "s" and reescolha != "n":
                print("Opção inválida, por favor digitar novamente a opção.")
                reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
                if reescolha == "n" or reescolha == "s":
                    while reescolha == "s":
                        valor_saque = int(input("Informe o valor a ser sacado: "))
                        if valor_saque < 0:
                            print("Valor de deposito inválido, por gentileza verificar o valor sacado.")
                            reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
                            while reescolha != "s" and reescolha != "n":
                                print("Opção inválida, por favor digitar novamente a opção.")
                                reescolha = input("Deseja tentar novamente? [s] ou [n]: ")
                        elif valor_saque <= limite and numero_saques < LIMITE_SAQUES:
                            print(f"Saque de R$ {valor_saque} realizado com sucesso.")
                            saldo += valor_saque
                            lista_depositos.append(valor_saque)
                            reescolha = "n"
                        elif valor_saque > limite:
                            print(f"Valor de saque excedeu o limite de R${limite} por saque, por gentileza verificar o valor sacado.")
                        elif numero_saques >= LIMITE_SAQUES:
                            print(f"O limite dos {LIMITE_SAQUES} saques diários foi atingidos.")
    else:
        print("Saldo insuficiente para o saque.")
    return saldo, limite, numero_saques, lista_saques

menu = """
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_depositos = []
lista_saques = []

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, lista_depositos = depositar(saldo, lista_depositos)

    elif opcao == "2":
        saldo, limite, numero_saques, lista_saques = sacar(saldo, limite, numero_saques, lista_saques, LIMITE_SAQUES)
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not lista_depositos and not lista_saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in lista_depositos:
                temp_deposito = int(deposito)
                print(f"Depósito: R$ {temp_deposito:.2f}")
            for saque in lista_saques:
                temp_saque = int(saque)
                print(f"Saque: R$ {temp_saque:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "4":
        break

    else:
        print("Opção inválida, por favor digitar novamente a opção.")
    
