import random

num = random.randint(0, 100)
print(num)
guess = float(input("Type a number 1-100: "))
guessed = False

try:
    while(guessed == False):
        if (guess > num):
            print("Higher")

        if (guess < num):
            print("Lower")

        if (guess == num):
            print("You have guessed the number")
            guessed = True
            breakpoint()
except ValueError:
    print("Please input a number 1-100")