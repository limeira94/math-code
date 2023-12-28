"""
Task
Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer).
x and y are non-zero integers, therefore the given point never lies on the axes.

Examples
(1, 2)     => 1
(3, 5)     => 1
(-10, 100) => 2
(-1, -9)   => 3
(19, -56)  => 4
"""

def quadrant(x, y):
    if x == 0 or y == 0:
        return 'x and y must not be zero'
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


def test_quadrant_1():
    result = quadrant(1, 2)
    assert result == 1
    
def test_quadrant_2():
    result = quadrant(-1, 2)
    assert result == 2

def test_quadrant_3():
    result = quadrant(-1, -2)
    assert result == 3        
    
def test_quadrant_4():
    result = quadrant(1, -2)
    assert result == 4   
    
def test_quadrant_with_0():
    result = quadrant(0, 1)
    assert result == 'x and y must not be zero'