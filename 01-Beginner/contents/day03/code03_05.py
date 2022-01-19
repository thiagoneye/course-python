# Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

score1 = 0
for i in 'true':
    score1 += name1.count(i)
    score1 += name2.count(i)

score2 = 0
for i in 'love':
    score2 += name1.count(i)
    score2 += name2.count(i)

score = int(str(score1) + str(score2))

if ((score < 10) or (score > 90)):
    print("Your score is %d, you go together like coke and mentos." %score)
elif ((score > 40) and (score < 50)):
    print("Your score is %d, you are alright together." %score)
else:
    print("Your score is %d." %score)
