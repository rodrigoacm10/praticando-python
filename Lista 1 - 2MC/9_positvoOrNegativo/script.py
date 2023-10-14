# Solicita um valor ao usuário
valor = float(input("Digite um valor: "))

# Verifica se o valor é positivo, negativo ou zero
if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")