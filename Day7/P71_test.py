# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run

from P71_template import main
# from P71_solution import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "[[3, 2, 0], [1, -1, 0], [0, 5, 1]]\n[2, 4, -1]"
	out = "[ 2. -2.  9.]"
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\n[3, 4, 5]"
	out = "ERROR: Cannot find solution."
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]\n[3, 4, 5]"
	out = "[3. 4. 5.]"
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = "[[1,1], [2, -1]]\n[24, -6]"
	out = "[ 6. 18.]"
	res = run(main, inp)
	assert (out == res)


def test_case5():
	inp = "[[2, 0], [3, 1]]\n[6, 10]"
	out = "[3. 1.]"
	res = run(main, inp)
	assert (out == res)


def test_case6():
	inp = "[[1, 0, 0], [2, 0, 0], [3, 1, 0]]\n[3, 6, 10]"
	out = "ERROR: Cannot find solution."
	res = run(main, inp)
	assert (out == res)


def test_case7():
	inp = "[[1, 0], [2, 0]]\n[3, 6]"
	out = "ERROR: Cannot find solution."
	res = run(main, inp)
	assert (out == res)


def test_case8():
	inp = "[[1, 0, 1], [2, 0, 0], [3, 1, 0]]\n[3, 6, 10]"
	out = "[3. 1. 0.]"
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
