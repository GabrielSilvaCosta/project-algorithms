def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        merged = []

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
            k += 1

        merged.extend(left_half[i:])
        merged.extend(right_half[j:])

        arr[:] = merged


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return "", "", False

    first_sorted = list(first_string.lower())
    second_sorted = list(second_string.lower())

    merge_sort(first_sorted)
    merge_sort(second_sorted)

    result = first_sorted == second_sorted

    return "".join(first_sorted), "".join(second_sorted), result
