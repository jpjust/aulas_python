# coding: utf-8

"""Módulo de funções das videoaulas de Python.

Versão da videoaula #21.

Este módulo contém algumas funções desenvolvidas nos exemplos e
práticas das videoaulas de Python do Professor Just.

As videoaulas e links para outros materiais podem ser encontradas
no canal do YouTube: https://youtube.com/ProfessorJust ."""

def menu(padrao, *opcoes):
    """Exibe um menu automatizado.
    
    Lista os valores em *opcoes como opções de um menu, apresentando
    o valor padrão por último como opção 0. Retorna a escolha do
    usuário ou -1 em caso de erro."""
    i = 1
    
    for op in opcoes:
        print(f"{i}: {op}")
        i += 1
    
    print(f"0: {padrao}")
    
    try:
        return int(input(f"Escolha uma opção: "))
    except ValueError:
        return -1

def titulo(texto):
    """Exibe o texto entre ===."""
    print(f"\n\n=== {texto} ===")
