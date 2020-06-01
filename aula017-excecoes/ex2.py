# coding: utf-8
#
# Exemplos da videoaula Python #17.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

while True:
    try:
        lista = ["João", "Pedro", "Maria"]

        print("LISTA DE NOMES:")
        for i in range(0, len(lista)):
                print(f"{i}: {lista[i]}")

        indice = int(input("Digite o número da pessoa que quer remover: "))
        del(lista[indice])

        print(f"A lista agora ficou assim: {lista}")
        break

    except (ValueError, IndexError):
        print("Você digitou algo inválido.")
