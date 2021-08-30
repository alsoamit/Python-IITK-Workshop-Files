import numpy as np
from scipy import linalg
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    matrixA = eval(input())
    matrixB = eval(input())
    A, B = np.array(matrixA), np.array(matrixB)
    try:
        solution = linalg.solve(A, B)
        print(solution)
    except:
        print("ERROR: Cannot find solution.")

if __name__ == "__main__":
    main()
