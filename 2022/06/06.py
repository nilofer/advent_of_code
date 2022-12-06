import os
import sys

file1 = open(os.path.join(sys.path[0], "06_input.txt"), "r")
input_lines = file1.readlines()
buffer = input_lines[0]

## part 1

marker1 = 0

for x in range(len(buffer)-3):
    sub4 = (buffer[x:x+4])
    unique = len(set(sub4)) == len(sub4)
    if unique:
        marker1 = x + 4
        break
    
print(marker1)

## part 2

marker2 = 0

for x in range(len(buffer)-3):
    sub14 = (buffer[x:x+14])
    unique = len(set(sub14)) == len(sub14)
    if unique:
        marker2 = x + 14
        break
    
print(marker2)