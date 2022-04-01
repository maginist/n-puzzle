import argparse

from queue import PriorityQueue

from n_puzzle.utils.logger import Logger
from n_puzzle.utils.utils import parse_data, open_file#, is_solvable


def n_puzzle(puzzle, size, args):
    print(f"numbers = {puzzle}")
    # print(f"size = {size}")
    # print(f"data = {args.npuzzle}")


def cli():
    parser = argparse.ArgumentParser(
        description="N-puzzle project. This project intend to create a solver of n-puzzle with at least 3 differents "
                    "heuristics functions.")
    parser.add_argument("-he", '--heuristic_choose', default=1,
                        help='Set on 1 by default. This option is use for choosing an heuristic functions. '
                             '1 is Manhattan distance heuristic, 2 is Euclidian distance heuristic and 3 is ____.')

    parser.add_argument("npuzzle", type=open_file, help="input a n-puzzle file. Can be generated from generate_puzzle"
                                                        " command or create from scratch. You need to specify"
                                                        " the size at the first line.")
    parser.add_argument("-t", "--time", action="store_true", help="Print the algorithm time.")
    parser.add_argument("-g", "--greedy", action="store_true", help="Enable greedy searching.")
    parser.add_argument("-u", "--uniform_cost", action="store_true", help="Enable uniform cost searching.")
    parser.add_argument(
        "-l",
        "--level",
        metavar="log-level",
        choices=["ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        default="INFO",
        help="Choices: ERROR, WARNING, INFO, DEBUG. The parameter set by default is INFO.",
    )
    args = parser.parse_args()
    logger = Logger(level=args.level, name="Log from npuzzle solver")
    if not args.npuzzle:
        logger.error(f"The npuzzle is empty or not usable, please check the file. Now exiting the program.")
    puzzle, size = parse_data(args.npuzzle, logger)
    n_puzzle(puzzle, size, args)


if __name__ == "__main__":
    cli()
