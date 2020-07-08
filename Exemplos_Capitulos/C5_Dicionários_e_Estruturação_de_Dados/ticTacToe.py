# Manipulando um tabuleiro de jogo da velha com o uso de dicionário
# ao alterar a chave do dicionário vamos inserir a jogada no tabuleiro

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(f'\t{board["top-L"]} | {board["top-M"]} | {board["top-R"]}')
    print('\t--+---+--')
    print(f'\t{board["mid-L"]} | {board["mid-M"]} | {board["mid-R"]}')
    print('\t--+---+--')
    print(f'\t{board["low-L"]} | {board["low-M"]} | {board["low-R"]}')


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f'Turn for {turn}. Move on which space?')
    move = input()
    theBoard[move] = turn
if turn == 'X':
    turn = 'O'
else:
    turn = 'X'
printBoard(theBoard)
