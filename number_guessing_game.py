import random
secret_number=random.randint(1,10)
print("==== number guessing game=====")
print("guess a number between 1 and 10")
guess=int(input("Enter your guess:"))
if guess==secret_number:
    print("congratulations! you guessed the correct number.")
else:
    print("Wrong guess!")
    print("The correct number was:",secret_number)
print("Thank you for playing")    
