# coding: utf-8
#
# Exemplos da videoaula Python #17.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

while True:
    try:
        idade = int(input("Quantos anos você tem? "))
        nascimento = 2020 - idade
        print(f"Você provavelmente nasceu em {nascimento}.")
        break
    except ValueError:
        print("Você precisa digitar um número.")
