# Heap Sort

import time
import matplotlib.pyplot as plt

def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, N, largest)

def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [870, 406, 566, 776, 179, 941, 855, 820, 942, 171, 717, 459, 547, 444,
         999, 246, 948, 604, 651, 782, 148, 394, 484, 292, 135, 125, 877, 742,
         261, 687, 858, 286, 683, 940, 321, 756, 496, 508, 419, 334, 800, 508, 87,
         660, 395, 5, 810, 706, 236, 412, -23, 256, 839, 565, 50, 291, 938, 741,
         268, 617, 744, 534, 192, 677, 493, 998, 751, 826, 489, 34, -11, 931, 550,
         776, 685, 554, 53, 23, 324, 880, 289, 397, 549, 646, 483, 995, 474, 417,
         310, 968, 755, 828, 785, 780, 146, 805, 615, 86, 55, -33]

    times = []  # store execution times
    for i in range(10):
        start_time = time.time()  # record start time
        heapSort(arr)
        end_time = time.time()  # record end time
        times.append(end_time - start_time)
        time.sleep(1)  # slow down execution for clearer graph

    N = len(arr)
    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")

    plt.plot(range(10), times)
    plt.title('Heap Sort Execution Time')
    plt.xlabel('Iteration')
    plt.ylabel('Time (s)')
    plt.show()
