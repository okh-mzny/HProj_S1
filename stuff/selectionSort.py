"""
This is an example implementation of the selection sort algorithm in python
"""
import random


def selection_sort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
    return array


# Testing, generating a shuffled list and sorting it
testArray = list(range(24))
random.shuffle(testArray)
print(f"Unsorted Array: {testArray}")
print(f"Sorted Array: {selection_sort(testArray)}")
