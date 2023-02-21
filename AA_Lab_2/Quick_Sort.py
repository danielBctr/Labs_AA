# QuickSort

import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Create a list to store the execution times
execution_times = []

for i in range(10):
    arr = [870, 406, 566, 776, 179, 941, 855, 820, 942, 171, 717, 459, 547, 444,
         999, 246, 948, 604, 651, 782, 148, 394, 484, 292, 135, 125, 877, 742,
         261, 687, 858, 286, 683, 940, 321, 756, 496, 508, 419, 334, 800, 508, 87,
         660, 395, 5, 810, 706, 236, 412, -23, 256, 839, 565, 50, 291, 938, 741,
         268, 617, 744, 534, 192, 677, 493, 998, 751, 826, 489, 34, -11, 931, 550,
         776, 685, 554, 53, 23, 324, 880, 289, 397, 549, 646, 483, 995, 474, 417,
         310, 968, 755, 828, 785, 780, 146, 805, 615, 86, 55, -33]

    # Start the timer
    start_time = time.time()

    # Sort the array
    quicksort(arr, 0, len(arr) - 1)

    # End the timer
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    # Append the execution time to the list
    execution_times.append(execution_time)

    # Slow down the execution by 0.5 seconds
    time.sleep(0.5)

print(f'Sorted array: {arr}')

# Plot the graph
plt.plot(execution_times)
plt.title("Quick Sort Execution Times")
plt.xlabel("Execution Number")
plt.ylabel("Execution Time (Seconds)")
plt.show()

