import time
import matplotlib.pyplot as plt


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quickSort(left) + [pivot] + quickSort(right)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


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


if __name__ == "__main__":
    arr = [870, 406, 566, 776, 179, 941, 855, 820, 942, 171, 717, 459, 547, 444,
           999, 246, 948, 604, 651, 782, 148, 394, 484, 292, 135, 125, 877, 742,
           261, 687, 858, 286, 683, 940, 321, 756, 496, 508, 419, 334, 800, 508, 87,
           660, 395, 5, 810, 706, 236, 412, -23, 256, 839, 565, 50, 291, 938, 741,
           268, 617, 744, 534, 192, 677, 493, 998, 751, 826, 489, 34, -11, 931, 550,
           776, 685, 554, 53, 23, 324, 880, 289, 397, 549, 646, 483, 995, 474, 417,
           310, 968, 755, 828, 785, 780, 146, 805, 615, 86, 55, -33]

    times_bubble = []
    times_quik = []
    times_merge = []
    times_heap = []

    for i in range(10):
        arr_copy = arr.copy()

        start_time = time.time()
        bubbleSort(arr_copy)
        end_time = time.time()
        times_bubble.append(end_time - start_time)

        arr_copy = arr.copy()
        start_time = time.time()
        quickSort(arr_copy)
        end_time = time.time()
        times_quik.append(end_time - start_time)

        arr_copy = arr.copy()
        start_time = time.time()
        mergeSort(arr_copy)
        end_time = time.time()
        times_merge.append(end_time - start_time)

        arr_copy = arr.copy()
        start_time = time.time()
        heapSort(arr_copy)
        end_time = time.time()
        times_heap.append(end_time - start_time)

        time.sleep(0.5)  # slowing down the execution for a clearer graph

    plt.plot(range(1, 11), times_bubble, label='Bubble Sort')
    plt.plot(range(1, 11), times_quik, label='Quik Sort')
    plt.plot(range(1, 11), times_merge, label='Merge Sort')
    plt.plot(range(1, 11), times_heap, label='Heap Sort')
    plt.legend()
    plt.title('Sorting Algorithm Comparison')
    plt.xlabel('Attempt')
    plt.ylabel('Time (s)')
    plt.show()

