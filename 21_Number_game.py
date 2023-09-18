def nearestMultiple(num):
    if num >= 4:
        num = num + (4 - (num%4))
    return num


def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i += 1
    return True


def loose():
    print('\nYOU LOSE!!')
    print('Better luck nex time!!')
    exit(0)


def start():
    xyz = []
    last = 0

    while True:
        print('Enter "F" to take the first chance.')
        print('Enter "S" to take the second chance.')
        chance = input('>' ).lower()
        
        if chance == 'f':
            while True:
                if last >= 20:
                    loose()
                else:
                    print('You turn.')
                    print('How many number do you wish to enter.')
                    num = int(input('> '))

                    if num > 0 and num <= 3:
                        comp = 4 - num
                    else:
                        print('Invalid input you are disqualified.')
                        loose()

                    i, j = 1, 1

                    print('Enter the value.')
                    while i <= num:
                        a = int(input('>'))
                        xyz.append(a)
                        i += 1

                    last = xyz[-1]
                    if check(xyz) == True:
                        if last == 21:
                            loose()
                        
                        else:
                            while j <= comp:
                                xyz.append(last + j)
                                j += 1
                            print('Order of inputs after computer\'s turn is:')
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print('You did not enter consecutive integers.')
                        loose()
        elif chance == 's':
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                print('Order of inputs after computer\'s turn is:')
                print(xyz)
                if xyz[-1] == 20:
                    loose()
                else:
                    print('Your turn.')
                    print('How many number do you wish to enter:')
                    num = int(input('> '))
                    i = 1

                    print('Enter your values.')
                    while i <= num:
                        xyz.append(int(input('> ')))
                        i += 1
                    last = xyz[-1]
                    
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print('You did not insert consecutive integers.')
                        loose()
            print('Congratulations!!')
            print('You won!!')
            exit()
        else:
            print('Wrong choice!!')

game = True
while game == True:
    print('Do you want to play the game ("yes/no"): ')
    perm = input('> ').lower()
    if perm == 'yes':
        start()
    else:
        print('Do you want to exit the game ("yes/no")')
        another_perm = input('> ').lower()

        if another_perm == 'yes':
            print('You are quitting the game...')
            exit()
        elif another_perm == 'no':
            print('Continue...')
        else:
            print('Invalid input!!')











