# Prime Numbers

#Write your code below this line 👇

def prime_checker(number):
    isPrime = True

    for i in range(2, int(number/2)+1):
        if (number % i == 0):
            isPrime = False
            break

    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
