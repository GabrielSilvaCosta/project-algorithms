def merge(left, right):
    merged = []
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    merged.extend(left[left_cursor:])
    merged.extend(right[right_cursor:])

    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array.copy()

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def are_lists_equal(list1, list2):
    return all(x == y for x, y in zip(list1, list2))


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return "", "", False

    first_sorted = merge_sort(list(first_string.lower()))
    second_sorted = merge_sort(list(second_string.lower()))

    is_anagram = len(first_sorted) == len(second_sorted) and are_lists_equal(
        first_sorted, second_sorted
    )

    return "".join(first_sorted), "".join(second_sorted), is_anagram
