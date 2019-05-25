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
Enter "REMOVE" to remove an item from the list
  ''')


show_help()

# Second operation


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should i add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
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

    # SAME AS LINE 62 BUT WITH TUPLE OPERATION
    for index, item in enumerate(shopping_list, start=1):
        # print(item)
        print("{}. {}".format(index, item))

    print("-" * 10)

    # index = 1
    # for item in shopping_list:
    #     print("{}. {}".format(index, item))
    #     index += 1
    # print("-" * 10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


show_help()
# Fourth operation:

while True:
    print("Add or remove items:")  # Ask user to add more items
    new_item = input("> ")

    # Added empty string if user didn't enter any items
    if new_item.upper() == "DONE" or new_item.upper() == "":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":  # The brackets are important
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()  # calling show list function

# NOTES:
# I didn't know you can call show_list in other functions as well
