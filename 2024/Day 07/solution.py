import datetime
from advent_of_code_utility import read_file_to_list
import itertools


def check_calculation(task, with_concatenation = False):
    solution = task[0]
    numbers = task[1]
    solutions = [numbers[0]]
    for number in numbers[1:]:
        new_solutions = []
        for result in solutions:
            new_result_plus = result + number
            if new_result_plus == solution:
                return True
            elif new_result_plus > solution:
                continue
            elif new_result_plus < solution:
                new_solutions.append(new_result_plus)
            new_result_multiplication = result * number
            if new_result_multiplication == solution:
                return True
            elif new_result_multiplication > solution:
                continue
            elif new_result_multiplication < solution:
                new_solutions.append(new_result_multiplication)
            new_result_concatenation= int(str(result) + str(number))
            if with_concatenation:
                if new_result_concatenation == solution:
                    return True
                elif new_result_concatenation > solution:
                    continue
                elif new_result_concatenation < solution:
                    new_solutions.append(new_result_concatenation)
        solutions = new_solutions
    return False







start = datetime.datetime.now()
input_list = read_file_to_list("input.txt")
true_test_values = []

calculations = []
for row in input_list:
    solution = int(row.split(":")[0])
    numbers = row.split(" ")[1:]
    numbers = [int(x) for x in numbers]
    calculations.append((solution,numbers))


for calculation in calculations:
    if check_calculation(calculation):
        true_test_values.append(calculation[0])
    else:
        continue

print(f"Part 1: {sum(true_test_values)}")

true_test_values = []
for calculation in calculations:
    if check_calculation(calculation, True):
        true_test_values.append(calculation[0])
    else:
        continue

print(f"Part 2: {sum(true_test_values)}")

runtime = datetime.datetime.now() - start
print(f"Runtime: {runtime}")

