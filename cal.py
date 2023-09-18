def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def DD(x,y):
    return x//y

if __name__=="__main__":
    while True:
        print('''1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
6.DoubleDivide''')
        user = input('Select a number between (1 to 6) to do operations: ')

        if user in ('1','2','3','4','5','6'):
            try:
                num1 = float(input('Enter first value: '))
                num2 = float(input('Enter second value: '))

                if user == '1':
                    print(f'{num1} + {num2} = {add(num1,num2)}')
                elif user == '2':
                    print(f'{num1} - {num2} = {sub(num1,num2)}')
                elif user == '3':
                    print(f'{num1} x {num2} = {mul(num1,num2)}')
                elif user == '4':
                    print(f'{num1} / {num2} = {div(num1,num2)}')
                elif user == '5':
                    print(f'{num1} % {num2} = {mod(num1,num2)}')
                elif user == '6':
                    print(f'{num1} // {num2} = {DD(num1,num2)}')
            except ValueError:
                print('!!Invalid Syntax!! ')
        else:
            print('SyntaxError: Invalid Syntax!!')

        ques = input('Do you want to continue(y/n): ').lower()
        if ques == 'n':
            break
