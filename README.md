
A simpel Asteroid rover control system.

## Installation

just install with pip


## Usage

Edit data/input.txt to set diffrent input commands

Grid is generated with 0 as empty space and 1 as obstacle.

As default the grid is generated with 0 obstacles.

## Testing

run $ `python3 -m pytest` in the root directory

## Todo list


- [x] **Three lined input from file**
    - [x] First line: cordinats to upper right corner
    - [x] Second line: rovers starting position and direction
    - [x] Third line: commands
- [x] **Define the grid on the asteroid**
    - [x] Cordinat system
    - [x] Max grid size 100 X 100
- [ ] Define rover
    - [ ] Takes commands from file input
    - [ ] Can start from any cordinats inside of the grid
    - [ ] Outputs the final position and direction of the rover
    - [ ] If it falls off the grid it outputs: "I fell off!"

- [ ] Bonus
    - [/] **unit tests**
        - [x]: test input file
        - [x]: test grid generation
        - [ ]: test rover movment
    - [/] **obstacles and collision detection**
        - [x]: generate grid with obstacles
        - [ ]: rover needs to scan the next move and check for obstacles
        - [ ]: rover can find new path

    - [ ] **Keep it simpel**
