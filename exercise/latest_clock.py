"""
    Write Function which receives 4 digits and return the latest
    time of day that can be built with those digits.
    The time should be in HH:MM format.
    
    Result should be a valid 24-hour time, between 00:00 and 23:59.
    
    examples:
        digits: 1, 9, 8, 3 => result: "19:38"
        digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)
"""

from itertools import permutations


def latest_clock(a, b, c, d):
    max_time = -1
    for h1, h2, m1, m2 in permutations([a, b, c, d]):
        hours = h1 * 10 + h2
        minutes = m1 * 10 + m2
        if hours < 24 and minutes < 60:
            max_time = max(max_time, hours * 60 + minutes)
    if max_time == -1:
        return ""
    return f"{max_time // 60:02d}:{max_time % 60:02d}"


def late_clock(*a):
    for h in range(23, -1, -1):
        for m in range(59, -1, -1):
            x = f'{h:02}'
            y = f'{m:02}'
            s = list(map(int,list(x + y)))
            if sorted(s)==sorted(a):
                return f'{x}:{y}'


def test_1():
    result = latest_clock(1, 9, 8, 3)
    assert result == "19:38"
    

def test_2():
    result = latest_clock(9, 1, 2, 5)
    assert result == "21:59"

    
if __name__ == '__main__':
    print(late_clock(0, 1, 2, 3))