# N-Puzzle

The goal of this project is to solve the N-puzzle game using the A* search algorithm, Greedy search algorithm or Djikstra's  search algorithm.

<table>
    <thead align="center">
        <tr>
            <td>A* search algorithm</td>
            <td>Greedy algorithm</td>
            <td>Djikstra's algorithm</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://miro.medium.com/max/420/1*HppvOLfDxXqQRFn0Cv2dHQ.gif"></td>
            <td><img width="300" src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Greedy-search-path.gif"></td>
            <td><img src="https://miro.medium.com/max/420/1*2jRCHqAbTCY7W7oG5ntMOQ.gif"></td>
        </tr>
    </tbody>
 </table>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

```python npuzzle.py```

```bash
usage: npuzzle.py [-h] -f FILE [-l]
                  [-he {euclidian,square_euclidian,manhattan,gaschnig,linear_conflict,hamming}]
                  [-a {a*,greedy,uniform cost}] [-v]

Solver of N-Puzzle

    optional arguments:
    
      -h, --help            show this help message and exit
    
      -f FILE, --file FILE  path of N-Puzzle file
      
      -l, --linear          resolve N-Puzzle lineary
      
      -he {euclidian,square_euclidian,manhattan,gaschnig,linear_conflict,hamming}, 
           --heuristic{euclidian,square_euclidian,manhattan,gaschnig,linear_conflict,hamming}
                            heuristic function used Default: manhattan
      
      -a {a*,greedy,uniform cost}, --algorithm {a*,greedy,uniform cost}
                            search algorithm used Default: a*
      
      -v, --verbose         display path to final puzzle
```

## Example

```
python npuzzle.py -f an_example_of_N-Puzzle
python npuzzle.py -f an_example_of_N-Puzzle -l
```
