import zmq


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")

    print("Server is ready to receive requests.")

    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")

        # Simulate some processing
        response = f"Hello, {message}! This is the server."

        # Send the response back to the client
        socket.send_string(response)


if __name__ == "__main__":
    server()
