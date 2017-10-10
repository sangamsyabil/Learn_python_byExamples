# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
# the main idea of memorization is to store the values for recent function calls


from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range (1, 501):
    print(n, ": ", fibonacci(n))

# Happy coding!!!