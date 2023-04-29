from karel.stanfordkarel import *


def main():
    for i in range(4):
        build_column()
        for j in range(4):
            move()

def build_column():
    turn_left()
    for i in range(4):
        build_floor()
    put_beeper()
    turn_left()
    turn_left()
    for i in range(4):
        move()
    turn_left()


def build_floor():
    put_beeper()
    move()


if __name__ == '__main__':
    main()
