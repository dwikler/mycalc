import sys

from mycalc.calc import add

def test_add():
    print("PYTHONPATH:", sys.path)
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2