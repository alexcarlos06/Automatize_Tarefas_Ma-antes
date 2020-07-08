# Este é um	jogo de adivinhar o número.
import random

secretNumber = random.randint(1, 20)
guess = 0
guessesTaken = 0

print('I am thinking of a number between 1 and 20.')
# Peça para o jogador adivinhar	6 vezes.

for guessesTaken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break  # Esta	condição	corresponde	ao	palpite	correto!
    except ValueError:
        print(f'{guess} não é um número inteiro.')
        continue
if guess == secretNumber:
    print('Good	job! You guessed my	number in ' + str(guessesTaken) + '	guesses!')
else:
    print('Nope. The number was thinking of	was	' + str(secretNumber))
