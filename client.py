from socket import *

serverName = '192.168.101.191'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Digite um intervalo separado por uma barra\n Exemplo: 1 / 100\n")
number1 = str(input(":"))
clientSocket.sendto(number1.encode(),(serverName, serverPort))
env, serverAddress = clientSocket.recvfrom(2048)
print("O número Sorteado é: ", env.decode())
clientSocket.close()