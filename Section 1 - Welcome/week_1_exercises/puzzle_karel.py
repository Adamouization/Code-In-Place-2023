"""
File: puzzle_karel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""
from karel.stanfordkarel import *


def main():
    # go to pick up last piece of puzzle
    while no_beepers_present():
        move()
    
    # pick uo piece of puzzle and go place it
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    
    # go back down
    turn_180_degrees()
    while front_is_clear():
        move()
    turn_right()
    
    # return to beginning position
    while front_is_clear():
        move()
    turn_180_degrees()
    
    
def turn_180_degrees():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()
