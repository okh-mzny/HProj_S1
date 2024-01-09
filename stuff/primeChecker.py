"""
This code takes an input number from the user and checks if it is a prime number or not. It does this
by iterating through all numbers from 2 to the square root of the input number, and checking if the input number is
divisible by any of these numbers.

If the input number is divisible by any of these numbers, then it is not a prime
number and the program prints "Number is not a prime". If the loop completes without finding any divisor,
then the input number is a prime number and the program prints "Number is a prime".
"""

x = int(input("Enter number:"))

for i in range(2, (x ** 0.5).__floor__()):
    if x % i == 0:
        print("Number is not a prime")
        break
else:
    print("Number is a prime")
