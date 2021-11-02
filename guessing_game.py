import random

guesses = 1

print('**** WELCOME TO THE NUMBER GUESSING GAME ****')


def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	best_score = 0
	continue_game = True
	while continue_game == True:
		guess = input(f'Guess a Number between 1 and {x} ')
		if check_number(guess, random_number):
			if best_score == 0 or guesses < best_score:
				best_score = guesses
			print(
				f'Yay, congrats. You have guessed the number {random_number} correctly,it only took you {guesses} guesses!')
			print('Would you like to play again? y/n?')
			print('Your best score is {} tries.'.format(best_score))
			answer = input()
			if answer == 'y':
				continue_game = True
				random_number = random.randint(1, x)
			elif answer == 'n':
				continue_game = False
				print('Thanks for playing, see you next time')


def check_number(guess, random_number):
	global guesses
	if guess.isdigit():
		guess = int(guess)
		if guess < 1:
			print('please guess a number within the range 1-10')
		elif guess > 10:
			print('please guess a number within the range 1-10')
		elif guess < random_number:
			print('Sorry guess again, too low')
			guesses = guesses + 1
		elif guess > random_number:
			print('Sorry guess again, too high')
			guesses = guesses + 1
		if guess == random_number:
			return True
		else:
			return False
	else:
		print('Your guess must use valid digits')


guess(10)


				 