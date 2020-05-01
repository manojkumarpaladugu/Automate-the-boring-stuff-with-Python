# This program asks user to guess a number
import random

# Ask user name
print('Enter your name: ', end='')
name = input()
print('Hello', name + '!,', 'Let us play a game guess number')
print('Yout have to enter a number between 10 to 20')

#generate a random number
randomNumber = random.randint(10, 20)

for guessCount in range(1, 6, 1):
    # ask user to guess a number
    print('Take a guess: ', end='')
    userGuess = int(input())
    if(userGuess < randomNumber):
        print('Your guess is low')
    elif (userGuess > randomNumber):
        print('Your guess is high')
    if (userGuess == randomNumber):
        break

if (userGuess == randomNumber):
        print('Good job,', name + '!,', 'You guessed it correctly in', guessCount, 'guesses')
else:
    print('Hey,', name + '!,', 'you missed it, the secret number is', randomNumber)
