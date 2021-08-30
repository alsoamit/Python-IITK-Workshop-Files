# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P61 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = 'x123\n[1, 1+2, "def_" + "abc"]\n["int", "float", "str"]'
	out = "1\n3\ndef_abc\n\nint\nfloat\nstr\n"
	res = run(main, inp)
	assert (out == res)

def test_case2():
	inp = '1234\n[]\n[]'
	out = "\n"
	res = run(main, inp)
	assert (out == res)

def test_case3():
	inp = 'axbyczd\n["Hello", "hi", "hi "*3]\n[0,0,0]'
	out = "Hello\nhi\nhi hi hi \n\n0\n0\n0\n"
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = '''000\n["math", "trigno", "intgr"]\n['__lt__', '__gt__', '__eq__']'''
	out = 'math\ntrigno\nintgr\n\n__lt__\n__gt__\n__eq__\n'
	res = run(main, inp)
	assert (out == res)


############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)



