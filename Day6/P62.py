######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

def main():
    roll = input()
    item = input()
    fileA=roll + 'A.txt'
    fileB=roll + 'B.txt'

    f1, f2 = open(fileA, "r"), open(fileB, "r")
    f1Content, f2Content = f1.read(), f2.read()

    if item in f1Content and item in f2Content:
        print("Item", item, "found in both", fileA, "and", fileB)
    elif item in f1Content:
        print("Item", item, "found in", fileA)
    elif item in f2Content:
        print("Item", item, "found in", fileB)
    else:
        print("Item", item, "found nowhere")

if __name__ == "__main__":
    main()