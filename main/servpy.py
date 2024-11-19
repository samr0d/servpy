import socket

class Server:
    def __init__(self,HOST: str,PORT: int,IPvX: int,PROTO: int,NUM_DEVICES: int):
        self._server = None
        self._host = HOST
        self._port = PORT
        self._proto = PROTO
        self._ipvx = IPvX
        self._num_devices = NUM_DEVICES    
        self.client_socket = None    
        if IPvX == 4:
            if PROTO == "tcp":
                try:
                    self._server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            elif PROTO == "udp":
                try:
                    self._server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            else:
                print("INVALID PROTO (tcp/udp) ONLY")
        elif IPvX == 6:
            if PROTO == "tcp":
                try:
                    self._server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            elif PROTO == "udp":
                try:
                    self._server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            else:
                print("INVALID PROTO (tcp/udp) ONLY")
        else:
            print("INVALID IP VERSION (4/6) ONLY")
        
    #TURN ON
    def start(self):
        if self._server:
            try:
                #STAR THE SERVER's FUNCTION
                self._server.bind((self._host,self._port))
                self._server.listen(self._num_devices)
                global clnt_connection 
                self.client_socket, client_addr = self._server.accept()
                clnt_connection = (self.client_socket, client_addr)
            except socket.error as e:
                print(f"ERROR TURNNING ON SERVER: {e}")
        else:
            print("NOT SERVER CREATED")

    #OUT DATA
    def send(self, OUTDATA=None):
        if self._server:
            if OUTDATA is not None:
                clnt_connection[0].sendall(OUTDATA.encode())
        else:
            print("ERROR SENDING DATA")

    #IN DATA
    def recv(self, INDATA=int(),DECODING=str()):
        if self._server:
            if INDATA is not None:
                try:
                    packet = self.client_socket.recv(INDATA).decode(DECODING)
                    return packet
                except Exception as e:
                    print(f"ERROR RECIVING DATA: {e}")
            else:
                pass


    #TURN OFF
    def stop(self):
        if self._server:
            self._server.close()
        else:
            print("NOT SERVER CREATED")
    
    def __str__(self):
        return f"HOST={self._host}\nPORT={self._port}\nIPvX={self._ipvx}\nPROTO=tcp"


class Client:
    def __init__(self,HOST=str(),PORT=int(),IPvX=int(),PROTO=str()):
        self._client = None
        self._host = HOST
        self._port = PORT
        self._proto = PROTO
        self._ipvx = IPvX
        if IPvX == 4:
            if PROTO == "tcp":
                try:
                   self._client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                except Exception as e:
                   print(f"ERROR: {e} AT CREATING SOCKET")
            elif PROTO == "udp":
                try:
                    self._client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            else:
                print("INVALID PROTO (tcp/udp) ONLY")
        elif IPvX == 6:
            if PROTO == "tcp":
                try:
                    self._client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            elif PROTO == "udp":
                try:
                    self._client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                except Exception as e:
                    print(f"ERROR: {e} AT CREATING SOCKET")
            else:
                print("INVALID PROTO (tcp/udp) ONLY")
        else:
            print("INVALID IP VERSION (4/6) ONLY")

        
    #CONNECT TO SERVER
    def connect(self):
        try:
            self._client.connect((self._host,self._port))
        except socket.error as e:
            print("ERROR TRYING TO CONNECT TO HOST {self._host}") 

    #OUT DATA
    def send(self,OUTDATA=None):
        if OUTDATA is not None:
            self._client.sendall(OUTDATA.encode())
        else:
            print("ERROR SENDING DATA")

    #IN DATA
    def recv(self,INDATA=int(),DECODING=str()):
        if self._client and INDATA:
            try:
                return self._client.recv(INDATA).decode(DECODING)
            except Exception as e:
                print(f"ERROR RECIVING DATA: {e}")
        else:
            pass

    #CLOSE SOCKET AND DISCONNECT
    def disconnect(self) -> None:
        self._client.close()

    def __str__(self):
        return f"HOST={self._host}\nPORT={self._port}\nIPvX={self._ipvx}\nPROTO={self._proto}"
    
