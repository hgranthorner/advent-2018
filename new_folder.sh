#!/usr/bin/env bash

folder_path="./2018/$1_day"

mkdir $folder_path
touch "$folder_path/main.py"
touch "$folder_path/input.txt"
touch "$folder_path/sample.txt"

echo 'def part_one(input: line[str]): pass \n \
\n \
if __name__==\'__main__\':
    file_name = \'sample.txt\'
    input = \'\'
    try:
        with open(file_name) as f:
            input = f.readlines()
        part_one(input)
    except FileNotFoundError:
        print(f\'can not find file {file_name}\')' > "$folder_path/main.py"