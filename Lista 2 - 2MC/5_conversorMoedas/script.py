class ConversorMoedas:
    def __init__(self, taxa_cambio):
        self.taxa_cambio = taxa_cambio

    def converter(self, valor, moeda_origem, moeda_destino):
        if moeda_origem.upper() in self.taxa_cambio and moeda_destino.upper() in self.taxa_cambio:
            valor_em_usd = valor / self.taxa_cambio[moeda_origem.upper()]
            valor_convertido = valor_em_usd * self.taxa_cambio[moeda_destino.upper()]
            return f"{valor:.2f} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}"
        else:
            return "Moeda não suportada."

def main():
    taxa_cambio_fixa = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}

    conversor = ConversorMoedas(taxa_cambio_fixa)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Converter moeda")
        print("2 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser convertido: "))
            moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ")
            moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ")

            resultado = conversor.converter(valor, moeda_origem, moeda_destino)
            print(resultado)
        elif opcao == '2':
            print("Saindo do conversor de moedas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

 
main()