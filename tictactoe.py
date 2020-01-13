import os

def main():

    player_1 = 1
    player_2 = 2
    player_move = True # for switching players between next rounds
    round = 1          # There is no possibility to achieve more than 9 rounds, so there is a counter
    move_check = True  # Variable to check if move is legal (must be first assign to True for start game

    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Initial board

    while check_score(table) and round <= 9:
        os.system('clear') # To keep clean on screen
        print_table(table)
        if move_check == False:
            print('Incorrect move!')
        if player_move:
            move_check = move(player_1, table)
        else:
            move_check = move(player_2, table)
        if move_check:
            player_move = not player_move # Switch to next player
            round += 1
        else:
            continue # If move is incorrect, than do not change player and start round again

    if not check_score(table): # If score returns False, than one of players win
        os.system('clear')
        print_table(table)
        if player_move:
            print('Player 2 Win!')
        else:
            print('Player 1 Win!')

    if round > 9: # If rounds counter is greater than 9, that means tie in game
        os.system('clear')
        print_table(table)
        print(' ')
        print("It's tie!")
        print(' ')

    return

def check_score(tab):

# Check if one of players win. If there are 3 same signs on row, column or cross, that means one of players win
    if len(set(tab[0])) != 1 and len(set(tab[1])) != 1 and len(set(tab[2])) != 1 and len(set([tab[0][0], tab[1][0], tab[2][0]])) != 1 and len(set([tab[0][1], tab[1][1], tab[2][1]])) != 1 and len(set([tab[0][2], tab[1][2], tab[2][2]])) != 1 and len(set([tab[0][0], tab[1][1], tab[2][2]])) != 1 and len(set([tab[0][2], tab[1][1], tab[2][0]])) != 1:
        return True
    else:
        return False

def print_table(tab):
# Print table to get nice format
    print('{0:_^5} {1:_^5} {2:_^5}'.format('_', '_', '_'))
    print(' ')
    print('|{0:^3} | {1:^4}| {2:^3} |'. format(tab[2][0], tab[2][1], tab[2][2]))
    print('{0:_^5} {1:_^5} {2:_^5}'.format('_', '_', '_'))
    print(' ')
    print('|{0:^3} | {1:^4}| {2:^3} |'. format(tab[1][0], tab[1][1], tab[1][2]))
    print('{0:_^5} {1:_^5} {2:_^5}'.format('_', '_', '_'))
    print(' ')
    print('|{0:^3} | {1:^4}| {2:^3} |'. format(tab[0][0], tab[0][1], tab[0][2]))
    print('{0:_^5} {1:_^5} {2:_^5}'.format('_', '_', '_'))

def move(player_num, tab):
    if player_num == 1:
        sign = 'x'
    else:
        sign = 'o'
    print(' ')
    place = int(input("Player {} turn, your sign is {}, where to put it? ".format(player_num, sign)))
# Check if field is valid to put sign. If choose field isn't integer, that means other sign was put earlier.
    if place == 1 and tab[0][0] == 1:
        tab[0][0] = sign
    elif place == 2 and tab[0][1] == 2:
        tab[0][1] = sign
    elif place == 3 and tab[0][2] == 3:
        tab[0][2] = sign
    elif place == 4 and tab[1][0] == 4:
        tab[1][0] = sign
    elif place == 5 and tab[1][1] == 5:
        tab[1][1] = sign
    elif place == 6 and tab[1][2] == 6:
        tab[1][2] = sign
    elif place == 7 and tab[2][0] == 7:
        tab[2][0] = sign
    elif place == 8 and tab[2][1] == 8:
        tab[2][1] = sign
    elif place == 9 and tab[2][2] == 9:
        tab[2][2] = sign
    else:
        print('incorrect move!')
        return False

    return True

if __name__ == '__main__':
    main()
