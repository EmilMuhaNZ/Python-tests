def get_name():
    name = input("Please enter your name: ")
    return name

def main():
    output = get_name()
    print("Hello, " + output)
    

main()