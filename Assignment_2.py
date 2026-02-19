# Program Name: Assignment2.py 
# Course: IT3883/Section W01
# Student Name: Christopher Lee
# Assignment Number: 2
# Due Date: 2/19/2026
# Purpose: Read from an input file, extract the student’s name, convert the remaining fields to numbers, compute the average for each, store and print the results in descending order. 
# List Specific resources used to complete the assignment.   Course material, youtube videos, and VS Studio predictive AI when typing code. 




filename = input("Enter the filename of the data: ")

#create empty lists to store the data

students = []

#open the file
file = open(filename, "r")

#read the file
for line in file:
    parts = line.strip().split()
    name = parts[0]
    total = 0
    count = 0

    for i in range (1, len(parts)):
        score = float(parts[i])
        total = total+score
        count = count+1

    #calculate the average score for each student
    average = total/count

    #Name and avg as list
    students.append((name, average))

#close the file
file.close()

#sort the list by average score in descending order
students.sort(reverse=True, key=lambda student: student[1])

#print the sorted list
print("\nFinal Averages (Highest to Lowest):")
for student in students:
    print(f"{student[0]}: {student[1]:.2f}")
