import math

# Solicita o raio do círculo ao usuário
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo usando a fórmula A = π * r^2
area = math.pi * (raio ** 2)

# Exibe a área
print(f"A área do círculo com raio {raio} é: {area}")