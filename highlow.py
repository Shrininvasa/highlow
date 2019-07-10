import random as r

print("Welcome to game of HighLow.")
print("How many guesses would you like to have??")
nog = int(input()) # Number of Guesses

number = int(r.random()*100)
print(number)
print("Okay I have chosen a number between 1 and 100.")
print("You have", nog, "number of guesses to guess it.")

while nog > 0:
    count = 1
    guess = int(input())
    if guess == number:
        print("CONGRATULATIONS, you guesed correctly, in", count, "rounds.")
        break
    if guess > number:
        print("Your guess is Too High.")
    if guess < number:
        print("Your guess is Too Low.")
    nog -= 1
    count += 1

print("You Lose. The correct answer is:", number, ".")
