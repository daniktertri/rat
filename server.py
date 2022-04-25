import socket

HOST = "192.168.100.4"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        request=conn.recv(1024)
        request=request.decode('utf-8')
        print(f"Connected by {addr}")
        print(request)
        while True:
            msg = str(input("Command: "))
            conn.sendall(msg.encode())
