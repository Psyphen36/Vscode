# when its your turn you get to roll the die when you roll the die you get the number from (1 to 6)
# and if you get anything other than (1) you add that in your score
# ex:(you get 5 you score is 5 in next turn you get 6 your score is 11...) but
# when you get 1 whatever is your score now 0 and you can stop whenever you want it's
# like a gambling if you continue  

import random


def dice():
    value = [1,2,3,4,5,6]
    dice_num = random.choice(value)

    return dice_num


while True:
    choose_player = input('Choose the number of players (2-4):')
    if choose_player.isdigit():
        player = int(choose_player)
        if 2 <= player <= 4:
            break
        else:
            print('Please enter a valid number from (2-4)')
    else:
        print('Invalid input please use numbers from (2-4)')

max_score = 50
player_scores = [0 for _ in range(player)]

while max(player_scores) < max_score:
    for player_idx in range(player):
        print('='*50)
        print(f'player number {player_idx + 1} turn just started')
        print(f'Your total score is {player_scores[player_idx]}\n')
        print('='*50)
        current_score = 0
        
        while True:
            should_roll = input('Would you like to roll ("y"/"n")? ')
            if should_roll.lower() != 'y':
                break

            value = dice()
            if value == 1: 
                print('='*50)
                print('Oops!! You rolled a: 1 your turn is over!!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a:', value)

            print(f'Your score is: {current_score}')

        player_scores[player_idx] += current_score
        print(f'Your total score is: {player_scores[player_idx]}')
        print('_'*50)
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f'Player number: {winning_idx + 1} is the winner with score of {max_score}')





            