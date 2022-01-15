import subprocess
import sys


def get_player_markers():
    player1_marker = ''
    player2_marker = ''
    while True:
        player1_marker = input('\nPlease select marker for Player 1 (X or O): ')
        if player1_marker.upper() != 'X' and player1_marker.upper() != 'O':
            print(f'\'{player1_marker}\' is not a valid option. Please try again.')
        else:
            player1_marker = player1_marker.upper()
            break

    player2_marker = 'O' if player1_marker == 'X' else 'X'
    print(f'\nPlayer 1 marker is {player1_marker}\nPlayer 2 marker is {player2_marker}\n')

    return (player1_marker, player2_marker)


def print_board(board_values):
    print(f'\n {board_values[0]} | {board_values[1]} | {board_values[2]}')
    print('---|---|---')
    print(f' {board_values[3]} | {board_values[4]} | {board_values[5]}')
    print('---|---|---')
    print(f' {board_values[6]} | {board_values[7]} | {board_values[8]}\n')


def get_board_input(player, board_values):
    while True:
        board_input = input(f'\nPlayer {player} select the board location: ')

        if not board_input.isnumeric():
            print('Invalid input, value must be numberic, try again!')
        elif int(board_input) < 1 or int(board_input) > 9:
            print(f'Invalid input, value must be between 1 & 9, try again')
        elif not board_values[int(board_input) - 1] == ' ':
            print(
                f'Spot {int(board_input)} is taken, please select another location')
        else:
            subprocess.check_call(['cls'], shell=True)
            return int(board_input)


def verify_winner(board_values, player1_marker):
    match_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for item in match_list:
        if (board_values[item[0]] != ' ') and (board_values[item[0]] == board_values[item[1]] == board_values[item[2]]):
            winner = "Player1" if board_values[item[0]] == player1_marker else 'Player2'
            print('\n****************************************')
            print(f'*** Congratulations: {winner} has won ***')
            print('****************************************\n')
            return True


def play_again():
    play_again = input("Would you like to play again? ('y' -> yes, any other key -> no): ")
    if play_again == 'y':
        main()
    else:
        print('Exiting Game. Bye!')
        sys.exit()


def main():
    player1_marker, player2_marker = get_player_markers()
    board_values = [' '] * 9
    print_board(board_values)

    current_player = 2
    while True:
        current_player = 2 if current_player == 1 else 1

        board_item_count = 0
        for val in board_values:
            if val == 'X' or val == 'O':
                board_item_count += 1

        if board_item_count > 8:
            print(f'Board Full, No Winners')
            play_again()

        input_from_player = get_board_input(current_player, board_values)
        board_values[input_from_player - 1] = player1_marker if current_player == 1 else player2_marker
        print_board(board_values)
        winner_confirmed = verify_winner(board_values, player1_marker)
        if winner_confirmed:
            play_again()


if __name__ == "__main__":
    main()
