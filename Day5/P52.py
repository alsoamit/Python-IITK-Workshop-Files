######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os
import string
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########



alphabet = set(string.ascii_lowercase) 
  
def ispangram(s):
    s = s.lower()
    missing_chars = []
    for i in alphabet:
        if i not in s:
            missing_chars.append(i)
    return missing_chars

def main():
    s = input()
    missing_chars = ispangram(s)
    string_from_list = ""
    for i in sorted(missing_chars):
        string_from_list += i + ", "

    if len(missing_chars) == 0:
        print("Yes, the string is a pangram.")
    else:
        print("No, the string is NOT a pangram. Missing letter(s) is(are) {}.".format( string_from_list[:-2]))


if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END ######### 