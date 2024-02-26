import zmq

context = zmq.Context()
dealer = context.socket(zmq.DEALER)
dealer.setsockopt_string(
    zmq.IDENTITY, "client-1"
)  # Set a unique identity for the dealer (optional)
dealer.connect("tcp://127.0.0.1:5555")

for i in range(5):
    message = f"Request {i}"
    print(f"Sending: {message}")
    dealer.send_string(message)

    # Receive the reply from the server
    reply = dealer.recv_string()
    print(f"Received reply: {reply}")
