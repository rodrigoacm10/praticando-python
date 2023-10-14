# Solicita o valor por hora e o número de horas trabalhadas ao usuário
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total (Salário = Valor por hora * Horas trabalhadas)
salario_total = valor_por_hora * horas_trabalhadas

# Exibe o resultado
print(f"O total do seu salário no mês é: R${salario_total:.2f}")