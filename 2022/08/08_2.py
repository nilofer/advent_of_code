import os
import sys

file1 = open(os.path.join(sys.path[0], "08_input.txt"), "r")
input_lines = file1.readlines()

## functions

def check_north():
    tree_heights = []
    for y in range(tree_y-1, -1, -1):
        tree_heights.append(int((input_lines[y][tree_x])))
    return distance(tree_heights)

def check_south():
    tree_heights = []
    for y in range(tree_y+1, vertical_max, 1):
        tree_heights.append(int((input_lines[y][tree_x])))
    return distance(tree_heights)

def check_west():
    tree_heights = []
    for x in range(tree_x-1, -1, -1):
        tree_heights.append(int((input_lines[tree_y][x])))
    return distance(tree_heights)

def check_east():
    tree_heights = []
    for x in range(tree_x+1, horizontal_max+1, 1):
        tree_heights.append(int((input_lines[tree_y][x])))
    return distance(tree_heights)

def distance(tree_heights):
    distance = 0
    for tree in tree_heights:
        if tree < tree_height:
            distance += 1
        else:
            distance += 1
            return distance
    return distance


## initialize vars

horizontal_max = len(input_lines[0]) - 2
vertical_max = len(input_lines)
interior_visible = 0
max_scenic_score = 0

## loop through inner grid

for horizontal in range(1, horizontal_max, 1):
    for vertical in range(1, vertical_max-1, 1):
        tree_x = horizontal
        tree_y = vertical
        tree_height = int(input_lines[tree_y][tree_x])

        scenic_score = check_north() * check_west() * check_east() * check_south()

        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)
