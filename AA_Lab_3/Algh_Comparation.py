# Comparing all together
import math
import time
import matplotlib.pyplot as plt

def algorithm1(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i * i <= n:
        if c[i] == True:
            j = i * i
            while j <= n:
                c[j] = False
                j = j + i
        i = i + 1
    return c

def algorithm2(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j = j + i
        i = i + 1
    return c

def algorithm3(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1
    return c

def algorithm4(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0:
                c[i] = False
            j = j + 1
        i = i + 1
    return c

def algorithm5(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                c[i] = False
            j = j + 1
        i = i + 1
    return c

n_values = [1000, 5000, 10000, 50000]

t1 = []
t2 = []
t3 = []
t4 = []
t5 = []

for n in n_values:
    start_time = time.time()
    algorithm1(n)
    end_time = time.time()
    t1.append(end_time - start_time)

    start_time = time.time()
    algorithm2(n)
    end_time = time.time()
    t2.append(end_time - start_time)

    start_time = time.time()
    algorithm3(n)
    end_time = time.time()
    t3.append(end_time - start_time)

    start_time = time.time()
    algorithm4(n)
    end_time = time.time()
    t4.append(end_time - start_time)

    start_time = time.time()
    algorithm5(n)
    end_time = time.time()
    t5.append(end_time - start_time)

plt.plot(n_values, t1, label="Algorithm 1")
plt.plot(n_values, t2, label="Algorithm 2")
plt.plot(n_values, t3, label="Algorithm 3")
plt.plot(n_values, t4, label="Algorithm 4")
plt.plot(n_values, t5, label="Algorithm 5")
plt.title('Putting All Together: ')
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.legend()
plt.show()
