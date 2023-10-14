import json
import os

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

def adicionar_tarefa(titulo, descricao):
    tarefas = carregar_tarefas()
    tarefa = {'titulo': titulo, 'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada com sucesso.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{i}. {tarefa['titulo']} - {tarefa['descricao']} ({status})")

def marcar_como_concluida(numero):
    tarefas = carregar_tarefas()
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]['concluida'] = True
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefas[numero - 1]['titulo']}' marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(numero):
    tarefas = carregar_tarefas()
    if 1 <= numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_removida['titulo']}' removida com sucesso.")
    else:
        print("Número de tarefa inválido.")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            numero = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_como_concluida(numero)
        elif opcao == '4':
            numero = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(numero)
        elif opcao == '5':
            print("Saindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()