import socket

BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recv_address = ('127.0.0.1', 2362)
server.bind(recv_address)

server.listen()

print( "listen" )

conn, addr = server.accept()
print( "Accepted, socket name:", server.getsockname(), addr )

while 1:
    try:
        data = conn.recv(BUFFER_SIZE)
        print('Received', repr(data.decode()))

        print("보낼 말:", end="")
        conn.send( input().encode() )
    except Exception as e:
        print( "connection expired.")
        break

print( "done" )
conn.close()