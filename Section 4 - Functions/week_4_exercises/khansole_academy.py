import random


# Define constants
CONSECUTIVE_CORRECT_ANSWERS_NEEDED = 3
SUM_RANGE_MIN = 10
SUM_RANGE_MAX = 99


def main():
    # Initialise the Khansole
    print("Khansole Academy")
    number_of_consecutive_correct_solutions = 0
    
    # Repeat questions until defined number of constants reached
    while number_of_consecutive_correct_solutions < CONSECUTIVE_CORRECT_ANSWERS_NEEDED:
        
        # Generate random 2-digit numbers
        num1 = random.randint(SUM_RANGE_MIN, SUM_RANGE_MAX)
        num2 = random.randint(SUM_RANGE_MIN, SUM_RANGE_MAX)
        
        # Print question
        print(f"What is {num1} + {num2}?")
        sum_solution = num1 + num2
        
        # Capture user input
        sum_user = int(input("Your answer: "))
        
        # Check if solution correct or not
        if sum_user == sum_solution:  # correct
            # Increment number of correct solutions by 1
            number_of_consecutive_correct_solutions += 1
            
            # Print message
            print("Correct! You've gotten {} correct in a row.".format(
                number_of_consecutive_correct_solutions
            ))
        
        else:  # incorrect
            # Reset number of correct solutions to 0
            number_of_consecutive_correct_solutions = 0
            
            # Print message
            print("Incorrect!")
            print(f"The expected answer is {sum_solution}")
        
        # Add an extra space between questions
        print()
    
    # Exit message  
    print("Congratulations! You mastered addition.")
    
    
    
if __name__ == '__main__':
    main()
