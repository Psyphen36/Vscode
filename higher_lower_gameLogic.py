import random
from art import logo, vs
from game_data import data
import colorama


def assign():
    return random.choice(data)


def compare(p1, p2, userInput):
    sum1 = p1['follower_count']

    sum2 = p2['follower_count']

    max = ''

    if sum1 > sum2:
        max = p1['name']

    elif sum1 < sum2:
        max = p2['name']

    if max == userInput:
        return True
    else:
        return False


def play_higher_lower():
    playing_game = True

    while playing_game:
        score = 0

        still_guessing = True
        while still_guessing:
            print(colorama.ansi.clear_screen())
            colorama.init()
            print(colorama.Fore.LIGHTCYAN_EX,colorama.Style.BRIGHT, logo)

            person1 = assign()
            person2 = assign()

            if score > 0:
                person1 = person2
                person2 = assign()

                if person1 == person2:
                    person2 = assign()

            print(colorama.Fore.LIGHTMAGENTA_EX,f'1. Name {person1["name"]}, Description {person1["description"]}')

            colorama.init()

            print(colorama.Fore.LIGHTGREEN_EX, vs)

            colorama.init()
            print(colorama.Fore.LIGHTMAGENTA_EX, f'2. Name {person2["name"]}, Description {person2["description"]}')

            colorama.init()
            print(colorama.Fore.LIGHTBLUE_EX)
            print('-'*40)
            print(f'Your current score is: {score}')
            print('-'*40)

            colorama.init()
            print(colorama.Fore.RESET)
            guess = input('Enter the name of person with higher followers: ')
            
            if compare(person1, person2, guess):
                score += 1
            else:
                still_guessing = False



        want_to_play = input('Do you want to play again ("y"/"n"): ').lower()

        if want_to_play == 'y':
            print(colorama.ansi.clear_screen())
            play_higher_lower()
        elif want_to_play == 'n':
            print('Program exited successfully.')
            break
        else:
            print('Invalid input taken as no! Program exited!!')
            break

    
if __name__ == '__main__':
    play_higher_lower()
    