import re

password_file = open('python/02/passwords.txt', 'r')
passwords = password_file.readlines()
password_file.close()

password_file = open('python/02/passwords.txt', 'r')
passwords_string = password_file.read()
password_file.close()
valid_password = 0

# Part 1
for j in range(len(passwords)):
    split_password = passwords[j].split(' ')
    split_char_count = split_password[0].split('-')
    char_min = int(split_char_count[0])
    char_max = int(split_char_count[1])
    char_required = split_password[1][0:1]
    current_password = split_password[2]
    char_count = 0
    for i in range(len(current_password)):
        if current_password[i] == char_required:
            char_count = char_count + 1
    if (char_count >= char_min) and (char_count <= char_max):
        valid_password = valid_password + 1

print(valid_password)

valid_password = 0
# Part 1 using regex
pass_regex = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')
match_pass = pass_regex.findall(passwords_string)

for j in range(len(match_pass)):
    char_min = int(match_pass[j][0])
    char_max = int(match_pass[j][1])
    char_required = match_pass[j][2]
    current_password = match_pass[j][3]
    char_count = 0
    for i in range(len(current_password)):
        if current_password[i] == char_required:
            char_count += 1
    if (char_count >= char_min) and (char_count <= char_max):
        valid_password += 1

print(valid_password)

# Part 2
valid_password = 0
for j in range(len(passwords)):
    split_password = passwords[j].split(' ')
    split_char_count = split_password[0].split('-')
    char_min = int(split_char_count[0])
    char_max = int(split_char_count[1])
    char_required = split_password[1][0:1]
    current_password = split_password[2]
    if (current_password[char_min-1] == char_required) or (current_password[char_max-1] == char_required):
        if (current_password[char_min-1] == char_required) != (current_password[char_max-1] == char_required):
            valid_password = valid_password + 1

print(valid_password)
