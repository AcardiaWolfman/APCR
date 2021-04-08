import socket, os

class FileClient():
  def ClientProcess(self, file_path, file_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
      TCPClientSocket.connect((self.HOST, self.PORT))
      print(f"Enviando archivo {file_name}...")
      TCPClientSocket.sendall(bytes(file_name,'utf-8'))
      file_to_send = open(file_path, "rb")
      print("El Servidor recibirá el archivo")
      while True:
        part_of_file = file_to_send.read(self.buffer_size)
        if not part_of_file:
          break
        TCPClientSocket.sendall(part_of_file)
      print("Enviando señal de fin")
      file_to_send.close()
      print("terminando")
  def ProcessFolder(self):
    #path = input("Introduce la ruta de archivos a enviar")
    path = "/home/acardiawolfman/Documentos/filesToSend"
    for f in os.listdir(path):
      self.ClientProcess(os.path.join(path, f), f)
  def __init__(self):
    self.HOST = "127.0.0.1"  # The server's hostname or IP address
    self.PORT = 65432  # The port used by the server
    self.buffer_size = 1024
    self.ProcessFolder()
FileClient()
