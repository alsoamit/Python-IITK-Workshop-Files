# P41

# Python program to check leap year or not
def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else: 
                False
        else:
            return True
    else:
        return False

# Driver Code
def main():
    year = int(input())
    print(is_leap_year(year))

if __name__ == "__main__":
    main()