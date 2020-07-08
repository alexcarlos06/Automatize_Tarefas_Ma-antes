# Apresentação elegante com pprint()
import pprint

message = 'It	was	a	bright	cold	day	in	April,	and	the	clocks	were	striking	thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(
    count)  # Utilizando a instrução pprint não precisamos colocar uma instrução for para termos os resultados aninhados
