import sys
import string

def count_characters(input_string):
    """
    Count the types of characters in a given string.

    Parameters:
    input_string (str): The string to analyze.

    Returns:
    dict: A dictionary containing counts of character types.
    """
    counts = {
        'upper': sum(1 for char in input_string if char.isupper()),
        'lower': sum(1 for char in input_string if char.islower()),
        'punctuation': sum(1 for char in input_string if char in string.punctuation),
        'spaces': sum(1 for char in input_string if char == ' '),
        'digits': sum(1 for char in input_string if char.isdigit())
    }
    return counts

def display_character_counts(input_string):
    """
    Display the counts of different character types for a given string.

    Parameters:
    input_string (str): The string to analyze and display the counts.
    """
    counts = count_characters(input_string)
    total_chars = len(input_string)
    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

def main():
    """
    Main function to handle user input and execute the program.
    """
    if len(sys.argv) > 2:
        print("AssertionError: Too many arguments provided.")
        sys.exit(1)

    if len(sys.argv) == 2:
        input_string = sys.argv[1]
    else:
        input_string = input("What is the text to count?\n")

    display_character_counts(input_string)

if __name__ == "__main__":
    main()
