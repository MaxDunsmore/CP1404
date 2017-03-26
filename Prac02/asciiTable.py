LOWER_LIMIT = 33
UPPER_LIMIT = 127

userNumber = 0
userCharacter = "00"
while len(userCharacter) > 1:
    userCharacter = str(input("Enter a character: "))
print("The ASCII code for {} is {}." .format(userCharacter, ord(userCharacter)))
while userNumber < LOWER_LIMIT or userNumber >= UPPER_LIMIT:
    userNumber = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
print("The character for {} is {}.".format(userNumber, chr(userNumber)))


for i in range(LOWER_LIMIT, UPPER_LIMIT):
    print("{:3}{:>5}".format(i, chr(i)))

