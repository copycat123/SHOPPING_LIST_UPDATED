import os


shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# First operation


def show_help():
    clear_screen()
    print("what should we buy from the store?")
    print('''
Enter "DONE" to stop adding items
Enter "HELP" for help
Enter "SHOW" for selected items list
  ''')


show_help()

# Second operation


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should i add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         ">".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()


# Third operation

def show_list():

    clear_screen()
    print('Here is your shoping list:')
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-" * 10)


# Fourth operation:

while True:
    print("Add more items:")  # Ask user to add more items
    new_item = input("> ")

    # Added empty string if user didn't enter any items
    if new_item.upper() == "DONE" or new_item.upper() == "":
        break
    elif new_item.upper == "HELP":
        show_help()
        continue
    elif new_item.upper == "SHOW":
        show_list()
        continue
    else:
        add_to_list(new_item)

show_list()  # calling show list function

# NOTES:
# I didn't know you can call show_list in other functions as well
