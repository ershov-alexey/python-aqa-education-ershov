import logging
from pathlib import Path
import sys

Path("logs").mkdir(parents=True, exist_ok=True)
FILENAME = 'game_log.log'


def configure_logger():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(FILENAME)
    file_handler.setLevel(logging.WARNING)
    file_format = logging.Formatter('%(asctime)s %(message)s', "%d-%b-%Y %H:%M:%S")
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)

    stream_handler.setLevel(logging.WARNING)
    console_format = logging.Formatter('%(message)s')
    stream_handler.setFormatter(console_format)
    logger.addHandler(stream_handler)
    return logger


log = configure_logger()


def show_logs():
    try:
        with open(FILENAME, "r") as log_file:
            print(log_file.read())
    except OSError:
        log.critical('File not found')
    else:
        log_file.close()
    return main()


def clear_logs():
    try:
        with open(FILENAME, "w") as log_file:
            log_file.truncate()
    except OSError:
        log.critical('File not found')
    else:
        log_file.close()
    return main()


def display_board(board):
    blankBoard = """
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1, 10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)


def player_input():
    while True:
        player1 = input("Please pick a marker 'X' or 'O' ")
        if player1.upper() == 'X':
            player2 = 'O'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        print('Enter only X or O!!!')
        continue


def place_marker(board, marker, position):
    board[position] = marker
    return board


def space_check(board, position):
    return board[position] == '#'


def full_board_check(board):
    return len([x for x in board if x == '#']) == 1


def win_check(board, mark):
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in range(0, len(win_list)):
        result = all(board[element] == mark for element in win_list[i])
        if result:
            break
    return result

def player_choice(board):
    while True:
        try:
            choice = input("Please select an empty space between 1 and 9 : ")
            if int(choice) < 1 or int(choice) > 9:
                print('Enter only numbers between 1 and 9!!!')
                continue
            if not space_check(board, int(choice)):
                print("This space isn't free. Please choose between 1 and 9 : ")
                continue
            else:
                return choice
        except ValueError:
            print('Enter only numbers between 1 and 9!!!')


def play_game():
    i = 1
    players = player_input()
    # Empty board init
    board = ['#'] * 10
    # game_on = full_board_check(board) #пока не будет равно 1 (не будет свободных клеток
    while True:
        # Who's playing ?
        marker = players[1] if i % 2 == 0 else players[0]
        # Player to choose where to put the mark. Play !
        place_marker(board, marker, int(player_choice(board)))
        # Check the board
        display_board(board)
        i += 1
        if win_check(board, marker):
            log.warning(f'{marker} wins')
            print("You won !")
            return
        elif full_board_check(board):
            log.warning('Tie')
            return

def main():
    options = {'1': 'Play game', '2': 'Show Logs', '3': 'Clear Logs', '0': 'Exit'}
    actions = {'1': play_game, '2': show_logs, '3': clear_logs, '0': exit}
    for k in options:
        print(f"{k}: {options.get(k)}", sep="\n")
    try:
        user_choice = input('> ')
        actions[user_choice]()
    except KeyError:
        print("This option does not exist.\nPlease try again")
    return main()


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    main()
