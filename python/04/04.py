passport_file = open('python/04/passports.txt','r')
passport_contents = passport_file.readlines()

print(len(passport_contents))
#print(passport_contents)
i = 0
valid_passport = 0
while i <= (len(passport_contents)-1):
    current_passport = ''
    while (i <= (len(passport_contents)-1)) and (passport_contents[i] != '\n'):
        current_passport = current_passport + ' ' + passport_contents[i]
        i += 1
    current_passport = current_passport.split()
    print(current_passport)
    if i <= (len(passport_contents)-1):
        i += 1
    if len(current_passport) > 6:
        if len(current_passport) == 7:
            if any("cid" not in s for s in current_passport):
                print('check')
                valid_passport += 1
        elif len(current_passport) == 8:
            valid_passport += 1
    print(valid_passport)
