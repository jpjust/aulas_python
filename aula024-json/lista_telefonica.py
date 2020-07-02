# coding: utf-8
#
# Exemplo da videoaula Python #24.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

# Importa o módulo funcoes
import funcoes as f

# Importa o módulo json
import json

programa = "LISTA TELEFÔNICA 2.0"

# Cria uma lista vazia
lista = []

# Faz a leitura da lista em arquivo
try:
    arquivo = open("lista.txt", "r")
    lista = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo não encontrado.")

except PermissionError:
    print("Sem permissão para abrir o arquivo.")
    
except IOError:
    print("Erro de E/S.")

except json.decoder.JSONDecodeError:
    print("O arquivo não está no formato JSON.")

else:
    # Fecha o arquivo
    arquivo.close()

# Repetição principal do programa
while True:
    try:
        # Exibe o menu e solicita uma opção do usuário
        f.titulo(programa)
        opcao = f.menu("Sair", "Adicionar", "Remover", "Exibir")
        
        # Opção 0: Sair
        if opcao == 0:
            # Faz a gravação dos dados
            try:
                arquivo = open("lista.txt", "w")
                json.dump(lista, arquivo)
            
            except PermissionError:
                print("Sem permissão para abrir o arquivo.")
    
            except IOError:
                print("Erro de E/S.")

            else:
                # Fecha o arquivo
                arquivo.close()
                print("Arquivo gravado.")
            break

        # Opção 1: Adicionar contato
        # - Solicita o nome e o telefone
        # - Cria um dicionário
        # - Adiciona na lista
        elif opcao == 1:
            f.titulo(programa)
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            
            # Remove os espaços em branco com strip()
            nome = nome.strip()
            telefone = telefone.strip()
            
            # Testa se as entradas estão vazias
            if nome == "" or telefone == "":
                print("Todos os campos são obrigatórios.")
            else:
                contato = {"nome": nome, "telefone": telefone}
                lista.append(contato)
                print(f"{nome} foi adicionado.")

        # Opção 2: Remover contato
        # - Solicita o nome do contato
        # - Inicializa a variável de controle com valor Falso
        # - Percorre a lista procurando o contato para remover
        # - Caso não encontre, exibe uma mensagem informando
        elif opcao == 2:
            f.titulo(programa)
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
            f.titulo(programa)
            print("\nLISTA DE CONTATOS:")
            for contato in lista:
                print(f"Nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
        
        # Nenhuma das opções acima
        else:
            print("Opção inválida.")

    # Exceção para ValueError
    except ValueError:
        print("Você digitou uma opção inválida.")
