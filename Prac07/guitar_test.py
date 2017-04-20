from Prac07.guitar import Guitar

guitar = Guitar("test", 1000, 300)
guitar2 = Guitar("test", 2010, 30)

print("get_age() - Expected {}. Got {}.".format(2017-guitar.year, guitar.get_age()))
print("get_age() - Expected {}. Got {}.".format(2017-guitar2.year, guitar2.get_age()))

print("is_vintage() - Expected {}. Got {}.".format(True if 2017 - guitar.year >= 50 else False, guitar.is_vintage()))
print("is_vintage() - Expected {}. Got {}.".format(True if 2017 - guitar2.year >= 50 else False, guitar2.is_vintage()))
