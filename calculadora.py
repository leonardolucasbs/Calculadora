def op():
    print("      Opções       ")
    print("  1 - Adição       ")
    print("  2 - Subtração    ")
    print("  3 - Multiplicação ")
    print("  4 - Divisão      ")
    print("  0 - Para sair    ")

def fabrica_de_funcoes(operacao):
    # Funções definidas internamente para cada operação
    def soma(*args):
        return sum(args)

    def subtracao(*args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado

    def multiplicacao(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    def divisao(*args):
        resultado = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida.")
            resultado /= num
        return resultado

    # Retorna a função correspondente com base na operação solicitada
    if operacao == "soma":
        return soma
    elif operacao == "subtracao":
        return subtracao
    elif operacao == "multiplicacao":
        return multiplicacao
    elif operacao == "divisao":
        return divisao
    else:
        raise ValueError("Operação inválida.")

# Entrada dos números
numeros = list(map(float, input("Digite números separados por espaço: ").split()))
op()
opcao = int(input("Digite sua opção: "))

# Processamento das operações com base na escolha
match opcao:
    case 1:
        adicao = fabrica_de_funcoes("soma")
        resultado = adicao(*numeros)  # Desempacota a lista em argumentos individuais
        print("Resultado da soma:", resultado)
    case 2:
        subtrair = fabrica_de_funcoes("subtracao")
        resultado = subtrair(*numeros)
        print("Resultado da subtração:", resultado)
    case 3:
        multiplicar = fabrica_de_funcoes("multiplicacao")
        resultado = multiplicar(*numeros)
        print("Resultado da multiplicação:", resultado)
    case 4:
        dividir = fabrica_de_funcoes("divisao")
        try:
            resultado = dividir(*numeros)
            print("Resultado da divisão:", resultado)
        except ValueError as e:
            print(e)
    case 0:
        print("Saindo...")
    case _:
        print("Opção inválida.")
