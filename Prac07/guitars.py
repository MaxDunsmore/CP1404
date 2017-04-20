from Prac07.guitar import Guitar

print("My guitars!")
guitar_list = []
while True:
    name = str(input("Name: "))
    if name == "":
        print("       ...snip...")
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitar_list.append(guitar)
    print("{} ({}) : ${:.2f} added.".format(name, year, cost))

counter = 1
for guitar in guitar_list:
    print("Guitar {}: {}".format(counter, guitar))
    counter += 1

#  it's probably wrong but i'm super tired and my head hurts when i try to think, sorry - i tried
