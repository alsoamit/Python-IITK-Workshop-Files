# helper library functions
import pandas as pd
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    marks_file = input()

    result_df = None

    out_path = os.path.split(marks_file)[0] + os.sep + "result.csv"
    result_df.to_csv(out_path)


if __name__ == "__main__":
    main()
    