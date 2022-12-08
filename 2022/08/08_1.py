import os
import sys

file1 = open(os.path.join(sys.path[0], "08_input.txt"), "r")
input_lines = file1.readlines()

## functions

def edge_visible(input_lines):
    horizontal_visible = (len(input_lines[0]) - 1) * 2
    vertical_visible = (len(input_lines) - 2) * 2
    edge_visbile = horizontal_visible + vertical_visible
    return edge_visbile

## check nsew

def check_north():
    tree_heights = []
    for y in range(tree_y-1, -1, -1):
        tree_heights.append(int((input_lines[y][tree_x])))
    return taller(tree_heights)

def check_south():
    tree_heights = []
    for y in range(tree_y+1, vertical_max, 1):
        tree_heights.append(int((input_lines[y][tree_x])))
    return taller(tree_heights)

def check_west():
    tree_heights = []
    for x in range(tree_x-1, -1, -1):
        tree_heights.append(int((input_lines[tree_y][x])))
    return taller(tree_heights)

def check_east():
    tree_heights = []
    for x in range(tree_x+1, horizontal_max+1, 1):
        tree_heights.append(int((input_lines[tree_y][x])))
    return taller(tree_heights)

def taller(tree_heights):
    if all((tree_height > tree) is True for tree in tree_heights):
        return 1
    else:
        return 0

## initialize vars

horizontal_max = len(input_lines[0]) - 2
vertical_max = len(input_lines)
interior_visible = 0

## loop through inner grid

for horizontal in range(1, horizontal_max, 1):
    for vertical in range(1, vertical_max-1, 1):
        tree_x = horizontal
        tree_y = vertical
        tree_height = int(input_lines[tree_y][tree_x])

        directions = []
        directions.append(check_north())
        directions.append(check_south())
        directions.append(check_east())
        directions.append(check_west())
        visible = sum(directions)

        if visible != 0:
            interior_visible += 1

## add in outer grid for total visible

edge_visible = edge_visible(input_lines)
print(interior_visible + edge_visible)
