import random
times = 0
P1 = 0 
P2 = 0  
draws = 0    
def convert(str):
    if str == 'r':
        return 0
    elif str == 'p':
        return 1
    elif str == 's':
        return 2 
    else:
        return -2

def item_conv(item):
    if item == 0:
        return 'Rock'
    elif item == 1:
        return 'Paper'
    elif item == 2:
        return 'Scissor'

def check(computer,player):
    global times,P1,P2,draws 

    if computer == player:
        draws += 1
        times +=1
        return 0
    elif computer == 0 and player == 2:
        P1 += 1
        times += 1
        return -1
    elif computer == 1 and player == 0:
        P1 += 1
        times += 1
        return -1
    elif computer == 2 and player == 1:
        P1 += 1
        times += 1
        return -1
    elif player == -2:
        return -2
    else:
        P2 += 1
        times += 1
        return 1

if __name__ == '__main__':
    while True:
        print('-'*50)
        user = input('Press ("r","p" or "s") for rock,paper or scissor: ').lower()


        comp_choice = random.randint(0,2)
        new_comp = item_conv(comp_choice)

        conv = convert(user)
        new_conv = item_conv(conv)
        play = check(comp_choice,conv)

        if play == -2:
            print('Invalid syntax')
            continue

        print(f'Computer choose {new_comp}')
        print(f'You choose {new_conv}')

        if play == 1:
            print('You won!!')
        elif play == -1:
            print('Computer won!!')
        elif play == 0:
            print('Draw')

        ask = input('Press ("c") to continue or ("q") to quit: ').lower()
        print('-'*50)
        if ask == 'q':
            break

    print(f'Total times you play {times}')
    print(f'Draws {draws}')
    print(f'Computer wins {P1} times')
    print(f'You win {P2} times')




