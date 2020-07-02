# coding: utf-8
#
# Exemplo da videoaula Python #24.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

# Módulo JSON
import json

try:
    # Abre o arquivo para leitura
    arquivo = open("lista.txt", "r")

    # Faz a leitura no formato JSON
    itens = json.load(arquivo)

    # Percorre cada ítem da lista e exibe na tela
    for i in itens:
        print(f"{i}")

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
