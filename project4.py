# Personal Expense Chart Program
# Anthony Garrett
# 11/8/2019
# Displaying the personal expenses from user input in a format
# that is chosen by the user
import matplotlib.pyplot as plt


# Main program control
# Maintains the menu and user selections for the program
# Calls indicated functions based on user input
def main():
    menu_choice = ''
    expenseItems = []
    expenseAmounts = []

    # Loop to control the main menu
    while menu_choice != 'q' and menu_choice != 'quit':

        print()
        print(format('Main Menu', '>30s'))
        print('-' * 30)
        print(format('Input Expense Names (n)', '>30s'))
        print(format('Input Expense Amounts (a)', '>30s'))
        print(format('Display an Expense Report (d)', '>30s'))
        print(format('Quit (q)', '>30s'))
        print()

        # Getting menu input from the user
        menu_choice = input('Please enter your selection >>> ').lower()

        # Deciding what to do based on the user input
        if menu_choice == 'n':
            # Call InputExpenseNames to get the names of the expenses from the user
            expenseItems = InputExpenseNames()
        elif menu_choice == 'a':
            # Call InputExpense Amounts to get the amount of each user expense
            expenseAmounts = InputExpenseAmounts(expenseItems)
        elif menu_choice == 'd':
            # Call DisplayExpenseReport to display the expenses with amounts
            DisplayExpenseReport(expenseItems, expenseAmounts)

    print("\n\nThanks for using my program. Goodbye.")


# Accepts no parameters
# Prompts the user for expense item names
# Returns a list of string items entered by the user or an empty list if none are entered
def InputExpenseNames():

    print()
    print('*' * 28)
    print(format('Expense Item Addition', '>24s'))
    print('*' * 28)
    print()

    expense_items = []
    new_item = ''

    # Loop to allow the user to keep adding items or return to the main menu
    while new_item != 'q':
        print()
        new_item = input(
            "Please enter the name of an expense item or \n\t    (q) to return to the main menu: ").lower()

        # Input validation loop to ensure the expense name is not empty before adding to the list
        while new_item == '':
            new_item = input(
                "Expense names cannot be blank, please try again: ")

        # Stop from adding the quit command to the items list
        if new_item != 'q':
            expense_items.append(new_item)

    return expense_items


# Accepts one parameter which is the list of strings that are names of the expense items
# Prompts the user for the amount associated with each of the expense list items
# returns a list of the float amounts entered in the same order as the names in the parameter list
# returns an empty list if no items in the parameter list
def InputExpenseAmounts(expense_items):

    print()
    print('*' * 28)
    print(format('Expense Amount Addition', '>26s'))
    print('*' * 28)
    print()

    expense_amounts = []
    counter = 0

    # Notifying the user of an empty list
    if len(expense_items) == 0:
        print('No items available for adding amounts')
        print('Returning to main menu...')

    # loop that iterates over the expense items in the items list
    # Will not enter if items list is empty
    while counter < len(expense_items):

        # Ensure that the input for expense amount is a number
        try:
            new_amount = float(input('How much was spent on ' +
                                     expense_items[counter] + ' expense item? '))

        except ValueError:
            print('\nPlease enter a number.')
            continue

        expense_amounts.append(new_amount)

        counter += 1

    return expense_amounts


# Accepts 2 parameters. One is a list of string expense item names
# The second is a list of float expense item amounts
# Prompts user for method to display the data
# Displays the data and returns nothing
def DisplayExpenseReport(expense_items, expense_amounts):

    user_choice = 'y'

    while user_choice != 'q' and user_choice != 'quit':
        print()
        print(format('Display Menu', '>30s'))
        print('-' * 30)
        print(format('Table Display (a)', '>30s'))
        print(format('Pie Chart (b)', '>30s'))
        print(format('Bar Chart (c)', '>30s'))
        print(format('return to Main Menu (q)', '>30s'))
        print()

        user_choice = input('Please Enter Your Selection >>> ').lower()

        # Display method if the user chooses table
        if user_choice == 'a':
            print('\n\n')
            print(format('EXPENSE ITEM', '<20s'), format('AMOUNT', '>28s'))
            print(format('------------', '<20s'), format('------', '>28s'))

            # loop to display expense items and expense amounts
            counter = 0
            while counter < len(expense_items):
                print(format(expense_items[counter].title(), '<20s'),
                      format(expense_amounts[counter], '>28.2f'))

                counter += 1

            # Not displaying totals if the expense_amounts list is empty
            if sum(expense_amounts) > 0:
                print('-' * 49)
                print(format('TOTALS', '<20s'), format(
                    sum(expense_amounts), '>28,.2f'))

            # Holding from displaying menu until user presses a key
            input('\nPress Enter to return to the display menu...')

        # Display method if the user chooses Pie Chart
        elif user_choice == 'b':

            # Matplotlib Pie Chart Display
            # Explodes is an iterable that gives the space between each slice of pie
            explodes = []

            # loop to create the explodes iterable
            for expense in expense_amounts:
                explodes.append(0.06)

            # using pyplot to create a pie chart with auto percentage and a title
            plt.pie(expense_amounts, explodes,
                    expense_items, autopct='%1.1f%%', shadow=True)
            plt.title("Expense Amounts")
            plt.show()

        # Display method if the user chooses Bar Chart
        elif user_choice == 'c':

            # Matplotlib Bar Chart Display
            plt.bar(expense_items, expense_amounts)
            plt.xticks(expense_items)
            plt.ylabel('Cost')
            plt.title('Expense Item Amounts')
            plt.show()


# Call the main function
main()
