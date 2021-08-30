import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P41_solution import main
from P41 import main


def testcase1() -> None:
    inp='''2024'''
    out='''True'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''2025'''
    out='''False'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''2011'''
    out='''False'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''2016'''
    out='''True'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''2028'''
    out='''True'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''2029'''
    out='''False'''
    res=run(main,inp)
    assert(res==out)