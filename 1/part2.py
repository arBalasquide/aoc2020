#!/usr/bin/env python3

def main():
    with open('input') as f:
        expenses = f.readlines()
        expenses = [int(i) for i in expenses]

        for i in range(len(expenses)-1):
            s = set()
            curr = 2020 - expenses[i]
            for j in range(i+1, len(expenses)):
                if (curr - expenses[j]) in s:
                    print(expenses[i]*expenses[j]*(curr - expenses[j]))
                    return
                s.add(expenses[j])

if __name__ == "__main__":
    main()
