# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame. This interactive simulation allows users to create and watch cellular patterns evolve according to Conway's rules.

## Features

- Interactive grid where users can toggle cells by clicking
- Start/Pause button to control simulation
- Step Forward button for manual progression
- Reset button to clear the grid
- Iteration counter to track generations
- Smooth animations with cell transitions
- User-friendly interface with hover effects

## Requirements

- Python 3.x
- Pygame

## Installation

1. Ensure Python is installed on your system.
2. Install Pygame using pip:
```
pip install pygame
```

## How to Run

To run the game, execute:
```
python game_of_life.py
```
## How to Play

1. **Create Pattern**: Click on cells in the grid to toggle them between alive (blue) and dead (gray)
2. **Controls**:
   - **Start/Pause**: Begin or pause the simulation
   - **Step Forward**: Advance the simulation by one generation
   - **Reset**: Clear the grid and reset the iteration counter

## Rules of the Game

The game follows Conway's classic rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.

## License

This project is open source and available under the MIT License.