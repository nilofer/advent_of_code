import os
import sys

file1 = open(os.path.join(sys.path[0], "04_input.txt"), "r")
input_lines = [ line.strip() for line in file1 ]

# Part 1

def parse_line(line):
    section_list = line.replace('-', ',').split(',')
    return(section_list)

contain_count = 0

for line in input_lines:
    parsed_sections = parse_line(line)
    parsed_sections = [eval(i) for i in parsed_sections]
    if parsed_sections[0] >= parsed_sections[2] and parsed_sections[1] <= parsed_sections[3]:
        contain_count += 1
    elif parsed_sections[2] >= parsed_sections[0] and parsed_sections[3] <= parsed_sections[1]:
        contain_count += 1

print(contain_count)

# Part 2

def section_list(first, last):
    elf_section = []
    for number in range(first,last+1,1):
        elf_section.append(number)
    return elf_section

overlap_count = 0

for line in input_lines:
    parsed_sections = parse_line(line)
    parsed_sections = [eval(i) for i in parsed_sections]

    elf1 = section_list(parsed_sections[0], parsed_sections[1])
    elf2 = section_list(parsed_sections[2], parsed_sections[3])

    if set(elf1).intersection(elf2):
        overlap_count += 1

print(overlap_count)
