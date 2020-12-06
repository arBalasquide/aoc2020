#!/usr/bin/env python3


def get_questions_answered(answers):
    count = 0
    for answer in answers:
        s = {a for a in answer}
        count += len(s)
    
    return count


def get_intersecting_answers(answers): 
    count = 0
    for answer in answers:
        sets = [set(a) for a in answer]
        intersection = set.intersection(*sets)
        count += len(intersection)
    
    return count


if __name__ == "__main__":
    with open('input') as f:
        lines = f.read().split("\n\n")

        # TODO: Find an alternative to this inneficiency
        answers = [[l for l in line.split()] for line in lines]
        a = [line.replace("\n", "") for line in lines]

        print("Part one:", get_questions_answered(a))
        print("Part two:", get_intersecting_answers(answers))
