from inheritance import Taxi
from inheritance import SilverServiceTaxi


def main():
    total_cost = 0.0
    taxi_choice = ""
    print("Let's drive!")
    taxis = [Taxi("Broom Broom car", 100), SilverServiceTaxi("Long car", 100, 2), SilverServiceTaxi("Big car", 200, 4)]
    menu_choice = menu_list()
    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available:")
            taxi_choice = choose_taxi(taxis)

        if menu_choice == "d":
            taxi_choice.start_fare()
            if taxi_choice != "":
                distance_to_drive = int(input("Drive how far? "))
                taxi_choice.drive(distance_to_drive)
                print("your {} trip cost you ${:.2f}".format(taxi_choice.name, taxi_choice.get_fare()))
                fare_cost = taxi_choice.get_fare()
                total_cost += fare_cost
            else:
                print("pick a taxi, dummy")

        print("Bill to date: ${:.2f}".format(total_cost))
        menu_choice = menu_list()
    print("Total trip cost: {}".format(total_cost))
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


def choose_taxi(taxi_list):
    for index, taxi in enumerate(taxi_list):
        print("{} - {}".format(index, taxi))
    taxi_choice = int(input("Choose taxi: "))
    taxi = taxi_list[taxi_choice]
    return taxi


def menu_list():
    choice = input("q)uit, c)hoose taxi, d)rive" + "\n" +
                   ">>> ")
    return choice

main()
