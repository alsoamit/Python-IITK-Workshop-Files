# helper modules
import os
import sys
import math

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P72_template import main
# from P72_solution import main


############ TEST CASES BEGIN ############


def test_case1():
    inp = "70\n75"
    out = "Time of Flight = 13.8\nDistance Covered = 250.0\nPeak Height = 233.25"
    res = run(main, inp)
    assert (out == res)


def test_case2():
    inp = "20\n15"
    out = "Time of Flight = 1.06\nDistance Covered = 20.41\nPeak Height = 1.37"
    res = run(main, inp)
    assert (out == res)


def test_case3():
    inp = "12\n33"
    out = "Time of Flight = 1.33\nDistance Covered = 13.42\nPeak Height = 2.18"
    res = run(main, inp)
    assert (out == res)


def test_case4():
    inp = "1000\n1"
    out = "Time of Flight = 3.56\nDistance Covered = 3561.17\nPeak Height = 15.54"
    res = run(main, inp)
    assert (out == res)


def test_case5():
    inp = "100\n90"
    out = "Time of Flight = 20.41\nDistance Covered = 0.0\nPeak Height = 510.2"
    res = run(main, inp)
    assert (out == res)


############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
