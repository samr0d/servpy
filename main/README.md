# ServPy #

This a project created to write sockets faster and more efficiently.

## Interface ##

### Server side ###
```
Server(HOST,PORT,IPversion,PROTOCOL,LISTEN)
```

Example:
```python
srv = Server = ('localhost',5000,4,'tcp',5)
```

### Client side ###

```
Client(HOST,PORT,IPversion,PROTOCOL)
```

Is similar to the server's side interface but only
omitting the LISTEN argument.

Example:
```python
clnt = Client('127.0.0.1',5000,4,'tcp',5)
```

## Usage ##

In this repo, you'll have examples of how to use the module step by step
creating a connection between a server and client with the local host. The examples
are in the directory examples.

## Details ##

This module only requires having python3 already installed as the only module imported required
is sockets.



