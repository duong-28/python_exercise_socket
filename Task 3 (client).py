import socket

class TextClient: 
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try: 
            self.client_socket.connect((self.host, self.port))
            print("Connected to server. Type 'exit' to disconnect.")

            while True: 
                message = input("You (client): ")
                self.client_socket.send(message.encode())

                if message.lower() == "exit":
                    print("Disconnected from server")
                    break

                filtered_message = self.client_socket.recv(10240).decode()
                print(f"Server (filtered): {filtered_message}")

            self.client_socket.close()

        except Exception as e:
            print(f"Client error: {e}")
            self.client_socket.close()

if __name__=='__main__':
    client = TextClient()
    client.start()