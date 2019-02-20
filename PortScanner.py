import os, sys, platform
from socket import *

import socket
print("------------Escaneo de Red-------------\n")
ip = input("Ingresar IP y rango a escanear (ejemplo: 10.10.10.10 255): ")
ipParse = ip.split('.')
print(ipParse)
convertir = ipParse[3]
print (ipParse)
for i in range(0, 100):
    convertir = int(convertir) + 1
    host = ipParse[0] + "." + ipParse[1] + "." + ipParse[2] + "." + str(convertir)
    response = os.popen("ping -n 1 " + host)
    for line in response.readlines():
        #print(line)
        if ("ttl" in line.lower()):
            print(host, "está activo")
            break
    s = socket.socket(AF_INET, SOCK_STREAM)
    for i in range(10, 445):
        conn = s.connect_ex((host, i))
        if (conn == 0):
            print(host + ' Puerto: ' + str(i) + ' OPEN')
            s.close()
