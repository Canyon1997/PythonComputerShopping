available_parts = ["Computer", 
                   "Monitor", 
                   "Keyboard", 
                   "Mouse", 
                   "Mouse Mat", 
                   "HDMI Cable",
                   "Graphics Card",
                   "CPU",
                   "Headset",
                   "Ram",
                   "Fans",
                   "Mother Board",
                   "SSD",
                   "Computer Case",
                   "Power Supply"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

choice = "-"
computer_parts = []

while choice != "0":
    print("Please add options from the list below:")
    for number, item in enumerate(available_parts):
        print("{0}: {1}".format(number + 1, item))

    print("0: Exit")
    choice = input()

    if not choice.isnumeric():
        while not choice.isnumeric():
            print("Invalid Choice, try again")
            choice = input()

    if choice in valid_choices:
        print("Adding {}".format(available_parts[int(choice) - 1]))
        computer_parts.append(available_parts[int(choice) - 1])
    elif choice == "0":
        print("Exiting")
    else:
        print("Choice not available")

print(computer_parts)
