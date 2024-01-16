"""
List sorting

This script uses NumPy's random.choice-function to generate a 10 element long NumPy with values from 0 to 10.
This 1-D array can be used just like a List.

The script then demonstrates a sorting and deduplication algorithm. Afterwards, one can look up the first and last
number within the array to find the lowest and highest number.
"""

import numpy as np

arr = np.random.choice(10, 10, replace=True)

print(f"The testarray is \n{arr}\n")

arr_sorted = []

arr.sort()

for e in arr:
    if e not in arr_sorted:
        arr_sorted.append(e)

print(f"The sorted and deduplicated array is now \n{arr_sorted}")

print(f"The lowest number is {arr_sorted[0]} and the highest is {arr_sorted[-1]}")