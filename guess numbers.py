'''
Make a game guess the number
Generate random numbers between 1 and 10 and the u guess what that number can be
only three chances are allowed else print msg "You lost the game"
'''
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    chance = 3

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 10. You have 3 chances to guess it.")

    for chance in range(1, chance + 1):
        guess = int(input(f"Attempt {chance}: Enter your guess: "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the number!")
            break
        elif chance < chance:
            print("Wrong guess. Try again!")
        else:
            print("You lost the game. The number was:", number_to_guess)

if __name__ == "__main__":
    guess_the_number()
