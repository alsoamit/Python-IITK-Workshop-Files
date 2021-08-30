###############################[ IMMUTABLE CODE SECTION BEGIN ]##################################
# --------------------------------------------------------------------------------------------- #
# helper library functions                                                                      #
from math import gcd                                                                            #
import sys, os                                                                                  #
sys.path.insert(0, "..")                                                                        #
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))           #
from Util.misc import VALID, INVALID, FIRST, SECOND, THIRD, FOURTH, LAST, InvalidInputException #
#                                                                                               #
# additional constants                                                                          #
EXPECTED_ARGS_POW_OP, EXPECTED_ARGS_NON_POW_OP = 4, 5                                           #
#                                                                                               #
switch_op_func = {                                                                              #
    "+" :   lambda a, b: a + b,                                                                 #
    "-" :   lambda a, b: a - b,                                                                 #
    "*" :   lambda a, b: a * b,                                                                 #
    "/" :   lambda a, b: a / b,                                                                 #
    "<" :   lambda a, b: a < b,                                                                 #
    ">" :   lambda a, b: a > b,                                                                 #
    "<=":   lambda a, b: a <= b,                                                                #
    ">=":   lambda a, b: a >= b,                                                                #
    "==":   lambda a, b: a == b,                                                                #
    "!=":   lambda a, b: a != b                                                                 #
}                                                                                               #
# --------------------------------------------------------------------------------------------- #
################################[ IMMUTABLE CODE SECTION END ]###################################


class RationalNumber(object):
    """Class for representing rational numbers of the form p/q"""

    # define constructor

    # overloading the addition (+) operator
    def __add__(self, other):
        pass

    # overloading the multiplication (*) operator
    def __mul__(self, other):
        pass

    # overloading the subtraction (-) operator
    def __sub__(self, other):
        pass

    # overloading the division (/) operator
    def __truediv__(self, other):
        pass

    # overloading the power (**) operator
    def __pow__(self, number):
        pass

    # overloading the less than (<) operator
    def __lt__(self, other):
        pass

    # overloading the less than (<) operator
    def __gt__(self, other):
        pass

    # overloading the equal to (==) operator
    def __eq__(self, other):
        pass

    # overloading the less than or equal to (<=) operator
    def __le__(self, other):
        pass

    # overloading the greater than or equal to (>=) operator
    def __ge__(self, other):
        pass

    # overloading the not equal to (!=) operator
    def __ne__(self, other):
        pass

    # overloading the default string conversion
    def __str__(self):
        pass

    def is_canonical(self):
        """Whether the rational number is in canonical form."""
        pass

    def to_canonical(self):
        """Return canonical form of the rational number."""
        pass

    def is_integer(self):
        """Whether the rational number is a pure integer."""
        pass


#######[ IMMUTABLE CODE SECTION BEGIN ]#######
# ------------------------------------------ #
def main():                                  #
# ------------------------------------------ #
########[ IMMUTABLE CODE SECTION END ]########
    """
    INPUT:
        p q m [n] op
            Two rational numbers represented by p q and m n, and an Operator op
            Note that n is optional if op is a power operator
    OUTPUT:
        resulting rational number (based on arithmetic operation b/w the two) \\
            in canonical form or integer form (if it's also a pure integer) (or)
        boolean result (based on logical operation b/w the two)
    """

    # read input

    # validate input and create rational number object(s)

    # result = first_number operator second_number
    # result = switch_op_func[operator](first_rational_number, second_rational_number)

    # if input valid and operation valid
        # print(rational_number_result) in case of arithmetic operation
        # or
        # print(str(boolean_result).title()) in case of logical operation

    pass


#######[ IMMUTABLE CODE SECTION BEGIN ]#######
# ------------------------------------------ #
# Using the special variable __name__        #
if __name__ == "__main__":                   #
    main()                                   #
# ------------------------------------------ #
########[ IMMUTABLE CODE SECTION END ]########
