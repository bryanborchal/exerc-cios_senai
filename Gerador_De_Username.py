#|------------------------------ JEITO MENOS PRÁTICO ------------------------------|
nome = input('Digite seu nome completo: ')
nome = nome.strip()
nome = nome.lower()
nome = nome.split()
primeiro_nome = (nome[0])
ultimo_nome = nome[-1]
print(primeiro_nome+"."+ultimo_nome)

#|------------------------------ JEITO MAIS PRÁTICO ------------------------------|

nome = input('Digite seu nome completo: ').lower().strip().split()
print(f'{nome[0]}.{nome[-1]}')