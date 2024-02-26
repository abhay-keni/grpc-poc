import threading

import zmq


def handle_client(context, identity, address):
    socket = context.socket(zmq.REP)
    socket.identity = identity
    socket.connect(address)

    while True:
        message = socket.recv_string()
        print(f"Received message from {identity.decode()}: {message}")

        # Broadcast the message to all connected clients
        for client_socket in client_sockets:
            if client_socket != socket:
                client_socket.send_multipart([identity, message.encode()])


def server(context):
    socket = context.socket(zmq.ROUTER)
    socket.bind("tcp://127.0.0.1:5555")

    print("Server is ready to receive streaming requests.")

    while True:
        identity, _, *message = socket.recv_multipart()

        # Check if the client is new, if yes, create a new thread to handle it
        if identity not in client_threads:
            address = f"tcp://127.0.0.1:{5556 + len(client_threads)}"
            new_thread = threading.Thread(
                target=handle_client, args=(context, identity, address), daemon=True
            )
            new_thread.start()
            client_threads[identity] = new_thread

        # Forward the message to the corresponding client thread
        client_sockets[identity] = context.socket(zmq.REQ)
        client_sockets[identity].connect(address)
        client_sockets[identity].send_multipart([b"", *message])
        client_sockets[identity].recv()


if __name__ == "__main__":
    # Create a ZeroMQ context in the server
    server_context = zmq.Context()

    # Dictionary to store client threads and sockets
    client_threads = {}
    client_sockets = {}

    # Start the server with the context
    server(server_context)
