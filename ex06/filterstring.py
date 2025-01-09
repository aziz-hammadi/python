# filterstring.py
import sys
from ft_filter import ft_filter

def main():
    """
    The main function that accepts two arguments: a string S and an integer N.
    It outputs a list of words from S that have a length greater than N.

    If the number of arguments is not two or if any argument has the wrong type,
    it raises an AssertionError.
    """
    try:
        # check argument
        assert len(sys.argv) == 3, "the arguments are bad"

        # conformite arguments
        S, N = sys.argv[1], sys.argv[2]
        assert N.isdigit(), "The second argument must be an integer."
        N = int(N)

        # parsing
        words = S.split()
        filtered_words = ft_filter(lambda word: len(word) > N, words)

        # affiche mots filtre selon les conditions 
        print(list(filtered_words))

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
