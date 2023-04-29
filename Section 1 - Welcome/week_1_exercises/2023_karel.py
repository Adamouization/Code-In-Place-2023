"""
File: 2023_karel.py
--------------------
When you finish writing this file, Karel should be able to 
place 20 beepers, then 23 beepers, and end facing East to 
the right of the 23 beepers.
"""
from karel.stanfordkarel import *


def main():
    for i in range(20):
        put_beeper()
    move()
    for i in range(23):
        put_beeper()
    move()


if __name__ == '__main__':
    main()
