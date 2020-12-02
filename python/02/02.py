password_file = open('python/02/passwords.txt', 'r')
passwords = password_file.readlines()
valid_password = 0

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