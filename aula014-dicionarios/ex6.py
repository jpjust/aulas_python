# coding: utf-8
#
# Exemplos da videoaula Python #14.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

dados = {"nome": "João", "twitter": "jpjust", "nascimento": 1982}

print(dados.get("nome", "Sem nome"))
print(dados.get("apelido", "Sem apelido"))

print(dados.pop("nome", "Sem nome"))
print(dados.pop("apelido", "Sem apelido"))

print(dados)
