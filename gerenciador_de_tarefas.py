lista_de_tarefas = { 
        'Tarefas' : ['Limpar fogão', 'Lavar a louça'],
        'Data das tarefas' : ['2/7', '2/7']
    }

def mostrar_tarefas():
    barra = f'|{"_"*30}|'
    print(barra)
    for i in range(len(lista_de_tarefas['Tarefas'])):
        print(f"{i+1}. Tarefas: {lista_de_tarefas['Tarefas'][i]} - Data: {lista_de_tarefas['Data das tarefas'][i]}")
    print(barra)



def mostrar_menu():
    barra = f'|{"_"*30}|'
    print(barra)
    print('1 - Adicionar tarefa')
    print('2 - Lista de tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')
    print(barra)
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        nome_tarefa = input('Qual tarefa deseja adicionar? ')
        dia_tarefa = (input('Qual dia a tarefa será feita? '))
    elif opcao == 2:
        mostrar_tarefas()
    
#Chamando função
mostrar_menu()


