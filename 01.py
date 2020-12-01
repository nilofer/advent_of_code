expense_file = open('expense_report.txt','r')
expense_content = expense_file.read()
expense_list = expense_content.split('\n')
expense_file.close()

for i in range(len(expense_list)):
    n1 = int(expense_list[i])
    for j in range(len(expense_list)):
        n2 = int(expense_list[j])
        if (n1+n2) == 2020:
            answer2 = n1 * n2

print(answer2)

for i in range(len(expense_list)):
    n1 = int(expense_list[i])
    for j in range(len(expense_list)):
        n2 = int(expense_list[j])
        for k in range(len(expense_list)):
            n3 = int(expense_list[k])
            if (n1+n2+n3) == 2020:
                answer3 = n1 * n2 * n3

print(answer3)