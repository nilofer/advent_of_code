file1 = open('01_input.txt', 'r')
input_lines = file1.readlines()

cals_list = [0]
elf_cals = 0

for line in input_lines:
    if line != '\n':
        elf_cals = elf_cals + int(line)
    else:
        for i in range(len(cals_list)):
            if elf_cals > cals_list[i]:
                cals_list.insert(i, elf_cals)
                break
        elf_cals = 0

for i in range(len(cals_list)):
            if elf_cals > cals_list[i]:
                cals_list.insert(i, elf_cals)
                break

print(sum(cals_list[0:3]))