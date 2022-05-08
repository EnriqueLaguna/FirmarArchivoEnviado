# mandar el archivo para que el server lo encripte y firme
import socket

BUFFER_SIZE = 4096

host = "127.0.0.1"
port = 65432

filename = "D:\ITESO\Semestre 8\SeguridadEnRedes\cripto\FirmEncryptedFile/message.txt"

with open(filename, 'rb') as fileDataToRead:
    message = fileDataToRead.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(f"{message}".encode())
data = s.recv(BUFFER_SIZE)


