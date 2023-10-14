def calcular_media(notas):
    return sum(notas) / len(notas)

def obter_nota_final(media):
    if 90 <= media <= 100:
        return 'A'
    elif 80 <= media < 90:
        return 'B'
    elif 70 <= media < 80:
        return 'C'
    elif 60 <= media < 70:
        return 'D'
    else:
        return 'F'

def main():
    try:
        num_notas = int(input("Quantas notas você deseja inserir? "))
        notas = []

        for i in range(num_notas):
            nota = float(input(f"Insira a nota {i + 1}: "))
            notas.append(nota)

        media = calcular_media(notas)
        nota_final = obter_nota_final(media)

        print(f"\nMédia: {media:.2f}")
        print(f"Nota final: {nota_final}")

    except ValueError:
        print("Por favor, insira valores numéricos para as notas.")

main()
