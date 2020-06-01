# coding: utf-8
#
# Exemplos da videoaula Python #17.
# Assista o vídeo no YouTube em youtube.com/ProfessorJust

try:
    print("-- CALCULADORA --")
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    oper = input("Escolha a operação [+, -, *, /]: ")

    if oper == "+":
        resultado = a + b
    elif oper == "-":
        resultado = a - b
    elif oper == "*":
        resultado = a * b
    elif oper == "/":
        resultado = a / b
    else:
        print("Operação inválida.")

except ValueError:
    print("Você precisa digitar números.")

except ZeroDivisionError:
    print("Você não pode dividir por zero.")

else:
    # Este código executa apenas se não ocorrer
    # nenhuma exceção
    print(f"O resultado da operação é {resultado}.")

finally:
    # Este código executa em todos os casos,
    # havendo ou não exceção
    print("O programa encerrou.")
