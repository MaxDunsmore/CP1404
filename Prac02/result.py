finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = 1
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is: {}".format(result))
