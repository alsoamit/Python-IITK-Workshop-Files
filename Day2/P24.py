# P24

def main():
    string = input()
    part1 = string.split('not')[0]
    part2 = string.split('bad')[1]

    print(part1 + "good" + part2)

if __name__ == "__main__":
    main()