def main():
    # Take user input
    curr_value = int(input("Enter a number: "))
    
    # Double as long as number is smaller than 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double value
        print(curr_value)


if __name__ == '__main__':
    main()
