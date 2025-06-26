import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the higher Bound: "))

helpGuess = bool(input("Do you want helper after each guess ? (Y/N)") == "Y")

num = random.randint(low, high)

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

chance = 1
win = False

while chance <= 7:
    guess = int(input("Enter your guess: "))
    if num == guess:
        win = True
        break
    else:
        if(helpGuess):
            print("it's " + "Lower" if num < guess else "Higher")
        print("Wrong guess, {} guess left".format(7-chance))
        chance+=1

if win:
    print("GG you guess the number in {} hit(s)!".format(chance))
else:
    print("Loser KEKW, the guess was {}".format(num))