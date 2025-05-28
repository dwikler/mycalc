import sys
from mycalc.calc import add


def main():
    print("PYTHONPATH:", sys.path)
    print(f"3 + 4 = {add(3, 4)}")


if __name__ == "__main__":
    main()