from arte import logo


def adiciona(n1, n2):
    return n1 + n2


def subtrai(n1, n2):
    return n1 - n2


def multiplica(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def main():
    print(logo)
    operacoes = {
        "+": adiciona,
        "-": subtrai,
        "*": multiplica,
        "/": divide
    }

    print("Operações: ")
    for operacao in operacoes:
        print(operacao)

    numero1 = float(input("\nDigite o primeiro número: "))

    while True:
        operacaoEscolhida = input("Qual operação deseja fazer? ")
        numero2 = float(input("Digite o próximo número: "))

        funcaoOperacao = operacoes[operacaoEscolhida]
        resultado = funcaoOperacao(numero1, numero2)

        print(f"{numero1} {operacaoEscolhida} {numero2} = {resultado}")
        numero1 = resultado

        deveContinuar = input(f"\nPara continuar a calcular com {resultado} digite 'sim' e para iniciar um novo cálculo digite 'novo: ").lower() == "sim"
        print("")

        if not deveContinuar:
            main()


if __name__ == "__main__":
    main()
