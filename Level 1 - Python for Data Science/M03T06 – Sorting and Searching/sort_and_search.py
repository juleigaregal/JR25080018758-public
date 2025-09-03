#this works because the list does not have to be ordered and goes through each item one by one
#binary search would not work because the list would need to be sorted

def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index.
    for index in range(len(items)):
        if items[index] == target:
            return index  # Target found, return index

    # If the target item is not found, return None.
    return None

# Example usage:
items_list =items = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9
result = sequential_search(target_item, items_list)

if result is not None:
    print(f"Item {target_item} found at index {result}.")
else:
    print(f"Item {target_item} not found in the list.")

#Implementation of insertion sort 
#resource used 
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
     
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
 
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr =  [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
insertionSort(arr)
print(arr)

#Jump search is good for large datasets
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump in blocks
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return None

# Search for 9
target_item = 9
result = jump_search(arr, target_item)
print(result)  # Output: index of 9 in the sorted list
