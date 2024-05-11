'''
Task 1
--------------------------------------------------------------------------------------------

Closure in programming is a function that retains references to variables from its lexical context, i.e., 
from the area where it was declared.
Implement the function caching_fibonacci, which creates and uses a cache to store and reuse already computed Fibonacci numbers.
The Fibonacci sequence is a series of numbers such as: 0, 1, 1, 2, 3, 5, 8, ..., where each subsequent number is the sum 
of the two preceding ones.

In general, to calculate the nth Fibonacci number, the following expression needs to be evaluated.
This task can be solved recursively, calling the function that computes the sequence numbers 
until the call reaches the terms of the sequence less than n=1, where the sequence is defined.

Task Requirements:

• The function caching_fibonacci() should return an inner function fibonacci(n).
  fibonacci(n) computes the nth Fibonacci number. If the number is already in the cache, 
  the function should return the value from the cache.
• If the number is not in the cache, the function should compute it, save it in the cache, and return the result.
• Using recursion to compute Fibonacci numbers.

Execution Recommendations:

• As a recommendation, we provide the pseudocode for the task.

👆 Pseudocode is a way of writing an algorithm or program code used to describe an idea or process in a form 
understandable to humans. It is not intended for direct execution on a computer but helps developers 
clearly understand and plan how the program or algorithm will work. Its main goal is to clearly and simply 
convey the idea of the algorithm.

Here is the pseudocode for the caching_fibonacci function, which calculates Fibonacci numbers using caching:

FUNCTION caching_fibonacci
    Create an empty dictionary cache

    FUNCTION fibonacci(n)
        If n <= 0, return 0
        If n == 1, return 1
        If n is in cache, return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Return cache[n]

    Return function fibonacci
END FUNCTION caching_fibonacci

The caching_fibonacci function creates an inner function fibonacci and a dictionary cache to store the results 
of calculating Fibonacci numbers. Each time fibonacci(n) is called, it first checks whether the value 
for n is already saved in the cache. If the value is in the cache, it is returned immediately, significantly 
reducing the number of recursive calls. If the value is not in the cache, it is calculated recursively and 
stored in the cache. The caching_fibonacci function returns the inner function fibonacci, which can now be 
used to calculate Fibonacci numbers using caching.

Evaluation Criteria:

• Correct implementation of the fibonacci(n) function considering the use of the cache.
• Efficient use of recursion and caching to optimize calculations.
• Code cleanliness, including readability and the presence of comments.

Usage Example:

# Obtain the fibonacci function
  fib = caching_fibonacci()

# Use the fibonacci function to compute Fibonacci numbers
  print(fib(10))  # Outputs 55
  print(fib(15))  # Outputs 610

In this example, when you call fib(10) or fib(15), the fibonacci function inside caching_fibonacci 
calculates the respective Fibonacci numbers, storing previous results in the cache. 
This makes subsequent calls for the same values of n much faster, as they simply return the value 
from the cache. Closure allows fibonacci(n) to "remember" the state of the cache between different calls, 
which is key to caching computation results.
'''

def caching_fibonacci():
    # This dictionary will act as the cache to store computed Fibonacci numbers
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            # Return the cached result if already computed
            return cache[n]  
        
        # Compute the Fibonacci number recursively and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return the nested function
    return fibonacci  

# Test the function
fib = caching_fibonacci()

# Calculate and print Fibonacci numbers using the memoized function
print(fib(10))  # Outputs 55, the 10th Fibonacci number
print(fib(15))  # Outputs 610, the 15th Fibonacci number
