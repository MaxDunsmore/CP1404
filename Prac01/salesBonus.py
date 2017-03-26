"""
Program to calculate
and display
a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 1
while sales > -1:
    sales = float(input("Enter sales: $"))
    if -1 < sales < 1000:
        sales *= .1
    elif sales >= 1000:
        sales *= .15
    else:
        break
    print("$" + "{:.2f}".format(sales))
