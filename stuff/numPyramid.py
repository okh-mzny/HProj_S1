"""
This code asks the user to provide a number of iterations to run for. Then, with two nested for loops, it prints half of
a pyramid made up of numbers. The outer for loop runs for the user specified amount of iterations, and the inner loop
runs for i iterations in each iteration of the outer loop.

The created number pattern is made of increasing numbers from top to bottom, with the number being repeated for number
amount of times.

1
22
333
4444
...
999999999
"""

iterations = int(input("Number of iterations: "))
for i in range(1, iterations+ 1):
    for j in range(i):
        print(i,end="")
    print("")