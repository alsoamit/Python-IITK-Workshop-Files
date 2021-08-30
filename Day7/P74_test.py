# helper modules
import os
import sys
import pandas as pd

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run

from P74_template import main
# from P74_solution import main


############ TEST CASES BEGIN ############


def test_case1():
    inp = "./marks.csv"
    correct_result = pd.read_csv("./Correct_results.csv")

    res = run(main, inp)
    result = pd.read_csv("./result.csv")
    assert(correct_result.shape == result.shape)
    for i in range(result.shape[0]):
        if i < 2:
            continue
        assert(correct_result.at[i, "GPA"] == result.at[i, "GPA"])
        assert (correct_result.at[i, "Grade"] == result.at[i, "Grade"])


############# TEST CASES END #############
