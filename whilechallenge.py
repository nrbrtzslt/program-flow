import random

guess = ''
highest = 1000
answer = random.randint(1, highest)

while guess != answer:
    print("Please guess a number between 1 and {}: ".format(highest))
    guess = int(input())
    if guess == 0:
        print("Terminating program")
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("That is correct!")
