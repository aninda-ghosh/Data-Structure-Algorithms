from timeit import default_timer as timer
import numpy as np

dataset_size = 10

jumbled_array = list(np.random.randint(dataset_size, size=dataset_size))
print("Unsorted Array: ", jumbled_array)


def bubble_sort(data_array):
    for i in range(len(data_array)):
        # Spanning the entire data set. The Minimum number of pass required is the number of elements in the Jumbled Up
        # Array
        for j in range(0, len(data_array)-i-1):
            # Check the subsets of the span from the ith position to the end
            # [3, 2, 1]
            # i = 3
            # j will span from 2 to 1 in the array
            # if there is an unsorted context then sort that and move on to the end of the program.
            if data_array[j] > data_array[j + 1]:
                # This implementation is much faster than the below one
                temp = data_array[j]
                data_array[j] = data_array[j+1]
                data_array[j+1] = temp
                # data_array[j+1] = data_array[j] + data_array[j+1]
                # data_array[j] = data_array[j+1] - data_array[j]
                # data_array[j+1] = data_array[j+1] - data_array[j]
                # The below implementation is much slower than the upward ones
                # data_array[j], data_array[j+1] = data_array[j+1], data_array[j]
    return data_array


if __name__ == "__main__":
    start = timer()
    sorted_array = bubble_sort(jumbled_array)
    end = timer()
    print("Sorted Array: ", sorted_array)
    print("Elapsed Time ", end-start)
