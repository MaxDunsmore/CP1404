"""
CP1404/CP5632 Practical
Number facts
"""


number_list = []
for i in range(5):
    number = int(input("Number: "))
    number_list.append(number)
print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("the average of the numbers is {}".format(sum(number_list)/len(number_list)))
