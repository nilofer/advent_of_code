answer_file = open('python/06/answers.txt','r')
answer_contents = answer_file.readlines()

# print(answer_contents)
questions = []
question_sum = 0

for i in range(len(answer_contents)):
    if answer_contents[i] != '\n':
        for j in range(len(answer_contents[i])):
            if answer_contents[i][j] not in questions and answer_contents[i][j] != '\n':
                questions.append(answer_contents[i][j])
    else:
        question_sum = question_sum + len(questions)
        questions = []

print(question_sum)

questions = []
question_count = []
person_count = 0
all_yes = 0

for i in range(len(answer_contents)):
    if answer_contents[i] != '\n':
        for j in range(len(answer_contents[i])):
            if answer_contents[i][j] != '\n':
                if answer_contents[i][j] not in questions:
                    questions.append(answer_contents[i][j])
                    question_count.append(0)
                curr_index = questions.index(answer_contents[i][j])
                question_count[curr_index] = question_count[curr_index] + 1
        person_count += 1
    else:
        for k in range(len(question_count)):
            if question_count[k] == person_count:
                all_yes += 1
        questions = []
        question_count = []
        person_count = 0

print(all_yes)