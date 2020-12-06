#!/usr/bin/env python3


def get_number(characters, r, upper, lower):
    for c in characters:
        division = (len(r)+1)//2
        if c is upper:
            r = r[division:]
        elif c is lower:
            r = r[:division]

    return r[0]


def get_seat_id(p):
    row_range = [i for i in range(0, 127+1)]
    col_range = [i for i in range(0, 7+1)]
    
    row_number = get_number(p[:7], row_range, "B", "F")
    col_number = get_number(p[7:], col_range, "R", "L")

    return (row_number*8) + col_number


def find_max(passes):
    max_id = 0
    for p in passes:
        id = int(get_seat_id(p))
        if id > max_id:
            max_id = id

    return max_id


# Maybe better to store in hashset since lookup is O(1)
# and then itll just be a linear search ... for i in range(...) do hashset.contains(i)
def find_pass(passes):
    ids = [get_seat_id(p) for p in passes]
    ids.sort()

    # Sort then do binary search
    # sort() O(n logn)
    # Binary Search O(log n)
    a = mid = 0
    b = len(ids) - 1
    while b > a + 1: 
        mid = (a + b) // 2
        if (ids[a] - a) != (ids[mid] - mid): 
            b = mid 
        elif (ids[b] - b) != (ids[mid] - mid): 
            a = mid

    return ids[mid] + 1


if __name__ == "__main__":
    with open('input') as f:
        passes = [line.strip() for line in f]

        print("Part one:", find_max(passes))
        print("Part Two:", find_pass(passes))
