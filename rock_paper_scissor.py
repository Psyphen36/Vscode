import random


def player_choice(player):
    out_player = 0
    if player == 'r' or player == 'rock':
        out_player = 0
    elif player == 'p' or player == 'paper':
        out_player = 1
    elif player == 's' or player == 'scissor':
        out_player = 2
    else:
        return -1
    return out_player


def comp_convert(computer):
    if computer == 0:
        return 'rock'
    elif computer == 1:
        return 'Paper'
    else:
        return 'Scissor'


def player_convert(player):
    if player == 'r' or player == 'rock':
        return 'Rock'
    elif player == 'p' or player == 'paper':
        return 'Paper'
    elif player == 's' or player == 'scissor':
        return 'Scissor'


flag = True

game = 0
comp_win = 0
player_win = 0
draw = 0

while flag:
    player = input('Enter your choice:\n 1. Rock("r")\n2. Paper("p")\n3. Scissor("s")\n> ').lower()

    p = player_choice(player)

    rand_comp = random.randint(0,2)

    comp_eng = comp_convert(rand_comp)

    player_eng = player_convert(player)

    print('-'*50)

    if p == rand_comp :
        print(f'computer chooses {comp_eng} and player chooses {player_eng}')
        print('Draw')
        game += 1
        draw += 1

    elif (p == 0 and rand_comp == 1 or p == 1 and rand_comp == 2 or p == 2 and rand_comp == 0):
        print(f'computer chooses {comp_eng} and player chooses {player_eng}')
        print('Computer is the winner')
        game += 1
        comp_win += 1
        print('-'*50)

    elif (p == 0 and rand_comp == 2 or p == 1 and rand_comp == 0 or p == 2 and rand_comp == 2):
        print('-'*50)
        print(f'computer chooses {comp_eng} and player chooses {player_eng}')
        print()
        print('You win')
        game += 1
        player_win += 1
        print('-'*50)

    elif p == -1:
        print('Invalid Syntax!!')
        
    again = input('Do you want to play again? (y/n): ').lower()
    if again == 'n':
        break
print() 
print('Thanks for playing the game!!\n')

print(f'Total time you played the game = {game}\n Total times computer wins = {comp_win} \n Total times you win = {player_win} \n Total times the game is draw = {draw} ')
