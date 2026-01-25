age = 28
op = 3
guess = 0
t = 0

while t < op:
    guess = int(input("Guess a age: "))

    if(guess == age):
        print("You guessed correctly")
        break
    t += 1
else:
    print("Out of guess")