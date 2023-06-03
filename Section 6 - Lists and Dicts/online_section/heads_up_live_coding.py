import random
import scikit-learn


# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    # load list of words
    words_lst = get_words_from_file()
    
    while True:
        # choose random from list
        # random_word_from_lst = words_lst[random.randint(0, len(words_lst) - 1)]
        random_word_from_lst = random.choice(words_lst)
        print("\nWord to guess: " + random_word_from_lst)
        
        user_input = input("Hit enter to get next word.")


if __name__ == '__main__':
    main()


# Extensions:
# Different user input that is not "enter"
# For the first, we might make it so we can have our players’ names which cycles to make things a bit more organized when playing.
# For the second, we might want to make categories of words so we can play with different words which might be more recognizable for a different audience! 
