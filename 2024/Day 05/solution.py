from advent_of_code_utility import read_file_to_list


input_list = read_file_to_list("input.txt")


split_index = input_list.index("")

page_ordering_rules = input_list[:split_index]
page_numbers = input_list[split_index + 1:]



# Idea: Creat a dict per number if the other numbers should be before or after itself. Then check against it.
rule_dict = {}
for rule in page_ordering_rules:
    before, after = rule.split("|")
    before_dict = rule_dict.get(before,[[],[]])
    before_dict[1].append(after)
    rule_dict[before] = before_dict

    after_dict = rule_dict.get(after, [[], []])
    after_dict[0].append(before)
    rule_dict[after] = after_dict

middle_numbers = []
middle_numbers_failures = []

for page in page_numbers:
    failure = False
    numbers = page.split(",")
    for index, number in enumerate(numbers):
        rule = rule_dict[number]
        before = numbers[:index]
        after = numbers[index+1:]

        if failure:
            break

        for item in before:
            if item in rule[1]:
                failure = True
        for item in after:
            if item in rule[0]:
                failure = True

    if failure:
        ordered = []
        ordered.append(numbers[0])
        for item in numbers[1:]:
            added = False
            rule = rule_dict[item]
            for index, ordered_number in enumerate(ordered):
                if ordered_number in rule[1]:
                    ordered.insert(index, item)
                    added = True
                    break
            if not added:
                ordered.append(item)
        middle_index = len(ordered) // 2
        middle_numbers_failures.append(ordered[middle_index])


    else:
        middle_index = len(numbers) // 2
        middle_numbers.append(numbers[middle_index])

print(f"Part 1: {sum([int(x) for x in middle_numbers])}")

print(f"Part 2: {sum([int(x) for x in middle_numbers_failures])}")



