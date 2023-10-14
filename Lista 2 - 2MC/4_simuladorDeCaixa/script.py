class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        return f"Saldo disponível: R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Valor inválido. O depósito deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        elif valor <= 0:
            return "Valor inválido. O saque deve ser maior que zero."
        else:
            return "Saldo insuficiente."

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Consultar saldo")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            print(caixa.consultar_saldo())
        elif opcao == '2':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            print(caixa.depositar(valor_deposito))
        elif opcao == '3':
            valor_saque = float(input("Digite o valor a ser sacado: "))
            print(caixa.sacar(valor_saque))
        elif opcao == '4':
            print("Saindo do caixa eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()