import time
import numpy as np
from matplotlib import pyplot as plt
from math import atan


def bbp(n):
    # Returns the nth decimal digit of Pi using the BBP formula.
    if n < 0:
        raise ValueError("Invalid value of n.")

    pi = 0
    for k in range(n + 1):
        pi += (1 / pow(16, k)) * (
                4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))

    return int(pi * pow(10, n) % 10)


def machin_formula(n):
    num_digits = n + 10

    pi_over_4 = 4 * (4 * atan(1 / 5) - atan(1 / 239))

    decimal_digits = []
    carry = 0

    for _ in range(num_digits):
        term = pi_over_4 * (10 ** (n + 1))
        quotient = (term + carry) // 10
        digit = quotient % 10
        carry = (term + carry) % 10
        decimal_digits.append(digit)

    return decimal_digits[n - 1] if n <= len(decimal_digits) else None


def spigot(n):

    if n < 0:
        raise ValueError("Invalid value of n.")

    pi = 0
    d = 1
    for i in range(n):
        pi += 4 * d
        d = (d * 10 - int(d * 10 / 10) * 10)

    return int(pi / pow(10, n - 1)) % 10


def bar(alg):
    plt.bar(1, alg[0], 0.4)
    plt.bar(2, alg[1], 0.4)
    plt.bar(3, alg[2], 0.4)
    plt.bar(4, alg[3], 0.4)
    plt.bar(5, alg[4], 0.4)


if __name__ == "__main__":

    n = [10, 50, 100, 200, 300]
    bbp_time = []
    machin_time = []
    spigot_time = []
    xAxis = []
    for i in n:
        xAxis.append(str(i))

    arr = [i for i in range(len(n))]
    x = np.arange(1, len(arr) + 1)

    for nr in n:
        startTime = time.perf_counter()
        bbp(nr)
        endTime = time.perf_counter()
        bbp_time.append(endTime - startTime)
        startTime = time.perf_counter()
        machin_formula(nr)
        endTime = time.perf_counter()
        machin_time.append(endTime - startTime)
        startTime = time.perf_counter()
        spigot(nr)
        endTime = time.perf_counter()
        spigot_time.append(endTime - startTime)

    plt.plot(bbp_time)
    plt.xticks(x, xAxis)
    plt.xlabel('Digit of Pi')
    plt.ylabel('Time(s)')
    plt.title('BBP algorithm')
    plt.show()

    plt.plot(machin_time)
    plt.xticks(x, xAxis)
    plt.xlabel('Digit of Pi')
    plt.ylabel('Time(s)')
    plt.title('Machin Formula algorithm')
    plt.show()

    plt.plot(spigot_time)
    plt.xticks(x, xAxis)
    plt.xlabel('Digit of Pi')
    plt.ylabel('Time(s)')
    plt.title('Spigot algorithm')
    plt.show()

    plt.plot(n, bbp_time, linewidth=3, label='BBP')
    plt.plot(n, machin_time, linewidth=3, label='Machin Formula')
    plt.plot(n, spigot_time, linewidth=3, label='Spigot')
    plt.xlabel('Digit of Pi')
    plt.ylabel('Time(s)')
    plt.title('Comparison:')
    plt.legend()
    plt.show()

