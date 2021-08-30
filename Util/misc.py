import pandas as pd
import os

# constants

VALID = True
INVALID = False
FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH = range(6)
LAST = -1


# exception classes

class InvalidInputException(Exception):
    """Exception raised for errors in input."""

    def __init__(self, message="Invalid Input."):
        self.Message = message
        super().__init__(self.Message)


class Event(Exception):
    """Exception used for various events."""
    
    def __init__(self, message="Invalid Input."):
        self.Message = message
        super().__init__(self.Message)


# functions

def create_empty_dataframe(columns, dtypes, index=None):
    assert len(columns) == len(dtypes)
    dataframe = pd.DataFrame(index=index)
    for c,d in zip(columns, dtypes):
        dataframe[c] = pd.Series(dtype=d)
    return dataframe


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wait():
    print("\nPress Enter to continue...")
    input()
