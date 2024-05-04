import time
import matplotlib.pyplot as plt
from collections import defaultdict

# Top-Down Recursive Method
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Bottom-Up Dynamic Programming Method
def fib_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Function to measure execution time for both methods
def measure_execution_time(method, n_values):
    times = []
    for n in n_values:
        start_time = time.time()
        try:
            method(n)
        except:
            times.append(None)
            break
        times.append(time.time() - start_time)
    return times

# Counting overlaps
def fib_recursive_count(n, counter):
    if n <= 1:
        return n
    if n == 4:
        counter['F(4)'] += 1
    return fib_recursive_count(n - 1, counter) + fib_recursive_count(n - 2, counter)

# Plotting Task 1
n_values = range(1, 101)
recursive_times = measure_execution_time(fib_recursive, n_values)
dp_times = measure_execution_time(fib_dp, n_values)

plt.plot(n_values, recursive_times, label='Recursive (Top-Down)')
plt.plot(n_values, dp_times, label='DP (Bottom-Up)')
plt.xlabel('Fibonacci Number (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.title('Execution Time of Fibonacci Methods')
plt.show()

# Plotting Task 2
overlap_counts = []
for n in range(5, 51):
    counter = defaultdict(int)
    fib_recursive_count(n, counter)
    overlap_counts.append(counter['F(4)'])

plt.plot(range(5, 51), overlap_counts)
plt.xlabel('Fibonacci Number (n)')
plt.ylabel('Number of Times F(4) is Computed')
plt.title('Overlapping Subproblems in Recursive Method')
plt.show()