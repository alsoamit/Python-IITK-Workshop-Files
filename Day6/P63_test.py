# helper modules
import os
import sys

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
from P63 import main

############ TEST CASES BEGIN ############


def test_case1():
	inp = 'Chocolate\n10'
	out = "Sorry, can not buy item. Not enough money"
	res = run(main, inp)
	assert (out == res)


def test_case2():
	inp = '''batata vada\npani-puri\nPotato Chips\ncredit-card\ndebit-card\n25'''
	out = "Available Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nAvailable Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nBad Input credit-card.\nTry Again.\nBad Input debit-card.\nTry Again.\nThank you for your purchase. Enjoy\nDo not forget to collect your change, 5 Rs."
	res = run(main, inp)
	assert (out == res)


def test_case3():
	inp = 'Chocolate\n15'
	out = "Thank you for your purchase. Enjoy"
	res = run(main, inp)
	assert (out == res)

def test_case4():
	inp = "Potato Chips\n25"
	out = "Thank you for your purchase. Enjoy\nDo not forget to collect your change, 5 Rs."
	res = run(main, inp)
	assert (out == res)

def test_case5():
	inp = "rabdi\nrasgulla\nchocolate\nBiscuit\nRs10\n10.0\n5"
	out = "Available Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nAvailable Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nAvailable Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nBad Input Rs10.\nTry Again.\nBad Input 10.0.\nTry Again.\nSorry, can not buy item. Not enough money"
	res = run(main, inp)
	assert (out == res)


def test_case6():
	inp = "rabdi\nrasgulla\nchocolate\nBiscuit\nRs10\n10.0\n10"
	out = "Available Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nAvailable Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nAvailable Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].\nTry Again.\nBad Input Rs10.\nTry Again.\nBad Input 10.0.\nTry Again.\nThank you for your purchase. Enjoy"
	res = run(main, inp)
	assert (out == res)



############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)



