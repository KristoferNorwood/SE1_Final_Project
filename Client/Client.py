import socket, time

s = socket.socket()
s.connect(("98.168.143.109", 7123))
file = open(r"C:/Users/rlore/Desktop/SE1_Final_Project-main/Client/schema.xml", "rb")
stream = file.read(65536)
i = 0
while stream:
    s.settimeout(30)
    s.send(stream)
    data = s.recv(65536)
    print(data.decode("utf8"))
    break

s.close()
