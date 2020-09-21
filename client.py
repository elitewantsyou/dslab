
import socket
import os
import sys

fname = sys.argv[1]  # take the file name from cmd args
TCP_IP = sys.argv[2]  # take the ip from cmd args
TCP_PORT = int(sys.argv[3])  # take the port from cmd args

BUFFSZ = 1024  # size of each chunk sent

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize new socket
s.connect((TCP_IP, TCP_PORT))  # init new connection

f = open(fname, 'rb')  # open file to start reading chunks
fileInfo = os.stat(fname)  # get info of the file

s.send(fname.encode())  # send the file name
check = s.recv(1)

chunksRead = 0

print("The process of sending file began")

checkpoint = 0  # denoting how much data was sent successfully

while True:

    l = f.read(BUFFSZ);  # read new chunk
    # chunksRead += BUFFSZ*2   #increment
    """
    progress=chunksRead/fileInfo.st_size*100;
    if(checkpoint < progress - 2):
        print("Percentage of file sent = " + str(min(100,int(progress))) + "%") #print progress 5% each time
        checkpoint=progress #save checkpoint
    """
    if (l):
        s.send(l)  # if we read data send it
    l = f.read(BUFFSZ)

    if not l:
        f.close()  # close everything
    s.close()
    break

print('File is sent :)')
s.close()
print('Connection is closed')

import socket
import os
import sys

fname = sys.argv[1]  # take the file name from cmd args
TCP_IP = sys.argv[2]  # take the ip from cmd args
TCP_PORT = int(sys.argv[3])  # take the port from cmd args

BUFFSZ = 1024  # size of each chunk sent

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize new socket
s.connect((TCP_IP, TCP_PORT))  # init new connection

f = open(fname, 'rb')  # open file to start reading chunks
fileInfo = os.stat(fname)  # get info of the file

s.send(fname.encode())  # send the file name
check = s.recv(1)

chunksRead = 0

print("The process of sending file began")

checkpoint = 0  # denoting how much data was sent successfully

while True:
    l = f.read(BUFFSZ);  # read new chunk
    chunksRead += BUFFSZ * 2  # increment

    progress = chunksRead / fileInfo.st_size * 100

    if (checkpoint < progress - 2):
        print("Percentage of file sent = " + str(min(100,int(progress))) + "%")  # print progress 5% each time
        checkpoint = progress  # save checkpoint

    if (l):
        s.send(l)  # if we read data send it
    l = f.read(BUFFSZ)

    if not l:
        f.close()  # close everything
        s.close()
        break

print('File is sent :)')
s.close()
print('Connection is closed')