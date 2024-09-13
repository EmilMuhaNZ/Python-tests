

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



introduction_message()
print_options()