# P36

def main():
    string = input()
    list_of_numbers = string.split(", ")
    print(list(map(lambda n: int(int(n)*2), list_of_numbers)))
     

if __name__ == "__main__":
    main()


