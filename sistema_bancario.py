from datetime import datetime

clientes = []
contas = []

LIMITE_SAQUES = 5
NUM_AGENCIA = "0001"


def registrar_cliente(nome, data_nascimento, cpf, endereco):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("\nCPF já cadastrado!")
            return

    novo_cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    clientes.append(novo_cliente)
    print("\nCliente registrado com sucesso!")

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


def registrar_conta(cpf_cliente):
    cliente = buscar_cliente(cpf_cliente)
    if cliente:
        nova_conta = {
            "agencia": NUM_AGENCIA,
            "numero": len(contas) + 1,
            "cpf_cliente": cpf_cliente,
            "saldo": 0,
            "limite": 500,
            "extrato": [],
            "numero_saques": 0
        }
        contas.append(nova_conta)
        print("\nConta registrada com sucesso!")
        print(f"Agência: {NUM_AGENCIA} | Conta: {nova_conta['numero']}")
    else:
        print("\nCliente não encontrado!")

def buscar_conta(cpf_cliente):
    return [conta for conta in contas if conta["cpf_cliente"] == cpf_cliente]


def depositar(numero_conta, valor):
    for conta in contas:
        if conta["numero"] == numero_conta:
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"].append(f"Depósito: R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                print("\nDepósito realizado com sucesso!")
            else:
                print("\nValor de depósito inválido.")
            return
    print("\nConta não encontrada.")

def sacar(numero_conta, valor):
    for conta in contas:
        if conta["numero"] == numero_conta:
            if valor <= 0:
                print("\nValor de saque inválido.")
            elif valor > conta["saldo"]:
                print("\nSaldo insuficiente.")
            elif conta["numero_saques"] >= LIMITE_SAQUES:
                print("\nVocê atingiu o limite de saques diários.")
            else:
                conta["saldo"] -= valor
                conta["numero_saques"] += 1
                conta["extrato"].append(f"Saque: R$ {valor:.2f} em {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                print("\nSaque realizado com sucesso!")
            return
    print("\nConta não encontrada.")

def exibir_extrato(numero_conta):
    for conta in contas:
        if conta["numero"] == numero_conta:
            print("\n=== EXTRATO ===")
            if not conta["extrato"]:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in conta["extrato"]:
                    print(movimento)
            print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
            print("================")
            return
    print("\nConta não encontrada.")


while True:
    print("""
[1] Registrar Cliente
[2] Registrar Conta
[3] Listar Contas do Cliente
[4] Depositar
[5] Sacar
[6] Exibir Extrato
[0] Sair
""")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nInforme os dados do cliente.")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (DD-MM-AAAA): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço: ")
        registrar_cliente(nome, data_nascimento, cpf, endereco)

    elif opcao == "2":
        cpf = input("\nInforme o CPF do cliente: ")
        registrar_conta(cpf)

    elif opcao == "3":
        cpf = input("\nInforme o CPF do cliente: ")
        contas_cliente = buscar_conta(cpf)
        if contas_cliente:
            print("\nContas do Cliente:")
            for conta in contas_cliente:
                print(f"Agência: {conta['agencia']} | Conta: {conta['numero']}")
        else:
            print("\nNenhuma conta encontrada para este cliente.")

    elif opcao == "4":
        numero_conta = int(input("\nInforme o número da conta: "))
        valor = float(input("Informe o valor do depósito: "))
        depositar(numero_conta, valor)

    elif opcao == "5":
        numero_conta = int(input("\nInforme o número da conta: "))
        valor = float(input("Informe o valor do saque: "))
        sacar(numero_conta, valor)

    elif opcao == "6":
        numero_conta = int(input("\nInforme o número da conta: "))
        exibir_extrato(numero_conta)

    elif opcao == "0":
        break

    else:
        print("\nOpção inválida, tente novamente.")