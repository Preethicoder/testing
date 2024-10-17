"""Create a variable named secret that random selects a number from 1 to 9 both inclusive.
Ask the player to guess the secret number. Save the guess in a variable named guess.
Compare the secret and guess. If the guess was right print out a message saying "You won! Your guess was right!" Otherwise, inform the user.
Use a for-loop to allow the user to enter maximum of 3 guesses."""
import random

player_1 = random.randint(1, 6)
player_2 = random.randint(1, 6)

print("-------Dice Game --------")
if player_1 > player_2:
    print("Player 1 wins!")
elif player_1 < player_2:
    print("Player 2 wins!")
else:
    print("Draw!")

