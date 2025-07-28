"""
Write a function that prints the prime factors of a given number

example input = 100
output = 2 5

"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(a):
    factors = []
    for i in range(2, a + 1):
        if is_prime(i) and a % i == 0:
            factors.append(i)
    print("Prime factors are:", *factors)

a = int(input("Please enter a number: "))
prime_factors(a)


