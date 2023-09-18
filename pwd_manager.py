def add():
    name = input('Enter your account name: ')
    pwd = input('Enter your password: ')
    with open('password.txt','a') as f:
        f.write(f'{name}:{pwd}\n')

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(':')
            print(f'user: {user}, password: {pwd}')

while True:
    user = input('Do you want to ("add") a password or ("view") existing one or press ("q") to exit? ').lower()
    if user == 'q':
        break
    elif user == 'add':
        add()
        ask = input('Do you want to add more ("y/n"): ').lower()
        if ask == 'y':
            continue
        elif ask == 'n':
            break
    elif user == 'view':
        view()
    else:
        print('Invalid input!! Try again!!')
        continue

