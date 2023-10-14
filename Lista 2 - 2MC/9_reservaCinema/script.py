import os

def mostrar_filmes():
    print("Filmes disponíveis:")
    print("1. Filme A")
    print("2. Filme B")
    print("3. Filme C")

def escolher_horario():
    print("Horários disponíveis:")
    print("1. 14:00")
    print("2. 18:00")
    print("3. 20:30")

def fazer_reserva(filme, horario, quantidade_ingressos):
    with open('reservas.txt', 'a') as arquivo:
        arquivo.write(f"Filme: {filme}, Horário: {horario}, Ingressos: {quantidade_ingressos}\n")
    print("Reserva realizada com sucesso!")

def mostrar_reservas():
    if os.path.exists('reservas.txt'):
        with open('reservas.txt', 'r') as arquivo:
            reservas = arquivo.read()
            if reservas:
                print("Reservas existentes:")
                print(reservas)
            else:
                print("Nenhuma reserva encontrada.")
    else:
        print("Nenhuma reserva encontrada.")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Mostrar filmes disponíveis")
        print("2 - Escolher filme e horário")
        print("3 - Mostrar reservas")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            mostrar_filmes()
        elif opcao == '2':
            mostrar_filmes()
            filme = input("Escolha o filme (digite o número): ")
            escolher_horario()
            horario = input("Escolha o horário (digite o número): ")
            quantidade_ingressos = int(input("Digite a quantidade de ingressos desejada: "))
            fazer_reserva(filme, horario, quantidade_ingressos)
        elif opcao == '3':
            mostrar_reservas()
        elif opcao == '4':
            print("Saindo do sistema de reservas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()