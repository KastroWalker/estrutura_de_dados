def binary_search(array, value, start=0, end=None):
    if end == None:
        end = len(array)-1

    if start <= end:
        middle = (start + end) // 2
        if array[middle] == value:
            return middle

        if value < array[middle]:
            return binary_search(array, value, start, middle - 1)
        else:
            return binary_search(array, value, middle + 1, end)

    return -1


array = [1, 2, 3, 4, 8, 11, 12, 36, 37, 50, 60, 70]

print(binary_search(array, 12))
print(binary_search(array, 1))
print(binary_search(array, 70))
print(binary_search(array, 100))
