import numpy as np


def euclidian_Distance(puzzle, opt, size):
    puzzle2 = puzzle.copy()
    puzzle2 = np.reshape(puzzle2, (size, size))
    opt = np.reshape(opt, (size, size))
    res = 0
    for i in range(size):
        for j in range(size):
            res += (puzzle2[i][j] - opt[i][j]) ** 2
    return round(int(res))


def square_euclidian_Distance(puzzle, opt, size):
    puzzle2 = puzzle.copy()
    puzzle2 = np.reshape(puzzle2, (size, size))
    opt = np.reshape(opt, (size, size))
    res = 0
    for i in range(size):
        for j in range(size):
            res += (puzzle2[i][j] - opt[i][j]) ** 2
    return round(int(np.sqrt(res)))


def manhattan_Distance(puzzle, opt, size):
    res = 0
    puzzle2 = puzzle.copy()
    puzzle2 = np.reshape(puzzle2, (size, size))
    opt = np.reshape(opt, (size, size))
    for i in range(size):
        for j in range(size):
            if puzzle2[i][j] == 0:
                continue
            for k in range(size):
                for z in range(size):
                    if puzzle2[i][j] == opt[k][z]:
                        res += abs(i - k) + abs(j - z)
                        break
    return res


def gaschnig_Distance(puzzle, opt, size):
    res = 0
    puzzle = list(puzzle)
    opt = list(opt)
    while puzzle != opt:
        zi = puzzle.index(0)
        if opt[zi] != 0:
            sv = opt[zi]
            ci = puzzle.index(sv)
            puzzle[ci], puzzle[zi] = puzzle[zi], puzzle[ci]
        else:
            for i in range(size * size):
                if opt[i] != puzzle[i]:
                    puzzle[i], puzzle[zi] = puzzle[zi], puzzle[i]
                    break
        res += 1
    return res


def count_conflicts(puzzle_row, opt_row, size, ans=0):
    counts = [0 for x in range(size)]
    for i, tile_1 in enumerate(puzzle_row):
        if tile_1 in opt_row and tile_1 != 0:
            for j, tile_2 in enumerate(puzzle_row):
                if tile_2 in opt_row and tile_2 != 0:
                    if tile_1 != tile_2:
                        if (opt_row.index(tile_1) > opt_row.index(tile_2)) and i < j:
                            counts[i] += 1
                        if (opt_row.index(tile_1) < opt_row.index(tile_2)) and i > j:
                            counts[i] += 1
    if max(counts) == 0:
        return ans * 2
    else:
        i = counts.index(max(counts))
        puzzle_row[i] = -1
        ans += 1
        return count_conflicts(puzzle_row, opt_row, size, ans)


def linear_conflicts_Distance(puzzle, opt, size):
    res = manhattan_Distance(puzzle, opt, size)
    puzzle_rows = [[] for y in range(size)]
    puzzle_columns = [[] for x in range(size)]
    opt_rows = [[] for y in range(size)]
    opt_columns = [[] for x in range(size)]
    for y in range(size):
        for x in range(size):
            idx = (y * size) + x
            puzzle_rows[y].append(puzzle[idx])
            puzzle_columns[x].append(puzzle[idx])
            opt_rows[y].append(opt[idx])
            opt_columns[x].append(opt[idx])
    for i in range(size):
        res += count_conflicts(puzzle_rows[i], opt_rows[i], size)
    for i in range(size):
        res += count_conflicts(puzzle_columns[i], opt_columns[i], size)
    return res


def hamming_Distance(puzzle, opt, size):
    res = 0
    puzzle2 = puzzle.copy()
    puzzle2 = np.reshape(puzzle2, (size, size))
    opt = np.reshape(opt, (size, size))
    for i in range(size):
        for j in range(size):
            if puzzle2[i][j] == 0:
                continue
            if puzzle2[i][j] != opt[i][j]:
                res += 1
    return res
