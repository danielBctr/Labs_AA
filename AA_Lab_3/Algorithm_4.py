# Algorithm 4

import time
import matplotlib.pyplot as plt


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


n_values = list(range(100, 10001, 1000))
time_values = []

for n in n_values:
    start_time = time.time()
    algorithm4(n)
    end_time = time.time()
    time_values.append(end_time - start_time)
    print("Time taken to compute primes up to {}: {:.5f} seconds".format(n, end_time - start_time))

plt.plot(n_values, time_values)
plt.title('Algorithm 4: ')
plt.xlabel('n')
plt.ylabel('Time taken (seconds)')
plt.show()
