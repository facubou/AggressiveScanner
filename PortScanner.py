from socket import *
import socket

print("------------Escaneo de Red-------------\n")
ip = input("Ingresar IP y rango a escanear (ejemplo: 10.10.10.0:255): ")
ipParse = ip.split('.')
print(ipParse)
rangoParse = ipParse[3].split(':')
rango = int(rangoParse[1]) + 1

for i in range(int(rangoParse[0]), int(rango)):
    host = ipParse[0] + "." + ipParse[1] + "." + ipParse[2] + "." + str(rangoParse[0])
    response = os.popen("ping -n 1 " + host)
    for linea in response.readlines():
        if ("ttl" in linea.lower()):
            print(host, "está activo")
            s = socket.socket(AF_INET, SOCK_STREAM)
            print("Escaneando puertos de: " + host + "\n")
            for j in range(10, 445):
                conn = s.connect_ex((host, j))
                if (conn == 0):
                    print(host + ' Puerto: ' + str(j) + ' OPEN \n')
                    s.close()
    rangoParse[0] = int(rangoParse[0]) + 1
