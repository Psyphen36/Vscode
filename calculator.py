import math


def add(a, b):
	return a + b


def sub(a, b):
	return a - b


def mul(a, b):
	return a * b


def div(a, b):
	return a / b


def modul(a, b):
	return a % b


def inp():
	a = float(input('Enter first number: '))
	b = float(input('Enter second number: '))
	return a, b


def main():
	print('!!Welcome to the anonymous calculator!!')
	print('''=============== Main Menu ===============
	
	1. Add
	2. Subtract
	3. Multiply
	4. Divide
	5. Percent
	6. Square root
	7. Exponent
	8. Exit
	
=========================================
''')
	while True:
		user = int(input('Choose the number from the main menu: '))

		if user == 1:
			num = inp()
			addition = add(*num)
			print(addition)

		elif user == 2:
			num = inp()
			subtraction = sub(*num)
			print(subtraction)

		elif user == 3:
			num = inp()
			multiply = mul(*num)
			print(multiply)

		elif user == 4:
			num = inp()
			divide = div(*num)
			print(divide)

		elif user == 5:
			num = inp()
			percentage = modul(*num)
			print(percentage)

		elif user == 6:
			num = float(input('Enter the value to get its square root: '))
			square_root = math.sqrt(num)
			print(square_root)

		elif user == 7:
			num = float(input('Enter the value to get its exponential value: '))
			exp = int(input('Enter the exponent/power for the value: '))

			exponent = num ** exp
			print(exponent)

		if user == 8:
			print('='*80)
			print('Thankyou!! for using the Anonymous calculator we hope you enjoy using it!!')
			print('='*80)
			break


if __name__ == '__main__':
	main()

