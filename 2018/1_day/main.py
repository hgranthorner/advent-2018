def part_one():
    with open('input.txt') as f:
        lines = f.readlines()
        print(sum(map(lambda x: int(x), lines)))


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()
        nums = set()
        acc = 0

        while acc not in nums:
            for line in lines:

                nums.add(acc)

                val = int(line)
                acc += val

                if acc in nums:
                    print('found!')
                    return acc


if __name__ == '__main__':
    print(part_two())
