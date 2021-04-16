

def part_one(input: list[str]): pass


if __name__ == '__main__':
    file_name = 'sample.txt'
    input = ''
    try:
        with open(file_name) as f:
            input = f.readlines()
        part_one(input)
    except FileNotFoundError:
        print(f'can not find file {file_name}')
