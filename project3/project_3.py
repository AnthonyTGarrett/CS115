# Math Tutor Deluxe
# Anthony Garrett
# 10/3/2019
# Math Tutor to check the answers of the student to help with basic math functions

# while loop pretest
# Display menu for user selection
print()
print(format('Math Tutor Deluxe', '>30s'))
print('-' * 30)
print(format('Addition', '>30s'))
print(format('Subtraction', '>30s'))
print(format('Multiplication', '>30s'))
print(format('Division', '>30s'))
print(format('Quit', '>30s'))

# Read user selection
print()
menu_selection = input('Which math problem do you want to try? ')

# Program runs until user inputs 'quit'
# While loop for menu control
while menu_selection != 'quit' and menu_selection != 'Quit':

    # Using if statement to separate division because of special cases of
    # dividing by zero
    if menu_selection == 'division' or menu_selection == 'Division':

        # Prompt user for two integers
        print()
        num_1 = int(input('Please enter the first integer for the operation: '))
        num_2 = int(
            input('Please enter the second integer for the operation: '))

        # input verification loop
        # Make sure second number isn't 0 for division
        while num_2 == 0:
            print()
            print(
                'You can not divide a number by 0. Please enter valid numbers to divide.')
            num_1 = int(
                input('Please enter the first integer for the operation: '))
            num_2 = int(
                input('Please enter the second integer for the operation: '))
    else:
        print()
        num_1 = int(input('Please enter the first integer for the operation: '))
        num_2 = int(
            input('Please enter the second integer for the operation: '))

    # Prompt user for their answer
    # Be specific for division calc_result that will be floats
    print()
    if menu_selection == 'division' or menu_selection == 'Division':
        user_answer = float(input('Please enter your answer to the ' +
                                  menu_selection.lower() + ' problem to 2 decimal places: '))  # making operation names lowercase for consistency
    else:
        user_answer = int(
            input('Please enter your answer to the ' + menu_selection.lower() + ' problem: '))  # making operation names lowercase for consistency

    # Calculate the calc_result of the chosen operation
    if menu_selection == 'addition' or menu_selection == 'Addition':
        calc_result = num_1 + num_2
    elif menu_selection == 'subtraction' or menu_selection == 'Subtraction':
        calc_result = num_1 - num_2
    elif menu_selection == 'multiplication' or menu_selection == 'Multiplication':
        calc_result = num_1 * num_2
    elif menu_selection == 'division' or menu_selection == 'Division':

        # After dividing the number round to two places to check the answer with the users answer
        calc_result = num_1 / num_2
        calc_result = round(calc_result, 2)
    else:
        print()
        print('You entered an incorrect menu option.')
        print('Please select a valid option from the menu.')

        # re-display menu for user selection
        print()
        print(format('Math Tutor Deluxe', '>30s'))
        print('-' * 30)
        print(format('Addition', '>30s'))
        print(format('Subtraction', '>30s'))
        print(format('Multiplication', '>30s'))
        print(format('Division', '>30s'))
        print(format('Quit', '>30s'))

        # Read user menu selection
        print()
        menu_selection = input('Which math problem do you want to try? ')
        # restart loop
        continue

    # Display if the user is correct or incorrect
    # If incorrect display the correct answer for the user
    if user_answer == calc_result:
        print()
        print('*' * 40)
        print("Great Job! You got the answer correct.")
        print('*' * 40)
    else:
        print()
        print('*' * 40)
        print("I'm sorry but that answer is incorrect.")
        print("The correct answer is", calc_result)
        print('*' * 40)

    # re-display menu for user selection
    print()
    print(format('Math Tutor Deluxe', '>30s'))
    print('-' * 30)
    print(format('Addition', '>30s'))
    print(format('Subtraction', '>30s'))
    print(format('Multiplication', '>30s'))
    print(format('Division', '>30s'))
    print(format('Quit', '>30s'))

    # Read user menu selection
    print()
    menu_selection = input('Which math problem do you want to try? ')


# Thank the user and say goodbye after quitting the program
print()
print('Thank You For Using Math Tutor Deluxe')
print('Goodbye')
print()
