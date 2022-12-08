# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:15:46 2022

@author: pphilipiak
"""


def remove_last_folder(path: str) -> str:
    # Remove the trailing '/' character from the path if it exists
    if path.endswith("/"):
        path = path[:-1]

    # Split the path into its individual folders
    folders = path.split("/")

    # Remove the last folder from the list of folders
    folders = folders[:-1]

    # Join the folders back together to form the modified path
    modified_path = "/".join(folders)

    # Add the trailing '/' character back to the end of the path if it was removed earlier
    if not modified_path.endswith("/"):
        modified_path += "/"

    # Return the modified path
    return modified_path


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

puzzel_input = [x.strip() for x in puzzel_input]
current_path = "/"
path_dict = {"/": 0}
for i in puzzel_input:
    print("current path", current_path)
    if "$ cd /" in i:
        print("Back to Master Path")
        current_path = "/"
        continue

    if "$ ls" in i:
        print("Ignore list command")
        continue

    if i.split(" ")[0] == "dir":
        if not current_path + "/" + i.split(" ")[1] in path_dict:
            print(i, " is not in dict. Adding it.",
                  current_path + i.split(" ")[1] + "/")
            path_dict[current_path + i.split(" ")[1] + "/"] = 0
        continue

    if i.split(" ")[0].isdigit():
        print("adding number to current path", current_path)
        path_dict[current_path] += int(i.split(" ")[0])
        if current_path == "/":
            continue
        temp_folder = current_path
        while True:
            temp_folder = remove_last_folder(temp_folder)
            print(temp_folder)
            path_dict[temp_folder] += int(i.split(" ")[0])
            if temp_folder == "/":
                break

        continue

    if i.split(" ")[1] == "cd":
        if i.split(" ")[2] == "..":
            print("directory up")
            current_path = remove_last_folder(current_path)
        else:
            current_path = current_path + i.split(" ")[2] + "/"
            if not current_path in path_dict:
                print("add directory which you changed to", current_path)
                path_dict[current_path] = 0
        continue

sum_of_paths = 0
space_to_free = path_dict["/"] - 40000000

smallest_dict_to_delete = path_dict["/"]
for i in path_dict:
    if path_dict[i] > space_to_free:
        if path_dict[i] < smallest_dict_to_delete:
            smallest_dict_to_delete = path_dict[i]
    if path_dict[i] <= 100000:
        sum_of_paths += path_dict[i]


print("\n\nPart 1:", sum_of_paths)

print("Part 2:", smallest_dict_to_delete)
