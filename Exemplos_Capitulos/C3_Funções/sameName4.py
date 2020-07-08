# Exmplo de escopo de variável (# ERRO #)
# O erro ocorre porque o python entende que existe um variável local com o nome de eggs dentro da função e considera
# eggs sendo uma variável local e não global, assim resultando no erro pois o print está antes da nova atribuição

def spam():
    print(eggs)  # ERRO!
    eggs = 'spam local'


eggs = 'global'
spam()
