""" 
Final project: Give My Money Back

This code is a simple program for tracking borrowed money and extra payments made by borrowers.
It uses a dictionary to store the borrowed money and extra payments as key-value pairs, where the keys are the names of the borrowers and the values are dictionaries containing the amount borrowed and the date of borrowing.

NAME: <MengTian>
SEMESTER: <2023 spring>
"""
import pickle
from datetime import datetime

borrowed_money = {}
extra_payments = {}
DATA_FILE = "who_owened_my_money.pickle"  # File name to store data


def add_name() -> None:
    """
    Function to add a borrower's name and the amount of money borrowed to the borrowed_money dictionary.
    Parameters:
    None
    Returns:
    None
    """
    name = input("Enter name of borrower: ").lower()
    while not name.isalpha():
        name = input("Invalid name. Please enter a valid name of borrower: ").lower()
    if name in borrowed_money:
        print(f"{name} already exists. Adding amount to the existing borrowed money.")
        amount = input("Enter amount borrowed: ")
        while not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
            amount = input("Invalid amount. Please enter a positive amount borrowed: ")
        borrowed_money[name]["amount"] += float(amount)
    else:
        amount = input("Enter amount borrowed: ")
        while not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
            amount = input("Invalid amount. Please enter a positive amount borrowed: ")
        print("Enter the date of borrowing in the format YYYY-MM-DD")
        date_input = input("Enter date of borrowing: ")
        while True:
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                break
            except ValueError:
                date_input = input("Invalid date format. Please enter a valid date of borrowing in the format YYYY-MM-DD: ")
        borrowed_money[name] = {"amount": float(amount), "date": date}


def pay_back() -> None:
    """
    Function to calculate and display the amount of borrowed money to be paid back by a borrower.
    Parameters:
    None
    Returns:
    None
    """
    name = input("Enter name of borrower: ").lower()
    while not name.isalpha() or name not in borrowed_money:
        name = input("Borrower not found. Please enter a valid name of borrower: ").lower()
    amount = input("Enter amount to be paid back: ")
    while not amount.replace(".", "", 1).isdigit():
        amount = input("Invalid amount. Please enter a positive amount to be paid back and make sure it is not greater than the borrowed amount: ")
    if borrowed_money[name]["amount"] == float(amount):
        del borrowed_money[name]
        print(f"{name} has paid back the borrowed money.")
    elif borrowed_money[name]["amount"] > float(amount):
        borrowed_money[name]["amount"] -= float(amount)
        print(f"{name} has paid back {amount} dollars.")
    else:
        extra_payment = float(amount) - borrowed_money[name]["amount"]
        borrowed_money[name]["amount"] = 0
        print(f"Wow! Your friend is so generous! He/She paid back {extra_payment} dollars more.")
        print(f"{name} has paid back the borrowed money and extra {extra_payment} dollars.")
        extra_payments[name] = extra_payments.get(name, 0) + extra_payment
        print(f"Your friend has paid back more than they borrowed. You might want to consider this when lending them money again in the future.")


def fall_in_love() -> None:
    """
    Function to set the borrowed money to 0 for a borrower who has fallen in love.
    Parameters:
    None
    Returns:
    None
    """
    name = input("Enter name of borrower who fell in love: ").lower()
    while not name.isalpha() or name not in borrowed_money:
        name = input("Borrower not found. Please enter a valid name of borrower: ").lower()
    borrowed_money[name]["amount"] = 0
    print(f"Because you have fallen in love with {name} , the borrowed money has been set to 0.\n" + "Oh! Love is most expensive thing in the world!!!")


def list_borrowers() -> None:
    """
    Function to display the list of borrowers with their borrowed amount and any extra payments.
    Parameters:
    None
    Returns:
    None
    """
    total_borrowed = 0
    total_paid_back = 0
    print("List of borrowers:")
    for name, info in borrowed_money.items():
        days_late = (datetime.now() - info["date"]).days
        if days_late > 30 and info['amount'] != 0:
            print(f"{name}: {info['amount']} dollars (OVERDUE by {days_late} days!)")
        else:
            print(f"{name}: {info['amount']} dollars")
        total_borrowed += info["amount"]
    for name, amount in extra_payments.items():
        print(f"{name} paid extra {amount} dollars")
        total_paid_back += amount
    print(f"Total borrowed money: {total_borrowed} dollars")
    print(f"Total paid back money: {total_paid_back} dollars")

    
def exit_program() -> None:
    """
    Function to save data to file and exit the program.
    Parameters:
    None
    Returns:
    None
    """
    with open(DATA_FILE, "wb") as file:
        pickle.dump((borrowed_money, extra_payments), file)
        print("Exiting the program...")
    exit()

# Load data from file if available
def main():
    try:
        with open(DATA_FILE, "rb") as file:
            borrowed_money, extra_payments = pickle.load(file)
    except FileNotFoundError:
        print("No data file found. Starting with empty data.")

        
    while True:
        print("Give My Money Back")
        print("1. Add name and amount borrowed")
        print("2. Pay back borrowed money")
        print("3. Fall in love and set borrowed money to 0")
        print("4. List borrowers")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        while choice not in ["1", "2", "3", "4", "5"]:
            choice = input("Invalid choice. Please enter a valid choice (1/2/3/4/5): ")
        if choice == "1":
            add_name()
            list_borrowers()
        elif choice == "2":
            pay_back()
            list_borrowers()
        elif choice == "3":
            fall_in_love()
            list_borrowers()
        elif choice == "4":
            list_borrowers()
        elif choice == "5":
            exit_program()


main()
