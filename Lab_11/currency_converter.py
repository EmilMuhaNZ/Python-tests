def main():
    currencies = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars",
                     "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
    rates = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
    print_banner()
    print("")
    print_menu(currencies, rates)
    print("")
    perform_currency_exchange(currencies, rates)

def print_banner():
    banner_text = "A Currency Converter"
    print("*" * (len(banner_text) + 2))
    print("*" + banner_text + "*")
    print("*" * (len(banner_text) + 2))

def print_menu(currencies, rates):
    print("Select an operation:")
    print(f"Enter 1 to exchange NZ Dollars to {currencies[0]} (1 NZD = {rates[0]} {currencies[0]})")
    print(f"Enter 2 to exchange NZ Dollars to {currencies[1]} (1 NZD = {rates[1]} {currencies[1]})")
    print(f"Enter 3 to exchange NZ Dollars to {currencies[2]} (1 NZD = {rates[2]} {currencies[2]})")
    print(f"Enter 4 to exchange NZ Dollars to {currencies[3]} (1 NZD = {rates[3]} {currencies[3]})")
    print(f"Enter 5 to exchange NZ Dollars to {currencies[4]} (1 NZD = {rates[4]} {currencies[4]})")
    print(f"Enter 6 to exchange NZ Dollars to {currencies[5]} (1 NZD = {rates[5]} {currencies[5]})")
    print(f"Enter 7 to exchange NZ Dollars to {currencies[6]} (1 NZD = {rates[6]} {currencies[6]})")
    print("Enter 0 to exit the currency converter")

def get_user_selection():
    user_selection = int(input("Enter your selection: "))
    while user_selection < 0 or user_selection > 7:
        print("Invalid selection!")
        user_selection = int(input("Enter your selection: "))
    return user_selection

def perform_currency_exchange(currencies, rates):
    user_selection = get_user_selection()
    while user_selection != 0:
        nz_dollar_amount = float(input("Enter the amount of NZ dollars you want to convert: "))
        if user_selection != 7:
            exchange_amount = round(nz_dollar_amount * rates[user_selection - 1], 2)
        else:
            exchange_amount = round(nz_dollar_amount * rates[user_selection - 1])
        print(f"${nz_dollar_amount} NZ dollars = ${exchange_amount} {currencies[user_selection - 1]}")
        user_selection = int(input("Enter your selection: "))
        while user_selection < 0 or user_selection > 7:
            print("Invalid selection!")
            user_selection = int(input("Enter your selection: "))
    print("")
    print_exit_message()

def print_exit_message():
    print("Exiting the currency converter...")
    print("Have a good day!")