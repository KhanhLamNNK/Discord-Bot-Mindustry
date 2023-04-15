import socket 
from socket import *
import time 
from time import time
import struct
from struct import unpack
s = socket(AF_INET, SOCK_DGRAM)
# Using This File A Module importimeout
class Server:
    def __init__(self, host, port=6567, socketPort=6859):
        self.host = host
        self.server = (host, port)
        self.socketPort = socketPort
    
    def get_info(self, timeout=10.0):
        s.connect(self.server)
        s.send(b"\xfe\x01")
        s.settimeout(timeout)
        statusdict = {}
    
        data = s.recv(1024)
        statusdict["name"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        statusdict["map"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        statusdict["players"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["wave"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["version"] = unpack(">i", data[:4])[0]
        data = data[4:]
        statusdict["vertype"] = data[1:data[0]+1].decode("utf-8")
        
        return statusdict
    def send(self, command):
        s = create_connection((self.host, self.socketPort))

        s.sendall(bytes(command.encode()))
        s.close()
        



