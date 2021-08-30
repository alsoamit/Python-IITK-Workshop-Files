# P23

def main():
    text = input()
    # Check for palindrome
    print(text, text.lower() == text[::-1].lower())

if __name__ == "__main__":
    main()