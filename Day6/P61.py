######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

def main():
    roll= input()
    fileA=roll + 'A.txt'
    fileB=roll + 'B.txt'

    fileAContent = eval(input())
    fileBContent = eval(input())
    # Open file to write content
    f1, f2 = open(fileA, "a"), open(fileB, "w")

    f1.write("\n".join(map(str, fileAContent)))
    f2.write("\n".join(map(str, fileBContent)))

    # Close file
    f1.close()
    f2.close()

    A, B = open(fileA, 'r'), open(fileB, 'r')
    print (A.read())
    print (B.read())
    A.close()
    B.close()


if __name__ == "__main__":
    main()