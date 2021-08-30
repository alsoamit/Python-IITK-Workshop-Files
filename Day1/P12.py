# P12

def main():
    # Take inputs for u, a and t. 
    u = float(input())
    a = float(input())
    t = float(input())

    v = round(u + a*t,2)
    print("The final velocity is {}.".format(v))

if __name__ == "__main__":
    main()