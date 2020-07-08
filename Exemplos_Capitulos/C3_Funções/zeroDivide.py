# Exemplo de tratamento de exceção


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Não é possível dividir uma valor por zero!'


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
