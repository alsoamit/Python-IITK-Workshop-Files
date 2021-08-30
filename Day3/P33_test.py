import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P33_solution import main
from P33 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''371'''
    out='''Sum of Cubes is 371. It is the same as the number 371.'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''5'''
    out='''Sum of Cubes is 125. It is NOT same as the number 5.'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''10203020'''
    out='''Sum of Cubes is 44. It is NOT same as the number 10203020.'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''1634'''
    out='''Sum of Cubes is 308. It is NOT same as the number 1634.'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''407'''
    out='''Sum of Cubes is 407. It is the same as the number 407.'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''0'''
    out='''Sum of Cubes is 0. It is the same as the number 0.'''
    res=run(main,inp)
    assert(res==out)

def testcase7() -> None:
    inp='''1'''
    out='''Sum of Cubes is 1. It is the same as the number 1.'''
    res=run(main,inp)
    assert(res==out)
