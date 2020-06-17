import argparse
from algorithm import algorithm
from parsing import parse_file


def parse_args():
    parser = argparse.ArgumentParser(description='Solver of N-Puzzle')
    parser.add_argument("-f", "--file", type=str, required=True,
                        help="path of n-puzzle file")
    parser.add_argument("-l", "--linear", action="store_true",
                        help="resolve N-Puzzle lineary")
    parser.add_argument("-he", "--heuristic", choices=["euclidian", "square_euclidian", "manhattan", "gaschnig", "linear_conflict", "hamming"], default="manhattan",
                        help="heuristic function used Default: manhattan")
    parser.add_argument("-a", "--algorithm", choices=["a*", "greedy", "uniform cost"], default="a*",
                        help="search algorithm used Default: a*")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help='display path to final puzzle')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    puzzle = parse_file(args.file, args.linear)
    algorithm(puzzle, args.linear, args.verbose, args.heuristic, args.algorithm)
