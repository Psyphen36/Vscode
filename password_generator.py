import secrets
import string

def pass_generator(length):

    password = ''  
    min_length = 5

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    punc = string.punctuation
    int_value = '0,1,2,3,4,5,6,7,8,9'

    pwd = upper + lower + punc + int_value 

    while length:
        if length < min_length:
            print('minimum length is required i.e(5)!!')
            length = int(input('Please enter at least minimum length: '))
            continue
        for _ in range(length):
            password += ''.join(secrets.choice(pwd))
        break   

    print(f'your password is = {password}')

if __name__ == '__main__':
    user = int(input('Choose the length of the password minimum(5 char): '))
    pass_generator(user) 
    