import re
from advent_of_code_utility import read_file_to_list

# Idea: Regex
input_list = read_file_to_list("input.txt")
input_string = ""
for line in input_list:
    input_string += line

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, input_string)

multiplication = []

for match in matches:
    multiplication.append(int(match[0])*int(match[1]))

print(f"Part 1: {sum(multiplication)}")

# Idea: more regex
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = list(re.finditer(pattern, input_string))

part2_multiplication = []
status = True
for match in matches:
    if match.group() == "do()":
        status = True
    elif match.group() == "don't()":
        status = False
    elif status is True:
        # String like this: mul(313,218)
        a = match.group().split("(")[1].split(",")[0]
        b = match.group().split(",")[1].split(")")[0]
        part2_multiplication.append(int(a)*int(b))

print(f"Part 2: {sum(part2_multiplication)}")

