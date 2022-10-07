from Sorting_Algorithms.merge_sort import merge_sort
import math
import matplotlib.pyplot as plt

def dist(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) * (p1[0] - p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1])))


def stripClosest(arr_strip, delta):
    # Initialize the minimum distance as d
    min_val = delta

    sorted_strip = merge_sort(arr_strip)
    print(sorted_strip)

    i = j = 0
    for i in range(len(sorted_strip)):
        for j in range(0, 6):
            if



    return min_val

def Closest_Pair(arr_points):
    # when the array contains 2 elements calculate the distance
    if len(arr_points) and len(arr_points) == 2:
        return dist(arr_points[0], arr_points[1])

    # DIVIDE STEP
    # Find the median in the x direction
    median = len(arr_points) // 2
    # Recursively run the same function
    delta_1 = Closest_Pair(arr_points[:median])  # Left Half
    delta_2 = Closest_Pair(arr_points[median + 1:])  # Right Half
    delta = min(delta_1, delta_2)

    # Find the strip of elements whose x distance is delta from the partitioning line.
    mid_point = arr_points[median]
    print(mid_point)

    # GENERATE STRIP STEP
    strip = []
    for point in arr_points:
        if dist(mid_point, point) < delta:
            strip.append(point)

    # CHECK AND COMBINE STEP




    return delta


if __name__ == "__main__":
    # Points = [Point(2, 3), Point(4, 5), Point(1, 2), Point(2, 4), Point(5, 6), Point(7, 8), Point(1, 9), Point(2, 6)]
    Points = [(2, 3), (4, 5), (1, 2), (2, 4), (5, 6), (7, 8), (1, 9), (2, 6)]

    points_sorted = sorted(Points)

    print(points_sorted)

# function to show the plot
plt.show()
