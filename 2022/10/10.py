import os
import sys

file1 = open(os.path.join(sys.path[0], "10_input.txt"), "r")
input_lines = file1.readlines()

X_register = 1
cycle = 0
all_signal_strengths = []

CRT_output = []

def cycle_check():
    if ((cycle - 20) % 40) == 0:
        signal_strength = X_register * cycle
        return signal_strength

def sprite_CRT_overlap():
    CRT_position = cycle % 40
    sprite_mid = X_register + 1
    if (sprite_mid == CRT_position) or ((sprite_mid - 1) == CRT_position) or ((sprite_mid + 1) == CRT_position):
        CRT_output.append('#')
    else:
        CRT_output.append('.')

for line in input_lines:
    instruction = line.split()
    if instruction[0] == 'noop':
        cycle += 1
        all_signal_strengths.append(cycle_check())
        sprite_CRT_overlap()
    else:
        cycle += 1
        all_signal_strengths.append(cycle_check())
        sprite_CRT_overlap()
        cycle += 1
        all_signal_strengths.append(cycle_check())
        sprite_CRT_overlap()
        X_register += int(instruction[1])
        
## part 1
filter_signal_strengths = [i for i in all_signal_strengths if i is not None]
print(sum(filter_signal_strengths))

## part 2
CRT_row = ''
for pos in range(len(CRT_output)):
    CRT_row += CRT_output[pos]
    if ((pos - 39) % 40) == 0:
        print(CRT_row)
        CRT_row = ''