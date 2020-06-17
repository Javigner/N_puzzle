import math
from queue import PriorityQueue
from heuristics import *


def change_Position(puzzle, direction, size):
    pos = 0
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            pos = i
    if direction == 'up':
        puzzle[pos], puzzle[pos - size] = puzzle[pos - size], puzzle[pos]
    if direction == 'down':
        puzzle[pos], puzzle[pos + size] = puzzle[pos + size], puzzle[pos]
    if direction == 'right':
        puzzle[pos], puzzle[pos + 1] = puzzle[pos + 1], puzzle[pos]
    if direction == 'left':
        puzzle[pos], puzzle[pos - 1] = puzzle[pos - 1], puzzle[pos]
    return puzzle


def position_Valid(puzzle, size):
    up = down = right = left = 1
    pos = 0
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            pos = i
    if pos < size:
        up = 0
    if pos >= len(puzzle) - size:
        down = 0
    if pos % size == 0:
        left = 0
    if (pos + 1) % size == 0 and pos != 0:
        right = 0
    return up, down, left, right


def spiral(n):
    def spiral_part(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x + 1) and x < (n // 2):
            return spiral_part(x - 1, y - 1, n - 1) + 4 * (n - y)
        if (n - y) > x >= y:
            return spiral_part(y - 1, y, n) + (x - y) + 1
        if x >= (n - y) and y <= x:
            return spiral_part(x, y - 1, n) + 1
        if (n - y) <= x < y:
            return spiral_part(x + 1, y, n) + 1
        if x < (n - y) and y > x:
            return spiral_part(x, y - 1, n) - 1

    array = [[0] * n for j in range(n)]
    for x in range(n):
        for y in range(n):
            array[x][y] = spiral_part(y, x, n)
    array = np.squeeze(array)
    array = np.squeeze(np.reshape(array, (1, n * n)))
    array = array + 1
    array = np.where(array == n * n, 0, array)
    return array


def heuristics(puzzle, opt, size):
    if HEURISTIC == "euclidian":
        return euclidian_Distance(puzzle, opt, size)
    elif HEURISTIC == "square_euclidian":
        return square_euclidian_Distance(puzzle, opt, size)
    elif HEURISTIC == "manhattan":
        return manhattan_Distance(puzzle, opt, size)
    elif HEURISTIC == "gaschnig":
        return gaschnig_Distance(puzzle, opt, size)
    elif HEURISTIC == "linear_conflict":
        return linear_conflicts_Distance(puzzle, opt, size)
    elif HEURISTIC == "hamming":
        return hamming_Distance(puzzle, opt, size)


def compute_Position(move, puzzle, test_list, opt, used_list, size, cost, selected):
    puzzle_new = change_Position(puzzle.copy(), move, size)
    if tuple(puzzle_new) in used_list:
        return test_list, selected
    if ALGORITHM == "a*":
        dist_new = heuristics(puzzle_new, opt, size) * math.log(size) * size + cost
    elif ALGORITHM == "greedy":
        dist_new = heuristics(puzzle_new, opt, size),
    elif ALGORITHM == "uniform cost":
        dist_new = cost
    if not any(puzzle in item[1] for item in test_list.queue):
        test_list.put((dist_new, puzzle_new, puzzle, cost + 1))
        selected += 1
    return test_list, selected


def find_path(puzzle, path):
    res = []
    while 1:
        for i in range(len(path)):
            if puzzle == path[i][0]:
                res.append(path[i][1])
                puzzle = path[i][1]
                if puzzle == ROOT:
                    return list(reversed(res))
                break


def solver(puzzle, opt, size):
    path = []
    used_list = set()
    test_list = PriorityQueue()
    test_list.put((0, puzzle, puzzle, 0))
    complexity = 0
    selected = 0
    while not test_list.empty():
        complexity += 1
        dist, puzzle, parent, cost = test_list.get()
        used_list.add(tuple(puzzle))
        path.append((puzzle, parent, dist))
        if puzzle == list(opt):
            path = find_path(puzzle, path)
            path.append(list(opt))
            break;
        up, down, left, right = position_Valid(puzzle, size)
        if up == 1:
            test_list, selected = compute_Position('up', puzzle, test_list, opt, used_list, size, cost,
                                                   selected)
        if down == 1:
            test_list, selected = compute_Position('down', puzzle, test_list, opt, used_list, size, cost,
                                                   selected)
        if left == 1:
            test_list, selected = compute_Position('left', puzzle, test_list, opt, used_list, size, cost,
                                                   selected)
        if right == 1:
            test_list, selected = compute_Position('right', puzzle, test_list, opt, used_list, size, cost,
                                                   selected)
    return path, complexity, selected


def algorithm(puzzle, is_linear, is_verbose, heuristic, algorithm):
    global ROOT
    global HEURISTIC
    global ALGORITHM
    ROOT = puzzle.copy()
    HEURISTIC = heuristic
    ALGORITHM = algorithm
    size = int(np.sqrt(len(puzzle)))
    opt = np.roll(np.arange(size ** 2), -1) if is_linear else spiral(size)
    path, complexity, selected = solver(puzzle, opt, size)
    if is_verbose:
        [print(route.reshape(size, size)) for route in np.array(path)]
        print('Number of moves :', len(path))
    else:
        print(np.array(path[len(path) - 1]).reshape(size, size))
    print('Complexity in time :', complexity)
    print('Complexity in size :', selected)
