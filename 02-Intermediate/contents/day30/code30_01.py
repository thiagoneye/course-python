"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 30
Errors, Exceptions and JSON Data
"""

# File Not Found
#with open('a_file.txt') as file:
#    file.read()

# Key Error
#a_dictionary = {'key': 'value'}
#value = a_dictionary['not_existent_key']

# Index Error
#fruit_list = ['Apple', 'Banana', 'Pear']
#fruit_list[3]

# Type Error
#text = 'abc'
#print(text + 5)

try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    #print(a_dictionary['not_existent_key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f'The key {error_message} does not exist.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
