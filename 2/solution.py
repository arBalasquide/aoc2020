#!/usr/bin/env python3

"""
Kinda ugly solution but ¯\_(ツ)_/¯
"""


def part1(data):
    count = 0
    for password in data:
        parse = password.split()
        parse[0] = parse[0].split('-')
        if int(parse[2].count(parse[1][0])) <= int(parse[0][1]):
            if int(parse[2].count(parse[1][0])) >= int(parse[0][0]):
                count += 1
        
    return count


def part2(data):
    count = 0
    for password in data:
        parse = password.split()
        ranges = parse[0].split('-')  
        
        char = parse[1][0]

        policy1 = parse[2][int(ranges[0])-1] is char
        policy2 = parse[2][int(ranges[1])-1] is char

        if policy1 ^ policy2:
            count += 1
        
    return count


if __name__ == "__main__":
   with open('input') as f:
        data = f.readlines()

        print("Part one:", part1(data))
        print("Part two:", part2(data))
