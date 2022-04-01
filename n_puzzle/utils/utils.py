import re
import numpy as np

from colorama import Fore, Style


def get_array(puzzle, size):
    array = np.zeros((size, size))
    tmp = []
    counter = 0
    for index, x in enumerate(puzzle):
        tmp.append(x)
        if len(tmp) == size:
            array[counter] = tmp
            counter += 1
            tmp = []
    array = array.astype(int)
    return array


def is_valid(sol, x, y, sx, sy, size):
    if x == size or y == size or sol[y][x] != 0:
        if sx == 1 and sy == 0:
            return 0, 1
        elif sx == 0 and sy == 1:
            return -1, 0
        elif sx == -1 and sy == 0:
            return 0, -1
        else:
            return 1, 0
    return sx, sy


def solution_puzzle(size):
    solution = np.zeros((size, size))
    i = 1
    x, y = [0, 0]
    sx, sy = [1, 0]
    while i != size * size:
        sx, sy = is_valid(solution, x + sx, y + sy, sx, sy, size)
        solution[y][x] = i
        i += 1
        x += sx
        y += sy
    return solution.astype(int)


def is_solvable(puzzle, size, logger):
    solution = solution_puzzle(size)
    print("solution :\n", solution, "\n")


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
                    numbers.append(int(num))
    return numbers, size


def get_duplicate(data, logger):
    tmp_list = []
    for i in data:
        if i not in tmp_list:
            tmp_list.append(i)
        else:
            logger.error(f"Duplicate data with {i}. Format not good in puzzle. Exiting program.")
    if 0 not in data:
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
        if i != 0 and i != size:
            logger.error(f"The format is not supposed to differ of size x size format. Now exiting the program.")


def parse_data(puzzle, logger):
    numbers, size = get_numbers_and_size(puzzle)
    if len(numbers) % int(size) != 0:
        logger.error(f"The puzzle is not on a good format. There is to many data compared with size ({size})."
                     f" Now exiting program.")
    get_duplicate(numbers, logger)
    get_sequence(numbers, logger)
    get_good_format(puzzle, logger)
    is_solvable(numbers, size, logger)
    print(get_array(numbers, size))
    return numbers, size


def open_file(file):
    try:
        f = open(file, "r")
        puzzle = f.readlines()
        f.close()
        return puzzle
    except Exception as errno:
        print(f"{Fore.RED}{errno}{Style.RESET_ALL}")
        exit()
