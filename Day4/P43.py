# P43
# function to reverse the number 
def revNum(num1, num2):
    return [int(num1[::-1]), int(num2[::-1])]

# function to check whether the number is prime or not
def isPrime(n):
    factors = 0
    for i in range(2, n):
        if n%i == 0:
            factors += 1
    
    if(factors > 0):
        return False
    return True

def main():
    numbers = input().split(",")
    num1, num2 = numbers[0], numbers[1]
    x, y = revNum(num1, num2)
    num1, num2 = int(num1), int(num2)
    x_is_prime = isPrime(x)
    y_is_prime = isPrime(y)

    if x_is_prime and y_is_prime:
        print(x + y)
    elif x_is_prime or y_is_prime:
        print(num1 + num2)
    else:
        print(num1 * num2)
    

if __name__ == "__main__":
    main()
