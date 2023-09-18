import random 
import time



OPERATOR = ['*', '-', '+']
MIN_VALUE = 3
MAX_VALUE = 15
PROBLEMS = 10


def ask_questions():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATOR)

    exp = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(exp)
    return exp, answer


wrong = 0
input('Press enter to start:')
print('='*30)

start_time = time.time()

for i in range(PROBLEMS):
    exp, answer = ask_questions()

    while True:
        guess = input(f'#{i+1}. {exp} = ')
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()

total_time = end_time - start_time

print('='*30)
print(f'Nice work! You finished it in {total_time:.2f} seconds')
print(f'Total problems you did wrong is {wrong}')





