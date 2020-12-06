#!/usr/bin/env python3


def get_sum(sets):
    print("Part one:", sum(len(set.union(*group)) for group in answers))
    print("Part two:", sum(len(set.intersection(*group)) for group in answers))


if __name__ == "__main__":
    with open('input') as f:
        answers = [
            list(set(yes for yes in person.strip()) for person in group.split())
            for group in f.read().split('\n\n')
        ]
    
        get_sum(answers)
