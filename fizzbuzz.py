num = 20
for x in range(1, num+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

