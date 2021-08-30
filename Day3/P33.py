# P33

def main():
    num = input()
    sum_of_cubes = 0
    for i in num:
        sum_of_cubes += int(i)**3

    if sum_of_cubes == int(num):
        print("Sum of Cubes is {}. It is the same as the number {}.".format(sum_of_cubes, num))
    else:
        print("Sum of Cubes is {}. It is NOT same as the number {}.".format(sum_of_cubes, num))

if __name__ == "__main__":
    main()
