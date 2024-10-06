num = 9 
guess = None

while guess != num:
    guess = int(input("Enter your guess (1-10): "))

    if guess == num:
        print("You win!")
    elif guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
