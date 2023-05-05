"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""
from karel.stanfordkarel import *


def main():
    # Move to first beeper in stack to spread
    move()
    
    # Spread beepers until there are no more to spread
    # logic: if at least 1 beeper still present in stack, then keep spreading
    while beepers_present():
        # Pick beeper to spread
        # If still one left after, spread
        # If it was the last one, none left and can end loop (put back and return)
        pick_beeper()
        
        # Continue loop because there is still a beeper left in stack
        if beepers_present():
            
            # Put beeper in next free spot
            while beepers_present():
                move()
            put_beeper()
            
            # Go back to stack of beepers to spread
            go_back()
            move()
            
            
    # End condition: put back beeper picked up go back to start     
    put_beeper()
    go_back()


def go_back():
    spin_180_degrees()
    while front_is_clear():
        move()
    spin_180_degrees()


def spin_180_degrees():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
