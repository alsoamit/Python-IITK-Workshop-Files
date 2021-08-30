##################################[ IMMUTABLE CODE SECTION BEGIN ]#######################################
# ----------------------------------------------------------------------------------------------------- #
# helper library functions                                                                              #
from math import sqrt, pi                                                                               #
import sys, os
from typing import Sized                                                                                          #
#                                                                                                       #
sys.path.insert(0, "..")                                                                                #
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))                   #
from Util.misc import FIRST, SECOND, LAST, InvalidInputException                                        #
#                                                                                                       #
# additional constants                                                                                  #
min_side_args = {  # minimum no of numeric 'sides' to be input (apart from 'color' and 'filled' status) #
    "shape"         :   0,                                                                              #
    "triangle"      :   3,  # a triangle is defined by at least 3 sides                                 #
    "quadrilateral" :   4,  # a quadrilateral is defined by at least 4 sides                            #
    "rectangle"     :   2,  # a rectangle is defined by 2 sides (length, breadth)                       #
    "square"        :   1,  # a square is defined by by its side (length)                               #
    "n-gon"         :   3,  # a polygon is made up of a minimum of 3 sides                              #
    "circle"        :   1   # a circle is defined by its radius                                         #
}                                                                                                       #
valid_shape_names = min_side_args.keys()                                                                #
#                                                                                                       #
DEFAULT_COLOR = "Black"                                                                                 #
DEFAULT_FILLED_STATUS = False                                                                           #
# ----------------------------------------------------------------------------------------------------- #
####################################[ IMMUTABLE CODE SECTION END ]#######################################


class Shape(object):
    """A top level class for various shapes.
    Class specific attributes:
        Color:  Color of the Shape
        Filled: Fill status of the Shape
    """

    # define constructor
    def __init__(self, sides, color = "Black", filled = "False"):
        self.sides = sides
        self.Color = color.title()
        self.Filled = filled.title()
        self.perimeter = None
        self.area = None

    def is_filled(self):
        """Return the fill status of the Shape."""
        return self.Filled

    def perimeter(self):
        """Return the perimeter of the Shape."""
        pass

    def area(self):
        """Return the area of the Shape."""
        pass

class Triangle(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Side1, Side2, Side3
    """

    # define constructor

    # override the perimeter, area methods
    
    pass


class Quadrilateral(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Side1, Side2, Side3, Side4
    """

    # define constructor

    # override the perimeter method
    
    pass


class Rectangle(Quadrilateral):
    """Inherits Quadrilateral class.
    Class specific attributes:
        Length, Breadth
    """

    # define constructor

    # override the area method
    
    pass


class Square(Rectangle):
    """Inherits Rectangle class.
    Class specific attributes:
        Side
    """

    # define constructor
    
    pass


class Ngon(Shape):
    """Inherits Shape class."""

    # define constructor

    # override the perimeter method
    
    pass


class Circle(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Radius
    """

    def __init__(self, side, color = "Black", filled = "False"):
        self.sides = side
        self.Color = color
        self.Filled = filled

    def perimeter(self):
        """Return the perimeter of the Shape."""
        self.perimeter = 2 * self.side * pi

    def area(self):
        """Return the area of the Shape."""
        self.area = pi * (self.side**2)

switch_shape_func = {                       #
    "shape"         :   Shape,              #
    "triangle"      :   Triangle,           #
    "quadrilateral" :   Quadrilateral,      #
    "rectangle"     :   Rectangle,          #
    "square"        :   Square,             #
    "circle"        :   Circle              #
}                                           #

def validate_and_create_shape(user_input):
    """Helper function for creating a Shape Object."""

    user_input = user_input.split()
    shape = user_input[0]
    shape_cls = switch_shape_func[shape]
    if shape_cls == Shape:
        if len(user_input) == 3:
            shape_obj = Shape(0, color = user_input[1], filled = user_input[2])
            print(shape_obj.perimeter(), shape_obj.area(), shape_obj.Color, shape_obj.Filled)
        elif len(user_input) == 2:
            shape_obj = Shape(0, color = user_input[1])
            print(shape_obj.perimeter, shape_obj.area, shape_obj.Color, shape_obj.Filled)
        elif len(user_input) == 1:
            shape_obj = Shape(0)
            # print(shape_obj, shape_obj.Color)
            print(shape_obj.perimeter, shape_obj.area, shape_obj.Color, shape_obj.Filled)

    if shape_cls == Circle:
        if len(user_input) == 4:
            shape_obj = Shape(user_input[1], color = user_input[2], filled = user_input[3])
            print(shape_obj.perimeter(), shape_obj.area(), shape_obj.Color, shape_obj.Filled)
        elif len(user_input) == 3:
            shape_obj = Shape(user_input[1], color = user_input[2])
            print(shape_obj.perimeter(), shape_obj.area(), shape_obj.Color, shape_obj.Filled)
        elif len(user_input) == 2:
            shape_obj = Shape(user_input[1])
            print(shape_obj.perimeter(), shape_obj.area(), shape_obj.Color, shape_obj.Filled)

    # create corresponding Shape object
    # the below line initializes and returns the corresponding shape object
    # switch_shape_func[shape_name](params)
    return shape

def main():
    """
    INPUT:
        shape sides* [color] [filled_status]
            sides* -> 'n' number of sides (n depends on shape - for Square it's 1, for n-gon it's dynamic)
            color and filled_status -> optional (either both omitted or only filled_status omitted)
    OUTPUT:
        area perimeter color filled_status (or)
        'Invalid Input:<custom error message>' if input is invalid
    """

    user_input = input()
    shape = validate_and_create_shape(user_input)
    # if input valid and shape valid
    # print formatted shape parameters (rounded to 2 decimal places, title case)
    # else print 'Invalid Input:<custom error message>'
    
    pass


#######[ IMMUTABLE CODE SECTION BEGIN ]######
# ----------------------------------------- #
# Using the special variable __name__       #
if __name__ == "__main__":                  #
    main()                                  #
# ----------------------------------------- #
########[ IMMUTABLE CODE SECTION END ]#######
