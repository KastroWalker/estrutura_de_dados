array = [-2, -1, 3, 4, 8, 50, 60, 37, 12, 11, 36, 70]


def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)

    if end - start > 1:
        middle = (end + start) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle, end)
        merge(array, start, middle, end)

    return array


def merge(array, start, middle, end):
    left = array[start:middle]
    right = array[middle:end]
    top_left = 0
    top_right = 0

    for index in range(start, end):
        if top_left >= len(left):
            array[index] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            array[index] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            array[index] = left[top_left]
            top_left += 1
        else:
            array[index] = right[top_right]
            top_right += 1


orded_array = merge_sort(array)
print(orded_array)
