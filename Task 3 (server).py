import socket

OFFENSIVE_WORDS = {"bad word", "offensive", "curse"}

def filter_text(message):
    # Filtering offensive words from the input text
    words = message.split()
    clean_words = filter(lambda word: word.lower() not in OFFENSIVE_WORDS, words)
    return " ".join(list(clean_words))

class TextServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try: 
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            print(f"Server is running on {self.host}:{self.port}")

            conn, addr = self.server_socket.accept()
            print(f"Connection established with {addr}")

            while True:
                data = conn.recv(1024).decode()
                if not data or data.lower() == "exit":
                    print("Client disconnected")
                    break
                print(f"Received from client: {data}")

                filtered_message = filter_text(data)
                print(f"Filtered message: {filtered_message}")

                conn.send(filtered_message.encode())

            conn.close()

        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.server_socket.close()

if __name__== '__main__':
    server = TextServer()
    server.start()