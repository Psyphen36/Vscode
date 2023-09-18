import random
from collections import Counter

print('Welcome to hangman game!!')

someWords = ['apple', 'banana', 'mango', 'strawberry', 
'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 
'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! Hint: the word is related to fruit.')
    for i in word:
        print('_ ',end='')
    print()

    chance = len(word) + 2 
    letter_guessed = ''
    correct = 0
    flag = 0

    try:
        while chance != 0 and flag == 0:
            print()

            guess = str(input('Guess the character: '))

            if not (guess.isalpha()):
                print('Invalid character!! Only alphabets are allowed!!')
            elif len(guess) > 1:
                print('Only single character are allowed!!')
            elif guess in letter_guessed:
                print('You already guessed that letter!!')
                chance += 1

            if guess in word:                
                k = word.count(guess)
                for _ in range(k):
                    letter_guessed += guess
            
            if guess not in word:
                    chance -= 1
                    print(f'You have {chance} chances left!!')

            for char in word:
                if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                    print(char,end=' ')
                    correct +=1 
                elif Counter(letter_guessed) == Counter(word):
                    flag = 1
                    print(word)
                    print('Congratulations!! You won!!')
                    
                    break
                else:
                    print('_',end='')

        if chance == 0 and (Counter(letter_guessed) != Counter(word)):
            print()
            print('You lost!! Try again!!')
            print('The word is',word)

    except KeyboardInterrupt:
        print('Bye! Try again!!')
        exit()