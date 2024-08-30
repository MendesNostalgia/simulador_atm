import tkinter as tk
from tkinter import messagebox, simpledialog


class Conta:
    def __init__(self, numero, pin, saldo_inicial=0):
        self.numero = numero
        self.pin = pin
        self.saldo = saldo_inicial
        self.historico = []

    def verificar_saldo(self):
        self.historico.append(f"Verificação de saldo: R${self.saldo:.2f}")
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R${valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if valor <= 0:
            return False, "O valor do saque deve ser positivo."
        elif valor > self.saldo:
            return False, "Saldo insuficiente para o saque."
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: -R${valor:.2f}")
            return True, None

    def exibir_historico(self):
        return "\n".join(self.historico) if self.historico else "Nenhuma transação realizada."


class ATMInterface:
    def __init__(self, root):
        self.contas = {
            "1234": Conta("1234", "1111", saldo_inicial=1000),
            "5678": Conta("5678", "2222", saldo_inicial=500)
        }
        self.usuario_atual = None
        self.linguagem = "pt"

        self.root = root
        self.root.title("Simulador de ATM")
        self.root.geometry("400x300")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.traduzir = {
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
                "Obrigado por usar o simulador de ATM. Até mais!": "Obrigado por usar o simulador de ATM. Até mais!",
                "Depósito realizado com sucesso.": "Depósito realizado com sucesso.",
                "O valor do depósito deve ser positivo.": "O valor do depósito deve ser positivo.",
                "Saldo insuficiente para o saque.": "Saldo insuficiente para o saque.",
                "O valor do saque deve ser positivo.": "O valor do saque deve ser positivo."
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
                "Obrigado por usar o simulador de ATM. Até mais!": "Thank you for using the ATM simulator. Goodbye!",
                "Depósito realizado com sucesso.": "Deposit successful.",
                "O valor do depósito deve ser positivo.": "Deposit amount must be positive.",
                "Saldo insuficiente para o saque.": "Insufficient funds.",
                "O valor do saque deve ser positivo.": "Withdrawal amount must be positive."
            }
        }

        self.pagina_login()

    def traduzir_texto(self, texto):
        return self.traduzir[self.linguagem].get(texto, texto)

    def pagina_login(self):
        self.limpar_frame()

        tk.Label(self.frame, text=self.traduzir_texto("Bem-vindo ao simulador de ATM!")).grid(row=0, columnspan=2)

        tk.Label(self.frame, text=self.traduzir_texto("Digite o número da sua conta: ")).grid(row=1, column=0)
        self.entry_numero = tk.Entry(self.frame)
        self.entry_numero.grid(row=1, column=1)

        tk.Label(self.frame, text=self.traduzir_texto("Digite o PIN: ")).grid(row=2, column=0)
        self.entry_pin = tk.Entry(self.frame, show="*")
        self.entry_pin.grid(row=2, column=1)

        tk.Button(self.frame, text="Login", command=self.autenticar).grid(row=3, columnspan=2)
        tk.Button(self.frame, text="Sair", command=self.root.quit).grid(row=4, columnspan=2)

    def autenticar(self):
        numero = self.entry_numero.get()
        pin = self.entry_pin.get()

        if numero in self.contas and self.contas[numero].pin == pin:
            self.usuario_atual = self.contas[numero]
            messagebox.showinfo(self.traduzir_texto("Autenticação bem-sucedida."), self.traduzir_texto("Autenticação bem-sucedida."))
            self.selecionar_linguagem()
        else:
            messagebox.showerror(self.traduzir_texto("Erro"), self.traduzir_texto("Número da conta ou PIN incorretos."))

    def selecionar_linguagem(self):
        self.limpar_frame()

        tk.Label(self.frame, text=self.traduzir_texto("Selecione o idioma:")).grid(row=0, columnspan=2)
        tk.Button(self.frame, text="Português", command=lambda: self.definir_linguagem("pt")).grid(row=1, column=0)
        tk.Button(self.frame, text="English", command=lambda: self.definir_linguagem("en")).grid(row=1, column=1)

    def definir_linguagem(self, idioma):
        self.linguagem = idioma
        messagebox.showinfo(self.traduzir_texto("Idioma selecionado."), self.traduzir_texto("Idioma selecionado."))
        self.menu_principal()

    def menu_principal(self):
        self.limpar_frame()

        tk.Label(self.frame, text=self.traduzir_texto("Escolha uma opção:")).grid(row=0, columnspan=2)
        tk.Button(self.frame, text=self.traduzir_texto("1. Verificar Saldo"), command=self.verificar_saldo).grid(row=1, columnspan=2)
        tk.Button(self.frame, text=self.traduzir_texto("2. Depositar Dinheiro"), command=self.depositar).grid(row=2, columnspan=2)
        tk.Button(self.frame, text=self.traduzir_texto("3. Sacar Dinheiro"), command=self.sacar).grid(row=3, columnspan=2)
        tk.Button(self.frame, text=self.traduzir_texto("4. Ver Histórico de Transações"), command=self.exibir_historico).grid(row=4, columnspan=2)
        tk.Button(self.frame, text=self.traduzir_texto("5. Sair"), command=self.sair).grid(row=5, columnspan=2)

    def verificar_saldo(self):
        saldo = self.usuario_atual.verificar_saldo()
        messagebox.showinfo(self.traduzir_texto("Saldo Atual"), f"{self.traduzir_texto('Seu saldo atual é:')} R${saldo:.2f}")

    def depositar(self):
        valor = simpledialog.askfloat(self.traduzir_texto("Depósito"), self.traduzir_texto("Digite o valor a ser depositado: R$"))
        if valor is not None:
            sucesso = self.usuario_atual.depositar(valor)
            if sucesso:
                messagebox.showinfo(self.traduzir_texto("Depósito realizado"), self.traduzir_texto("Depósito realizado com sucesso."))
            else:
                messagebox.showerror(self.traduzir_texto("Erro"), self.traduzir_texto("O valor do depósito deve ser positivo."))

    def sacar(self):
        valor = simpledialog.askfloat(self.traduzir_texto("Saque"), self.traduzir_texto("Digite o valor a ser sacado: R$"))
        if valor is not None:
            sucesso, mensagem = self.usuario_atual.sacar(valor)
            if sucesso:
                messagebox.showinfo(self.traduzir_texto("Saque realizado"), self.traduzir_texto(f"Você sacou R${valor:.2f}."))
            else:
                messagebox.showerror(self.traduzir_texto("Erro"), self.traduzir_texto(mensagem))

    def exibir_historico(self):
        historico = self.usuario_atual.exibir_historico()
        messagebox.showinfo(self.traduzir_texto("Histórico de Transações"), historico)

    def sair(self):
        messagebox.showinfo(self.traduzir_texto("Obrigado"), self.traduzir_texto("Obrigado por usar o simulador de ATM. Até mais!"))
        self.usuario_atual = None
        self.pagina_login()

    def limpar_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMInterface(root)
    root.mainloop()