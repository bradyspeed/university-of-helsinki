# Write your solution here
from math import factorial

def factorials(n: int):
    new_dictionary = {}
    for i in range(1, n + 1):
        new_dictionary[i] = factorial(i)
    return new_dictionary



if __name__ == "__main__":
    k = factorials(20)
    print(k[5])