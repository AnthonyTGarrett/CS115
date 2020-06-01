# Woody's Furniture Sales Calculator
# Anthony Garrett
# 9/18/2019
# Displaying the sales of different types of chairs in a table based
# on input from the user.

# Getting input about the chair style, price, and uints sold from the user
chair_style_1 = input('What chair style was sold? ')
chairs_sold_1 = int(input('How many ' + chair_style_1 + ' chairs were sold? '))
chair_price_1 = float(input('What was the price of each ' +
                            chair_style_1 + ' chair? '))

print('')
chair_style_2 = input('What chair style was sold? ')
chairs_sold_2 = int(input('How many ' + chair_style_2 + ' chairs were sold? '))
chair_price_2 = float(input('What was the price of each ' +
                            chair_style_2 + ' chair? '))

print('')
chair_style_3 = input('What chair style was sold? ')
chairs_sold_3 = int(input('How many ' + chair_style_3 + ' chairs were sold? '))
chair_price_3 = float(input('What was the price of each ' +
                            chair_style_3 + ' chair? '))

# Calculating Totals for each chair style and the total amount sold
chair_style_1_total = chair_price_1 * chairs_sold_1
chair_style_2_total = chair_price_2 * chairs_sold_2
chair_style_3_total = chair_price_3 * chairs_sold_3

total_amount_sold = chair_style_1_total + \
    chair_style_2_total + chair_style_3_total

# Giving a space between the input lines and the output lines
print('')

# Formatting the headings for the table
print(format('Chair Style', '<25s'), format('PRICE', '>15s'),
      format('SOLD', '>12s'), format('TOTAL SALES', '>20s'))
print('-' * 75)

# Printing out all of the information given by the user
print(format(chair_style_1, '<25s'), format('$', '>5s'), format(chair_price_1, '>9,.2f'),
      format(chairs_sold_1, '>12,d'), format('$', '>9s'), format(chair_style_1_total, '10,.2f'))

print(format(chair_style_2, '<25s'), format('$', '>5s'), format(chair_price_2, '>9,.2f'),
      format(chairs_sold_2, '>12,d'), format('$', '>9s'), format(chair_style_2_total, '10,.2f'))

print(format(chair_style_3, '<25s'), format('$', '>5s'), format(chair_price_3, '>9,.2f'),
      format(chairs_sold_3, '>12,d'), format('$', '>9s'), format(chair_style_3_total, '10,.2f'))

# Displaying the total amount of sales
print('')
print(format('TOTAL', '<45s'), format('$', '>18s'),
      format(total_amount_sold, '>10,.2f'))
