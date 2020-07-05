# Programa demonstra Conjectura de Collatz


def collatz(number):
    if number % 2 == 0:
        temporario = number // 2
    else:
        temporario = 3 * number + 1
    print(temporario)
    return temporario


if __name__ == '__main__':
    retorno = 0
    try:
        numero = int(input('Informe um valor inteiro: '))
        while retorno != 1:
            retorno = collatz(numero)
            numero = retorno
            continue
    except ValueError:
        print('Não foi digitado um valor do tipo inteiro')
        print('Programa encerrado!')




