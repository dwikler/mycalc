import sys
from mycalc.calc import add


def compute_addition(a, b):
    """
    Computes the sum of two numbers using the add function from mycalc.calc.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return add(a, b)


def main():
    """
    Entry point for the mycalculator CLI.

    Accepts two numbers as command-line arguments, adds them using the add function from mycalc.calc,
    and prints the result. Also prints the current PYTHONPATH.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Add two numbers using mycalc.")
    parser.add_argument("a", type=float, help="First number to add")
    parser.add_argument("b", type=float, help="Second number to add")
    args = parser.parse_args()

    result = compute_addition(args.a, args.b)
    print("PYTHONPATH:", sys.path)
    print(f"{args.a} + {args.b} = {result}")


if __name__ == "__main__":
    main()