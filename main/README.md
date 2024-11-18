# ServPy #

This a project created to write sockets faster and in an easier way.

## Interface ##

### Server side ###

Server(HOST,PORT,IPversion,PROTOCOL,LISTEN)

Example:

srv = Server = ('localhost',5000,4,'tcp',5)

### Client side ###

```
Client(HOST,PORT,IPversion,PROTOCOL)
```

Is actually really similar to the server's side interface but only
ommitting the LISTEN argument.

Example:
```python
clnt = Client('127.0.0.1',5000,4,'tcp',5)
```

## Usage ##

In this repo you'll have an examples of how to use the module step by step
creating a conection between a server and client with the local host. The examples
are in the directory examples.

## Details ##

This module only requires have python3 install as the only module imported required
sockets.



