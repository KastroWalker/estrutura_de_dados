array = [-2, -1, 3, 4, 8, 50, 60, 37, 12, 11, 36, 70]


def selection_sort(array):
    for index in range(0, len(array)):
        smaller = array[index]

        for number in array[index:]:
            if number < smaller:
                smaller = number

        array.insert(index, array.pop(array.index(smaller)))

    return array


orded_array = selection_sort(array)
print(orded_array)
