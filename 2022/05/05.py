import os
import sys
import re
import copy

file1 = open(os.path.join(sys.path[0], "05_input.txt"), "r")
input_lines = file1.readlines()

## part 1

stack_list = []

for line in range(len(input_lines)):
    if input_lines[line] == '\n':
        break
    stack_list.append(list(input_lines[line][k * 4 + 1] for k in range(len(input_lines[line]) // 4)))

stack_list.pop()
stack_list = [list("".join(crate).strip()[::-1]) for crate in zip(*stack_list)]
stack_list_2 = copy.deepcopy(stack_list)


def crate_move_9000(from_stack, to_stack):
    moved_crate = stack_list[from_stack - 1].pop()
    stack_list[to_stack - 1].append(moved_crate)
    return stack_list

for line in range(len(input_lines)):
    if input_lines[line][0] == 'm':
        count, from_stack, to_stack = map(int, re.findall('[0-9]+', input_lines[line]))
        for i in range(count):
            crate_move_9000(from_stack, to_stack)

top_crates = [(stack.pop()) for stack in stack_list]
top_crates = "".join(top_crates)
print(top_crates)

## part 2
def crate_move_9001(crate_count, from_stack, to_stack):
    moved_crates = stack_list_2[from_stack-1][-1 * crate_count:]
    stack_list_2[from_stack-1] = stack_list_2[from_stack - 1][:-1 * crate_count]
    stack_list_2[to_stack - 1].extend(moved_crates)
    return stack_list_2

for line in range(len(input_lines)):
    if input_lines[line][0] == 'm':
        count, from_stack, to_stack = map(int, re.findall('[0-9]+', input_lines[line]))
        crate_move_9001(count, from_stack, to_stack)

top_crates = [(stack.pop()) for stack in stack_list_2]
top_crates = "".join(top_crates)
print(top_crates)