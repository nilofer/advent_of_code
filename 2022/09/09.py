import os
import sys

file1 = open(os.path.join(sys.path[0], "09_input.txt"), "r")
input_lines = file1.readlines()

## part 1

## initialize
H_loc = [0,0]
T_loc = [0,0]

all_T_locs = []
all_T_locs.append(T_loc.copy())

for line in input_lines:
    move = line.replace('\n', '').split(' ')
    direction = move[0]
    steps = int(move[1])

    ## move head
    for i in range(steps):
        if direction == 'R':
            H_loc[0] = H_loc[0] + 1
        elif direction == 'L':
            H_loc[0] = H_loc[0] - 1
        elif direction == 'U':
            H_loc[1] = H_loc[1] + 1
        else:
            H_loc[1] = H_loc[1] - 1

        # get difference between head and tail
        diff_x = H_loc[0] - T_loc[0]
        diff_y = H_loc[1] - T_loc[1]

        # determine tail movement
        if abs(diff_x) > 1 or abs(diff_y) > 1:
            if diff_x == 0:
                if diff_y > 0:
                    T_loc[1] = T_loc[1] + 1
                else:
                    T_loc[1] = T_loc[1] - 1
            elif diff_y == 0:
                if diff_x > 0:
                    T_loc[0] = T_loc[0] + 1
                else:
                    T_loc[0] = T_loc[0] - 1
            else:
                if diff_y > 0:
                    T_loc[1] = T_loc[1] + 1
                else:
                    T_loc[1] = T_loc[1] - 1
                if diff_x > 0:
                    T_loc[0] = T_loc[0] + 1
                else:
                    T_loc[0] = T_loc[0] - 1
        
        # track tail positions
        all_T_locs.append(T_loc.copy())

## determine unique positions
count_T_locs = {}

for position in all_T_locs:
    count_T_locs.setdefault(tuple(position), list()).append(1)
for a, b in count_T_locs.items():
    count_T_locs[a] = sum(b)

print(len(count_T_locs))


## part 2

## initialize
knots = []

for k in range(10):
    knots.append([0,0])

all_T_locs = []
all_T_locs.append(knots[9].copy())

for line in input_lines:
    move = line.replace('\n', '').split(' ')
    direction = move[0]
    steps = int(move[1])

    ## move head
    for i in range(steps):
        H_loc = knots[0]
        if direction == 'R':
            H_loc[0] = H_loc[0] + 1
        elif direction == 'L':
            H_loc[0] = H_loc[0] - 1
        elif direction == 'U':
            H_loc[1] = H_loc[1] + 1
        else:
            H_loc[1] = H_loc[1] - 1

        for k in range(9):
            H_loc = knots[k]
            T_loc = knots[k + 1]
            # get difference between head and tail
            diff_x = H_loc[0] - T_loc[0]
            diff_y = H_loc[1] - T_loc[1]

            # determine tail movement
            if abs(diff_x) > 1 or abs(diff_y) > 1:
                if diff_x == 0:
                    if diff_y > 0:
                        T_loc[1] = T_loc[1] + 1
                    else:
                        T_loc[1] = T_loc[1] - 1
                elif diff_y == 0:
                    if diff_x > 0:
                        T_loc[0] = T_loc[0] + 1
                    else:
                        T_loc[0] = T_loc[0] - 1
                else:
                    if diff_y > 0:
                        T_loc[1] = T_loc[1] + 1
                    else:
                        T_loc[1] = T_loc[1] - 1
                    if diff_x > 0:
                        T_loc[0] = T_loc[0] + 1
                    else:
                        T_loc[0] = T_loc[0] - 1
        
        # track tail positions
        all_T_locs.append(T_loc.copy())

## determine unique positions
count_T_locs = {}

for position in all_T_locs:
    count_T_locs.setdefault(tuple(position), list()).append(1)
for a, b in count_T_locs.items():
    count_T_locs[a] = sum(b)

print(len(count_T_locs))