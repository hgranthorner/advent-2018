
def annihilate(x: str, y: str):
    # Same chem, same polarity?
    if x == y:
        return False

    # different chems?
    if x.upper() != y.upper():
        return False

    return True


def part_one(input: str):
    chems = list(input)
    reaction_occurred = True

    while reaction_occurred:
        reaction_occurred = False
        if len(chems) == 0:
            return ''

        # treat as stack: push smallest, then largest
        set_to_remove = set()
        for i, c in enumerate(chems):
            if i == 0:
                continue
            if annihilate(chems[i - 1], c):
                reaction_occurred = True
                if i not in set_to_remove and i - 1 not in set_to_remove:
                    set_to_remove.add(i - 1)
                    set_to_remove.add(i)

        indices_to_remove = list(set_to_remove)
        indices_to_remove.sort(reverse=True)
        for i in indices_to_remove:
            del chems[i]

        pass

    return ''.join(chems)


if __name__ == '__main__':
    file_name = 'input.txt'
    try:
        with open(file_name) as f:
            data = f.readline()
            # result = part_one(data)
            # print(len(result))
            char_set = set(data.lower())

            lst: list[int] = []
            for c in char_set:
                print(c)
                input = data.replace(c, '').replace(c.upper(), '')
                lst.append(len(part_one(input)))
            print(min(lst))
    except FileNotFoundError:
        print(f'cannot find file {file_name}')
