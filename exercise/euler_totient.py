"""
In number theory, Euler's totient is an arithmetic function, introduced in 1763 by Euler, that counts the positive 
integers less than or equal to n that are relatively prime to n. Thus, if n is a positive integer, then φ(n), notation
introduced by Gauss in 1801, is the number of positive integers k ≤ n for which gcd(n, k) = 1.
The totient function is important in number theory, mainly because it gives the order of the multiplicative group of 
integers modulo n. The totient function also plays a key role in the definition of the RSA encryption system.

For example let n = 9.
Then gcd(9, 3) = gcd(9, 6) = 3 and gcd(9, 9) = 9.
The other six numbers in the range 1 ≤ k ≤ 9 i.e. 1, 2, 4, 5, 7, 8 are relatively prime to 9.
Therefore, φ(9) = 6.
As another example, φ(1) = 1 since gcd(1, 1) = 1.

There are generally two approaches to this function:

Iteratively counting the numbers k ≤ n such that gcd(n,k) = 1.

Using the Euler product formula.
This is an explicit formula for calculating φ(n) depending on the prime divisor of n:
φ(n) = n * Product (1 - 1/p) where the product is taken over the primes p ≤ n that divide n.
For example: φ(36) = 36 * (1 - 1/2) * (1 - 1/3) = 36 * 1/2 * 2/3 = 12.
This second method seems more complex and not likely to be faster, but in practice we will often look for φ(n) with n prime. 
It correctly gives φ(n) = n - 1 if n is prime.

You have to code the Euler totient function, that takes an integer 1 ≤ n as input and returns φ(n).

You do have to check if n is a number, is an integer and that 1 ≤ n; if that is not the case, the function should return 0.

Input range: 1 ≤ n ≤ 1e10
"""


def totient(n):
    
    if isinstance(n, str) or n == None or n < 1:
        return 0
    
    euler = n
    primos = set()
    
    i = 2
    while i * i <= n:
        while n % i == 0:
            primos.add(i)
            n = n // i
        i += 1
    
    if n > 2:
        primos.add(n)

    for p in primos:
        euler *= (1 - (1 / p))
        
    return int(euler)


def test_euler_1():
    assert totient(1) == 1

def test_euler_6():
    assert totient(6) == 2

def test_euler_5():
    assert totient(5) == 4

def test_euler_9():
    assert totient(9) == 6    

def test_euler_36():
    assert totient(36) == 12

def test_euler_983():
    assert totient(983) == 982
    
def test_euler_negative():
    assert totient(-1) == 0

def test_euler_string():
    assert totient('a') == 0
    
def test_euler_none():
    assert totient(None) == 0