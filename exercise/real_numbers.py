"""
Task
The point is that a natural number N (1 <= N <= 10^9) is given.
You need to write a function which finds the number of natural numbers 
not exceeding N and not divided by any of the numbers [2, 3, 5].


"""

def real_number(n):
    return n - n // 2 - n //3 - n // 5 + n // 6 + n // 10 + n // 15 - n // 30
    


def test_number_5():
    assert real_number(5) == 1
    
def test_number_10():
    assert real_number(10) == 2
    
def test_number_20():
    assert real_number(20) == 6
    
def test_number_75():
    assert real_number(75) == 20    
    
def test_number_100():
    assert real_number(100) == 26
    
if __name__ == '__main__':
    real_number(10)