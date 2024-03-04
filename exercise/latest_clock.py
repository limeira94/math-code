"""
    Write Function which receives 4 digits and return the latest
    time of day that can be built with those digits.
    The time should be in HH:MM format.
    
    Result should be a valid 24-hour time, between 00:00 and 23:59.
    
    examples:
        digits: 1, 9, 8, 3 => result: "19:38"
        digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)
"""

def latest_clock(a, b):
    first_element = [0, 1, 2]
    maior_element = max(filter(lambda x: x in first_element, [a, b]))
    return f"{maior_element}: {b if a == maior_element else a}"


def test_1():
    result = latest_clock(1, 9, 8, 3)
    assert result == "19:38"
    
    
if __name__ == '__main__':
    print(latest_clock(3, 3))