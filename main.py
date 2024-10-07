def check_win(board, player):
    # Возможные выигрышные комбинации
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
        [0, 4, 8], [2, 4, 6]              # Диагонали
    ]

    # Проверяем, есть ли выигрышная комбинация
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

print("*" * 10, 'Крестики-Нолики', '*' * 10)
board = list(range(1, 10))
for i in range(3):
    print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
current_player = 'X'
while True:
    print("Ход игрока", current_player)
    position = int(input('Куда поставить ' + current_player + '? '))
    
    # Проверяем, что позиция на доске доступна
    if board[position - 1] != 'X' and board[position - 1] != 'O':
        board[position - 1] = current_player
        for i in range(3):
            print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        
        # Проверяем, выиграл ли игрок
        if check_win(board, current_player):
            print("Игрок", current_player, "выиграл!")
            break
        
        # Проверяем, если все поля заполнены и нет победителя (ничья)
        if all(x == 'X' or x == 'O' for x in board):
            print("Ничья!")
            break
        
        # Смена игрока
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Эта позиция уже занята. Попробуйте еще раз.")

