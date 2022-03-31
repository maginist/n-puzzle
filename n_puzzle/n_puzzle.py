import argparse
from n_puzzle.utils import *
from n_puzzle.logger import Logger


def cli():
    parser = argparse.ArgumentParser(
        description="N-puzzle project. This project intend to create a solver of n-puzzle with at least 3 differents "
                    "heuristics functions.")
    parser.add_argument("-he", '--heuristic_choose', default=1,
                        help='Set on 1 by default. This option is use for choosing an heuristic functions. '
                             '1 is Manhattan distance heuristic, 2 is ____ and 3 is ____.')

    parser.add_argument("npuzzle", type=open_file, help="input a npuzzle file. Can be generated from generate_puzzle"
                                                        " command or create from scratch. You need to specify"
                                                        " the size at the first line.")
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
    parse_data(args.npuzzle, logger)


if __name__ == "__main__":
    cli()
