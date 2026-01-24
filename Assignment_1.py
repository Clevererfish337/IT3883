# Program Name: Assignment1.py 
# Course: IT3883/Section W01
# Student Name: Christopher Lee 
# Assignment Number: 1
# Due Date: 01/24/ 2026
# Purpose: Implements a text-based menu system for user interaction.
# VS Studio, GitHib Copilot

print("Welcome to the Text Buffer Manager!")

buffer =""

while True:
    print("---Menu:---")
    print("1. Append Buffer")
    print("2. Clear Buffer")
    print("3. Display Buffer")
    print("4. Exit")
        
    choice = input("Please select an option (1-4): ")
    print("")
        
    if choice == '1':
        print("You selected Append Buffer.")
        new_buffer = input("Enter text to append to the buffer: ")
        buffer += new_buffer
        print("Buffer updated.")
        print("")
          
    elif choice == '2':
        print("You selected Clear Buffer.")
        buffer= ""
        print("Buffer cleared.")
        print("")

    elif choice == '3':
        print("You selected Display Buffer.")
        print("Current Buffer Content:")
        print(buffer)
        print("")

    elif choice == '4':
        print("Exiting the program. Dueces!")
        break
    else:
        print("Invalid selection. Please try again.")
        print("")

