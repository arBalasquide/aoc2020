#!/usr/bin/env python3

"""
    Run time complexity O(N). I give my code an OK pass. 
    Probably could be improved, though.
"""


def tree_finder(forest, right, down):
    row, col = 0,0
    trees = 0

    col_len = len(forest[0])
    
    while row < len(forest):
        if col >= col_len:
            col -= col_len

        if forest[row][col] == '#':
            trees += 1
        
        col += right
        row += down

    return trees


if __name__ == "__main__":
    with open('input') as f:
        arr = [list(line.strip()) for line in f]

        print("Part one:", tree_finder(arr,3,1))
        print("Part two:", tree_finder(arr,1,1)*tree_finder(arr,3,1)
                *tree_finder(arr,5,1)*tree_finder(arr,7,1)
                *tree_finder(arr,1,2))
