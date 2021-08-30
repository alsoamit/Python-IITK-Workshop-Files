########[ IMMUTABLE CODE SECTION BEGIN ]#########
# --------------------------------------------- #
# helper modules                                #
import sys, os, pytest                          #
sys.path.insert(0, "..")                        #
sys.path.append(os.path.join(os.path.dirname\
    (os.path.realpath(__file__)), os.pardir))   #
from Util.pyt import run                        #
from P82 import main                   #
# --------------------------------------------- #
#########[ IMMUTABLE CODE SECTION END ]##########


############ TEST CASES BEGIN ############

@pytest.mark.basic
def test_case1() -> None:
    inp = '''2 5 3 5 +'''
    out = '''1'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case2() -> None:
    inp = '''1 9 7 9 -'''
    out = '''-2/3'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case3() -> None:
    inp = '''15 4 -5 4 /'''
    out = '''-3'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case4() -> None:
    inp = '''1 2 3 **'''
    out = '''1/8'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case5() -> None:
    inp = '''7 10 -14 20 +'''
    out = '''0'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.basic
def test_case6() -> None:
    inp = '''2 -5 -25 15 *'''
    out = '''2/3'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case7() -> None:
    inp = '''6 -18 -18 54 =='''
    out = '''True'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case8() -> None:
    inp = '''2 -4 -3 **'''
    out = '''-8'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case9() -> None:
    inp = '''6 -18 -15 45 >'''
    out = '''False'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case10() -> None:
    inp = '''-1 -1 3 3 +'''
    out = '''2'''
    res = run(main, inp)
    assert (res == out)

@pytest.mark.advanced
def test_case11() -> None:
    inp = '''1 2 0 3 /'''
    out = '''Invalid Input'''
    res = run(main, inp)
    assert (res.find(out) != -1)

@pytest.mark.advanced
def test_case12() -> None:
    inp = '''3 0 2 1 *'''
    out = '''Invalid Input'''
    res = run(main, inp)
    assert (res.find(out) != -1)

############# TEST CASES END #############

######## ADD MORE TEST CASES BELOW #######

# def test11():
#     inp = '''input'''
#     out = '''output'''
#     res = run(main, inp)
#     assert(res == out)
