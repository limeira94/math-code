"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It' s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

from collections import Counter


def find_uniq(arr):
    a, b = set(arr)
    print(a, b)
    return a if arr.count(a) == 1 else b


def find_uniq1(arr):
    freq = Counter(arr)
    for e, c in freq.items():
        if c == 1:
            return e    


def find_uniq2(arr):
    """
    The method count in loop is not efficient because is O(n^2)
    """
    for i in arr:
        if arr.count(i) == 1:
            return i


def test_1():
    result = find_uniq([1, 1, 1, 2, 1, 1])
    assert result == 2
    
    
def test_2():
    result = find_uniq([0, 0, 0.55, 0, 0])
    assert result == 0.55

    
if __name__ == '__main__':
    find_uniq([1, 1, 1, 3, 1, 1])
    