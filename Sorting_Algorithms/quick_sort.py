from timeit import default_timer as timer
import numpy as np

dataset_size = 10

dataArray = list(np.random.randint(dataset_size, size=dataset_size))
print("Unsorted Array: ", dataArray)


def partition(arr, _start_, _end_):
    pivot = arr[_end_]    # Using last element as pivot
    swap_pos = _start_-1  # This is used to track to be empty positions

    i = _start_
    while i < _end_:
        if arr[i] < pivot:
            swap_pos += 1
            # Swapping Elements
            swap_var = arr[swap_pos]
            arr[swap_pos] = arr[i]
            arr[i] = swap_var
        i += 1

    swap_pos += 1

    swap_var = arr[swap_pos]
    arr[swap_pos] = arr[i]
    arr[i] = swap_var

    # Return the position of the Pivot
    return swap_pos


def quick_sort(arr, _start_, _end_):
    if _start_ < _end_:
        pix = partition(arr, _start_, _end_)
        quick_sort(arr, _start_, pix-1)   # Apply quick sort on the left hand side of the array
        quick_sort(arr, pix+1, _end_)   # Apply quick sort on the right hand side of the array


if __name__ == "__main__":
    _start_ = timer()
    # Call the recursive function
    quick_sort(dataArray, 0, dataset_size-1)
    _end_ = timer()
    print("Sorted Array: ", dataArray)
    print("Elapsed Time ", _end_ - _start_)
