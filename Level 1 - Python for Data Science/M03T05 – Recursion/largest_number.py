def largest_number(num_list):
    # Base case: if only one element, return it
    if len(num_list) == 1:
        return num_list[0]

    # Recursive case
    rest_max = largest_number(num_list[1:])   # largest in the rest of the list

    # Compare the first element with the rest_max
    if num_list[0] > rest_max:
        return num_list[0]
    else:
        return rest_max


num_list = [1, 4, 5, 8, 2]
x = largest_number(num_list)
print("Final Result:", x)
