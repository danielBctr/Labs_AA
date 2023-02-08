# Fibonacci Series using Dynamic Programming
import matplotlib.pyplot as plt
import datetime

def fibonacci(n):

    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

if __name__ == "__main__":

    print("Enter Fibonacci Number: ")
    n = int(input())
    t = []
    fibo = []

    for a in range(n):
        time = datetime.datetime.now()
        print(fibonacci(a))
        endTime = datetime.datetime.now()
        t.append((endTime - time).microseconds)
        print(t[a])

    for b in range(n):
        fibo.append(b)

    plt.plot(fibo, t, color="red", linewidth=5)
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Time, in sec")
    plt.title("Fibonacci Dynamic Programming")

    plt.show()
