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
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        raise AssertionError("AssertionError: the arguments are bad")

    # Unpack and validate arguments
    S, N = sys.argv[1], sys.argv[2]
    assert N.isdigit(), "AssertionError: The second argument must be an integer."
    N = int(N)

    # Split the string into words
    words = S.split()

    # Use lambda and ft_filter to filter words longer than N
    filtered_words = ft_filter(lambda word: len(word) > N, words)

    # Output the filtered words
    print(filtered_words)


if __name__ == "__main__":
    main()
