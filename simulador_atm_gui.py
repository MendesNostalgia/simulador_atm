import tkinter as tk
from tkinter import messagebox

class Conta:
    def __init__(self, numero, pin, saldo_inicial=0):
        self.numero = numero
        self.pin = pin
        self.saldo = saldo_inicial
        self.historico = []

    def verificar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R${valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R${valor:.2f}")
            return True
        return False

    def exibir_historico(self):
        return "\n".join(self.historico)


class ATMInterface:
    def __init__(self, root):
        self.contas = {
            "1234": Conta("1234", "1111", saldo_inicial=1000),
            "5678": Conta("5678", "2222", saldo_inicial=500)
        }
        self.usuario_atual = None

        self.root = root
        self.root.title("Simulador de ATM")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.label_idioma = tk.Label(self.frame, text="Selecione o idioma:")
        self.label_idioma.grid(row=0, column=0, columnspan=2)
        
        self.botao_pt = tk.Button(self.frame, text="Português", command=self.configurar_portugues)
        self.botao_pt.grid(row=1, column=0)
        
        self.botao_en = tk.Button(self.frame, text="English", command=self.configurar_ingles)
        self.botao_en.grid(row=1, column=1)

        self.label_id = tk.Label(self.frame, text="")
        self.label_id.grid(row=2, column=0, columnspan=2)

        self.entry_numero = tk.Entry(self.frame)
        self.entry_pin = tk.Entry(self.frame, show="*")

        self.botao_login = tk.Button(self.frame, text="", command=self.autenticar_usuario)
        self.botao_sair = tk.Button(self.frame, text="", command=self.root.quit)

    def configurar_portugues(self):
        self.idioma = "pt"
        self.label_id.config(text="Número da conta e PIN:")
        self.entry_numero.grid(row=3, column=0)
        self.entry_pin.grid(row=3, column=1)
        self.botao_login.config(text="Login")
        self.botao_login.grid(row=4, column=0)
        self.botao_sair.config(text="Sair")
        self.botao_sair.grid(row=4, column=1)

    def configurar_ingles(self):
        self.idioma = "en"
        self.label_id.config(text="Account number and PIN:")
        self.entry_numero.grid(row=3, column=0)
        self.entry_pin.grid(row=3, column=1)
        self.botao_login.config(text="Login")
        self.botao_login.grid(row=4, column=0)
        self.botao_sair.config(text="Exit")
        self.botao_sair.grid(row=4, column=1)

    def autenticar_usuario(self):
        numero = self.entry_numero.get()
        pin = self.entry_pin.get()

        if numero in self.contas and self.contas[numero].pin == pin:
            self.usuario_atual = self.contas[numero]
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
            self.mostrar_menu()
        else:
            messagebox.showerror("Erro de autenticação", "Número da conta ou PIN incorretos.")

    def mostrar_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.label_opcao = tk.Label(self.frame, text="Escolha uma opção:")
        self.label_opcao.grid(row=0, column=0, columnspan=2)

        self.botao_saldo = tk.Button(self.frame, text="Verificar Saldo", command=self.verificar_saldo)
        self.botao_saldo.grid(row=1, column=0)

        self.botao_deposito = tk.Button(self.frame, text="Depositar Dinheiro", command=self.depositar)
        self.botao_deposito.grid(row=1, column=1)

        self.botao_saque = tk.Button(self.frame, text="Sacar Dinheiro", command=self.sacar)
        self.botao_saque.grid(row=2, column=0)

        self.botao_historico = tk.Button(self.frame, text="Ver Histórico de Transações", command=self.exibir_historico)
        self.botao_historico.grid(row=2, column=1)

        self.botao_sair = tk.Button(self.frame, text="Sair", command=self.root.quit)
        self.botao_sair.grid(row=3, column=0, columnspan=2)

    def verificar_saldo(self):
        saldo = self.usuario_atual.verificar_saldo()
        messagebox.showinfo("Saldo", f"Seu saldo atual é: R${saldo:.2f}")

    def depositar(self):
        valor = self.entrada_valor("Depósito")
        if valor is not None:
            if self.usuario_atual.depositar(valor):
                messagebox.showinfo("Depósito", "Depósito realizado com sucesso.")
            else:
                messagebox.showerror("Erro", "O valor do depósito deve ser positivo.")

    def sacar(self):
        valor = self.entrada_valor("Saque")
        if valor is not None:
            if self.usuario_atual.sacar(valor):
                messagebox.showinfo("Saque", "Saque realizado com sucesso.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

    def exibir_historico(self):
        historico = self.usuario_atual.exibir_historico()
        messagebox.showinfo("Histórico de Transações", historico if historico else "Nenhuma transação realizada.")

    def entrada_valor(self, tipo):
        entrada = tk.simpledialog.askstring(tipo, "Digite o valor:")
        try:
            return float(entrada)
        except (TypeError, ValueError):
            messagebox.showerror("Erro", "Valor inválido.")
            return None


# Inicializando a interface gráfica do ATM
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMInterface(root)
    root.mainloop()