import ray
import zmq


@ray.remote
def client(client_id):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")

    while True:
        message = f"Client {client_id}"
        print(f"Sending request: {message}")
        with open("file.txt", "a") as file:
            file.write(str(f"Sending request: {message} \n\n"))

        # Send a request to the server
        socket.send_string(message)

        # Receive the response from the server
        response = socket.recv_string()
        if response == "Finish":
            break

        print(f"Received response: {response}")
        with open("file.txt", "a") as file:
            file.write(str(f"Received response: {response} \n\n"))


if __name__ == "__main__":
    # Start multiple clients

    ray.init()

    num_clients = 1
    res = []
    for i in range(num_clients):
        res.append(client.remote(i))

    ray.get(res)
    ray.shutdown()
