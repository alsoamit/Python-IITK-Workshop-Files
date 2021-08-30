import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P34_solution import main
from P34 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''3'''
    out='''*\n**\n***'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''4'''
    out='''*\n**\n***\n****'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''10'''
    out='''*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''13'''
    out='''*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********\n***********\n************\n*************'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''1'''
    out='''*'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''6'''
    out='''*\n**\n***\n****\n*****\n******'''
    res=run(main,inp)
    assert(res==out)

def testcase7() -> None:
    inp='''16'''
    out='''*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********\n***********\n************\n*************\n**************\n***************\n****************'''
    res=run(main,inp)
    assert(res==out)
