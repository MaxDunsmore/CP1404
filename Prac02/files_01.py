userName = input("Enter your name: ")
name_file = open("name.txt", "w")
print(userName, file=name_file)
name_file.close()
