board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# Возвращаем доску
def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

# Регистрируем ход и вставляем символ вместо цифры
def reg_step(step, symbol):
    ind = board.index(step)
    board[ind] = symbol

# Проверяем есть ли выигрышная комбинация
def exam():
    win = ''
    for i in victories:
        if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
            win = 'X'
        if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
            win = 'O'
    return win

# Проверяем, есть ли ничья
def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

# Пишем игровой процесс
player1 = True
game_over = False

print('Добро пожаловать в игру "Крестики Нолики"')
print('----------------------------------------')

while not game_over:
    print_board(board)

    if player1:
        symbol = 'X'
        step = int(input('Игрок X, сделайте ход (введите число от 1 до 9): '))
    else:
        symbol = 'O'
        step = int(input('Игрок O, сделайте ход (введите число от 1 до 9): '))

    # Проверяем, что вводимое значение допустимо и клетка свободна
    if step < 1 or step > 9 or board[step - 1] in ['X', 'O']:
        print("Недопустимый ход. Попробуйте снова.")
        continue

    reg_step(step, symbol)
    win = exam()

    if win:  # Если есть победитель
        game_over = True
    elif is_draw(board):  # Если есть ничья
        game_over = True

    player1 = not player1

# Объявляем результат
print_board(board)
if win:
    print('Победил игрок -', win, '!!!')
else:
    print('Игра закончилась вничью!')