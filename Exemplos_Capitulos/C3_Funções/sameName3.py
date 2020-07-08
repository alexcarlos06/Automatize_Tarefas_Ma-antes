# Exemplo de variável em escopo global e local


def spam():
    global eggs
    eggs = 'spam'  # essa é a variável global


def bacon():
    eggs = 'bacon'	 # essa é uma variável local


def ham():
    print(eggs)  # essa é a variável global


eggs = 42  # essa é a variável global
spam()

print(eggs)
