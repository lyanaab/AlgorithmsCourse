import time

# Iterative function to calculate factorial
def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive function to calculate factorial
def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)

# Function to measure execution time
def measureExecutionTime(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, (end_time - start_time) * 1000  # Time in milliseconds

# Main testing
if __name__ == "__main__":
    test_values = [5, 10, 20,100,200,500,700,1000]  # Test values of n
    print("n\tIterative Time (ms)\t Recursive Time (ms)")

    for n in test_values:
        # Measure iterative factorial
        iter_result, iter_time = measureExecutionTime(fact_iterative, n)

        # Measure recursive factorial
        rec_result, rec_time = measureExecutionTime(fact_recursive, n)

        # Print results
        print(f" {n} \t {iter_time:.4f} \t\t\t {rec_time:.4f} ")
