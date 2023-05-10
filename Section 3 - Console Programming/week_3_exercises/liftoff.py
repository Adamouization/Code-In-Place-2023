"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""
def main():
    # Counter used to count down in increments of 1
    countdown = 10
    
    # Keep counting until we reach 0
    while countdown > 0:
        print(countdown)  # print current number
        countdown -= 1  # subtract 1
    
    # Reached 0, exit while loop and print liftoff
    print("Liftoff!")


if __name__ == '__main__':
    main()
