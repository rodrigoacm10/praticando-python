def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    print("Bem-vindo à Calculadora de IMC!")

    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    interpretacao = interpretar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Interpretação: {interpretacao}")

 
main()