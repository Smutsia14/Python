from os import system #Biblioteca importada

print('Cadastro de Contatos\n')

contatos=[]

while(True):
    system('cls')
    print('1 - Inserir Contato')
    print('2 - Atualizar Contato')
    print('3 - Excluir Contato')
    print('4 - Listar Contatos')
    print('5 - Sair')

    op = int(input('Digite a opção escolhida: '))

    while( (op<1) or (op>5) ):
        print('Opção inválida!')
        op = int(input('Digite a opção escolhida: '))

    if (op == 1):
        nome = input('Digite o nome do Contato: ')
        contatos.append(nome)
        print('Cadastro realizado com sucesso!')
        input()
    elif (op == 2):
        for i in range(0 ,len(contatos),1):
            print(i,"-",contatos[i])
        aviaozinho=int(input("Escolha o contato: "))
        del (contatos[aviaozinho])
        novo=str(input("Digite o nome"))
        contatos.append(novo)
        print('O contato foi atualizado')
        input()
        
    elif (op == 3):
        for i in range(0 ,len(contatos),1):
            print(i,"-",contatos[i])
        fusquinha=int(input("Escolha o contato: "))
        del (contatos [fusquinha])
        print("Contato apagado")
        input()
        
    elif (op == 4):
        for c in contatos:
            print(c)
        input()
        
    else:
        break
