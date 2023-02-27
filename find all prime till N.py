'''
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
'''

def generateAllPrimes(n):

    m={x:1 for x in range(2,n+1)}
    odd=3
    i=2
    while odd*i<=n:
        x=odd*i
        if m.has_key(x):
            m.pop(x)
        i+=1
    even=2
    i=2
    while even*i<=n:
        x=even*i
        if m.has_key(x):
            m.pop(x)
        i+=1
    return m.keys()

print generateAllPrimes(10)

print generateAllPrimes(11)
print generateAllPrimes(12)

print generateAllPrimes(100)