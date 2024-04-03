print("Aqui está sua Calculadora")

numero1 = int(input("Insira um Numero de sua Escolha:    "))
numero2 = int(input("Insira outro Numero de sua Escolha:    "))

operadorAritmetico = (input("Por favor, escolha seu operador Aritmetico: "))
print(operadorAritmetico + "*, +, - ou /")

match operadorAritmetico:

    case '-':
        operadorAritmetico == '-'
        print(numero1 - numero2)

    case '+':
        operadorAritmetico == '+'
        print(numero1 + numero2)

    case '*':
        operadorAritmetico == '*'
        print(numero1 * numero2)

    case '/':
        if numero2 == 0:
            print("Não é possível dividir por zero.")
        else:
            print(numero1 / numero2)

    case _:
        print("Escolha um Operador Válido!!!")