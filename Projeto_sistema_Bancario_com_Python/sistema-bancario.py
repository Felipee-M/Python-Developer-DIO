def criar_usuario(lista_usuarios):
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o CPF (somente números): ")
    while cpf in lista_usuarios:
        print("Já existe usuário com esse CPF!")
        cpf = input("Informe o CPF (somente números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    print("\n=== Confirmação dos dados ===")
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"CPF: {cpf}")
    print(f"Endereço: {endereco}")

    confirmacao = input("Os dados estão corretos? [s] ou [n]: ")
    print("Por gentileza digite os dados novamente.")
    while confirmacao == "n":
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        while cpf in lista_usuarios:
            print("Já existe usuário com esse CPF!")
            cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        print("\n=== Confirmação dos dados ===")
        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {data_nascimento}")
        print(f"CPF: {cpf}")
        print(f"Endereço: {endereco}")

        confirmacao = input("Os dados estão corretos? [s] ou [n]: ")
    if confirmacao == "s":
        print("=== Usuário criado com sucesso! ===")
        return {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
    
    else:
        print("Opção inválida.")
        return None
    
def criar_conta_corrente(lista_usuarios,conta_corrente):
    cpf = input("Informe o CPF do usuário: ")
    if cpf in lista_usuarios:
        print("=== Conta criada com sucesso! ===")
        conta_corrente += 1
        print(f"=== Dados da conta ===\nTitular: {lista_usuarios[cpf]['nome']}\nCPF: {cpf}\nAgência: 0001\nConta Corrente: {conta_corrente}")
        return {
            "agencia": "0001",
            "conta": conta_corrente,
            "titular": lista_usuarios[cpf]['nome'],
            "cpf": cpf
        }, True
    else:
        print("Usuário não encontrado, por gentileza criar um usuário antes de criar uma conta.")
        return conta_corrente,None

def depositar(saldo, lista_depositos, /):
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

def sacar(*, saldo, limite, numero_saques, lista_saques, LIMITE_SAQUES):
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

def exibir_extrato(saldo, lista_depositos, lista_saques, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not lista_depositos and not lista_saques:
        extrato = "Não foram realizadas movimentações."
    else:
        for deposito in lista_depositos:
            temp_deposito = float(deposito)
            extrato += f"\nDepósito: R$ {temp_deposito:.2f}"
        for saque in lista_saques:
             temp_saque = float(saque)
             extrato = f"\nSaque: R$ {temp_saque:.2f}"
    extrato += f"\nSaldo: R$ {saldo:.2f}"
    print(extrato)
    print("=========================================")

menu = """
[1] - Criar usuário
[2] - Criar conta corrente
[3] - Depositar
[4] - Sacar
[5] - Extrato
[6] - Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_depositos = []
lista_saques = []
nome = ""
data_nascimento = ""
cpf = ""
endereco = ""
lista_usuarios = {}
usuario = {}
conta_corrente = 0
dados_conta = {}
lista_contas_corrente = {}

while True:
    opcao = input(menu)

    if opcao == "1":
        usuario = criar_usuario(lista_usuarios)
        if usuario:
            lista_usuarios[usuario["cpf"]] = usuario
        
    elif opcao == "2":
        conta_corrente, dados_conta = criar_conta_corrente(lista_usuarios,conta_corrente)
        if dados_conta:
            lista_contas_corrente[conta_corrente["conta"]] = conta_corrente
    elif opcao == "3":
        saldo, lista_depositos = depositar(saldo, lista_depositos)

    elif opcao == "4":
        saldo, limite, numero_saques, lista_saques = sacar(saldo=saldo, limite=limite, numero_saques=numero_saques, lista_saques=lista_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    
    elif opcao == "5":
        exibir_extrato(saldo, lista_depositos, lista_saques, extrato=extrato)
    
    elif opcao == "6":
        break

    else:
        print("Opção inválida, por favor digitar novamente a opção.")
    
