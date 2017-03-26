'''
James Collison
'''


def main():
    userName = getName()
    nameSkip = int(input(": "))
    nameLoop(userName, nameSkip)


def nameLoop(userName, nameSkip):
    for i in range(0, len(userName), nameSkip):
        print(userName[i], end="")


def getName():
    userName = str(input("Enter your name: "))
    while len(userName) < 1:
        userName = str(input("Enter your name: "))
    return userName


main()


