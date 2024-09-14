
def to_do_list():
    to_do_list = []
    introduction_message()
    print_options()
    command = get_command()
    while command != 4:
        if command == 1:
            add_a_task(to_do_list)
        elif command == 2:
            display_list(to_do_list)
        elif command == 3:
            remove_task(to_do_list)
        else:
            print("")
            print("Invalid option. Please try again.")

        print_options()
        command = get_command()
    exit_message()

def introduction_message():
    message = "Emil's To do list"
    print("*" * (len(message) + 2))
    print("*" + message + "*")
    print("*" * (len(message) + 2))

def print_options():
    print("")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("")

def add_a_task(existing_list):
    new_task = input("Please enter which task you would like to add: ")
    existing_list += [new_task]
    return existing_list

def get_command():
    command = input("Please select an option: ")
    while not command.isdigit():
        print("")
        print("Invalid option. Please try again.")
        command = input("Please select an option: ")
    command = int(command)
    return command

def display_list(existing_list):
    if len(existing_list) == 0:
        print("")
        print("The list is currently empty, no tasks to display!")
    else:
        print("")
        for i in range (len(existing_list)):
            print(f"{i + 1}. {existing_list[i]}")

def remove_task(to_do_list):
    task = input("Please select which task you would like to remove: ")
    while not task in to_do_list:
        print("The task is not in the list. Please try again!")
        task = input("Please select which task you would like to remove: ")
    position = to_do_list.index(task)
    to_do_list.pop(position)
    print("")
    print(f"The task '{task}' has been sucessfully removed.")


def exit_message():
    print("")
    print("Thank you for helping Emil test this code!")
    print("")

to_do_list()