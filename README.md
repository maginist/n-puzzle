# n-puzzle [(subject)](https://cdn.intra.42.fr/pdf/pdf/41733/en.subject.pdf)

The goal of this project is to solve the N-puzzle ("taquin" in French) game using the A*
search algorithm or one of its variants.

You start with a square board made up of N*N cells. One of these cells will be empty,
the others will contain numbers, starting from 1, that will be unique in this instance of
the puzzle.

Your search algorithm will have to find a valid sequence of moves in order to reach the
final state, a.k.a the "snail solution", which depends on the size of the puzzle (Example
below).  
While there will be no direct evaluation of its performance in this instance of the
project, it has to have at least a vaguely reasonable perfomance : Taking a few second to
solve a 3-puzzle is pushing it, ten seconds is unacceptable.

The only move one can do in the N-puzzle is to swap the empty cell with one of its
neighbors (No diagonals, of course. Imagine you’re sliding a block with a number on it
towards an empty space).

## How to install

Create a virtual environment and activate it

On windows:

```bash
python -m venv venv
.\venv\Scripts\activate.bat
```

Install the pre-requirement:
```bash
pip install -U -r pre-requirements.txt
```

Execute `setup.py`:

* for dev:
```bash
pip install --editable .[dev]
```
* For user:
```bash
pip install .
```

## How to run

```bash
> n_puzzle -h 
usage: n_puzzle [-h] [-he HEURISTIC_CHOOSE] [-l log-level] npuzzle

N-puzzle project. This project intend to create a solver of n-puzzle with at
least 3 differents heuristics functions.

positional arguments:
  npuzzle               input a n-puzzle file. Can be generated from
                        generate_puzzle command or create from scratch. You
                        need to specify the size at the first line.

optional arguments:
  -h, --help            show this help message and exit
  -he HEURISTIC_CHOOSE, --heuristic_choose HEURISTIC_CHOOSE
                        Set on 1 by default. This option is use for choosing
                        an heuristic functions. 1 is Manhattan distance
                        heuristic, 2 is Euclidian distance heuristic and 3 is ____.
  -l log-level, --level log-level
                        Choices: ERROR, WARNING, INFO, DEBUG. The parameter
                        set by default is INFO.
```

## How to test

```bash
pytest .\tests
```

## Resources
* [example](https://example.com)