# P44
def RecSum(n):
    if n <= 9 and n >= 0:
        return n
    s = 0
    for i in str(n):
        s += int(i)

    return RecSum(s)

def main():
    #take input
    n = int(input())
    print(RecSum(n))

if __name__ == "__main__":
    main()