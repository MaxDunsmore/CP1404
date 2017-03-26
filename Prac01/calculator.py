total = 0
numberOfItems = int(input("Enter number of items: "))
while numberOfItems < 0:
    print("Invalid number of items!")
    numberOfItems = int(input("Enter number of items: "))
for i in range(0, numberOfItems):
    itemPrice = (input("price of item: $"))
    total += float(itemPrice)
if total > 100:
    total *= .9
print("The total price for {} items is ${:.2f}".format(numberOfItems, total))
