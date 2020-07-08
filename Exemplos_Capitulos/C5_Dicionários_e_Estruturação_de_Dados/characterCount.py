# Programa conta a quantidade de caracteres repetidos em uma string
# Exemplo de uso do comando setdefaut()

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:  # Percorre todos os caracteres contidos na string
    count.setdefault(character, 0)  # Caso a chave não esteja no dicionárioseta o valor como 0 para não ocorrer erro
    count[character] = count[character] + 1

print(count)