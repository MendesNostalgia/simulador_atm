class ATM:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        print(f"Seu saldo atual é: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Você depositou R${valor:.2f}.")
            self.verificar_saldo()
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            self.saldo -= valor
            print(f"Você sacou R${valor:.2f}.")
            self.verificar_saldo()

    def iniciar(self):
        print("Bem-vindo ao simulador de ATM!")
        while True:
            print("\nEscolha uma opção:")
            print("1. Verificar Saldo")
            print("2. Depositar Dinheiro")
            print("3. Sacar Dinheiro")
            print("4. Sair")

            opcao = input("Digite o número da sua escolha: ")

            if opcao == "1":
                self.verificar_saldo()
            elif opcao == "2":
                valor = float(input("Digite o valor a ser depositado: R$"))
                self.depositar(valor)
            elif opcao == "3":
                valor = float(input("Digite o valor a ser sacado: R$"))
                self.sacar(valor)
            elif opcao == "4":
                print("Obrigado por usar o simulador de ATM. Até mais!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

# Criando uma instância do ATM e iniciando o simulador
atm = ATM(saldo_inicial=1000)  # Saldo inicial de R$1000
atm.iniciar()