import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

print('Welcome!! to Countdown program!!')

count = int(input('Enter your timer:\n> '))

if count > 0:
    countdown(count)
else:
    print('Invalid Input!!')

print('Thanks for using this program!!')
