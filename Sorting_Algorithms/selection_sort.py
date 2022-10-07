from timeit import default_timer as timer
import numpy as np

dataset_size = 10

jumbled_array = list(np.random.randint(dataset_size, size=dataset_size))
print("Unsorted Array: ", jumbled_array)


def selection_sort(data_array):
    for i in range(len(data_array)):
        minimum = data_array[i]
        min_index = i
        # We start with the first element as probable minimum
        # Then we check with every other elements to find the minimum of the first pass and swap it with the desired
        # element
        for j in range(i + 1, len(data_array)):
            # We check for the rest of the elements for any global minima of that pass.
            # Swapping of elements make the selection sort unstable but it can be made stable by pushing every element
            # forward rather than swapping.
            if data_array[j] < minimum:
                minimum = data_array[j]
                min_index = j
        data_array[min_index] = data_array[i]
        data_array[i] = minimum
    return data_array


if __name__ == "__main__":
    start = timer()
    sorted_array = selection_sort(jumbled_array)
    end = timer()
    print("Sorted Array: ", sorted_array)
    print("Elapsed Time ", end - start)
