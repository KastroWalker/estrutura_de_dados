array = [-2, -1, 3, 4, 8, 50, 60, 37, 12, 11, 36, 70]


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array)-1
    if start < end:
        p = partition(array, start, end)
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)

    return array


def partition(array, start, end):
    pivot = array[end]
    i = start
    for index in range(start, end):
        if array[i] <= pivot:
            array[index], array[i] = array[i], array[index]
            i = i + 1

    array[i], array[end] = array[end], array[i]
    return i


orded_array = quick_sort(array)
print(orded_array)
