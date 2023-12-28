"""
The triangular numbers, Tn, may be obtained by this formula:

T(n) = n * (n + 1) / 2
We select, for example, the first 5 (n terms) consecutive terms of this sequence.

They will be: 1, 3, 6, 10 and 15

Now we want to obtain, again for example, the first 8 (m terms) consecutive multiples to all of these five triangular numbers.

The least common multiple of them will be, 30, so the first eight multiple terms (for the sequence of the above five triangular numbers) will be:

30, 60, 90, 120, 150, 180, 210 and 240

Finally the sum of all these multiples will be: 30 + 60 + 90 + 120 + 150 + 180 + 210 + 240 = 1080

We want the function sum_mult_triangnum() that may calculate this sum with different values of n and m terms.

The values of n and m will be always integer values higher than 2.
"""

"""
    1. list [1, 2, 3, 4, 5]
    2. calculate o T(n) for each n
    3. add in a set()
    4. get least common multiple
    5. take mmc in multiple m elements
    6. add the multiples
"""

def gcd(a, b):
    """Calcula o MDC (maior divisor comum) usando o algoritmo de euclides"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Calcula o MMC (mínimo multiplo comum)"""
    return abs(a*b) // gcd(a, b)
 
 
def arithmetic_serie_sum(m, lcm):
    return m * (m + 1) // 2 * lcm


def sum_mult_triangnum(n, m):
    """
    This function performs better than the one mentioned
    """

    lcm_result = 1
    for i in range(1, n + 1):
        t_number = i * (i + 1) // 2
        lcm_result = lcm(lcm_result, t_number)
        
    sum_result = arithmetic_serie_sum(m, lcm_result)
    
    return sum_result
    # list_n = []
    # for i in range(1, n + 1):
    #     t_number = i * (i + 1) / 2
    #     list_n.append(t_number)
    
    # lcm_result = list_n[0]
    # for num in list_n[1:]:
    #     lcm_result = lcm(lcm_result, num)
    
    # sum_result = sum([e * lcm_result for e in range(1, m + 1)])
    
    # return sum_result



# def test_lcm_result():
#     assert sum_mult_triangnum(5, 8) == 30

# def test_calculate_trg_number():
#     assert sum_mult_triangnum(5, 8) == [1, 3, 6, 10, 15] 

def test_numbers_5_8():
    assert sum_mult_triangnum(5, 8) == 1080
    
def test_numbers_7_10():
    assert sum_mult_triangnum(7, 10) == 23100
    
def test_numbers_10_15():
    assert sum_mult_triangnum(10, 15) == 1663200    