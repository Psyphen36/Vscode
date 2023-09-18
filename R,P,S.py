import random

#! Rock Paper Scissor Game
player = 0
score = 0
comp_score = 0
times = 0
while True:
    user = input('Enter (r,p,s) for rock,paper,scissor: ').lower()

    des = [0,1,2]

    computer = random.choice(des)

    if user == 'r':
        player = 0
    elif user == 'p':
        player = 1
    elif user == 's':
        player = 2
    else:
        print('Enter correct syntax!!')
        continue

    if computer == 0:
        comp = 'rock'
    elif computer == 1:
        comp = 'paper'
    elif computer == 2:
        comp = 'scissor'

    print(f'Computer chooses {comp}')

    if player == 0 and computer == 0:
        print('Draw!!')
        times+=1
    elif player == 1 and computer == 1:
        print('Draw!!')
        times+=1
    elif player == 2 and computer == 2:
        print('Draw!!')
        times+=1
    elif player == 0 and computer == 1:
        print('computer wins!!')
        comp_score+=1
        times+=1
    elif player == 0 and computer == 2:
        print('You win!!')
        score+=1
        times+=1
    elif player == 1 and computer == 0:
        print('You win!!')
        score+=1
        times+=1
    elif player == 2 and computer == 0:
        print('computer wins!!')
        comp_score+=1
        times+=1
    elif player == 1 and computer == 2:
        print('computer wins!!')
        comp_score+=1
        times+=1
    elif player == 2 and computer == 1:
        print('You win!!')
        score+=1
        times+=1

    ask = input('Press ("p") to play again or ("q") to quit: ').lower()
    if ask == 'q':
        break
print('-'*50)
print(f'Total times you played the game is {times}')
print(f'you win {score} times and computer win {comp_score} times')


        