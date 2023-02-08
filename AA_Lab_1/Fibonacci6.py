# Fibonacci Series using Space Optimized Method 2

# Function for nth fibonacci number - Space Optimisation
import matplotlib.pyplot as plt
import datetime

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

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
    plt.title("Fibonacci Space Optimized Method 2")

    plt.show()
