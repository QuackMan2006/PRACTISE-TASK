def drop_off():
    dog_name = input("Enter the name of the dog: ")
    roll.append(dog_name)


def pick_up():
    dog_name = input("Enter the name of the dog you want to pick up: ")
    if dog_name in roll:
        roll.remove(dog_name)
        print(f"{dog_name} has been removed from the roll")
    else:
        print("Sorry, we have no dog by that name")


def calc_cost(number):
    rate = 22.50
    days = int(input("How many days to charge for: "))
    cost = number * days * rate
    print(f"The cost for {number} of dogs for {days} days is ${cost}")


def print_roll():
    print("Dogs currently staying with DosRus: ")
    for dog in roll:
        print(f"\t{dog}")
    print()


def end_program():
    print("Goodbye!")


roll = []

print("_______________________________________________________________________")
print("Welcome to DogsRus dog sitting service")
print("What would you like to do? Please choose one of the items below")
print("_______________________________________________________________________")



choice = 0
while choice != 5:
    print("What do you want to do? ")
    print()
    print("1 Drop off a dog")
    print("2 Pick up a dog")
    print("3 Calculate cost")
    print("4 Print dog roll")
    print("5 Exit the system")
    print()
    print("_______________________________________________________________________")

choice = int(input("Enter your choice (number between 1 and 5): "))
if choice == 1:
    drop_off()

elif choice == 2:
    pick_up()

elif choice == 3:
    calc_cost(len(roll))

elif choice == 4:
    print_roll()

elif choice == 5:
    end_program()

else:
    print("Must be an integer between 1 and 5")
