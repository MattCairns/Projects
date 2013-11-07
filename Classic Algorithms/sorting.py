def bubble_sort(array):
    for n in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


print bubble_sort([52, 6, 12, 6, 13, 72, 54, 32, 645, 5, 3, 54, 32])
