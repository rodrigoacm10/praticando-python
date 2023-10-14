# Solicita uma letra ao usuário
letra = input("Digite uma letra (F para Feminino, M para Masculino): ")

# Converte a letra para maiúscula para tornar a comparação insensível a maiúsculas/minúsculas
letra = letra.upper()

# Verifica o sexo com base na letra digitada
if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo Inválido")