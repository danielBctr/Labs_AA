# Algorithm 1

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


n_values = list(range(100, 1000001, 10000))
time_values = []

for n in n_values:
    start_time = time.time()
    algorithm1(n)
    end_time = time.time()
    time_values.append(end_time - start_time)
    print("Time taken to compute primes up to {}: {:.5f} seconds".format(n, end_time - start_time))

plt.plot(n_values, time_values)
plt.title('Algorithm 1: ')
plt.xlabel('Nuber')
plt.ylabel('Time taken (seconds)')
plt.show()
