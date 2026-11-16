# Conway's Game of Life (console)

A small Python 3 program that simulates
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
on a fixed-edge board and prints each generation to the console.

```
Generation 1
.......###..
##..#.#...#.
.######.##..
..##..#...#.
............
```

`#` is a live cell, `.` is a dead cell.

## Requirements

- Python 3.8 or newer
- No third-party packages (standard library only)

## How to run

```bash
python game_of_life.py
```

All settings are optional:

| Option          | Default | Meaning                                  |
|-----------------|---------|------------------------------------------|
| `--width`       | 20      | number of columns                        |
| `--height`      | 10      | number of rows                           |
| `--generations` | 20      | how many generations to print            |
| `--delay`       | 0.5     | pause between generations, in seconds    |
| `--seed`        | random  | fixed seed for a repeatable start board  |

Example:

```bash
python game_of_life.py --width 30 --height 15 --generations 50 --delay 0.2 --seed 42
```

The defaults are constants at the top of `game_of_life.py` (`WIDTH`, `HEIGHT`,
`GENERATIONS`, `DELAY_SECONDS`, `ALIVE_PROBABILITY`), so they can also be
changed there.

## Rules

For each new generation:

- A live cell with 2 or 3 live neighbours stays alive; otherwise it dies.
- A dead cell with exactly 3 live neighbours becomes alive.
- Neighbours are the 8 surrounding cells, including diagonals.

The board does **not** wrap around. Cells outside the grid are simply not
counted, so edge cells have 5 neighbours and corner cells have 3.

## How the code is organised

| Function                 | Responsibility                                            |
|--------------------------|-----------------------------------------------------------|
| `create_random_board`    | builds the random starting grid (list of rows of bools)   |
| `count_live_neighbours`  | counts live cells around one cell, skipping off-grid ones |
| `next_cell_state`        | applies the rules to a single cell                        |
| `next_generation`        | builds a new grid from the current one                    |
| `print_board`            | prints the generation number and the grid                 |
| `parse_args` / `main`    | reads settings and runs the loop with a pause             |

`next_generation` always builds a **new** board. Updating the board in place
would be wrong, because cells later in the loop would see neighbours that
already belong to the next generation.

## Tests

```bash
python -m unittest -v
```

The tests check neighbour counts in corners, on edges and in the middle, and
known patterns: a blinker (oscillates), a block (stays still), and a lone
cell (dies).

## Notes

- **Time spent:** _fill in_
- **AI tools used:** _fill in (for example: Claude Code to draft the code,
  tests and README; I reviewed, ran and tested everything myself)_
