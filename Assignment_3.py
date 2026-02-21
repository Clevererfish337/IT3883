# Program Name: Assignment_3.py
# Course: IT3883/Section W01
# Student Name: Christopher Lee
# Assignment Number: 3
# Due Date: 2/28/2026
# Purpose: Creates a GUI screen that converts miles per gallon (MPG) to kilometers per liter (KM/L). The user can enter a value for MPG, and the program will automatically calculate and display the corresponding KM/L value. The conversion factor used is 1 mile per gallon = 0.425143707 kilometers per liter.
# List Specific resources used to complete the assignment.  Lecture/class material, geeksforgeeks Tkinter documentation, and VScode copilot were used. 

import tkinter as tk

#converstion 
conversion_factor = 0.425143707

def convert(*args):
    value = mpg.get()
    if value == "":
        result.set("")
        return
    try:
        mgp = float(value)
        km_per_1=mgp * conversion_factor
        result.set(f"{km_per_1:.2f}")
    except ValueError:
        result.set("Invalid input")


#Main screen
mainscreen = tk.Tk()
mainscreen.title("MPG to KM/L Converter")
mainscreen.geometry("300x150")

#variables
mpg = tk.StringVar()
result = tk.StringVar()

#auto update w/ keystrokes
mpg.trace_add("write", convert)

#Labels and entry boxes
tk.Label(mainscreen, text = "Miles per Gallon (MPG):").pack(pady = 5)
mpg_entry = tk.Entry(mainscreen, textvariable = mpg)
mpg_entry.pack()

tk.Label(mainscreen, text = "Kilometers per Liter (KM/L):").pack(pady = 5)
result_label = tk.Label(mainscreen, textvariable = result, fg = "blue")
result_label.pack()


#Run GUI
mainscreen.mainloop()
