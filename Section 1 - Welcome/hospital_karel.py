from karel.stanfordkarel import *


def main():
    # Check Karel can move forward
    while front_is_clear():
        move()
        
        # If there are supplies, stop moving and build a hospital
        if beepers_present():
            build_hopsital()


def build_hopsital():
    # Turn left to be in right position to build up
    turn_left()
    build_up()
    
    # Turn right to be in right position to build down
    turn_right()
    build_down()
    
    # Turn left to keep going through line and find more supplies to build hospitals
    turn_left()


def build_up():
    build_single_floor()
    build_single_floor()


def build_down():
    build_single_floor()
    turn_right()
    build_single_floor()
    build_single_floor()


def build_single_floor():
    move()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
