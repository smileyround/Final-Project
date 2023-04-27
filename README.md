# Final Project
 This is my final project called Give My Money Back
### Hi, I'm Meng Tian and this is my final project called Give My Money Back

> This is the presentation link (https://youtu.be/PIwbY65Hhbo)
---
> This code is a simple program for tracking borrowed money and extra payments made by borrowers. It uses a dictionary to store the borrowed money and extra payments as key-value pairs, where the keys are the names of the borrowers and the values are dictionaries containing the amount borrowed and the date of borrowing.

> The program provides several functions:

- add_name(): This function allows the user to add a borrower's name and the amount of money borrowed to the borrowed_money dictionary. It validates user input for the borrower's name, amount borrowed, and date of borrowing.

- pay_back(): This function calculates and displays the amount of borrowed money to be paid back by a borrower. It validates user input for the borrower's name and the amount to be paid back, and updates the borrowed_money dictionary accordingly. If the amount paid back is greater than the borrowed amount, it also keeps track of the extra payment in the extra_payments dictionary.

- fall_in_love(): This function sets the borrowed money to 0 for a borrower who has fallen in love, indicating that the borrower does not need to pay back the borrowed amount. It validates user input for the borrower's name and updates the borrowed_money dictionary accordingly.

- list_borrowers(): This function displays the list of borrowers with their borrowed amount and any extra payments made. It calculates the total borrowed money and total paid back money, and displays them at the end.

- exit_program(): This function saves the data in the borrowed_money and extra_payments dictionaries to a file using pickle, and exits the program.

- The code also includes a try-except block to load data from a file named who_owened_my_money.pickle if available, and catch a FileNotFoundError if the file is not found.
