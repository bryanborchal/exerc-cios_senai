lista_de_tarefas = {
        ['Lavar louça 1/7', 'Limpar o fogão 2/7']
    }

def mostrar_menu():
    print('1 - Adicionar tarefa')
    print('2 - Lista de tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        nome_tarefa = input('Qual tarefa deseja adicionar? ')
        dia_tarefa = (input('Qual dia a tarefa será feita? '))
    
    
#Chamando função
mostrar_menu()


