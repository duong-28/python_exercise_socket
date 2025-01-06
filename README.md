# Text Filtering Client-Server Application

This project consists of a client-server application written in Python. The server filters out offensive words from the text messages sent by the client. The client sends messages to the server, and the server responds with the filtered version of the message. This application demonstrates basic socket programming in Python.

### Running the Server
1. Navigate to the project directory.
2. Run the server script:
    ```sh
    python "Task 3 (server).py"
    ```
3. The server will start and listen for incoming connections on `localhost:12345`.

### Running the Client
1. Open another terminal window.
2. Navigate to the project directory.
3. Run the client script:
    ```sh
    python "Task 3 (client).py"
    ```
4. The client will connect to the server. You can type messages to send to the server. Type `exit` to disconnect.