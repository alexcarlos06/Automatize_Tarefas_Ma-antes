# Exemplo de conversão de variável alterando o escopo dentro de uma função


def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
