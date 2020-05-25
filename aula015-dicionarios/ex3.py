# coding: utf-8
#
# Exemplos da videoaula Python #15.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

lista = []
lista.append({"nome": "João", "nascimento": 1982})
lista.append({"nome": "Fulano", "nascimento": 2000})

for dicionario in lista:
  print("\n-- DADOS DO USUÁRIO --")
  for chave in dicionario:
    print(f"{chave} = {dicionario[chave]}")
