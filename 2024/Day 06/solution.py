import datetime

from advent_of_code_utility import read_file_to_list

def turn_90_degrees(current_direction):
    if current_direction == "North":
        return "East"
    if current_direction == "East":
        return "South"
    if current_direction == "South":
        return "West"
    if current_direction == "West":
        return "North"






def find_route(field, guard):
    index_x = guard[0]
    index_y = guard[1]
    direction = [['' for _ in range(len(field))] for _ in range(len(field[0]))]
    step_book = {}
    while True:
        try:
            field[index_y][index_x] = "X"
            direction[index_y][index_x] = guard[2]
            if guard[2] == "North":
                step = (0,-1)
            elif guard[2] == "East":
                step = (1,0)
            elif guard[2] == "South":
                step = (0,1)
            elif guard[2] == "West":
                step = (-1,0)
            else:
                print("Something wrong here")

            if field[index_y+step[1]][index_x+step[0]] == "X" or field[index_y+step[1]][index_x+step[0]] == ".":
                index_y = index_y + step[1]
                index_x = index_x + step[0]
                if index_x < 0 or index_y < 0:
                    #print("Left Map")
                    return field, False
                step_direction = [index_x,index_y,guard[2]]
                loop = step_book.get(str(step_direction), False)
                if loop:
                    return field, True
                else:
                    step_book[str(step_direction)] = True
            else:
                guard[2] = turn_90_degrees(guard[2])
            if direction[index_y][index_x] == guard[2]:
                #print("Loop detected")
                return field, True
        except IndexError:
            #print("Left Map")
            return field, False

start = datetime.datetime.now()
input_list = read_file_to_list("input.txt")

field = []
for row in input_list:
    field.append(list(row))

guard = ["","",""]
for index, row in enumerate(field):
    if "^" in row:
        guard_index_x = row.index("^")
        guard_index_y = index
        guard = [guard_index_x, guard_index_y, "North"]

# part 1: Bruteforce
field, loop = find_route(field,guard)

field_count = 0
possible_obstructions = []
for y_index, y in enumerate(field):
    for x_index, x in enumerate(y):
        if x == "X":
            possible_obstructions.append((x_index,y_index))
            field_count +=1

print(f"Part 1: {field_count}")

#Part 2 even more Brute Force. But be smart about it. Obstructions only need to be placed where the guard will walk.

loop_counter = 0
for obstruction in possible_obstructions:
    field = []
    for row in input_list:
        field.append(list(row))
    guard = ["", "", ""]
    for index, row in enumerate(field):
        if "^" in row:
            guard_index_x = row.index("^")
            guard_index_y = index
            guard = [guard_index_x, guard_index_y, "North"]

    field[obstruction[1]][obstruction[0]] = "#"
    field, loop = find_route(field, guard)
    if loop:
        #print("Loop found")
        loop_counter +=1
    #for y_index, y in enumerate(field):
    #    print(y)
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(f"Part 2: {loop_counter}")

runtime = datetime.datetime.now()-start
print(runtime)