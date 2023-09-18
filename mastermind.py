import random

num = random.randrange(1000, 10000)

n = int(input('Guess the four digit number\n> '))

if n == num:
    print('Great you guess the number in 1 try! You are a Mastermind!!')
else:
    counter = 0

    while n != num:
        counter += 1

        count = 0
        correct = ['X']*4

        n, num = str(n), str(num)

        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = n[i]
            else:
                continue

        if count == 7:
            print('You didn\'t guess the correct number within 6 chances you are not a mastermind for now.')
            break
        
        elif count == 0:
            print('None of the numbers are correct from your input!!')
            count += 1
            print(f'Now you have only {6 - count} turns left to guess the number')
        else:
            print(f'Not quite the number. But you did {count} digit correct') 
            print(f'Now you have only {6 - count} turns left to guess the number')

            for display in correct:
                print(display,end=' ')
            print()
            
        again = input('Guess the number again\n> ')
        n = again

    if n == num:
        print(f'Congrats!! you can find the number just {count} tries!! You have the potential of a mastermind')
