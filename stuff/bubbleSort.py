"""
This is a bubble sort implementation in python
"""
import random


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


# Testing, generating a shuffled list and sorting it
testArray = list(range(24))
random.shuffle(testArray)
print(f"Unsorted Array: {testArray}")
print(f"Sorted Array: {bubble_sort(testArray)}")