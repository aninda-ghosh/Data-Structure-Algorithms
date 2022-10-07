from timeit import default_timer as timer
import numpy as np

dataset_size = 10

jumbled_array = list(np.random.randint(dataset_size, size=dataset_size))
print("Unsorted Array: ", jumbled_array)

# Insertion sort is quick when the data array is partially sorted since its number of operations get reduced
# significantly


def insertion_sort(data_array):
    for i in range(1, len(data_array)):
        key = data_array[i]
        j = i - 1
        # Compare the key element with everything preceding it and see if the key is smaller than the predecessor, if
        # yes then shift the data towards right and place the element in its proper position.
        while j >= 0 and key < data_array[j]:
            data_array[j + 1] = data_array[j]
            j = j-1
        data_array[j+1] = key
    return data_array


if __name__ == "__main__":
    start = timer()
    sorted_array = insertion_sort(jumbled_array)
    end = timer()
    print("Sorted Array: ", sorted_array)
    print("Elapsed Time ", end - start)
