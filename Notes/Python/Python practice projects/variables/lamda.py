# Lambda expressions in Python allow the creation of small, anonymous functions. 
# They are handy for situations where defining a full function might be overkill. 
# Lambda functions are limited to a single expression.

# Creating a lambda function that returns the sum of its two arguments
sum_lambda = lambda a, b: a + b
result = sum_lambda(3, 4)
print(result)  # Output: 7

# Defining a function that generates another function
def make_incrementor(n):
    return lambda x: x + n

# Creating a function that increments by 42
f = make_incrementor(42)
result1 = f(0)  # Output: 42
result2 = f(1)  # Output: 43

# Creating a list of pairs
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Sorting the list based on the second element of each pair
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
