import socket

class FileClient():
  def ClientProcess(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
      TCPClientSocket.connect((self.HOST, self.PORT))
      print("Enviando mensaje...")
      file_name = input("Escribe el nombre de tu archivo:\n")
      TCPClientSocket.sendall(bytes(file_name,'utf-8'))
      file_to_send = open(file_name, "rb")
      print("El Servidor recibirá el archivo")
      part_of_file = file_to_send.read(1024)
      while part_of_file:
        TCPClientSocket.sendall(part_of_file)
        part_of_file = file_to_send.read(1024)
      TCPClientSocket.sendall(bytes("fin", 'utf-8'))
      file_to_send.close()
  def __init__(self):
    self.HOST = "127.0.0.1"  # The server's hostname or IP address
    self.PORT = 65432  # The port used by the server
    self.buffer_size = 1024
    self.ClientProcess()
FileClient()
