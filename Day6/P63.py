######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os, csv
from types import DynamicClassAttribute
from typing import ItemsView

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e: 
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x

def ask_for_item(vendor_mapping):
    item = input()
    if item in vendor_mapping:
        return item
    else:
        raise Exception("ERROR: No such item found")

def ask_for_money(money, asked_item, vendor_mapping):
    try:
        money = int(money)
        if money > vendor_mapping[asked_item]:
            print("Thank you for your purchase. Enjoy\nDo not forget to collect your change,", money - vendor_mapping[asked_item], "Rs.")
        elif money == vendor_mapping[asked_item]:
            print("Thank you for your purchase. Enjoy")
        elif money < vendor_mapping[asked_item]:
            print("Sorry, can not buy item. Not enough money")
        else:
            raise Exception("Bad Input")
    except:
        raise Exception("Bad Input")

def main():
    vendor_mapping = dict()
    asked_item = []
    with open('VendingItems.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '|')
        for row in csv_reader:
            vendor_mapping[row[0]] = eval(row[1])
    
    while True:
        try:
            asked_item = ask_for_item(vendor_mapping)
            break
        except:
            print(f"Available Items are {list(vendor_mapping.keys())}.")
            print("Try Again.")

    while True:
        money = input()
        try:
            ask_for_money(money, asked_item, vendor_mapping)
            break
        except:
            print(f"Bad Input {money}.")
            
if __name__ == "__main__":
    main()