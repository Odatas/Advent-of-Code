from advent_of_code_utility import read_file_to_list
import datetime



def creat_antinodes(field, with_resonant_harmonics = False):
    antenna_dict = {}
    for index_y, y in enumerate(field):
        for index_x, x in enumerate(y):
            if x != ".":
                value = antenna_dict.get(x,[])
                value.append((index_x,index_y))
                antenna_dict[x] = value
    for key, value in antenna_dict.items():
        for coordinates in value:
            for neighbors in value:
                if coordinates == neighbors:
                    continue
                difference = (coordinates[0] - neighbors[0], coordinates[1] - neighbors[1])
                if not with_resonant_harmonics:
                    antinode_coordinate = (coordinates[0] + difference[0], coordinates[1] + difference[1])
                    if antinode_coordinate[0] < 0 or antinode_coordinate[0] > len(field[0])-1 or antinode_coordinate[1] <  0 or antinode_coordinate[1] > len(field)-1:
                        continue
                    field[antinode_coordinate[1]][antinode_coordinate[0]] = "#"
                else:

                    multiplier = 1
                    while True:
                        antinode_coordinate = (coordinates[0] + difference[0]*multiplier, coordinates[1] + difference[1]*multiplier)
                        if antinode_coordinate[0] < 0 or antinode_coordinate[0] > len(field[0]) - 1 or \
                                antinode_coordinate[1] < 0 or antinode_coordinate[1] > len(field) - 1:
                            break
                        multiplier += 1
                    multiplier = -1
                    while True:
                        antinode_coordinate = (
                        coordinates[0] + difference[0] * multiplier, coordinates[1] + difference[1] * multiplier)
                        if antinode_coordinate[0] < 0 or antinode_coordinate[0] > len(field[0]) - 1 or \
                                antinode_coordinate[1] < 0 or antinode_coordinate[1] > len(field) - 1:
                            break
                        field[antinode_coordinate[1]][antinode_coordinate[0]] = "#"
                        multiplier -= 1


start = datetime.datetime.now()
input_list = read_file_to_list("input.txt")

city = []
for row in input_list:
    city.append(list(row))

creat_antinodes(city)

antinode_count = 0
for y in city:
    antinode_count = antinode_count + y.count("#")

print(f"Part 1: {antinode_count}")

city = []
for row in input_list:
    city.append(list(row))

creat_antinodes(city, True)

antinode_count = 0
for y in city:
    antinode_count = antinode_count + y.count("#")

print(f"Part 2: {antinode_count}")

runtime = datetime.datetime.now() - start
print(f"Runtime: {runtime}")