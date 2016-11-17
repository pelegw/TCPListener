import socket
import sys
import os
import subprocess
import threading
import time


lock = threading.Lock()
class ThreadedServer(object):
    def __init__(self, host):
        self.host = "0.0.0.0"
        self.port = os.environ['PORT']
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, int(self.port)))
	print (os.environ)

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
	lock.acquire()
	f=open("log.txt","a")
	f.write("************************************************************************************\n")
	now = time.strftime("%c")
	f.write("%s ---- Connection from:%s \n\n" % (now,str(address)))

        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    response = data
                    if "PelegRulz123!" in response:
                     f.close()
                     with open("log.txt") as f:
                      content = f.readlines()
                      for line in content:
                       print line
                     f=open("log.txt","a")                     
		    f.write(response)
                else:
                    f.write('Client disconnected')
		    raise error('Client Disconnected')
                    
            except:
                client.close()
                lock.release()
 #               f.close()
                return False

if __name__ == "__main__":
    ThreadedServer('').listen()
