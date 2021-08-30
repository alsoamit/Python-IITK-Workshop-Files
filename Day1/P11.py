# P11

def main():
    temp_f = float(input())
    
    # Calculate the temperature in Celsius (C) using the formula C=(F−32)×5/9. Also, round the value obtained to two decimal places.
    temp_c = round((temp_f - 32)*5/9, 2)

    # Print the answer.
    print("Fahrenheit temperature {} is the same as {} degrees Celsius.".format(temp_f, temp_c))

if __name__ == "__main__":
    main()