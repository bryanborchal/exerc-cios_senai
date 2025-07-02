lista_de_tarefas = { 
        'Tarefas' : ['Limpar fogão', 'Lavar a louça'],
        'Data das tarefas' : ['2/7', '2/7']
    }


def mostrar_menu():
    while True:
        barra = f'|{"_"*30}|'
        print(barra)
        print('| Gerenciador de Tarefas')
        print(barra)
        print('| (1) Mostrar Tarefas')
        print('| (2) Adicionar Tarefas')
        print('| (3) Remover Tarefas')
        print('| (4) Sair')
        print(barra)
        try:
            resposta = int(input('| Escolha uma Opção: '))
            if resposta == 1:
                mostrar_tarefas()
                input('| Pressione enter para continuar...')
            elif resposta == 2:
                adicionar_tarefa()
                input('| Pressione enter para continuar...')
            elif resposta == 3:
                remover_tarefa()
                input('| Pressione enter para continuar...')
            elif resposta == 4:
                print('| Saindo do Gerenciador')
                break
            else:
                print('| Número inválido!')
        except ValueError:
            print('| Digite um número válido! ')
            

def mostrar_tarefas():
    barra = f'|{"_"*30}|'
    print(barra)
    print('| Tarefas:')
    for i in range(len(lista_de_tarefas['Tarefas'])):
        print(f"{i+1}. Tarefas: {lista_de_tarefas['Tarefas'][i]} - Data: {lista_de_tarefas['Data das tarefas'][i]}")
    print(barra)

def adicionar_tarefa():
    nome_da_tarefa = input('| Digite o nome da tarefa: ')
    dia_da_tarefa = input('| Digite a data da tarefa (dia/mês): ')
    lista_de_tarefas['Tarefas'].append(nome_da_tarefa)
    lista_de_tarefas['Data das tarefas'].append(dia_da_tarefa)
    print('| Tarefa adicionada')

def remover_tarefa():
    mostrar_tarefas()
    try:
        numero_tarefa = int(input('| Digite o número da tarefa que deseja remover: ')) -1
        if 0 <= numero_tarefa < len(lista_de_tarefas['Tarefas']):
            tarefa_removida = lista_de_tarefas['Tarefas'].pop(numero_tarefa)
            lista_de_tarefas['Data das tarefas'].pop(numero_tarefa)
            print(f'Tarefa "{tarefa_removida}" removida!')
        else:
            print('| Número de tarefa inválido!')
    except ValueError:
        print('| Digite um número válido!')

mostrar_menu()


