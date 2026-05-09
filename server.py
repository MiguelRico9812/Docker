import socket


IP = "0.0.0.0"  # Escucha en todas las interfaces del contenedor
PORT = 8080


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"Servidor de mensajería UDP iniciado en el puerto {PORT}...")

while True:
    data, addr = sock.recvfrom(1024) # Buffer de 1024 bytes
    message = data.decode('utf-8')
    print(f"Mensaje recibido de {addr}: {message}")
    
    
    response = f"Servidor: Recibí tu mensaje '{message}'".encode('utf-8')
    sock.sendto(response, addr)