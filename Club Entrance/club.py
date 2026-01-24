print("*" * 20)
print("Welcome to Club Heaven!")
name = input("What is your name?: ")

print (f"Hello {name}")
age = int(input("What is your age?: "))

if age < 18:
    print("You are not allowed")
elif age >= 18 and age < 65:
    print("You are allowed")
else:
    print("You are too old")