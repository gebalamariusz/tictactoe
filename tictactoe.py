import os

def main():

    player_1 = 1
    player_2 = 2
    player_move = True
    round = 1

    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    while check_score(table) and round <= 9:
        os.system('clear')
        print_table(table)
        if player_move:
            move(player_1, table)
        else:
            move(player_2, table)
        player_move = not player_move
        round += 1

    if not check_score(table):
        os.system('clear')
        print_table(table)
        if player_move:
            print('Player 2 Win!')
        else:
            print('Player 1 Win!')

    if round > 9:
        os.system('clear')
        print("It's tie!")

    return

def check_score(tab):
    if len(set(tab[0])) != 1 and len(set(tab[1])) != 1 and len(set(tab[2])) != 1 and len(set([tab[0][0], tab[1][0], tab[2][0]])) != 1 and len(set([tab[0][1], tab[1][1], tab[2][1]])) != 1 and len(set([tab[0][2], tab[1][2], tab[2][2]])) != 1 and len(set([tab[0][0], tab[1][1], tab[2][2]])) != 1 and len(set([tab[0][2], tab[1][1], tab[2][0]])) != 1:
        return True
    else:
        return False

def print_table(tab):
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
    place = int(input("Your sign is {}, where to put it? ".format(sign)))
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

if __name__ == '__main__':
    main()
