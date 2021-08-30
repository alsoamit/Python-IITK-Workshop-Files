import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P36_solution import main
from P36 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''123, 456, 222, 145'''
    out='''[246, 912, 444, 290]'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''-1, 0, -2, 2, 0, 1'''
    out='''[-2, 0, -4, 4, 0, 2]'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''1'''
    out='''[2]'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''1, 0, 3, 55, -3'''
    out='''[2, 0, 6, 110, -6]'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''-5'''
    out='''[-10]'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''9,-10,11'''
    out='''[18, -20, 22]'''
    res=run(main,inp)
    assert(res==out)

