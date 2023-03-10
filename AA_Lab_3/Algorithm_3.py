# Algorithm 3

import time
import matplotlib.pyplot as plt


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


n_values = list(range(100, 100001, 10000))
time_values = []

for n in n_values:
    start_time = time.time()
    algorithm3(n)
    end_time = time.time()
    time_values.append(end_time - start_time)
    print("Time taken to compute primes up to {}: {:.5f} seconds".format(n, end_time - start_time))

plt.plot(n_values, time_values)
plt.title('Algorithm 3: ')
plt.xlabel('n')
plt.ylabel('Time taken (seconds)')
plt.show()
