from advent_of_code_utility import read_file_to_list

moves = [(-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
         (0, -1), (0, 1),  # Left,         Right
         (1, -1), (1, 0), (1, 1)]  # Bottom-left, Bottom, Bottom-right

# Idea: Regex
input_list = read_file_to_list("input.txt")
input_string = ""
xmas_counter = 0
for x in range(len(input_list)):
    for y in range(len(input_list[x])):
        if input_list[x][y] == "X":
            for move in moves:
                try:
                    if x + move[0] >= 0 and y + move[1] >= 0 and input_list[x + move[0]][y + move[1]] == "M":
                        if x + 2 * move[0] >= 0 and y + 2 * move[1] >= 0 and input_list[x + 2 * move[0]][
                            y + 2 * move[1]] == "A":
                            if x + 3 * move[0] >= 0 and y + 3 * move[1] >= 0 and input_list[x + 3 * move[0]][
                                y + 3 * move[1]] == "S":
                                xmas_counter += 1
                except IndexError:
                    continue

print(f"Part 1: {xmas_counter}")

x_mas_counter = 0
for x in range(len(input_list)):
    for y in range(len(input_list[x])):

        if input_list[x][y] == "A":
            try:
                cross_1 = False
                cross_2 = False
                if x > 0 and y > 0 and input_list[x + 1][y + 1] == "S" and input_list[x - 1][y - 1] == "M":
                    cross_1 = True
                if x > 0 and y > 0 and input_list[x + 1][y + 1] == "M" and input_list[x - 1][y - 1] == "S":
                    cross_1 = True
                if y > 0 and input_list[x + 1][y - 1] == "S" and input_list[x - 1][y + 1] == "M":
                    cross_2 = True
                if x > 0 and input_list[x + 1][y - 1] == "M" and input_list[x - 1][y + 1] == "S":
                    cross_2 = True
                if cross_1 and cross_2:
                    x_mas_counter += 1

            except IndexError:
                continue

print(f"Part 2: {x_mas_counter}")
