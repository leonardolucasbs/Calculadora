import os
#função que limpa a tela
def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear") 

# Função principal do programa
def calculadora():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    while True:  # Loop infinito até que o usuário decida sair
        limpa_tela()
        print("      Opções       ")
        print("  1 - Adição       ")
        print("  2 - Subtração    ")
        print("  3 - Multiplicação ")
        print("  4 - Divisão      ")
        print("  0 - Para sair    ")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                print(f"{numero1} + {numero2} = {numero1 + numero2}")
            case 2:
                print(f"{numero1} - {numero2} = {numero1 - numero2}")
            case 3:
                print(f"{numero1} x {numero2} = {numero1 * numero2}")
            case 4:
                if numero2 != 0:  # Verifica se o divisor é zero
                    print(f"{numero1} / {numero2} = {numero1 / numero2}")
                else:
                    print("Erro: Não é possível dividir por zero.")
            case 0:
                print("O programa foi encerrado!")
                return  # Sai da função e encerra o programa
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        # Pergunta se o usuário deseja realizar outra operação
        erro = input("Para realizar outra operação digite [1] para sim e [2] para não: ")
        if erro != '1':
            print("Programa encerrado!")
            break  # Sai do loop se o usuário não quiser continuar

# Chama a função principal
calculadora()