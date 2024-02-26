import sys
import threading

import zmq


def receive_messages(socket):
    while True:
        identity, message = socket.recv_multipart()
        print(f"Received message from {identity.decode()}: {message.decode()}")


def client(client_id, context):
    socket = context.socket(zmq.REQ)
    socket.setsockopt_string(zmq.IDENTITY, f"Client-{client_id}")
    socket.connect("tcp://127.0.0.1:5555")

    # Create a thread to handle incoming messages
    receive_thread = threading.Thread(
        target=receive_messages, args=(socket,), daemon=True
    )
    receive_thread.start()

    try:
        while True:
            message = input("Type your message: ")
            socket.send_string(message)
            socket.recv()  # Wait for acknowledgment
    except KeyboardInterrupt:
        print("Client is exiting.")
        sys.exit()


if __name__ == "__main__":
    # Create a ZeroMQ context in the clients
    client_context = zmq.Context()

    # Start multiple clients
    num_clients = 2
    for i in range(num_clients):
        threading.Thread(target=client, args=(i, client_context), daemon=True).start()

    # Keep the main thread running to allow the client threads to continue receiving messages
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Server is exiting.")
