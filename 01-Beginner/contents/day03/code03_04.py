# Pizza Order Practice

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

value = {'S': 15, 'M': 20, 'L': 25}
extra = {'Y': 1, 'N': 0}

if (add_pepperoni == 'Y'):
    if (size == 'S'):
        add = 2
    elif ((size == 'M') or (size == 'L')):
        add = 3
elif (add_pepperoni == 'N'):
    add = 0

total = value[size] + add + extra[extra_cheese]

print('Your final bill is: $%d.' %total)
