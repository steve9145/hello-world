import random

# create the die
# begin the roll
# Random selection of the side
# Print out the result
# Repeat, or break out
die = 1
rolling = True

while rolling:
	die = random.randint(1,6)
	print('You roll the die, and you got a %i' % die)
	
	prompt = raw_input("Would you like to roll again?: y/n ")
	if prompt == 'y':
		rolling = True
	elif prompt == 'n':
		rolling = False
	else:
		prompt = raw_input("Incorrect option.  Please select y or n to continue")