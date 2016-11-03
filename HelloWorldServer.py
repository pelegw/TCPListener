import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
port = os.environ['PORT']
message = "I am a basic TCP hellow world server listening on port 4444! Resistance is futile!"
server_address = ('localhost', 4444)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
# Wait for a connection
 print('waiting for a connection')
 connection, client_address = sock.accept()
 try:
  print('connection from', client_address)
  # Receive the data in small chunks and retransmit it
  connection.sendall(bytes(message.encode('utf8')))
 finally:
  # Clean up the connection
  connection.close()