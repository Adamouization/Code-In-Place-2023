import random


# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def main():
    lines = get_words_from_file()
    play_game(lines)
    

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    with open(FILE_NAME) as file:
        lines = file.read().splitlines() 
    lines.pop(0)
    return lines


def play_game(words_lst):
    # Generate max index to access list items without errors
    max_index = len(words_lst) - 1  # transform to 0-index
    
    # Loop
    while True:
        # Print a random word
        random_index = random.randint(0, max_index)
        print(words_lst[random_index])
        
        # Wait for user input before continuing loop
        input()


if __name__ == '__main__':
    main()
