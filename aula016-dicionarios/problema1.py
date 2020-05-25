# coding: utf-8
#
# Problema resolvido da videoaula Python #16.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

# Cria uma lista vazia
lista = []

# Repetição principal do programa
while True:
    # Exibe o menu e solicita uma opção do usuário
    print("1) Adicionar contato")
    print("2) Remover contato")
    print("3) Exibir a agenda")
    print("0) Sair")
    opcao = int(input("Digite uma opção [0-3]: "))
    
    # Opção 0: Sair
    if opcao == 0:
        break

    # Opção 1: Adicionar contato
    # - Solicita o nome e o telefone
    # - Cria um dicionário
    # - Adiciona na lista
    elif opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        contato = {"nome": nome, "telefone": telefone}
        lista.append(contato)
        print(f"{nome} foi adicionado.")

    # Opção 2: Remover contato
    # - Solicita o nome do contato
    # - Inicializa a variável de controle com valor Falso
    # - Percorre a lista procurando o contato para remover
    # - Caso não encontre, exibe uma mensagem informando
    elif opcao == 2:
        nome = input("Digite o nome do contato que deseja remover: ")

        contato_encontrado = False
        for contato in lista:
            if contato["nome"] == nome:
                lista.remove(contato)
                print(f"{nome} foi removido.")
                contato_encontrado = True
                break
        
        if contato_encontrado == False:
            print(f"{nome} não foi encontrado.")

    # Opção 3: Exibir a agente
    # - Percorre a lista e exibe valores de cada dicionário
    elif opcao == 3:
        print("\nLISTA DE CONTATOS:")
        for contato in lista:
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
    
    # Nenhuma das opções acima
    else:
        print("Opção inválida.")
