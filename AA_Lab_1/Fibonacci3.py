# Fibonacci Series using power of the matrix {{1, 1}, {1, 0}}
import matplotlib.pyplot as plt
import datetime


def fibonacci(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]


    for i in range(2, n + 1):
        multiply(F, M)


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
    plt.title("Fibonacci Matrix")

    plt.show()
