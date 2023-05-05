"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""
from karel.stanfordkarel import *


def main():
    # move to the stack
    move()
    
    # repeat
    while beepers_present():
        # pick a beeper from the stack
        pick_beeper()
        
        # check if there are any beepers left in the stack
        if beepers_present():
            # move to empty cell
            while beepers_present():
                move()
            
            # place it
            put_beeper()
            
            # go home (first cell)
            go_to_first_cell()
            
            # move to the stack
            move()
        
        # end condition    
        else:
            put_beeper()
            go_to_first_cell()


def go_to_first_cell():
    # go back
    turn_around()
    while beepers_present():
        move()
    # face in the right direction
    turn_around()
    

def turn_around():
    """
    This function turns left 90 degrees twice to spin around.
    """
    for i in range(2):
        turn_left()


if __name__ == '__main__':
    main()
