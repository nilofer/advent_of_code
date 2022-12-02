import os
import sys

file1 = open(os.path.join(sys.path[0], "02_input.txt"), "r")
input_lines = file1.readlines()

your_play = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

opp_play = {
  "A": 1,
  "B": 2,
  "C": 3
}

shape_score = 0
outcome_score = 0

## part 1
for line in range(len(input_lines)):
    opp_shape = opp_play.get(input_lines[line][0])
    your_shape = your_play.get(input_lines[line][2])

    shape_score = shape_score + your_shape

    if opp_shape == your_shape:
        outcome_score = outcome_score + 3
    elif opp_shape == 3:
        if your_shape == 2:
            outcome_score = outcome_score + 0
        else:
            outcome_score = outcome_score + 6
    elif opp_shape == 2:
        if your_shape == 1:
            outcome_score = outcome_score + 0
        else:
            outcome_score = outcome_score + 6
    else:
        if your_shape == 3:
            outcome_score = outcome_score + 0
        else:
            outcome_score = outcome_score + 6

total_score = shape_score + outcome_score
print(total_score)

## part 2

game_outcome = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

shape_score = 0
outcome_score = 0

for line in range(len(input_lines)):
    opp_shape = opp_play.get(input_lines[line][0])
    your_outcome = game_outcome.get(input_lines[line][2])

    outcome_score = outcome_score + your_outcome

    if your_outcome == 3:
        shape_score = shape_score + opp_shape
    elif your_outcome == 6:
        if opp_shape == 3:
            shape_score = shape_score + 1
        elif opp_shape == 2:
            shape_score = shape_score + 3
        else:
            shape_score = shape_score + 2
    else:
        if opp_shape == 3:
            shape_score = shape_score + 2
        elif opp_shape == 2:
            shape_score = shape_score + 1
        else:
            shape_score = shape_score + 3

total_score = shape_score + outcome_score
print(total_score)