# P13

def main():
    u = float(input())
    a = float(input())
    t = float(input())

    d = round(u*t + (1/2)*a*t*t,2)
    print("The displacement is {}.".format(d))

if __name__ == "__main__":
    main()