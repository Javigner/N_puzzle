import sys
import math
import numpy as np


def error(filename):
    try:
        with open(filename, 'r') as f:  # open the file
            for line in f:
                print(line, end='')
    except Exception as e:
        sys.exit(print("{}: {}".format(type(e).__name__, e)))
    print("\nError")


def open_and_parse_comments(filename):
    try:
        puzzle = []
        with open(filename, 'r') as f:  # open the file
            for line in f:
                l = line.split('#')[0].split()
                if l:
                    if all(str(s).isdigit() for s in l):
                        puzzle.append(list(map(int, l)))
                    else:
                        return
    except Exception as e:
        sys.exit(print("{}: {}".format(type(e).__name__, e)))
    return puzzle


def parse_puzzle(puzzle2d):
    if len(puzzle2d) <= 3 or len(puzzle2d[0]) != 1:
        return
    dims = puzzle2d[0][0]
    if len(puzzle2d[1:]) != dims:  # check number of lines
        return
    for line in puzzle2d[1:]:
        line = list(x for x in line if 0 <= x <= dims * dims - 1)  # delete int too large or too small
        if len(line) != dims:  # check number of int in line
            return
    puzzle1d = [item for sublist in puzzle2d[1:] for item in sublist]
    if not len(puzzle1d) == len(set(puzzle1d)):  # check if there is duplicate number
        return
    return puzzle1d


def spiral_traversal(matrix):
    res = []
    while matrix.size:
        res.append(matrix[0])  # take first row
        matrix = matrix[1:].T[::-1]  # cut off first row and rotate counterclockwise
    return np.concatenate(res)


def cost_of_inversion(puzzle):
    inversion = 0
    for idx, val in enumerate(puzzle):
        inversion += (sum(val > i for i in puzzle[idx:]))
    return inversion


def row_of_zero(puzzle):
    return math.ceil((puzzle.index(0) + 1) / (math.sqrt(len(puzzle))))


def is_solvable_linear(puzzle):
    row = 1
    if len(puzzle) % 2 == 0:
        row = row_of_zero(puzzle[::-1])
        puzzle.remove(0)
        inversion = cost_of_inversion(puzzle)
    else:
        inversion = cost_of_inversion(puzzle)
    return True if not row % 2 == inversion % 2 else False


def cost_zero(puzzle):
    init = np.argwhere(puzzle == 0)[0]
    if len(puzzle) % 2 == 0:
        final = np.array([len(puzzle) // 2, len(puzzle) // 2 - 1])
    else:
        final = np.array([len(puzzle) // 2, len(puzzle) // 2])
    return sum([abs(x - y) for x, y in zip(init, final)])


def is_solvable_snail(spiral, puzzle):
    spiral[np.where(spiral == np.min(spiral))] = np.max(spiral) + 1
    inversion = cost_of_inversion(spiral)
    cost = cost_zero(puzzle)
    return True if inversion % 2 == cost % 2 else False


def parse_file(filename, is_linear):
    puzzle2d = open_and_parse_comments(filename)
    if not puzzle2d:
        sys.exit(error(filename))
    puzzle1d = parse_puzzle(puzzle2d)
    if not puzzle1d:
        sys.exit(error(filename))
    spiral = spiral_traversal(np.array(puzzle2d[1:]))
    if is_solvable_linear(puzzle1d.copy()) if is_linear else is_solvable_snail(spiral, np.array(puzzle2d[1:])):
        return puzzle1d
    else:
        error(filename)
        sys.exit(print("This puzzle is unsolvable"))
