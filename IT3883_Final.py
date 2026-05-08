# Program Name: IT3883 FInal.py 
# Course: IT3883/Section WO1
# Student Name: Christopher Lee
# Assignment Number: FInal
# Due Date: 5/7/2026
# Purpose: What does the program do (in a few sentences)?  Ingests a psuedo-English sentence describing coin quantities and returns the total value of the coins in cents. 

#dictionary of coins and their values
from math import e


COIN_VALUES ={
    "penny": .01,
    "pennies": .01,
    "nickel": .05,
    "nickels": .05,
    "dime": .10,
    "dimes": .10,
    "quarter": .25,
    "quarters": .25,
    }


#sentence intake
print("=" * 50)
print("WELCOME TO THE COIN CONVERTER PROGRAM")
print("This program converts a sentence describing coin quantities into a total value in dollars.")
print("Type 'quit' to exit the program.")
print("=" * 50)

while True:
    sentence = input("\nEnter your coin sentence: ").strip()
    #The exit plan
    if sentence.lower() == "quit":
        print("Goodbye!")
        break
    #The input
    if not sentence: 
        print("Please enter a sentence.")
        continue

    #splitting apart the sentence into groups
    coin_groups = sentence.split("and")
    total = 0.0
    error = False

    for group in coin_groups:
        group = group.strip()
        parts = group.split()
        #error if group does not have two parts (quantity and denomination)
        if len(parts) != 2:
            print(f"Warning: Skipping unrecognized group '{group}'")
            continue
        #error if quantity is not a valid integer
        try:
            quantity = int(parts[0])
        except ValueError:
            print(f"Warning: Invalid quantity '{parts[0]}' in group '{group}'skipping")
            continue

        denomination = parts[1].lower()

        #error if denomination is not recognized in the COIN_VALUES dictionary
        if denomination not in COIN_VALUES:
            print(f"Warning: Unknown denomination '{denomination}'skipping")
            continue
        #tally it up and print!
        total += quantity * COIN_VALUES[denomination]
    print(f"  Result: {round(total, 2):.2f}")
