def sequential_search(array, value):
    index = 0
    for i in array:
        if value == i:
            return index

        index += 1

    return -1


array = [2, 1, 3, 4, 8, 50, 60, 37, 12, 11, 36, 70]

print(sequential_search(array, 11))
print(sequential_search(array, 1))
print(sequential_search(array, 70))
print(sequential_search(array, 100))
