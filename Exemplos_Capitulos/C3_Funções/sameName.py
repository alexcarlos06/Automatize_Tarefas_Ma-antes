# Exemplo de funcionamento de variável em escopo global e local


def spam():
    eggs = 'spam local'
    print(eggs)  # exibe	'spam	local'


def bacon():
    eggs = 'bacon local'
    print(eggs)  # exibe	'bacon	local'
    spam()
    print(eggs)  # exibe	'bacon	local'


eggs = 'global'
bacon()
print(eggs)  # exibe	'global'
