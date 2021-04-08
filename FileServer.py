import socket
import time
import datetime
class FileServer():
  def ServerProcess(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
        TCPServerSocket.bind((self.HOST, self.PORT))
        TCPServerSocket.listen()
        print("El servidor TCP está disponible y en espera de solicitudes")
        while True:
            Client_conn, Client_addr = TCPServerSocket.accept()
            with Client_conn:
                print("Cliente", Client_addr)
                data = Client_conn.recv(self.buffer_size)
                file_name = data.decode('utf-8')
                print("Salvando "+file_name)
                file_to_save = open(f"{datetime.datetime.today().strftime('%d-%m-%y-%I-%M-%S-%p')}_{file_name}","wb")
                while True:
                    data = Client_conn.recv(self.buffer_size)
                    if  not data:
                        break
                    file_to_save.write(data)
                file_to_save.close()
                print("Se guardo exitosamente el archivo, listo para recibir  nuevo\n")
  def __init__(self):
    self.HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    self.PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    self.buffer_size = 1024
    self.ServerProcess()
FileServer()
