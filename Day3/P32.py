# P32

def main():
    # Take the input
    string = input()
    # Check if "bad" exists
    if string.find("bad") != -1:
        # Check if "not" is before "bad"
        if string.find("not") < string.find("bad"):
            part1 = string.split('not')[0]
            part2 = string.split('bad')[1]

            print(part1 + "good" + part2)
        else:
            print(string)
    else:
        print(string)

if __name__ == "__main__":
    main()
