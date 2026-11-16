"""Conway's Game of Life in the console.

How to run
----------
    python game_of_life.py                      # defaults below
    python game_of_life.py --width 30 --height 15 --generations 50 --delay 0.2
    python game_of_life.py --seed 42            # same random start every time

Requires Python 3 only (standard library, no NumPy).

Notes
-----
- Time spent: <fill in>
- AI tools: <fill in, e.g. "Claude (Claude Code) to draft the code and
  check the edge-handling logic; I reviewed and tested it myself.">
"""

import argparse
import random
import time

# Default settings - change these or override them on the command line.
WIDTH = 20
HEIGHT = 10
GENERATIONS = 20
DELAY_SECONDS = 0.5
ALIVE_PROBABILITY = 0.3   # chance that a cell starts alive

ALIVE_CHAR = "#"
DEAD_CHAR = "."


def create_random_board(width, height, alive_probability):
    """Return a height x width grid (list of rows) of True/False cells."""
    return [
        [random.random() < alive_probability for _ in range(width)]
        for _ in range(height)
    ]


def count_live_neighbours(board, row, col):
    """Count live cells among the up to 8 cells around (row, col).

    The board does not wrap: positions outside the grid are skipped,
    so edge cells have 5 neighbours and corner cells only 3.
    """
    height = len(board)
    width = len(board[0])
    count = 0
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue  # the cell itself is not its own neighbour
            r = row + d_row
            c = col + d_col
            if 0 <= r < height and 0 <= c < width and board[r][c]:
                count += 1
    return count


def next_cell_state(is_alive, live_neighbours):
    """Apply Conway's rules to one cell."""
    if is_alive:
        return live_neighbours in (2, 3)
    return live_neighbours == 3


def next_generation(board):
    """Build and return a new board; the old one is not modified.

    A new board is needed because every cell must be judged on the
    *current* generation, not on cells already updated in this step.
    """
    return [
        [
            next_cell_state(board[r][c], count_live_neighbours(board, r, c))
            for c in range(len(board[0]))
        ]
        for r in range(len(board))
    ]


def print_board(board, generation):
    """Print the generation number followed by the grid."""
    print(f"Generation {generation}")
    for row in board:
        print("".join(ALIVE_CHAR if cell else DEAD_CHAR for cell in row))
    print()


def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--width", type=int, default=WIDTH)
    parser.add_argument("--height", type=int, default=HEIGHT)
    parser.add_argument("--generations", type=int, default=GENERATIONS)
    parser.add_argument("--delay", type=float, default=DELAY_SECONDS,
                        help="seconds to pause between generations")
    parser.add_argument("--seed", type=int, default=None,
                        help="random seed for a repeatable start")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.width < 1 or args.height < 1:
        raise SystemExit("width and height must be at least 1")

    random.seed(args.seed)
    board = create_random_board(args.width, args.height, ALIVE_PROBABILITY)

    for generation in range(args.generations):
        print_board(board, generation)
        board = next_generation(board)
        time.sleep(args.delay)


if __name__ == "__main__":
    main()
