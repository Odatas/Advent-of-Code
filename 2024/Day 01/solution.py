import time
from advent_of_code_utility import read_file_to_list

# Start timing the entire script
start_time = time.perf_counter()

# Read the input file
input_list = read_file_to_list("input.txt")

# Start timing Part 1
part1_start_time = time.perf_counter()

# Create both columns
left_column = []
right_column = []

for item in input_list:
    left, right = item.split("  ")
    left_column.append(int(left))
    right_column.append(int(right))

# Sort both columns and calculate shortest distances
sorted_left_column = sorted(left_column)
sorted_right_column = sorted(right_column)
shortest_distances = []

for i in range(len(sorted_right_column)):
    shortest_distances.append(abs(sorted_left_column[i] - sorted_right_column[i]))

part1_result = sum(shortest_distances)
part1_end_time = time.perf_counter()

print(f"Part 1: {part1_result}")
print(f"Part 1 Execution Time: {part1_end_time - part1_start_time:.6f} seconds")

# Start timing Part 2
part2_start_time = time.perf_counter()

# Count right column values
right_counter_dict = {}

for i in sorted_right_column:
    value = right_counter_dict.get(i, 0)
    right_counter_dict[i] = value + 1

# Calculate similarity score
similarity_score = []

for i in sorted_left_column:
    similarity_score.append(i * right_counter_dict.get(i, 0))

part2_result = sum(similarity_score)
part2_end_time = time.perf_counter()

print(f"Part 2: {part2_result}")
print(f"Part 2 Execution Time: {part2_end_time - part2_start_time:.6f} seconds")

# End timing the entire script
end_time = time.perf_counter()

print(f"Total Execution Time: {end_time - start_time:.6f} seconds")
