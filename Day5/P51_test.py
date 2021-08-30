# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P51 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "3\n4\n0,1\n1,2\n2,0\n0,2\n2"
	out = "0,1"
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = "3\n4\n0,1\n0,2\n2,0\n0,2\n2"
	out = "0"
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = "1\n0\n0"
	out = ""
	res = run(main, inp)
	assert (out == res)


def test_case4():
	inp = "5\n6\n0,1\n1,1\n4,1\n3,1\n2,1\n2,1\n1"
	out = "0,1,2,3,4"
	res = run(main, inp)
	assert (out == res)	

def test_case5():
	inp = "1\n5\n0,0\n0,0\n0,0\n0,0\n0,0\n0"
	out = "0"
	res = run(main, inp)
	assert (out == res)	


def test_case6():
	inp = "1\n5\n0,0\n0,0\n0,0\n0,0\n0,0\n1"
	out = "ERROR: Invalid Node."
	res = run(main, inp)
	assert (out == res)	



def test_case7():
	inp = "1\n0\n2"
	out = "ERROR: Invalid Node."
	res = run(main, inp)
	assert (out == res)	

def test_case8():
	inp = "5\n6\n0,1\n1,1\n4,1\n3,1\n2,1\n2,1\n2"
	out = ""
	res = run(main, inp)
	assert (out == res)	


############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
