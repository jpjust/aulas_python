# coding: utf-8
#
# Exemplo da videoaula Python #24.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

# Módulo JSON
import json

try:
    # Abre o arquivo para gravação
    arquivo = open("lista.txt", "w")

    # Cria uma lista com o conteúdo
    lista = ["Sushi", "Hambúrguer", "Cachorro-quente"]

    # Grava a lista no formato JSON
    json.dump(lista, arquivo)

except PermissionError:
    print("Sem permissão para abrir o arquivo.")
    
except IOError:
    print("Erro de E/S.")

else:
    # Fecha o arquivo
    arquivo.close()
    print("Arquivo gravado.")
