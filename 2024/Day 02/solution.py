from advent_of_code_utility import read_file_to_list


# Read the input file
input_list = read_file_to_list("input.txt")



safe_counter = 0
part2_safe_counter = 0

#Idea is to brute force, create all differences and check them.

def check_safe(list_difference):
    if list_difference[0] > 0:
        positive = True
    else:
        positive = False
    for j in list_difference:
        if abs(j) > 3 or abs(j) < 1:
            return False
        if positive:
            if j < 0:
                return False
        else:
            if j > 0:
                return False
    return True

def calculate_differences(level):
    differences = []

    for j in range(len(level) - 1):
        differences.append(level[j + 1] - level[j])
    return differences

for i in input_list:
    level = i.split(" ")
    level = [int(x) for x in level]
    if check_safe(calculate_differences(level)):
        safe_counter += 1
        part2_safe_counter +=1
        continue

# Part 2 even more brute force. Just calculate all possible levels.
    for j in range(len(level)):
        level_temp = level.copy()
        level_temp.pop(j)
        differences_temp = calculate_differences(level_temp)
        if check_safe(differences_temp):
            part2_safe_counter +=1
            break

print(f"Part 1: {safe_counter}")
print(f"Part 2: {part2_safe_counter}")




