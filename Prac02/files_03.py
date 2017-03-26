numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
    total += int(line)
print(total)
numbers_file.close()
