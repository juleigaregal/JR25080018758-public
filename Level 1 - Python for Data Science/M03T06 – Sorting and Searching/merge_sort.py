def merge(items, sections, temporary_storage):
    (first_section_start, first_section_end), (second_section_start, second_section_end) = sections

    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Merge the two sections into temporary storage
    while left_index < first_section_end and right_index < second_section_end:
        if len(items[left_index]) > len(items[right_index]):
            temporary_storage[temp_index] = items[left_index]
            left_index += 1
        else:
            temporary_storage[temp_index] = items[right_index]
            right_index += 1
        temp_index += 1

    while left_index < first_section_end:
        temporary_storage[temp_index] = items[left_index]
        left_index += 1
        temp_index += 1

    while right_index < second_section_end:
        temporary_storage[temp_index] = items[right_index]
        right_index += 1
        temp_index += 1

    # Copy back to original list
    for i in range(temp_index):
        items[sections[0][0] + i] = temporary_storage[i]


def merge_sort(items):
    items_length = len(items)
    temporary_storage = [None] * items_length
    size_of_subsections = 1

    while size_of_subsections < items_length:
        for i in range(0, items_length, size_of_subsections * 2):
            first_section_start, first_section_end = i, min(i + size_of_subsections, items_length)
            second_section_start, second_section_end = first_section_end, min(first_section_end + size_of_subsections, items_length)
            sections = (first_section_start, first_section_end), (second_section_start, second_section_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    return items


# Example usage
example_list = ["apple", "dog", "cat", "elephant", "zebra", "catapault", "anything_everywhere"]
sorted_list = merge_sort(example_list)
print(sorted_list)
