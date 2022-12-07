import os
import sys

file1 = open(os.path.join(sys.path[0], "07_input.txt"), "r")
input_lines = file1.readlines()

# part 1

cwd = filesystem = {}
dir_level = []

for x in range(len(input_lines)):
    line = input_lines[x].split()
    if line[0] == '$':
        if line[1] == 'cd':
            dir = line[2]
            if dir == '..':
                cwd = dir_level.pop()
            elif dir == '/':
                cwd = filesystem
                dir_level = []
            else:
                print(dir)
                if dir not in cwd:
                    cwd[dir] = {}
                dir_level.append(cwd)
                print(dir_level)
                cwd = cwd[dir]
    else:
        if line[0] != 'dir':
            cwd[line[1]] = int(line[0])

#print(filesystem)

def get_sizes(d):
    if isinstance(d, int):
        return (d, 0)
    size = 0
    total = 0
    for child in d.values():
        return_size, return_total = get_sizes(child)
        size += return_size
        total += return_total
    if size <= 100000:
        total += size
    return(size, total)

print(get_sizes(filesystem)[1])

# part 2

def total_size(d):
    if isinstance(d, int):
        return (d)
    return sum(map(total_size, d.values()))

extra = total_size(filesystem) - 40000000

def delete_size(d):
    smallest = float("inf")
    full_size = total_size(d)
    if full_size >= extra:
        smallest = full_size
    for child in d.values():
        if isinstance(child, int):
            continue
        current_size = delete_size(child)
        smallest = min(smallest, current_size)
    return smallest

print(delete_size(filesystem))