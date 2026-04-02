# Program Name: AdvAppAssignment4.py 
# Course: IT3883/Section WO1
# Student Name: Christopher Lee
# Assignment Number: Assignment# 4
# Due Date: 04/01/2026
# Purpose: What does the program do (in a few sentences)? Prompts a user to type a string, sends it over a network socket to Program B, and prints the uppercase response it receives back.
# List Specific resources used to complete the assignment.  Lecture notes and Copilot suggestions in Visual Studio.


import socket

#configuration
HOST = '127.0.0.1'
PORT = 41000

# Create a socket
prog_a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to Program B
prog_a_socket.connect((HOST, PORT))
print(f"Connected to Program B at {HOST}:{PORT}")

#getting input
user_input = input("Type something to send to program B")

#send it!
prog_a_socket.send(user_input.encode())
print(f"Sent: {user_input}")

#wait for response
response = prog_a_socket.recv(1024)

#decode
print(f"Received back from Program B: {response.decode()}")

prog_a_socket.close()
print("Connection closed.")
