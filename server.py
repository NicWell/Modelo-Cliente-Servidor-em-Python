from socket import *
import random
serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Servidor Disponivel")
listInt = [2]
a = 0 
b = 0
while True:
    numberInterval, clientAddress = serverSocket.recvfrom(2048)
    numberFix= numberInterval
    decod = numberFix.decode()
    listInterval = decod.split("/")
    a = int(listInterval[0])
    b = int(listInterval[1])
    sort = random.randint(a,b)
    env = str(sort)
    serverSocket.sendto(env.encode(), clientAddress)
    if(serverSocket.send):
        break