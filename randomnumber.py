import random
n = random.randrange(1,10)
guess = int(input("entre number :"))
while n != guess:
    if guess < n:
        print("too low")
        guess = int(input("entre number :"))

    elif guess > n:
        print("too high")
        guess = int(input("entre number :"))

else:
    break
print("you guessed it right")

