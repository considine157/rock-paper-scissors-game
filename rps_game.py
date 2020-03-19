from random import randint

#Establish a list of player moves.

player_moves = ['Rock', 'Paper', 'Scissors']

#Assigning the computer's move as random.

computer = player_moves[randint(0,2)]

#Set player to False.

player = False

#Defining conditions for the game.
while player == False:
	player = input('Rock, Paper, Scissors?')
	if player == computer:
		print('Tie!')
	elif player == 'Rock' and computer == 'Paper':
			print('You lose! Paper covers rock!')
	elif player == 'Paper' and computer == 'Rock':
		 	print('You win! Paper covers rock!')
	elif player == 'Paper' and computer == 'Scissors':
		print('You lose! Scissors cuts Paper!')
	elif player == 'Scissors' and computer == 'Paper':	
		print('You win! Scissors cuts Paper!')
	elif player == 'Scissors' and computer == 'Rock':
		print('You lose! Rock smashes scissors!')
	elif player == 'Rock' and computer == 'Scissors':
		print('You win! Rock smashes scissors!')
		player = False
		computer = player_moves[randint(0,2)]

