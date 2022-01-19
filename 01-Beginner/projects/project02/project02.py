# Tip Calculator

print('Welcome to the tip calculator.')

value = float(input('What was the total bill? $'))
number = int(input('How many people to split the bill? '))
percent = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

total = (value*(100+percent)/100)/number

print('Each person should pay: $%.2f' %total)
