


to_do_list = []

def introduction_message():
    message = "Emil's To do list"
    print("*" * (len(message) + 2))
    print("*" + message + "*")
    print("*" * (len(message) + 2))

def print_options():
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_a_task(existing_list):
    new_task = input("Please enter which task you would like to add: ")
    existing_list += [new_task]
    return existing_list

def get_command():
    command = int(input("Please select an option: "))


def display_list(existing_list):
    if len(existing_list) == 0:
        print("The list is currently empty, no tasks to desplay!")
    else:
        for i in range (len(existing_list)):
            print(f"{i + 1}. {existing_list[i]}")

def exit_message():
    print("Thank you for helping Emil test this code!")

display_list()