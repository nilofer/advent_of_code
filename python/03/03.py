map_file = open('python/03/map.txt', 'r')
map_list = map_file.readlines()

x = 0
y = 0
slope1_tree_total = 0

while (x<len(map_list)):
    if y>=(len(map_list[x])-1):
        y = y % (len(map_list[x])-1)
    current_mark = map_list[x][y]
    if current_mark == '#':
        slope1_tree_total = slope1_tree_total + 1
    y = y + 1
    x = x + 1


x = 0
y = 0
slope2_tree_total = 0

while (x<len(map_list)):
    if y>=(len(map_list[x])-1):
        y = y % (len(map_list[x])-1)
    current_mark = map_list[x][y]
    if current_mark == '#':
        slope2_tree_total = slope2_tree_total + 1
    y = y + 3
    x = x + 1


x = 0
y = 0
slope3_tree_total = 0

while (x<len(map_list)):
    if y>=(len(map_list[x])-1):
        y = y % (len(map_list[x])-1)
    current_mark = map_list[x][y]
    if current_mark == '#':
        slope3_tree_total = slope3_tree_total + 1
    y = y + 5
    x = x + 1

x = 0
y = 0
slope4_tree_total = 0

while (x<len(map_list)):
    if y>=(len(map_list[x])-1):
        y = y % (len(map_list[x])-1)
    current_mark = map_list[x][y]
    if current_mark == '#':
        slope4_tree_total = slope4_tree_total + 1
    y = y + 7
    x = x + 1

x = 0
y = 0
slope5_tree_total = 0

while (x<len(map_list)):
    if y>=(len(map_list[x])-1):
        y = y % (len(map_list[x])-1)
    current_mark = map_list[x][y]
    if current_mark == '#':
        slope5_tree_total = slope5_tree_total + 1
    y = y + 1
    x = x + 2

print(slope1_tree_total)
print(slope2_tree_total)
print(slope3_tree_total)
print(slope4_tree_total)
print(slope5_tree_total)

mult_trees = slope1_tree_total * slope2_tree_total * slope3_tree_total * slope4_tree_total * slope5_tree_total

print(mult_trees)