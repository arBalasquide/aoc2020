#!/usr/bin/env python3

"""
Both parts run in O(N^2) time complexity. Kinda ugly solution but ¯\_(ツ)_/¯
"""

def part1(passwords):
    count = 0

    for password in passwords:
        parse = password.split()
        parse[0] = parse[0].split('-')
        if int(parse[2].count(parse[1][0])) <= int(parse[0][1]):
            if int(parse[2].count(parse[1][0])) >= int(parse[0][0]):
                count += 1
        
    return count


def part2(passwords):
    count = 0

    for password in passwords:
        parse = password.split()
        parse[0] = parse[0].split('-')  
        
        a = int(parse[0][0])
        b = int(parse[0][1])
        c = parse[1][0]

        if (parse[2][a-1] is c) != (parse[2][b-1] is c):
            count += 1
        
    return count


if __name__ == "__main__":
   with open('input') as f:
        passwords = f.readlines()

        print(part1(passwords))
        print(part2(passwords))
