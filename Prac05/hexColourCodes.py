COLOUR_CODES = {"black": "#000000", "white": "#ffffff", "red": "#ff0000", "blue": "#0000ff", "green": "#00ff00",
                "aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff"}

colour = input("Enter the name of a coulor: ")
while colour != "":
    if colour.lower() in COLOUR_CODES:
        print("{} is {}".format(colour, COLOUR_CODES[colour.lower()]))
    else:
        print("that's a hard one...")
    colour = input("Enter the name of a coulor: ")
