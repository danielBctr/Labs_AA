# Fibonacci Series using O(Log n) Time Method
import matplotlib.pyplot as plt
import datetime
MAX = 10000

# Create an array for memoization
f = [0] * MAX

def fib(n):
    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])


    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    if ((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]

if __name__ == "__main__":

    print("Enter Fibonacci Number: ")
    n = int(input())
    t = []
    fibo = []

    for a in range(n):
        time = datetime.datetime.now()
        print(fib(a))
        endTime = datetime.datetime.now()
        t.append((endTime - time).microseconds)
        print(t[a])

    for b in range(n):
        fibo.append(b)

    plt.plot(fibo, t, color="red", linewidth=5)
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Time, in sec")
    plt.title("Fibonacci O(Log n)")

    plt.show()
