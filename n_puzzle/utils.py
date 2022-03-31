import re


def get_numbers_and_size(puzzle):
    reg_comment = "( ?\d* ?)?(\#.*)?"
    numbers = []
    size = 0
    for i in puzzle:
        m = re.findall(reg_comment, i)
        for j in m:
            num = j[0].strip()
            if num.isdigit():
                if not numbers and size == 0:
                    size = int(num)
                else:
                    numbers.append(num)
    return numbers, size


def get_duplicate(data, logger):
    tmp_list = []
    for i in data:
        if i not in tmp_list:
            tmp_list.append(i)
        else:
            logger.error(f"Duplicate data with {i}. Format not good in puzzle. Exiting program.")
    if '0' not in data:
        logger.error("No space in puzzle. Need at least a 0 in those data. Exiting program.")


def get_sequence(data, logger):
    tmp_list = [int(x) for x in data]
    tmp_list.sort()
    for i in range(len(tmp_list)):
        if i + 1 < len(tmp_list) and tmp_list[i] == tmp_list[i + 1] - 1:
            continue
        elif not i + 1 < len(tmp_list):
            break
        else:
            logger.error(f"{tmp_list[i + 1]} is not following the order of the data. The file must be getting numbers "
                         f"following each other. Exiting program.")


def get_good_format(puzzle, logger):
    tmp_list = []
    size = 0
    reg_comment = "( ?\d* ?)?(\#.*)?"
    for i in puzzle:
        if not size and i[0].isdigit():
            size = int(i[0].strip())
        else:
            tmp_list.append(re.findall(reg_comment, i))
    counter = []
    for i in tmp_list:
        count = 0
        for j in i:
            tmp = j[0].strip()
            if tmp.isdigit():
                count += 1
        counter.append(count)
    for i in counter:
        if i != 0 and i != size and i != 1:
            logger.error(f"The format is not supposed to differ between lines. Now exiting the program.")


def parse_data(puzzle, logger):
    numbers, size = get_numbers_and_size(puzzle)
    if len(numbers) % int(size) != 0:
        logger.error(f"The puzzle is not on a good format. There is to many data compared with size ({size})."
                     f" Exiting program.")
    get_duplicate(numbers, logger)
    get_sequence(numbers, logger)
    get_good_format(puzzle, logger)


def open_file(file):
    f = open(file, "r")
    puzzle = f.readlines()
    f.close()
    return puzzle
