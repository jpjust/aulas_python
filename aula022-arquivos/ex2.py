# coding: utf-8
#
# Exemplo da videoaula Python #22.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

try:
    # Abre o arquivo para gravação
    arquivo = open("lista.txt", "w")

    # Cria uma lista com o conteúdo
    lista = ["Sushi\n", "Hambúrguer\n", "Cachorro-quente\n"]

    # Percorre cada ítem da lista e grava no arquivo
    arquivo.writelines(lista)

except PermissionError:
    print("Sem permissão para abrir o arquivo.")
    
except IOError:
    print("Erro de E/S.")

else:
    # Fecha o arquivo
    arquivo.close()
    print("Arquivo gravado.")
