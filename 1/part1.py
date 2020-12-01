#!/usr/bin/env python3

def main():
    with open('input') as f:
        expenses = f.readlines()
        expenses = [int(i) for i in expenses]
        
        for i in range(len(expenses)):
            for j in range(len(expenses)):
                if expenses[i]+expenses[j] == 2020 and j != i:
                    print(expenses[i]*expenses[j])
                    return

if __name__ == '__main__':
    main()
