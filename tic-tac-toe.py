import random


def display_board(board):
	print("---------")
	for row in board:
		print("|", end="")
		for cell in row:
			print(f" {cell} ", end="|")
		print("\n---------")


def check_winner(board):
	for row in board:
		if row[0] == row[1] == row[2] != ' ':
			return row[0]

	for col in range(3):
		if board[0][col] == board[1][col] == board[2][col] != ' ':
			return board[0][col]

	if board[0][0] == board[1][1] == board[2][2] != ' ':
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] != ' ':
		return board[0][2]

	return None


def make_computer_move(board):
	for row in range(3):
		for col in range(3):
			if board[row][col] == ' ':
				board[row][col] = 'O'
				if check_winner(board) == 'O':
					return

				board[row][col] = ' '

	for row in range(3):
		for col in range(3):
			if board[row][col] == ' ':
				board[row][col] = 'X'
				if check_winner(board) == 'X':
					board[row][col] = 'O'
					return

			board[row][col] = ' '

	while True:
		row = random.randint(0, 3)
		col = random.randint(0, 3)
		if board[row][col] == ' ':
			board[row][col] = 'O'
			return


def play():
	board = [[' ' for _ in range(3)] for _ in range(3)]
	player = 'X'

	print('Welcome to tic-tac-toe!!')
	display_board(board)

	while True:
		if player == 'X':
			row = int(input('Enter row from (0,2): '))
			col = int(input('Enter col from (0,2): '))

			if board[row][col] != ' ':
				print('Invalid move.The place is already taken!!')
				continue

			board[row][col] = player
		else:
			make_computer_move(board)

		display_board(board)

		winner = check_winner(board)
		if winner:
			if winner == 'X':
				print('Congratulations!! You win!!')
			else:
				print('You lost!!')
			break

		if all(all(cell != ' ' for cell in row) for row in board):
			print('Its a tie!!')
			break

		player = 'O' if player == 'X' else 'X'


play()

