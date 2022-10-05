import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("192.168.43.26", 4444))
listener.listen()

print("Server is started")

connection, address = listener.accept()

print(f("Connection from {address}"))