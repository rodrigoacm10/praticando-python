import csv
import os

def adicionar_contato(nome, telefone, email):
    with open('agenda.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone, email])

def listar_contatos():
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")

def buscar_contato(nome):
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == nome.lower():
                print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")
                return
        print("Contato não encontrado.")

def remover_contato(nome):
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        contatos = list(reader)

    with open('agenda.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in contatos:
            if row[0].lower() != nome.lower():
                writer.writerow(row)
        print("Contato removido com sucesso.")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Remover contato")
        print("5 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome para buscar: ")
            buscar_contato(nome)
        elif opcao == '4':
            nome = input("Digite o nome para remover: ")
            remover_contato(nome)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

    if not os.path.exists('agenda.csv'):
        with open('agenda.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Telefone', 'Email'])

main()