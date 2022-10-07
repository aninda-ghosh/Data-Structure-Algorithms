"""
Operations on Max Heap

1. Return minimum value
2. Pop minimum element
3. Decreasing Key - Basically to fix the Unordered Heap
4. Insert
5. Delete

Python has an implementation for heap
using heapq for priority queue
"""
import math


class MAXHEAP:
    array = []
    array_len = 0

    def __init__(self):
        self.array_len = 0
        self.array = []

    def insert(self, value):
        self.array.append(value)
        self.array_len += 1

    def insert_bulk(self, list_array):
        for item in list_array:
            self.array.append(item)
            self.array_len += 1

    def delete(self):
        if self.array_len <= 0:
            return
        self.array.pop(0)
        self.array_len -= 1
        self.build_heap()

    def peek_max(self):
        return self.array[0]

    def print(self):
        print("Heap {0}, Length {1}".format(self.array, self.array_len))

    def build_heap(self):
        i = math.floor(self.array_len/2)
        while i >= 0:
            self.heapify(self.array, self.array_len, i)
            # self.printify()
            i -= 1

    @staticmethod
    def heapify(arr, lenOfArray, index):
        parent = index
        l_child = (2*index) + 1
        r_child = (2*index) + 2

        if l_child < lenOfArray and arr[l_child] > arr[parent]:
            arr[parent], arr[l_child] = arr[l_child], arr[parent]

        if r_child < lenOfArray and arr[r_child] > arr[parent]:
            arr[parent], arr[r_child] = arr[r_child], arr[parent]


# if __name__ == "__main__":
#
#     array = [10, 30, 50, 40, 35, 15]
#
#     heap = MAXHEAP()
#
#     heap.insert_bulk(array)
#     heap.print()
#
#     heap.build_heap()
#     heap.print()
