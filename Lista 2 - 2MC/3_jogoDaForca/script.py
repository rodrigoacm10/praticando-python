import random

def escolher_palavra():
    palavras = ['python', 'java', 'javascript', 'ruby', 'html', 'css', 'react']
    return random.choice(palavras)

def exibir_forca(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_forca(palavra_secreta, letras_corretas))

    while tentativas > 0:
        palpite = input("\nDigite uma letra: ").lower()

        if palpite.isalpha() and len(palpite) == 1:
            if palpite in letras_corretas:
                print("Você já tentou esta letra. Tente novamente.")
            elif palpite in palavra_secreta:
                letras_corretas.append(palpite)
                print("Letra correta!")
            else:
                tentativas -= 1
                print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        else:
            print("Entrada inválida. Por favor, digite uma única letra.")

        print(exibir_forca(palavra_secreta, letras_corretas))

        if set(letras_corretas) == set(palavra_secreta):
            print("Parabéns! Você ganhou!")
            break

    if tentativas == 0:
        print(f"Fim de jogo! A palavra correta era '{palavra_secreta}'.")

# if __name__ == "__main__":
jogar_forca()
