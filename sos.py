NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def encode_to_morse(input_string):
    """
    Encode a string into Morse code.

    Parameters:
    input_string (str): The string to be encoded.

    Returns:
    str: The encoded Morse code representation.

    Raises:
    AssertionError: If input_string is not a string.
    """
    assert isinstance(input_string, str), "AssertionError: the arguments are bad"
    try:
        return ' '.join(NESTED_MORSE[char.upper()] for char in input_string)
    except KeyError:
        raise AssertionError("AssertionError: the arguments are bad")

def main():
    """
    Main function to handle the program execution.
    """
    import sys
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    try:
        encoded_message = encode_to_morse(sys.argv[1])
        print(encoded_message)
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
