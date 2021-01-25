array = [-2, -1, 3, 4, 8, 50, 60, 37, 12, 11, 36, 70]


def insertion_sort(array):
    for index in range(0, len(array)):
        smaller = array[index]

        while index > 0 and array[index - 1] > smaller:
            array[index] = array[index - 1]
            index -= 1

        array[index] = smaller

    return array


orded_array = insertion_sort(array)
print(orded_array)
