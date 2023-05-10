"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""
DEFAULT_VALUE = 1


def main():
    print("This program multiplies two numbers.")
    
    # Get both numbers that were inputted by the user.
    num1 = get_input_as_int("Enter first number: ")
    num2 = get_input_as_int("Enter second number: ")

    # Multiply the numbers
    print(num1 * num2)


def get_input_as_int(prompt_str):
    """
    Capture user input. Tries to convert the input to an integer, and if it fails, converts it to a default value of 1.
    """
    try:
        num = int(input(prompt_str))
    except ValueError as ve:
        print(f"The input passed was not an integer. The input value will be set to 1 by default. {ve}")
        num = DEFAULT_VALUE
    
    return num


if __name__ == '__main__':
    main()
