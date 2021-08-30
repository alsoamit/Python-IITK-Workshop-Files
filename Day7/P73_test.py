# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P74_template import main
# from P73_solution import main

############ TEST CASES BEGIN ############



def test_case1():
    inp = "./iris.csv"
    out = "Column wise means:\nsepal_length    5.843333\nsepal_width     3.054000\npetal_length    3.758667\npetal_width     1.198667\nplant           1.000000\ndtype: float64\nsepal_length    5.843333\nsepal_width     3.054000\npetal_length    3.758667\npetal_width     1.198667\nplant           1.000000\ndtype: float64\nsepal_length    5.843333\nsepal_width     3.054000\npetal_length    3.758667\npetal_width     1.198667\nplant           1.000000\ndtype: float64"
    res = run(main, inp)
    assert(out == res)

def test_case2():
    inp = "./iris_missing1.csv"
    out = "Column wise means:\nsepal_length    5.838667\nsepal_width     3.048000\npetal_length    3.759333\npetal_width     1.198667\nplant           1.006667\ndtype: float64\nsepal_length    5.838556\nsepal_width     3.049244\npetal_length    3.759125\npetal_width     1.198667\nplant           1.006667\ndtype: float64\nsepal_length    5.838667\nsepal_width     3.049333\npetal_length    3.759333\npetal_width     1.198667\nplant           1.006667\ndtype: float64"
    res = run(main, inp)
    assert (out == res)

def test_case3():
    inp = "./iris_missing2.csv"
    out = "Column wise means:\nsepal_length    5.797\nsepal_width     3.200\npetal_length    3.384\npetal_width     1.098\nplant           1.000\ndtype: float64\nsepal_length    5.797000\nsepal_width     3.208333\npetal_length    3.504543\npetal_width     1.135417\nplant           1.000000\ndtype: float64\nsepal_length    5.797\nsepal_width     3.208\npetal_length    3.507\npetal_width     1.134\nplant           1.000\ndtype: float64"
    res = run(main, inp)
    assert (out == res)

def test_case4():
    inp = "./iris_missing3.csv"
    out = "Column wise means:\nsepal_length    5.528972\nsepal_width     3.076636\npetal_length    2.887850\npetal_width     0.724299\nplant           0.598131\ndtype: float64\nsepal_length    5.528972\nsepal_width     3.076704\npetal_length    3.027663\npetal_width     0.784375\nplant           0.598131\ndtype: float64\nsepal_length    5.528972\nsepal_width     3.078037\npetal_length    3.029907\npetal_width     0.783000\nplant           0.598131\ndtype: float64"
    res = run(main, inp)
    assert (out == res)



############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)

