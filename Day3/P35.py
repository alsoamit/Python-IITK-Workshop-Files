# P35

def main():
    n = int(input())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i+1):
            print("_" + alphabet[j], end="")
        print("_", end="\n")

if __name__ == "__main__":
    main()
