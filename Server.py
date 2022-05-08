from cgitb import text
from fileinput import filename
import socket
from Crypto.Cipher import ChaCha20
import nacl.utils
from nacl.signing import SigningKey


BUFFER_SIZE = 4096

host = "127.0.0.1"
port = 65432
filename = "D:\ITESO\Semestre 8\SeguridadEnRedes\cripto\FirmEncryptedFile/encryptedFile.txt"

# Crear el socket
s = socket.socket()

# Bind the socket with the address and port
s.bind((host, port))

#Listen to the connection
s.listen()
print(f"[*] Listening as {host}:{port}")

# Block execution and waits for an incomming connection
client_socket, address = s.accept()

# Read whatever the client sends
message = client_socket.recv(BUFFER_SIZE).decode()

# Encriptar el mensaje que nos ha enviado el cliente
# llave
chacha20_key = nacl.utils.random()

# Chacha baby
chachaCipher = ChaCha20.new(key=chacha20_key)

# Convertir el mensaje en bytes
mensaje_a_bytes = bytes(message, 'utf-8')

# Encriptar la informacion
texto_encriptado = chachaCipher.encrypt(mensaje_a_bytes)

print(f"Texto encriptado por Chacha20: \n {texto_encriptado}\n")

# Crear la llave para firmar
signing_key = SigningKey.generate()

# Firmar el mensaje
mensaje_firmado = signing_key.sign(texto_encriptado)

# Obtener la llaver verificadora de la llave firmadora
verify_key = signing_key.verify_key

# Serializar la llave para enviarla
verify_key_bytes = verify_key.encode()

print(f"Verify_key_bytes: {verify_key_bytes}\n")

print(f"Texto firmado y encriptado por Chacha20: \n {mensaje_firmado}\n")

# Escribir el mensaje encriptado en el archivo
with open(filename, 'wb') as writeToFile:
    mensajeAEscribir = writeToFile.write(mensaje_firmado)






