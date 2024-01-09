"""
This Python code generates a Fibonacci sequence up to the number of iterations provided by the user. It
initializes a list called 'array' containing the first two elements in the sequence 0 and 1.

Then, a for-loop is used to iterate through the range from 2 to the amount of user provided iterations, where each
iteration sums the last two elements in the sequence and appends it to the array.

Finally, the complete sequence is printed out.
"""

iterations = int(input("Number of iterations: "))
array = [0, 1]
for i in range(iterations):
    array.append(array[-1] + array[-2])
print(array)
