from socket import *
import socket
import os

print("------------Escaneo de Red-------------\n")
ip = input("Ingresar IP y rango a escanear (ejemplo: 10.10.10.0:255): ")
puertos = [20, 21, 22, 23, 25, 29, 43, 53, 69, 80, 103, 108, 113, 115, 137, 138, 143, 443, 445, 1080, 2049, 6668, 6669, 8080]
ipParse = ip.split('.')
rangoParse = ipParse[3].split(':')
rango = int(rangoParse[1]) + 1
for i in range(int(rangoParse[0]), int(rango)):
    host = ipParse[0] + "." + ipParse[1] + "." + ipParse[2] + "." + str(rangoParse[0])
    response = os.popen("ping -n 1 " + host)
    print(response.readlines())
    for linea in response.readlines():
        if ("ttl" in linea.lower()):
            print(host, "esta activo")
            print("Escaneando puertos de: " + host + "\n")
            for j in range(10, 8081):
                if j in puertos:
                    s = socket.socket(AF_INET, SOCK_STREAM)
                    s.settimeout(4.0)
                    conn = s.connect_ex((host, j))
                    s.settimeout(None)
                    if (conn == 0):
                        print(host + ' Puerto: ' + str(j) + ' OPEN \n')
                        s.close()
                    if (conn == 111):
                        print(host + ' Puerto: ' + str(j) + ' FILTERED \n')
                        s.close()
    rangoParse[0] = int(rangoParse[0]) + 1
