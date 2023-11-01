menu = """

      Bem Vindo!
======================

     [d] Depositar
     [s] Sacar
     [e] Extrato
     [q] Sair

======================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
saque_minimo = 20
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Por favor, informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('\nDepósito realizado com sucesso!')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Por favor, informe o valor do saque: "))

        saque_minimo = valor < 20

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente para realizar a transação.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite da conta.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques diários excedido.")

        elif saque_minimo:
            print("\nOperação falhou! O valor minimo para saque é de R$ 20.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print('\nSaque realizado com sucesso!')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")