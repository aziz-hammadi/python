import sys

try:
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided" if len(sys.argv) > 2 else "no argument provided")

    arg = sys.argv[1]

    if not arg.lstrip('-').isdigit():
        raise AssertionError("argument is not an integer")

    number = int(arg)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print(f"AssertionError: {error}")
