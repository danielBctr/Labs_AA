# Bubble Sort

import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [870, 406, 566, 776, 179, 941, 855, 820, 942, 171, 717, 459, 547, 444,
         999, 246, 948, 604, 651, 782, 148, 394, 484, 292, 135, 125, 877, 742,
         261, 687, 858, 286, 683, 940, 321, 756, 496, 508, 419, 334, 800, 508, 87,
         660, 395, 5, 810, 706, 236, 412, -23, 256, 839, 565, 50, 291, 938, 741,
         268, 617, 744, 534, 192, 677, 493, 998, 751, 826, 489, 34, -11, 931, 550,
         776, 685, 554, 53, 23, 324, 880, 289, 397, 549, 646, 483, 995, 474, 417,
         310, 968, 755, 828, 785, 780, 146, 805, 615, 86, 55, -33]
    times = []
    for i in range(10):
        start_time = time.time()
        bubble_sort(arr)
        times.append(time.time() - start_time)
        time.sleep(0.5)
    print("Sorted array is: ", arr)
    plt.plot(range(1, 11), times)
    plt.title('Bubble Sort Execution Time')
    plt.xlabel('Attempt')
    plt.ylabel('Time (s)')
    plt.show()
