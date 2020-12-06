#!/usr/bin/env python3


def get_unique_answers(answers):
    count = 0
    for answer in answers:
        s = set()
        for c in answer:
            s.add(c)
        count += len(s)
    
    return count


def get_same_answers(answers): 
    count = 0
    for answer in answers:
        sets = [set(a) for a in answer]
        intersection = set.intersection(*sets)
        count += len(intersection)
    
    return count


if __name__ == "__main__":
    with open('input') as f:
        lines = f.read().split("\n\n")

        # part1 and part2 are easier to solve depending on how array is formatted
        # TODO: Find an alternative
        answers = [[l for l in line.split()] for line in lines]
        a = [line.replace("\n", "") for line in lines]

        print("Part one:", get_unique_answers(a))
        print("Part two:", get_same_answers(answers))
