# socket module import!
import socket

# socket create and connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2362))

# send msg
test_msg = "안녕하세요 상대방님2"
client.send(test_msg.encode())

# recv data
data_size = 1024
data = client.recv(data_size)
print( data.decode() )

# connection close
client.close()