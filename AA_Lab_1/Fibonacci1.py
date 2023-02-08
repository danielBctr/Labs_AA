# Fibonacci series using Recursion

import matplotlib.pyplot as plt
import datetime


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    print("Enter Fibonacci Number: ")
    n = int(input())
    t = []
    fibo = []

    for a in range(n+1):
        time = datetime.datetime.now()
        print(fibonacci(a))
        endTime = datetime.datetime.now()
        t.append((endTime - time).seconds)
        print(t[a])

    for b in range(n+1):
        fibo.append(b)

    plt.plot(fibo, t, color="red", linewidth=5)
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Time, in sec")


    plt.show()
