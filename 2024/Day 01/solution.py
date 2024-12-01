from advent_of_code_utility import read_file_to_list

# Create both columns
input_list = read_file_to_list("input.txt")

left_column = []
right_column = []

for item in input_list:
    left, right = item.split("  ")
    left_column.append(int(left))
    right_column.append(int(right))

# Idea: Just sort both columns and get the difference from the items on the same index.
sorted_left_column = sorted(left_column)
sorted_right_column = sorted(right_column)
shortes_distances = []

for i in range(len(sorted_right_column)):
    shortes_distances.append(abs(sorted_left_column[i]-sorted_right_column[i]))

print(f"Part 1: {sum(shortes_distances)}")

# Idea: Create a dict and count the right values. Then get the similarity score from all the values of the left column.
right_counter_dict = {}

for i in sorted_right_column:
    value = right_counter_dict.get(i, 0)
    right_counter_dict[i] = value+1

similarity_score = []

for i in sorted_left_column:
    similarity_score.append(i * right_counter_dict.get(i, 0))

print(f"Part 2: {sum(similarity_score)}")
