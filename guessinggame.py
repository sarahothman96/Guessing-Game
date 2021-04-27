import random
guessAttempts = 0
chances = 4
number = random.randint(1,15)
# Ask User to give name
print("Hello! I'm Hairiz, your computer guessing game. How about you?")
myName = input()
print("Hey",myName,"welcome to Guess Game. I'm thinking the number 1 to 15. Please wait...")
# use while loop for iteration that not fixed
while guessAttempts < 4:
    print("Take a guess... We give",chances,"chance(s).")
    guess = input()
    guess = int(guess)

    guessAttempts += 1
    chances -= 1

    # if-else loop for condition
    if guess > number:
        print("Your Guess is too HIGH. Try again...")
    if guess < number:
        print("Your Guess is too LOW. Try again...")
    if guess == number:
        break # out of the iteration
if guess == number:
    print("Congratulation, {}!".format(myName))
    print("Your Guesses the number in ",guessAttempts,"attempt(s)")
if guess != number:
    print("GAME OVER.\nThe Number that I was thinking is: ",number)
