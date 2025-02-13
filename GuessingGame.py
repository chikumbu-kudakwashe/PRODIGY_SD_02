import random

random_number = random.randint(0,9) #generates a random number between 0 and 9

number_of_guesses = 0


while True:
    while True: 
        '''
        prompts the user to enter their guess as an integer
        '''
        try:
            user_input = int(input('Please enter your guess: '))
            break
        except ValueError:
            print('Invalid input, enter an integer')
    
    number_of_guesses += 1

    if random_number == user_input: #compares the computer generated number and the user's guess
        print(f'\nYou have won with {number_of_guesses} attempt(s)')
        break
    elif user_input > random_number:
        print('\nValue too high, try again')

    else:
        print('\nValue too low, try again')