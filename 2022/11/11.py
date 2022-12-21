import os
import sys
import re
import numpy

file1 = open(os.path.join(sys.path[0], "11_input.txt"), "r")
input_lines = file1.readlines()

monkey_items = []
monkey_operator = []
monkey_term = []
monkey_divisor = []
monkey_true = []
monkey_false = []
monkey_inspections = []

for x in range(len(input_lines)):
    if (x % 7) == 0:
        monkey = re.findall('[0-9]+', input_lines[x])
        monkey = int(monkey[0])
    elif (x % 7) == 1:
        starting_items = re.findall('[0-9]+', input_lines[x])
        starting_items = [int(i) for i in starting_items]
        monkey_items.append(starting_items)
        monkey_inspections.append(0)
    elif (x % 7) == 2:
        operation = re.split(" ", input_lines[x])
        operator = operation[6]
        monkey_operator.append(operator)
        term = operation[7]
        monkey_term.append(term)
    elif (x % 7) == 3:
        divisor = re.findall('[0-9]+', input_lines[x])
        divisor = int(divisor[0])
        monkey_divisor.append(divisor)
    elif (x % 7) == 4:
        true_monkey = re.findall('[0-9]+', input_lines[x])
        true_monkey = int(true_monkey[0])
        monkey_true.append(true_monkey)
    elif (x % 7) == 5:
        false_monkey = re.findall('[0-9]+', input_lines[x])
        false_monkey = int(false_monkey[0])
        monkey_false.append(false_monkey)
    else:
        continue

worry_manager = numpy.prod(monkey_divisor)

for round in range(10000):    
    for monkey in range(len(monkey_items)):
        for item in range(len(monkey_items[monkey])):
            worry_level = monkey_items[monkey][item]

            if monkey_term[monkey] == 'old\n':
                term = worry_level
            else:
                term = int(monkey_term[monkey])

            if monkey_operator[monkey] == '*':
                worry_level = worry_level * term
            else:
                worry_level = worry_level + term

            # Part 1 worry management
            #worry_level = worry_level // 3
            
            # Part 2 worry management to keep numbers small
            worry_level = worry_level % worry_manager

            if (worry_level % monkey_divisor[monkey]) == 0:
                monkey_items[monkey_true[monkey]].append(worry_level)
            else:
                monkey_items[monkey_false[monkey]].append(worry_level)
            
            monkey_inspections[monkey] = monkey_inspections[monkey] + 1
        
        monkey_items[monkey] = []    

sorted_inspections = sorted(monkey_inspections)
print(sorted_inspections[-1] * sorted_inspections[-2])