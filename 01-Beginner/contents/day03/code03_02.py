# BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/(height**2))

if (bmi < 18.5):
    print('Your BMI is %d, you are underweight.' %bmi)
elif (bmi < 25):
    print('Your BMI is %d, you have a normal weight.' %bmi)
elif (bmi < 30):
    print('Your BMI is %d, you are slightly overweight.' %bmi)
elif (bmi < 35):
    print('Your BMI is %d, you are obese.' %bmi)
else:
    print('Your BMI is %d, you are clinically obese.' %bmi)
