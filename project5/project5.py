# Employee Payroll Program
# Anthony Garrett
# 12/6/2019
# Inputs employee information from a file in the CSV format, or from user input
# Computes pay for employees and displays a payroll report
# Writes employee name, hours worked, and pay rate to a file on exit

INPUT_FILENAME = 'data.txt'
OUTPUT_FILENAME = 'data.txt'


# Accept a list of lists that contain 4 pieces of information
# A string name, float hours worked, float pay rate, float gross pay
# Collects employee information from the user and adds it to the existing employee_info list
# Returns the list of employees back to the calling functions
def inputData(employee_info):
    menu_choice = ''

    while menu_choice != 'n' and menu_choice != 'no':
        temp_list = []

        temp_list.append(input("Enter the Employee Name: "))

        print()

        # Continue to loop until the user enters a valid number
        while True:
            try:
                temp_list.append(float(input("Enter the Hours Worked: ")))
            except ValueError:
                print('Please enter a valid number.')
                continue
            break
        print()

        # Continue to loop until the user enters a valid number
        while True:
            try:
                temp_list.append(float(input("Enter the Pay Rate: ")))
            except ValueError:
                print('Please enter a valid number.')
                continue
            break

        temp_list.append(0.0)
        print()
        menu_choice = input("Enter another employee? (Y/n) ").lower()
        print()
        employee_info.append(temp_list)

    return employee_info


# Accept a list of lists that contain 4 pieces of information
# A string name, float hours worked, float pay rate, float gross pay
# Calculating each employees pay and storing it back in the list.
# Returns the list of employees back to the calling functions
def computePay(employee_info):

    # Looping through the list and separating the calculation by < 40 hours or > 40 hours
    # If > 40 hours calculating overtime pay and overtime hours to add to the base pay of 40 hours
    for employee in employee_info:
        if employee[1] <= 40:
            employee[3] = round(employee[1] * employee[2], 2)
        else:
            employee[3] = round(employee[2] * 40, 2)
            employee[3] += round((employee[2] * 1.5) * (employee[1] - 40), 2)

    return employee_info


# Accept a list of lists that contain 4 pieces of information
# A string name, float hours worked, float pay rate, float gross pay
# Displays employee data in a table format
# Gross Pay that has not been calculated is left blank in the table
# Returns the list of lists back to the calling functions
def displayPay(employee_info):
    print()
    print()
    print('Anthony Garrett Web Designs Payroll')
    print(format('EMPLOYEE NAME', '<30s'), format('HOURS WORKED', '>15s'),
          format('PAY RATE', '>10s'), format('GROSS PAY', '>15s'))
    print(format('-' * 30, '<30s'), format('-' * 12, '>15s'),
          format('-' * 8, '>10s'), format('-' * 15, '>15s'))

    # Looping through the list to print employee information
    for employee in employee_info:
        print(format(employee[0], '<30s'), format(
            employee[1], '>15.1f'), format(employee[2], '>10.2f'), end='')

        # Checking if the gross pay has been calculated before printing to the table
        if(employee[3] > 0.0):
            print(format(employee[3], '>15.2f'))
        else:
            print('')
    print()
    print()


# Reads input from file at startup if it exists
# Displays Main Menu and calls functions based on user input
# Writes employee information to file on exit
def main():
    employee_data = []
    control = ''

    # read file of employee data checking for empty file and no file
    # No warning is given to the user
    try:
        with open(INPUT_FILENAME, 'r') as file:
            employee_data = file.readlines()
    except FileNotFoundError:
        pass

    # Checking for the existence of data in the list before cleaning the data
    # Cleaning the data to ensure the correct formatting
    if(employee_data):

        # splitting the data to remove the , and removing the newline character from the data
        for i in range(len(employee_data)):
            employee_data[i] = employee_data[i].rstrip('\n')
            employee_data[i] = employee_data[i].split(',')

        # Adding a 0.0 place holder for gross pay to be calculated later and converting strings to floats
        for employee in employee_data:
            employee.append(0.0)
            employee[1] = float(employee[1])
            employee[2] = float(employee[2])

    # Loop that shows the main menu until the user types 4 to exit the program
    while control != '4':
        print()
        print(format('Main Menu', '>50s'))
        print('-' * 50)
        print(format('Input Employee\'s Information (1)', '>50s'))
        print(format('Compute Pay For All Employees (2)', '>50s'))
        print(format('Display Payroll Report (3)', '>50s'))
        print(format('Exit (4)', '>50s'))
        print()

        control = input(format('Please enter your selection >>> ', '>50s'))

        # Checking for values from the user input to call the desired function
        if control == '1':
            employee_data = inputData(employee_data)
        elif control == '2':
            employee_data = computePay(employee_data)
        elif control == '3':
            displayPay(employee_data)
        elif control == '4':
            # Writing the employee information to a file
            with open(OUTPUT_FILENAME, 'w') as file:
                for employee in employee_data:
                    file.write(employee[0] + ', ' + str(employee[1]) +
                               ', ' + str(employee[2]) + '\n')
            print()
            print("Thank You For Using Our Payroll Application")


if __name__ == "__main__":
    main()
