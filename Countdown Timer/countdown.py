import time

mytime = int(input("Enter the time in seconds: "))

for x in range(0, mytime):
    print(x)
    time.sleep(1)


print("Time's Up!")