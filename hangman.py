import random


def guess_word():
	rand_words = ['volcano', 'mango', 'tsunami', 'mohanjodaro', 'hallucination', 'integration', 'marlboro','donxiotedoflamingo']
	word = random.choice(rand_words).lower()
	guessed_letters = []
	tries = 6
	print('Welcome to Hangman!!')
	print('Guess the word by entering one letter at a time. You have 6 tries.')

	while True:
		display_word = ''
		for letter in word:
			if letter in guessed_letters:
				display_word += letter + ''
			else:
				display_word += '_ '

		print('\n', display_word)

		if display_word.replace(' ', '') == word:
			print('Congratulations!! You guess the right word!!')
			break

		if tries == 0:
			print('Game Over!! You are out of tries!!')
			print(f'The word is {word}')
			break

		guesser = input('Enter a letter: ').lower()

		if len(guesser) != 1 or not guesser.isalpha():
			print('Invalid input.Please enter a single letter.')
			continue

		if guesser in guessed_letters:
			print('You already guessed this letter.')
			continue

		guessed_letters.append(guesser)

		if guesser not in word:
			tries -= 1
			print(f'Incorrect guess!!.You only have {tries} tries left.')


if __name__ == '__main__':
	guess_word()
