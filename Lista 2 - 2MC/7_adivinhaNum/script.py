import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

 
adivinhe_o_numero()