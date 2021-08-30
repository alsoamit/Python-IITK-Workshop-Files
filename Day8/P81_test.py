########[ IMMUTABLE CODE SECTION BEGIN ]#########
# --------------------------------------------- #
# helper modules                                #
import sys, os, pytest                          #
sys.path.insert(0, "..")                        #
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))   #
from Util.pyt import run                        #
from P81 import main                   #
# --------------------------------------------- #
#########[ IMMUTABLE CODE SECTION END ]##########


############[ TEST CASES BEGIN ]############

@pytest.mark.basic
def test_case1() -> None:
    inp = '''circle 12'''
    out = '''452.39 75.40 Black False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case2() -> None:
    inp = '''rectangle 10.5 2.5 Blue'''
    out = '''26.25 26.00 Blue False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case3() -> None:
    inp = '''circle 12 orange True'''
    out = '''452.39 75.40 Orange True'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case4() -> None:
    inp = '''Quadrilateral 10 5 15 5 red '''
    out = '''None 35.00 Red False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case5() -> None:
    inp = '''Square 10 yellow false'''
    out = '''100.00 40.00 Yellow False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case6() -> None:
    inp = '''Circle 0.32 black true'''
    out = '''0.32 2.01 Black True'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case7() -> None:
    inp = '''n-gon 12 5 2.5 6 2 4'''
    out = '''None 31.50 Black False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case8() -> None:
    inp = '''shape true'''
    out = '''None None True False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case9() -> None:
    inp = '''triangle 1 2 3'''
    out = '''Invalid Input'''
    res = run(main, inp)
    assert (res.find(out) != -1)

@pytest.mark.advanced
def test_case10() -> None:
    inp = '''rectangle 10.5 2.5 Red T'''
    out = '''Invalid Input'''
    res = run(main, inp)
    assert (res.find(out) != -1)

############[ TEST CASES END ]############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
