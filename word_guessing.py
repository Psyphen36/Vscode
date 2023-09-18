import random

name = input('Enter your name: ')

print(f'Hello {name} welcome to word_guessing game')

data = ['SteveJobs','Introspection','Hallucination','AbulPakeerJanuelAbadeenAbdulKalam','Thermodynamics']

word = random.choice(data)

guesses = ''
failed = 0
chance = 10

while chance > 0:
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print('_')
            failed += 1

    if failed == 0:
        print('You win!!')
        print('The word is', word)
        break

    print()
    guess = input('guess a character: ')

    guesses += guess

    if guess not in word:
        print('Incorrect character!! Try Again!!')
        chance -= 1
        print(f'You have {chance} try left!!')
    
        if chance == 0:
            print('You loose!!')

