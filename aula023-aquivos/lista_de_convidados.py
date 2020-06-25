# coding: utf-8
#
# Exemplo da videoaula Python #23.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

# Importa o módulo funcoes
import funcoes as f

# Cria uma lista vazia
lista = []

# Abre o arquivo para leitura
try:
    arquivo = open("lista.txt", "r")
    lista = arquivo.readlines()
    
    # Percorre os nomes na lista removendo o \n no final
    for i in range(len(lista)):
        lista[i] = lista[i].strip()    

except FileNotFoundError:
    print("Arquivo não encontrado.")
    
except PermissionError:
    print("Sem permissão para abrir o arquivo.")
    
except IOError:
    print("Erro de E/S.")

else:
    arquivo.close()

# Repetição principal do programa
while True:
    try:
        # Exibe o menu de opções e solicita entrada do usuário
        f.titulo("MENU PRINCIPAL")
        opcao = f.menu("Sair", "Adiconar nome", "Verificar nome", "Exibir lista", "Remover nome")

        # Opção 0: sair
        if opcao == 0:
            # Abre o arquivo para gravação dos nomes
            try:
                arquivo = open("lista.txt", "w")
                for nome in lista:
                    arquivo.write(f"{nome}\n")
            
            except PermissionError:
                print("Sem permissão para gravar no arquivo.")
            
            except IOError:
                print("Erro de E/S.")
            
            else:
                arquivo.close()
                print("Arquivo gravado.")
                
            break

        # Opção 1: Adicionar
        # - Pede o nome ao usuário
        # - Verifica se está na lista
        # - Caso não esteja, adiciona com append()
        elif opcao == 1:
            nome = input("Digite o nome do convidado: ")
            
            # Remove os espaços em branco com strip()
            nome = nome.strip()
            
            # Testa se a entrada está vazia
            if nome == "":
                print("Você precisa digitar um nome.")
            elif nome in lista:
                print(f"{nome} já está na lista.")
            else:
                lista.append(nome)
                print(f"{nome} foi adicionado à lista.")

        # Opção 2: Verificar nome
        # - Pede o nome ao usuário
        # - Verifica se está na lista com o operador in
        elif opcao == 2:
            nome = input("Digite o nome que deseja verificar: ")
            if nome in lista:
                print(f"{nome} está na lista.")
            else:
                print(f"{nome} não está na lista. CUIDADO: Pode ser um penetra!")

        # Opção 3: Exibir lista
        # - Ordena a lista com sort()
        # - Inicia a contagem em 1 e itera a lista
        #   com o for exibindo um nome em cada linha
        elif opcao == 3:
            lista.sort()
            print("LISTA DE CONVIDADOS: ")
            numero = 1
            for nome in lista:
                print(f"{numero}: {nome}")
                numero += 1

        # Opção 4: Remover
        # - Pede o nome ao usuário
        # - Verifica se o nome está na lista, caso esteja, remove
        elif opcao == 4:
            nome = input("Digite o nome que deseja remover: ")
            if nome in lista:
                lista.remove(nome)
                print(f"{nome} foi removido.")
            else:
                print(f"{nome} não estava na lista.")

    # Exceção para ValueError
    except ValueError:
        print("Digite uma opção válida.")
