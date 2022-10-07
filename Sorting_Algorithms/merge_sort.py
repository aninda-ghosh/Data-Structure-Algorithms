# from timeit import default_timer as timer
# import numpy as np

# dataset_size = 10

# dataArray = list(np.random.randint(dataset_size, size=dataset_size))
# print("Unsorted Array: ", )


def merge_sort(data_array):
    # First check if the data array length is more than 1
    # This is the recursive case the other case is the base case and will be used to terminate the recursive call
    if len(data_array) > 1:
        # Find the mid-point of the array
        mid_point = len(data_array)//2

        # Get the Left Part of the array
        # This is the reason why merge sort is not in place.
        # Since we require two auxiliary memory segments.
        L = data_array[:mid_point]
        R = data_array[mid_point:]

        # Make the recursive calls for the Left part
        merge_sort(L)

        # Make the recursive calls for the Right part
        merge_sort(R)

        # Now we need to compile the Individually sorted subsets
        # For that we will go through all the available elements and make elementwise comparisons
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data_array[k] = L[i]
                i += 1
            else:
                data_array[k] = R[j]
                j += 1
            k += 1

        # We also need to check if any pending elements are there since odd array length will have 1 elements extra
        while i < len(L):
            data_array[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            data_array[k] = R[j]
            k += 1
            j += 1

        return data_array
    else:
        return data_array


# if __name__ == "__main__":
#     start = timer()
#     merge_sort(dataArray)
#     end = timer()
#     print("Sorted Array: ", dataArray)
#     print("Elapsed Time ", end - start)
