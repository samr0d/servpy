from servpy import Server
import time

#Create the Server
srv = Server('127.0.0.1',6500,4,'tcp',1)
print(srv)

#Turn it on. We basically create the whole socket here
#Have to give the arg of what it'd be listen in socket
srv.start()

while True:
    mssg = input("[SrvPy]> ")
    if mssg == "close":
        print("Closing server...")
        srv.stop()
        break
    #Out Data
    srv.send(mssg)
    #I recomend to import time so you can sleep the process
    #and avoid any problem
    time.sleep(2)
    rspns = srv.recv(2048,"utf-8")
    print(rspns)
    if mssg == "close":
        #Turn off the Server
        srv.stop()
    else: continue


srv.stop()


    


