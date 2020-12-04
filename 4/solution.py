#!/usr/bin/env python3

import re


"""
Ugly solution but i don't think much could've been done
for this specific problem.
"""

def contains_tags(passport, tags):
    for tag in tags:
        if tag not in passport:
            return False
    return True


def validate_passports(passports, tags):
    count = 0
    for passport in passports:
        if contains_tags(passport, tags):
            count += 1
    return count


def invalid_data(passport):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    alphanumeric = "0123456789abcdef"
    digits = "0123456789"

    for k in passport:
        if k == "byr":
            if int(passport[k]) < 1920 or int(passport[k]) > 2002:
                return True
        elif k == "iyr":
            if int(passport[k]) < 2010 or int(passport[k]) > 2020:
                return True
        elif k == "eyr":
            if int(passport[k]) < 2020 or int(passport[k]) > 2030:
                return True
        elif k == "hgt":
            h = passport[k]
            h = h[:len(h)-2]
            if "cm" in passport[k]:
                if int(h) < 150 or int(h) > 193:
                    return True
            elif "in" in passport[k]:
                if int(h) < 59 or int(h) > 76:
                    return True
            else:
                return True
        elif k == "hcl":
            if passport[k][0] == "#":
                if len(passport[k][1::]) != 6:
                    return True
                else:
                    for c in passport[k][1::]:
                        if c not in alphanumeric:
                            return True
            else:
                return True
        elif k == "ecl":
            if passport[k] not in eye_colors:
                return True
        elif k == "pid":
            if len(passport[k]) != 9:
                return True
            for c in passport[k]:
                if c not in digits:
                    return True

    return False


def validate_strict_passports(passports, tags):
    count = 0
    for passport in passports:
        if contains_tags(passport, tags):
            if not invalid_data(passport):
                count += 1
    return count


if __name__ == "__main__":
    with open('input') as f:
        regex = re.compile("\n\n")
        passports = regex.split(f.read().strip())
        passports = [sub.replace("\n", " ") for sub in passports]
        
        l = []
        for passport in passports:
            dictlist = dict(item.split(":") for item in passport.split(" "))
            l.append(dictlist)

        tags = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        print("Part one:", validate_passports(l, tags))
        print("Part two:", validate_strict_passports(l, tags))
