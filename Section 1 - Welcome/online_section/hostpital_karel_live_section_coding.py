from karel.stanfordkarel import *


def main():
    # move 2 spaces until we find a beeper
    while no_beepers_present():
        move()
    build_hospital()
    
    # go to wall
    while front_is_clear():
        move()
    
    # build another hospital
    turn_right()
    while front_is_clear():
        move()
    
    # get in the right condition for the build_hosptial function
    turn_right()
    move()
    spin_180_degrees()
    build_hospital()
    
    # get karel to initial spot for 3rd hospital
    while not_facing_west():
        turn_left()
    
    # move back to the middle and build hospital
    for i in range(5):
        move()
    put_beeper()
    build_hospital()
    
    # go back to the end of the map (bottom right)
    while not_facing_east():
        turn_left()
    while front_is_clear():
        move()
    spin_180_degrees()
    move()
    spin_180_degrees()
    move()


def build_hospital():
    # start bottom left
    move()
    put_beeper_safely()
    turn_left()
    move()
    put_beeper_safely()
    turn_left()
    move()
    put_beeper_safely()
    turn_right()
    move()
    put_beeper_safely()
    turn_right()
    move()
    put_beeper_safely()
    # exit top right


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def spin_180_degrees():
    turn_left()
    turn_left()


def put_beeper_safely():
    if no_beepers_present():
        put_beeper()


if __name__ == '__main__':
    main()
