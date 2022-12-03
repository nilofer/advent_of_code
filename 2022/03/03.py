import os
import sys

file1 = open(os.path.join(sys.path[0], "03_input.txt"), "r")
input_lines = [ line.strip() for line in file1 ]
priority = []

## part 1

for line in input_lines:
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]

    ascii_comp1 = []
    ascii_comp2 = []

    for letter in comp1:
        ascii_comp1.extend(ord(num) for num in letter)
    
    for letter in comp2:
        ascii_comp2.extend(ord(num) for num in letter)

    common_item = set(ascii_comp1).intersection(ascii_comp2).pop()

    if common_item > 96:
        common_item = common_item - 96
    else:
        common_item = common_item - 38
    
    priority.append(common_item)

print(sum(priority))

## part 2

priority = []

def intersection(*rucksacks):
    common_item = set(rucksacks[0]).intersection(*rucksacks[1:]).pop()
    common_item = ord(common_item)

    if common_item > 96:
        common_item = common_item - 96
    else:
        common_item = common_item - 38

    return common_item

for line in range(len(input_lines)//3):
    group = input_lines[line*3:(line*3)+3]
    priority.append(intersection(group[0], group[1], group[2]))

print(sum(priority))