# Program Name: AdvAppAssignment4.py 
# Course: IT3883/Section WO1
# Student Name: Christopher Lee
# Assignment Number: Assignment# 4
# Due Date: 04/01/2026
# Purpose: What does the program do (in a few sentences)? Listens for an incoming connection, receives a string from Program A, converts it to uppercase, and sends it back.
# List Specific resources used to complete the assignment.  Lecture notes and Copilot suggestions in Visual Studio.

import socket

#configuration
HOST = '127.0.0.1'
PORT = 41000

# Create a socket
prog_b_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to the port
prog_b_socket.bind((HOST, PORT))

#listen for connections
prog_b_socket.listen(1)
print(f"Program is listening on {HOST}:{PORT}")
print("Waiting for a connection ...")

#accept a connection
connection, adress = prog_b_socket.accept()
print(f"Connected from : {adress}")

#recevie
data=connection.recv(1024)

#decode the message
received_message = data.decode()
print(f"Received message: {received_message}")

#convert to uppercase
uppercase_message = received_message.upper()
print(f"Coverted to Uppercase: {uppercase_message}")

#send it back
connection.send(uppercase_message.encode())
print("Sent message back")

connection.close()
prog_b_socket.close()
print("Connection closed.")
