import random
import math

num1 = int(input('Select the 1st value from where to start: '))
num2 = int(input('Select the 2nd value to end: '))

comp = random.randint(num1, num2)
print('\n\tYou have only',
        round(math.log(num2 - num1 + 1, 2)),
        'chances to guess the number!\n')

second_comp = comp
count = 0

while count < math.log(num2 - num1 + 1, 2):
    count += 1

    guess = int(input('Guess the number: '))

    if comp == guess:
        print('Congratulations!! You did it in', count, 'try')
        break
    elif not (guess > second_comp) and (guess >= (comp-5)):
        print('low but too close!!')
    elif not (guess < second_comp) and (guess <= (comp+5)):
        print('high but too close!!')
    elif guess <= (comp-5):
        print('Too low!!')
    elif guess >= (comp-5):
        print('Too high!!')
    else:
        print('Invalid input!!')

if count > math.log(num2 - num1 + 1, 2):
    print(f'\n the number is {comp}')
    print('\nbetter luck nex time!!')
    
