"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
# import math
WEIGHT_RATIO = 0.378


def main():
    # Take input from user as a string
    earth_weight_input_str = input("Enter a weight on Earth: ")
    
    # Casting string into a number (float)
    earth_weight_float = float(earth_weight_input_str)
    
    # Calculating weight on Mars
    mars_weight = earth_weight_float * WEIGHT_RATIO
    
    # Print new weight using f-string and converting new weight back to string
    print(f"The equivalent weight on Mars: {str(mars_weight)}")
    

if __name__ == "__main__":
    main()
