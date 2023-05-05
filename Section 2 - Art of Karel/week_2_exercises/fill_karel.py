"""
Karel should fill the whole world with beepers.
"""
from karel.stanfordkarel import *


def main():
    # Look north to be in correct initial state of main loop
    while not_facing_north():
        turn_left()
    
    # Main loop
    while front_is_clear():  # Checked while facing north
        # Look east to fill row
        while not_facing_east():
            turn_left()
        
        # Fill 1 row and return to starting position
        fill_full_row()
        return_to_row_start()
        
        # Go up 1 row
        turn_right()
        move()
        
        # Face north for initial while loop condition
        while not_facing_north():
            turn_left()
    
    # End condition - reached final row
    turn_right()
    fill_full_row()
    

def fill_full_row():
    while front_is_clear():
        put_beeper_safely()
        move()
    put_beeper_safely()


def return_to_row_start():
    spin_180_degrees()
    while front_is_clear():
        move()


def put_beeper_safely():
    if no_beepers_present():
        put_beeper()


def spin_180_degrees():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()
