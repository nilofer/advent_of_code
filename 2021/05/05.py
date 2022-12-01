import math

seat_file = open('python/05/seats.txt','r')
seat_contents = seat_file.readlines()

seat_ids = []

for i in range(len(seat_contents)):
    seat_row = [0.0,127.0]
    seat_column = [0.0,7.0]
    for x in range(len(seat_contents[i])):
        if seat_contents[i][x] == 'F':
            seat_row[1] = math.floor(sum(seat_row)/len(seat_row))
        elif seat_contents[i][x] == 'B':
            seat_row[0] = math.ceil(sum(seat_row)/len(seat_row))
        elif seat_contents[i][x] == 'L':
            seat_column[1] = math.floor(sum(seat_column)/len(seat_column))
        elif seat_contents[i][x] == 'R':
            seat_column[0] = math.ceil(sum(seat_column)/len(seat_column))

    seat_ids.append((seat_row[0]*8) + seat_column[0])

print(max(seat_ids))

seat_ids.sort()
my_seat = seat_ids[0]

for i in seat_ids:
    if i != my_seat:
        print (my_seat)
        break
    my_seat += 1