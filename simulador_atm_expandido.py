# Simulador de ATM expandido com autenticação, múltiplas contas, histórico de transações e internacionalização

class Conta:
    def __init__(self, numero, pin, saldo_inicial=0):
        self.numero = numero
        self.pin = pin
        self.saldo = saldo_inicial
        self.historico = []

    def verificar_saldo(self):
        print(f"Seu saldo atual é: R${self.saldo:.2f}")
        self.historico.append(f"Verificação de saldo: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Você depositou R${valor:.2f}.")
            self.historico.append(f"Depósito: +R${valor:.2f}")
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
            self.historico.append(f"Saque: -R${valor:.2f}")
            self.verificar_saldo()

    def exibir_historico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:
            print(transacao)


class ATM:
    def __init__(self):
        self.contas = {
            "1234": Conta("1234", "1111", saldo_inicial=1000),
            "5678": Conta("5678", "2222", saldo_inicial=500)
        }
        self.usuario_atual = None
        self.linguagem = "pt"  # Idioma padrão é Português

    def autenticar(self):
        print(self.traduzir("Bem-vindo ao simulador de ATM!"))
        numero = input(self.traduzir("Digite o número da sua conta: "))
        pin = input(self.traduzir("Digite o PIN: "))

        if numero in self.contas and self.contas[numero].pin == pin:
            self.usuario_atual = self.contas[numero]
            print(self.traduzir("Autenticação bem-sucedida."))
            self.selecionar_linguagem()
            self.menu_principal()
        else:
            print(self.traduzir("Número da conta ou PIN incorretos."))

    def selecionar_linguagem(self):
        print(self.traduzir("Selecione o idioma:"))
        print("1. Português")
        print("2. English")
        opcao = input(self.traduzir("Digite o número da sua escolha: "))
        if opcao == "2":
            self.linguagem = "en"
        else:
            self.linguagem = "pt"
        print(self.traduzir("Idioma selecionado."))

    def traduzir(self, texto):
        dicionario = {
            "pt": {
                "Bem-vindo ao simulador de ATM!": "Bem-vindo ao simulador de ATM!",
                "Digite o número da sua conta: ": "Digite o número da sua conta: ",
                "Digite o PIN: ": "Digite o PIN: ",
                "Autenticação bem-sucedida.": "Autenticação bem-sucedida.",
                "Número da conta ou PIN incorretos.": "Número da conta ou PIN incorretos.",
                "Selecione o idioma:": "Selecione o idioma:",
                "Digite o número da sua escolha: ": "Digite o número da sua escolha: ",
                "Idioma selecionado.": "Idioma selecionado.",
                "Escolha uma opção:": "Escolha uma opção:",
                "1. Verificar Saldo": "1. Verificar Saldo",
                "2. Depositar Dinheiro": "2. Depositar Dinheiro",
                "3. Sacar Dinheiro": "3. Sacar Dinheiro",
                "4. Ver Histórico de Transações": "4. Ver Histórico de Transações",
                "5. Sair": "5. Sair",
                "Opção inválida. Por favor, tente novamente.": "Opção inválida. Por favor, tente novamente.",
                "Digite o valor a ser depositado: R$": "Digite o valor a ser depositado: R$",
                "Digite o valor a ser sacado: R$": "Digite o valor a ser sacado: R$",
                "Obrigado por usar o simulador de ATM. Até mais!": "Obrigado por usar o simulador de ATM. Até mais!"
            },
            "en": {
                "Bem-vindo ao simulador de ATM!": "Welcome to the ATM simulator!",
                "Digite o número da sua conta: ": "Enter your account number: ",
                "Digite o PIN: ": "Enter your PIN: ",
                "Autenticação bem-sucedida.": "Authentication successful.",
                "Número da conta ou PIN incorretos.": "Incorrect account number or PIN.",
                "Selecione o idioma:": "Select language:",
                "Digite o número da sua escolha: ": "Enter the number of your choice: ",
                "Idioma selecionado.": "Language selected.",
                "Escolha uma opção:": "Choose an option:",
                "1. Verificar Saldo": "1. Check Balance",
                "2. Depositar Dinheiro": "2. Deposit Money",
                "3. Sacar Dinheiro": "3. Withdraw Money",
                "4. Ver Histórico de Transações": "4. View Transaction History",
                "5. Sair": "5. Exit",
                "Opção inválida. Por favor, tente novamente.": "Invalid option. Please try again.",
                "Digite o valor a ser depositado: R$": "Enter the amount to be deposited: $",
                "Digite o valor a ser sacado: R$": "Enter the amount to withdraw: $",
                "Obrigado por usar o simulador de ATM. Até mais!": "Thank you for using the ATM simulator. Goodbye!"
            }
        }
        return dicionario[self.linguagem].get(texto, texto)

    def menu_principal(self):
        while True:
            print(self.traduzir("\nEscolha uma opção:"))
            print(self.traduzir("1. Verificar Saldo"))
            print(self.traduzir("2. Depositar Dinheiro"))
            print(self.traduzir("3. Sacar Dinheiro"))
            print(self.traduzir("4. Ver Histórico de Transações"))
            print(self.traduzir("5. Sair"))

            opcao = input(self.traduzir("Digite o número da sua escolha: "))

            if opcao == "1":
                self.usuario_atual.verificar_saldo()
            elif opcao == "2":
                valor = float(input(self.traduzir("Digite o valor a ser depositado: R$")))
                self.usuario_atual.depositar(valor)
            elif opcao == "3":
                valor = float(input(self.traduzir("Digite o valor a ser sacado: R$")))
                self.usuario_atual.sacar(valor)
            elif opcao == "4":
                self.usuario_atual.exibir_historico()
            elif opcao == "5":
                print(self.traduzir("Obrigado por usar o simulador de ATM. Até mais!"))
                break
            else:
                print(self.traduzir("Opção inválida. Por favor, tente novamente."))


# Inicializando o simulador de ATM
atm = ATM()
atm.autenticar()