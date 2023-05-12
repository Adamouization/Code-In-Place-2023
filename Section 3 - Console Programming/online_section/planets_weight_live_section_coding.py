"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
# Define all the constants
MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.360
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.14
EARTH = 1.0


def main():
    # Take input from user as a string
    earth_weight_input_str = input("Enter a weight on Earth: ")
    
    # Casting string into a number (float)
    earth_weight_float = float(earth_weight_input_str)
    
    # Take input for planet choice
    planet_choice_str = input("Enter a planet: ")
    
    # Have a default value of 0 in case none of the if conditions below are true
    # (if the planet choice is wrong)
    weight = 0
    
    # Go through each condition to see which constant to multiply by
    if planet_choice_str == "Mars":
        weight = earth_weight_float * MARS
    elif planet_choice_str == "Mercury":
        weight = earth_weight_float * MERCURY
    elif planet_choice_str == "Venus":
        weight = earth_weight_float * VENUS
    elif planet_choice_str == "Jupiter":
        weight = earth_weight_float * JUPITER
    elif planet_choice_str == "Saturn":
        weight = earth_weight_float * SATURN
    elif planet_choice_str == "Uranus":
        weight = earth_weight_float * URANUS
    elif planet_choice_str == "Neptune":
        weight = earth_weight_float * NEPTUNE
    elif planet_choice_str == "Earth":
        weight = earth_weight_float * EARTH
    else:
        print("Invalid planet name")
    
    # Round to nearest 2nd decimal
    weight = round(weight, 2)
    
    # Print new weight back to user
    print(f"The equivalent weight on {planet_choice_str}: {str(weight)}")


if __name__ == "__main__":
    main()
