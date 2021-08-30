# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P54 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = "1\n101\n102\n-1\n2\n101\n18\n80\n90\n45\n3\n101\n4\n5\n101\n6"
	out = "[18.0, 80.0, 90.0, 45.0]\n8.6\nB"
	res = run(main, inp)
	assert (out == res)



def test_case2():
	inp = "1\n101\n102\n-1\n2\n101\n18\n80\n90\n45\n3\n102\n6"
	out = "ERROR: Student roll number marks information unavailable"
	res = run(main, inp)
	assert (out == res)


def test_case3():
	inp = "1\n101\n102\n103\n104\n105\n-1\n6"
	out = ""
	res = run(main, inp)
	assert (out == res)


def test_case4():
	inp = "6"
	out = ""
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = "1\n102\n103\n104\n-1\n2\n102\n13\n58\n71\n35\n3\n102\n4\n5\n102\n6"
	out = "[13.0, 58.0, 71.0, 35.0]\n6.47\nD"
	res = run(main, inp)
	assert (out == res)

def test_case6():
	inp = "1\n101\n-1\n2\n101\n25\n98\n67\n42\n6"
	out = "ERROR: Invalid Marks 25.0 > 20"
	res = run(main, inp)
	assert (out == res)

def test_case7():
	inp = "1\n101\n-1\n2\n101\n-2\n98\n67\n42\n6"
	out = "ERROR: Invalid Marks -2.0 < 0"
	res = run(main, inp)
	assert (out == res)



def test_case8():
	inp = "1\n101\n-1\n2\n101\n20\n102\n67\n42\n6"
	out = "ERROR: Invalid Marks 102.0 > 100"
	res = run(main, inp)
	assert (out == res)

############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)

