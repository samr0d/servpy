from servpy import Client
import time

#We specify the parameters of the client
clnt = Client('127.0.0.1',6500,4,'tcp')
print(clnt)
#Now we gotta connect to the Server
clnt.connect()

while True:
    data = clnt.recv(2048,"utf-8")
    print(data)
    rspns = input("[ClntPy]> ")
    if rspns == "close":
        #We stop the client
        clnt.disconnect()
    clnt.send(rspns)

clnt.disconnect()


