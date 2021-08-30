import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def main():
    # Take the user input
    V = float(input())
    A = math.radians(float(input()))
    g = 9.8

    # calculate the values
    t = (2 * V * math.sin(A)) / g
    d = (V**2 * math.sin(2*A)) / g
    y = (V* V * math.sin(A)* math.sin(A)) / (2 * g)

    print('Time of Flight = {}'.format(round(t, 2)))
    print('Distance Covered = {}'.format(round(d, 2)))
    print('Peak Height = {}'.format(round(y, 2)))

if __name__ == "__main__":
    main()
